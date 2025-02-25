# 🔍 Git Commit Lister

<div align="center">

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg?style=flat-square)
![Python](https://img.shields.io/badge/python-3.6+-green.svg?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-orange.svg?style=flat-square)

*[English](#english-documentation) | [Polski](#polska-dokumentacja)*

</div>

---

<h2 id="polska-dokumentacja">🇵🇱 Polska dokumentacja</h2>

## 📖 O programie

**Git Commit Lister** to eleganckie i skuteczne narzędzie do przeglądania i analizowania historii commitów w repozytoriach Git. Program wyświetla i numeruje commity, co jest nieocenione przy planowaniu operacji takich jak modyfikacja authorów, rebase, czy cherry-pick.

<div align="center">

```
┌─────────────────────────────────────────────┐
│ Numer ↔ Hash ↔ Data ↔ Autor ↔ Email ↔ Opis │
└─────────────────────────────────────────────┘
```

</div>

## ✨ Kluczowe funkcje

- **📋 Numerowana lista** - pokazuje commity z numerami porządkowymi liczonymi od HEAD
- **🔑 Identyfikacja** - wyświetla skrócone hashe, daty, autorów i opisy
- **📧 Pełne adresy email** - pokazuje kompletne adresy email bez obcinania
- **💾 Eksport** - zapisuje historię commitów do pliku tekstowego
- **📂 Elastyczność** - umożliwia wybór folderu docelowego dla eksportowanych plików

## 🔧 Wymagania

| Wymaganie | Minimalna wersja |
|-----------|------------------|
| Python    | 3.6+             |
| Git       | Dowolna          |
| Uprawnienia | Odczyt repozytorium, zapis w katalogu eksportu |

## 🚀 Instalacja

1. Pobierz plik `git_commit_lister.py`
2. Upewnij się, że masz Pythona 3.6+ (`python --version`)
3. Upewnij się, że Git jest w ścieżce systemowej (`git --version`)

> **Uwaga**: Program wykorzystuje tylko standardową bibliotekę Pythona, nie wymaga dodatkowych pakietów!

## 🎮 Jak używać

```bash
python git_commit_lister.py
```

### Krok po kroku:

1️⃣ **Uruchom program** w terminalu/wierszu poleceń  
2️⃣ **Podaj ścieżkę** do repozytorium (lub `.` dla bieżącego)  
3️⃣ **Przeglądaj listę** commitów wyświetlonych na ekranie  
4️⃣ **Zdecyduj** czy zapisać listę do pliku (t/n)  
5️⃣ **Wybierz folder** docelowy lub zaakceptuj domyślny  

#### Struktura wyświetlanych danych:

```
Nr   Hash     Data        Autor              Email                       Opis
1    a7b3c2d  2025-02-20  Jan Kowalski       jan.kowalski@example.com   Poprawa interfejsu
2    e5f8g1h  2025-02-19  Anna Nowak         anna.nowak@example.com     Dodanie nowych testów
```

## 🌟 Przykłady zastosowań

- 🔄 **Rebase interaktywny** - łatwa identyfikacja commitów do squasha, edycji itd.
- 🖋️ **Zmiana autora** - znajdowanie commitów wymagających korekty danych autora
- 📊 **Dokumentacja** - tworzenie raportów z historii projektu
- 🔍 **Analiza** - przegląd zmian w czasie

## ❓ Rozwiązywanie problemów

| Problem | Rozwiązanie |
|---------|-------------|
| "Git nie jest zainstalowany..." | Sprawdź instalację Git: `git --version` |
| "Podana ścieżka nie jest repozytorium..." | Upewnij się, że katalog zawiera folder `.git` |
| "Błąd podczas zapisywania..." | Sprawdź uprawnienia do zapisu lub zmień folder docelowy |

---

<h2 id="english-documentation">🇬🇧 English documentation</h2>

## 📖 About the program

**Git Commit Lister** is an elegant and effective tool for browsing and analyzing commit history in Git repositories. The program displays and numbers commits, which is invaluable when planning operations such as author modification, rebase, or cherry-pick.

<div align="center">

```
┌─────────────────────────────────────────────┐
│ Number ↔ Hash ↔ Date ↔ Author ↔ Email ↔ Message │
└─────────────────────────────────────────────┘
```

</div>

## ✨ Key features

- **📋 Numbered list** - shows commits with position numbers counted from HEAD
- **🔑 Identification** - displays shortened hashes, dates, authors and descriptions
- **📧 Full email addresses** - shows complete email addresses without truncation
- **💾 Export** - saves commit history to a text file
- **📂 Flexibility** - allows selection of target folder for exported files

## 🔧 Requirements

| Requirement | Minimum version |
|-------------|-----------------|
| Python      | 3.6+            |
| Git         | Any             |
| Permissions | Repository read access, write access in export directory |

## 🚀 Installation

1. Download the `git_commit_lister.py` file
2. Make sure you have Python 3.6+ (`python --version`)
3. Make sure Git is in your system path (`git --version`)

> **Note**: The program uses only the standard Python library, no additional packages required!

## 🎮 How to use

```bash
python git_commit_lister.py
```

### Step by step:

1️⃣ **Run the program** in terminal/command line  
2️⃣ **Provide path** to repository (or `.` for current)  
3️⃣ **Browse the list** of commits displayed on screen  
4️⃣ **Decide** whether to save the list to a file (y/n)  
5️⃣ **Choose target folder** or accept default  

#### Structure of displayed data:

```
No   Hash     Date        Author             Email                       Message
1    a7b3c2d  2025-02-20  John Smith         john.smith@example.com     Interface improvements
2    e5f8g1h  2025-02-19  Jane Doe           jane.doe@example.com       Add new tests
```

## 🌟 Example applications

- 🔄 **Interactive rebase** - easy identification of commits for squashing, editing etc.
- 🖋️ **Author change** - finding commits requiring author data correction
- 📊 **Documentation** - creating reports from project history
- 🔍 **Analysis** - reviewing changes over time

## ❓ Troubleshooting

| Problem | Solution |
|---------|----------|
| "Git is not installed..." | Check Git installation: `git --version` |
| "The specified path is not a Git repository..." | Make sure the directory contains a `.git` folder |
| "Error while saving..." | Check write permissions or change target folder |

---

<div align="center">

## 🛠️ Powodzenia z Twoimi projektami Git! / Good luck with your Git projects!

</div>