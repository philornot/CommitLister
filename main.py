#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Git Commit Lister - Program do listowania commitów w repozytorium Git.

Ten program wyświetla listę wszystkich commitów w repozytorium Git
wraz z ich numerami porządkowymi liczonymi od HEAD.
"""

import os
import subprocess
from datetime import datetime


# Klasa kolorów dla terminala
class TerminalColors:
    """Definicje kolorów dla terminala."""
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# Funkcje do logowania
def log_error(message):
    """Wypisuje błąd do konsoli."""
    print(f"{TerminalColors.FAIL}{message}{TerminalColors.ENDC}")


def log_success(message):
    """Wypisuje komunikat sukcesu do konsoli."""
    print(f"{TerminalColors.GREEN}{message}{TerminalColors.ENDC}")


def log_info(message):
    """Wypisuje informację do konsoli."""
    print(message)


def log_warning(message):
    """Wypisuje ostrzeżenie do konsoli."""
    print(f"{TerminalColors.WARNING}{message}{TerminalColors.ENDC}")


def log_header(message):
    """Wypisuje nagłówek do konsoli."""
    print(f"\n{TerminalColors.HEADER}{message}{TerminalColors.ENDC}")


def display_separator(length=100, character="-"):
    """Wyświetla separator w konsoli."""
    print(character * length)


# Funkcje operacji na Git
def check_git_installed():
    """
    Sprawdza, czy Git jest zainstalowany i dostępny w PATH.

    Returns:
        bool: True jeśli Git jest zainstalowany, False w przeciwnym razie
    """
    try:
        git_version_process = subprocess.run(
            ["git", "--version"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False
        )
        return git_version_process.returncode == 0
    except:
        return False


def is_git_repository(repository_path):
    """
    Sprawdza, czy podana ścieżka jest repozytorium Git.

    Args:
        repository_path (str): Ścieżka do sprawdzenia

    Returns:
        bool: True jeśli podana ścieżka jest repozytorium Git, False w przeciwnym razie
    """
    try:
        if not os.path.isdir(repository_path):
            log_warning(f"Ścieżka {repository_path} nie jest katalogiem.")
            return False

        git_check_process = subprocess.run(
            ["git", "-C", repository_path, "rev-parse", "--is-inside-work-tree"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=False
        )

        is_git_repo = git_check_process.returncode == 0

        if not is_git_repo:
            log_warning(f"Katalog {repository_path} nie jest repozytorium Git.")

        return is_git_repo
    except:
        return False


def get_git_commits(repository_path):
    """
    Pobiera listę wszystkich commitów z repozytorium Git.

    Args:
        repository_path (str): Ścieżka do repozytorium

    Returns:
        list: Lista słowników z informacjami o commitach
    """
    try:
        # Uruchamiamy git log aby pobrać wszystkie commity z pełnym hashem
        git_log_process = subprocess.run(
            ["git", "-C", repository_path, "log", "--pretty=format:%H|%an|%ae|%ad|%s", "--date=short"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )

        # Przetwarzamy wyjście
        commits_output = git_log_process.stdout.strip()

        if not commits_output:
            log_warning("Brak commitów w repozytorium.")
            return []

        commits_list = []

        # Parsujemy commity - linia po linii
        for line_index, line in enumerate(commits_output.split('\n'), 1):
            if not line:
                continue

            # Dzielimy linię na części wg separatora |
            parts = line.split('|', 4)

            if len(parts) == 5:
                commit_data = {
                    'position': line_index,  # Pozycja liczona od HEAD
                    'hash': parts[0],
                    'author_name': parts[1],
                    'author_email': parts[2],
                    'date': parts[3],
                    'subject': parts[4]
                }
                commits_list.append(commit_data)

        return commits_list
    except Exception as e:
        log_error(f"Błąd podczas pobierania listy commitów: {e}")
        return []


def display_commits(commits):
    """
    Wyświetla listę commitów w czytelnym formacie.

    Args:
        commits (list): Lista commitów do wyświetlenia
    """
    if not commits:
        log_warning("Brak commitów do wyświetlenia.")
        return

    log_header("Lista commitów w repozytorium:")

    # Wyświetlamy nagłówek tabeli
    print(
        f"{TerminalColors.BOLD}{'Nr':4} {'Hash':8} {'Data':12} {'Autor':20} {'Email'} {'Opis':60}{TerminalColors.ENDC}")
    display_separator(140)

    # Wyświetlamy każdy commit
    for commit in commits:
        # Skracamy hash
        hash_display = commit['hash'][:7]
        email_display = commit['author_email']

        # Dla autora zachowujemy pewne ograniczenie, żeby tabela była czytelna
        author_display = commit['author_name']
        if len(author_display) > 19:
            author_display = author_display[:16] + "..."

        date_display = commit['date']

        # Limitujemy tylko wiadomość commita, jeśli jest bardzo długa
        subject_display = commit['subject']
        if len(subject_display) > 60:
            subject_display = subject_display[:57] + "..."

        print(
            f"{commit['position']:4} {hash_display:8} {date_display:12} {author_display:20} {email_display:<35} {subject_display}")


def save_commits_to_file(commits, directory="./commits_exports"):
    """
    Zapisuje listę commitów do pliku.

    Args:
        commits (list): Lista commitów do zapisania
        directory (str): Katalog, w którym będzie zapisany plik

    Returns:
        bool: True jeśli zapis się powiódł, False w przeciwnym razie
    """
    try:
        # Sprawdzamy czy katalog istnieje, jeśli nie - tworzymy go
        if not os.path.exists(directory):
            os.makedirs(directory)

        # Tworzymy nazwę pliku z datą i godziną
        current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        file_name = f"git_commits_{current_time}.txt"
        file_path = os.path.join(directory, file_name)

        # Zapisujemy dane do pliku
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(
                "Nr   Hash        Data         Autor                Email                                    Opis\n")
            file.write("-" * 140 + "\n")

            for commit in commits:
                # Skracamy hash
                hash_display = commit['hash'][:7]
                email_display = commit['author_email']

                # Dla autora zachowujemy pewne ograniczenie, żeby plik był czytelny
                author_display = commit['author_name']
                if len(author_display) > 19:
                    author_display = author_display[:16] + "..."

                date_display = commit['date']

                # Limitujemy tylko wiadomość commita, jeśli jest bardzo długa
                subject_display = commit['subject']
                if len(subject_display) > 60:
                    subject_display = subject_display[:57] + "..."

                file.write(
                    f"{commit['position']:4} {hash_display:11} {date_display:12} {author_display:20} {email_display:<40} {subject_display}\n")

        log_success(f"Lista commitów została zapisana do pliku: {file_path}")
        return True
    except Exception as e:
        log_error(f"Błąd podczas zapisywania do pliku: {e}")
        return False


def main():
    """Główna funkcja programu."""
    try:
        # Wyświetlamy nagłówek programu
        log_header("Program do listowania commitów w Git")

        # Sprawdzamy, czy Git jest zainstalowany
        if not check_git_installed():
            log_error("Git nie jest zainstalowany lub nie jest dostępny w PATH.")
            return

        # Pobieramy ścieżkę do repozytorium
        repository_path = input("Podaj ścieżkę do repozytorium (lub . dla bieżącego katalogu): ").strip()
        if not repository_path:
            repository_path = "."

        # Sprawdzamy, czy to jest repozytorium Git
        if not is_git_repository(repository_path):
            log_error("Podana ścieżka nie jest repozytorium Git.")
            return

        # Pobieramy listę commitów
        log_info("Pobieram listę commitów z repozytorium...")
        commits = get_git_commits(repository_path)

        if not commits:
            log_error("Nie znaleziono commitów w repozytorium.")
            return

        # Wyświetlamy commity
        display_commits(commits)

        # Pytamy, czy zapisać listę do pliku
        save_to_file = input("\nCzy chcesz zapisać listę commitów do pliku? (t/n): ").lower().startswith('t')

        if save_to_file:
            # Pytamy o folder do zapisu
            save_folder = input("Podaj ścieżkę do zapisania pliku (lub Enter dla folderu ./commits_exports): ").strip()
            if save_folder:
                save_commits_to_file(commits, directory=save_folder)
            else:
                save_commits_to_file(commits)

    except KeyboardInterrupt:
        log_warning("\nOperacja przerwana przez użytkownika.")
    except Exception as e:
        log_error(f"\nWystąpił nieoczekiwany błąd: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
