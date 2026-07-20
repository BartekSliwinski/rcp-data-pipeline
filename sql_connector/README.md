# Konektor SQL dla danych systemu Rejestracji Czasu Pracy

Konektor danych dla systemu Rejestracji Czasu Pracy (RCP), umożliwiający import danych opisujących strukturę organizacyjną firmy, pracowników, urządzenia rejestrujące oraz zdarzenia czasu pracy z plików CSV do relacyjnej bazy danych MS SQL Server.

Moduł odpowiada za przygotowanie wymaganej struktury tabel, zachowanie zależności pomiędzy encjami oraz kontrolowanie przebiegu procesu ładowania danych poprzez system logowania.

## Spis treści

* [O projekcie](#o-projekcie)
* [Moduły](#moduły)
* [Struktura bazy danych](#struktura-bazy-danych)
* [Ustawienia konfiguracji](#ustawienia-konfiguracji)
* [Technologie i narzędzia](#technologie-i-narzędzia)
* [Jak uruchomić](#jak-uruchomić)
* [Możliwości rozwoju](#możliwości-rozwoju)

## O projekcie

System Rejestracji Czasu Pracy (RCP) to system służący do ewidencjonowania czasu pracy pracowników poprzez rejestrowanie zdarzeń wejścia i wyjścia z wykorzystaniem urządzeń rejestrujących. Dane pochodzące z takich systemów mogą być wykorzystywane między innymi do rozliczania czasu pracy, obecności oraz nadgodzin.

Konektor został stworzony jako część większego projektu poświęconego transformacji danych pomiędzy systemami RCP. Więcej informacji o całym projekcie znajduje się w głównym repozytorium: [Transformacja danych pomiędzy systemami RCP](https://github.com/BartekSliwinski/rcp-data-pipeline).

Celem konektora jest automatyczne przygotowanie struktury relacyjnej bazy danych MS SQL Server oraz zaimportowanie do niej danych zapisanych w plikach CSV. Podczas wykonywania operacji moduł tworzy wymagane tabele, zachowuje relacje pomiędzy nimi oraz umożliwia dwa tryby ładowania danych: dopisywanie rekordów lub całkowite zastąpienie istniejącej zawartości bazy.

Po zakończeniu procesu baza danych zawiera kompletny model systemu RCP wraz z zachowaniem spójności referencyjnej pomiędzy wszystkimi encjami i jest gotowa do wykorzystania w dalszych etapach projektu lub do własnych analiz i testów.

## Moduły

Konektor został podzielony na kilka niezależnych modułów odpowiedzialnych za poszczególne etapy przygotowania oraz załadowania danych do bazy MS SQL Server. Taki podział upraszcza rozwój projektu, ułatwia testowanie oraz pozwala oddzielić logikę związaną z połączeniem z bazą danych, tworzeniem schematu oraz importem danych.

Przebieg wykonywania programu przedstawia poniższy diagram.

```mermaid
flowchart LR
    A[main.py]
    B[database.py]
    C[schema.py]
    D[loader.py]

    A --> B
    B --> C
    C --> D
```

Poszczególne moduły pełnią następujące funkcje:

| Moduł | Odpowiedzialność |
|---|---|
| [`main.py`](main.py) | Koordynuje cały proces działania konektora, obsługuje błędy krytyczne oraz zamyka połączenie z bazą danych. |
| [`database.py`](database.py) | Nawiązuje połączenie z bazą danych oraz przygotowuje tryb ładowania danych (`append` / `replace`). |
| [`schema.py`](schema.py) | Tworzy strukturę relacyjnej bazy danych, w tym tabele, relacje oraz ograniczenia integralności. |
| [`loader.py`](loader.py) | Importuje dane z plików CSV do odpowiednich tabel z zachowaniem identyfikatorów (`IDENTITY_INSERT`). |
| [`logger.py`](logger.py) | Konfiguruje wspólny system logowania wykorzystywany przez wszystkie moduły programu. |

## Struktura bazy danych

Konektor tworzy relacyjną strukturę bazy danych przeznaczoną do przechowywania danych systemu Rejestracji Czasu Pracy. Model obejmuje informacje o strukturze organizacyjnej firmy, pracownikach, urządzeniach rejestrujących oraz zdarzeniach wejścia i wyjścia.

Poniższy diagram przedstawia strukturę tworzonych tabel oraz relacje pomiędzy nimi:

![Schemat bazy danych](docs/database_schema.png)

Wszystkie relacje pomiędzy tabelami zabezpieczone są za pomocą kluczy głównych, kluczy obcych oraz odpowiednich ograniczeń integralności, dzięki czemu importowane dane zachowują spójność referencyjną.

## Ustawienia konfiguracji

Zachowanie konektora kontrolowane jest za pomocą pliku [`config.py`](config.py), który zawiera parametry odpowiedzialne za tryb ładowania danych, lokalizację plików CSV oraz konfigurację połączenia z bazą danych MS SQL Server.

| Parametr | Opis |
|---|---|
| `LOAD_MODE` | Określa sposób ładowania danych do bazy. Wartość `append` dodaje nowe rekordy do istniejących danych, natomiast `replace` usuwa aktualną zawartość tabel przed rozpoczęciem importu. |
| `CSV_DIRECTORY` | Ścieżka do katalogu zawierającego pliki CSV przeznaczone do importu. |
| `SQL_SERVER_NAME` | Nazwa serwera SQL Server, z którym nawiązywane jest połączenie. |
| `DATABASE_NAME` | Nazwa docelowej bazy danych, do której importowane są dane. |
| `SQL_ODBC_DRIVER` | Sterownik ODBC wykorzystywany podczas połączenia z SQL Server. |
| `TRUSTED_CONNECTION` | Określa wykorzystanie uwierzytelniania systemowego Windows podczas łączenia z bazą danych. |
| `ENCRYPT` | Włącza lub wyłącza szyfrowanie połączenia z SQL Server. |
| `TRUSTED_SERVER_CERTIFICATE` | Określa, czy certyfikat serwera ma być akceptowany bez dodatkowej weryfikacji. |

> Tryb `replace` powinien być stosowany ostrożnie, ponieważ powoduje usunięcie istniejących danych z obsługiwanych tabel przed rozpoczęciem importu.

## Technologie i narzędzia

Projekt został wykonany w języku Python i wykorzystuje biblioteki umożliwiające komunikację z bazą danych MS SQL Server, przetwarzanie plików CSV oraz obsługę procesu importu danych.

### Język

- **Python 3.13+**

Konektor został napisany i przetestowany na wersji Python 3.13.

### Wykorzystane biblioteki

| Biblioteka | Zastosowanie |
|---|---|
| **SQLAlchemy** | Tworzenie połączenia z bazą danych oraz wykonywanie operacji SQL poprzez warstwę abstrakcji ORM/SQL Expression Language. |
| **pyodbc** | Sterownik umożliwiający komunikację pomiędzy Pythonem a bazą danych MS SQL Server poprzez protokół ODBC. |
| **Pandas** | Odczyt oraz przygotowanie danych z plików CSV przed załadowaniem ich do tabel bazy danych. |
| **colorlog** | Konfiguracja kolorowego formatowania komunikatów systemu logowania wyświetlanych podczas działania programu. |

### Narzędzia

| Narzędzie | Zastosowanie |
|---|---|
| **Microsoft SQL Server** | Relacyjna baza danych wykorzystywana jako docelowe miejsce importu danych. |
| **ODBC Driver 18 for SQL Server** | Sterownik wykorzystywany do komunikacji z serwerem SQL Server. |
| **SQL Server Management Studio (SSMS)** | Narzędzie wykorzystywane do zarządzania bazą danych oraz weryfikacji poprawności działania konektora. |
| **Git** | Kontrola wersji projektu. |
| **GitHub** | Przechowywanie kodu źródłowego oraz dokumentacji projektu. |

## Jak uruchomić

### Wymagania wstępne

Przed uruchomieniem konektora upewnij się, że masz zainstalowane:

- **Python 3.13** lub nowszy
- **pip** (menedżer pakietów Python)
- **Microsoft SQL Server** wraz z utworzoną instancją bazy danych
- **ODBC Driver 18 for SQL Server** wymagany do komunikacji pomiędzy Pythonem a SQL Server

Dodatkowo opcjonalnie zalecane jest zainstalowanie:

- **SQL Server Management Studio (SSMS)** – narzędzie umożliwiające wygodne zarządzanie bazą danych oraz weryfikację załadowanych danych.

Przydatne linki:

- Python: https://www.python.org/downloads/
- Microsoft SQL Server: https://www.microsoft.com/sql-server
- ODBC Driver 18 for SQL Server: https://learn.microsoft.com/sql/connect/odbc/download-odbc-driver-for-sql-server
- SQL Server Management Studio: https://learn.microsoft.com/sql/ssms/download-sql-server-management-studio-ssms

### Przygotowanie bazy danych

Przed pierwszym uruchomieniem konektora należy przygotować docelową bazę danych w Microsoft SQL Server.

Konektor nie tworzy samej bazy danych, a jedynie przygotowuje jej strukturę wewnętrzną (tabele, klucze główne, klucze obce oraz ograniczenia integralności).

Utwórz pustą bazę danych:

```sql
CREATE DATABASE rcp_system;
```

Następnie upewnij się, że dane połączeniowe w pliku [`config.py`](config.py) odpowiadają utworzonej bazie:

```python
SQL_SERVER_NAME = "nazwa_serwera"
DATABASE_NAME = "rcp_system"
```

Podczas pierwszego uruchomienia konektor automatycznie utworzy wymagane tabele oraz załaduje dane z plików CSV.

### Instalacja i uruchomienie

1. Sklonuj repozytorium:

    ```bash
    git clone https://github.com/BartekSliwinski/rcp-data-pipeline.git
    cd rcp-data-pipeline/sql_connector
    ```

2. Utwórz środowisko wirtualne:
    *   Windows:

        ```bash
        python -m venv venv
        venv\Scripts\activate
        ```

    *   Linux/MacOS:

        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```

3. Zainstaluj wymagane biblioteki:

    ```bash
    pip install -r requirements.txt
    ```

4. Skonfiguruj połączenie z bazą danych w pliku [`config.py`](config.py). Należy uzupełnić między innymi:
    *   nazwę serwera SQL (`SQL_SERVER_NAME`),
    *   nazwę docelowej bazy danych (`DATABASE_NAME`),
    *   tryb ładowania danych (`LOAD_MODE`),
    *   lokalizację plików CSV (`CSV_DIRECTORY`).

5. Uruchom konektor:

    ```bash
    python main.py
    ```

    Po zakończeniu działania programu baza danych zostanie przygotowana zgodnie ze schematem oraz zasilona danymi znajdującymi się w katalogu wskazanym w konfiguracji.

## Możliwości rozwoju

Dalszy rozwój konektora może obejmować między innymi:

- **Obsługa cyklicznego ładowania danych** – dostosowanie konektora do regularnego importu nowych partii danych, na przykład w ramach codziennego procesu zasilania bazy danych.
- **Przyrostowe ładowanie danych** – rozwinięcie obecnego mechanizmu importu o wykrywanie nowych oraz zmienionych rekordów, umożliwiające przetwarzanie wyłącznie aktualnych danych zamiast ponownego ładowania całego zbioru.
