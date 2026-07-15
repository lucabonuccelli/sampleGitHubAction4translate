# 🤖 Automated Documentation Translation Workflow (Proof of Concept)

*Choose your language / Scegli la lingua:*
* 🇬🇧 [English Version](#-english-version)
* 🇮🇹 [Versione Italiana](#-versione-italiana)

---

## 🇬🇧 English Version

This repository is a **Proof of Concept (PoC)** demonstrating how to automate documentation translation for open-source projects. It keeps translated files constantly synchronized with English updates, reducing maintainer overhead to practically zero.

The system relies entirely on free tools: **GitHub Actions** (for orchestration) and a lightweight **Python script** (for smart incremental translation).

### 🚀 How the Workflow Works

```text
[Edit doc in docs/en/] 
       │
       ▼ (GitHub Action triggers on push)
[Script calculates line-by-line git diff]
       │
       ▼ (Sends ONLY changed lines to Google Translate/LibreTranslate)
[Applies translation maintaining a 1:1 line alignment]
       │
       ▼ (Creates branch l10n-it-update)
[Opens a Pull Request with updated files in docs/it/]
       │
       ▼ (In parallel)
[Opens a GitHub Issue and assigns it to Italian reviewers]
