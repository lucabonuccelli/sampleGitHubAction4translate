import os
import subprocess
import re
import requests

ENGINE = os.environ.get("TRANSLATION_ENGINE", "google").lower()
LIBRETRANSLATE_API = os.environ.get("LIBRETRANSLATE_API", "https://libretranslate.com/translate")
TARGET_LANG = "it"
SOURCE_LANG = "en"

if ENGINE == "google":
    from deep_translator import GoogleTranslator

def translate_text(text):
    """Invia il testo al motore selezionato per la traduzione."""
    if not text.strip() or text.strip().startswith("```") or text.strip() == "":
        return text
    try:
        if ENGINE == "libretranslate":
            response = requests.post(
                LIBRETRANSLATE_API,
                json={"q": text, "source": SOURCE_LANG, "target": TARGET_LANG, "format": "text"},
                timeout=30
            )
            return response.json().get("translatedText", text) if response.status_code == 200 else text
        else:
            return GoogleTranslator(source=SOURCE_LANG, target=TARGET_LANG).translate(text)
    except Exception as e:
        print(f"Errore di traduzione: {e}")
        return text

def get_changed_files():
    """Trova i file modificati nell'ultimo commit."""
    try:
        output = subprocess.check_output(
            ["git", "diff", "--name-only", "HEAD~1", "HEAD", "--", "docs/en/"]
        ).decode("utf-8")
        return [f.strip() for f in output.splitlines() if f.strip().endswith(('.md', '.rst'))]
    except Exception as e:
        print(f"Errore git diff: {e}")
        return []

def translate_full_file(en_path, it_path):
    """Traduzione integrale (usata solo se il file italiano non esiste ancora)."""
    print(f"Traduzione integrale di {en_path}...")
    with open(en_path, "r", encoding="utf-8") as f:
        en_lines = f.readlines()
    
    translated_lines = []
    for i, line in enumerate(en_lines, start=1):
        print(f"riga {i} : {line}")
        if line.strip() == "":
            translated_lines.append("\n")
            continue
        has_newline = line.endswith("\n")
        print(f"[{i}] INPUT  : {repr(line.strip())}")
        translated = translate_text(line.strip())
        print(f"[{i}] OUTPUT : {repr(translated)}")
        if translated is None:
            print(f"GoogleTranslator ha restituito None alla riga {i}: {repr(line.strip())}")
            translated=line
                 
        translated_lines.append(translated + ("\n" if has_newline else ""))
    
    os.makedirs(os.path.dirname(it_path), exist_ok=True)
    with open(it_path, "w", encoding="utf-8") as f:
        f.writelines(translated_lines)

def apply_line_level_translations(en_path, it_path):
    """Traduzione incrementale riga per riga tramite git diff."""
    print(f"Aggiornamento incrementale per: {it_path}")
    
    with open(en_path, "r", encoding="utf-8") as f:
        en_lines = f.readlines()
    with open(it_path, "r", encoding="utf-8") as f:
        it_lines = f.readlines()

    # Se le righe differiscono, riallinea completamente il file
    if len(en_lines) != len(it_lines):
        print(f"⚠️ Disallineamento righe rilevato. Rigenerazione del file...")
        translate_full_file(en_path, it_path)
        return

    try:
        diff_output = subprocess.check_output(
            ["git", "diff", "-U0", "HEAD~1", "HEAD", "--", en_path]
        ).decode("utf-8")
    except Exception as e:
        print(f"Impossibile calcolare il diff: {e}")
        return

    hunk_re = re.compile(r'^@@ \-(\d+),?(\d+)? \+(\d+),?(\d+)? @@')
    current_hunk = None
    changes = []
    temp_added_lines = []

    for line in diff_output.splitlines():
        match = hunk_re.match(line)
        if match:
            if current_hunk:
                changes.append((current_hunk[0], current_hunk[1], temp_added_lines))
                temp_added_lines = []
            en_start = int(match.group(3)) - 1
            en_count = int(match.group(4)) if match.group(4) else 1
            current_hunk = (en_start, en_count)
        elif line.startswith('+') and not line.startswith('+++'):
            temp_added_lines.append(line[1:])

    if current_hunk:
        changes.append((current_hunk[0], current_hunk[1], temp_added_lines))

    for en_start, en_count, new_en_lines in sorted(changes, key=lambda x: x[0], reverse=True):
        translated_lines = []
        for line in new_en_lines:
            has_newline = line.endswith("\n")
            translated = translate_text(line.strip())
            translated_lines.append(translated + ("\n" if has_newline else "\n"))
        
        it_lines[en_start : en_start + en_count] = translated_lines

    with open(it_path, "w", encoding="utf-8") as f:
        f.writelines(it_lines)

def process_translations():
    changed_files = get_changed_files()
    if not changed_files:
        print("Nessun file modificato.")
        return False

    for filepath in changed_files:
        it_filepath = filepath.replace("docs/en/", "docs/it/")
        
        if not os.path.exists(filepath):
            if os.path.exists(it_filepath):
                os.remove(it_filepath)
                print(f"File eliminato: {it_filepath}")
            continue

        if not os.path.exists(it_filepath):
            translate_full_file(filepath, it_filepath)
        else:
            apply_line_level_translations(filepath, it_filepath)

    return True

if __name__ == "__main__":
    process_translations()
