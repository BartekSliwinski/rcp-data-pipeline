# Generator syntetycznych danych do Systemu Rejestracji Czasu Pracy

Generator syntetycznych danych przeznaczony do tworzenia realistycznych zbiorów danych dla systemu Rejestracji Czasu Pracy (RCP). Program generuje informacje o strukturze organizacyjnej firmy, pracownikach oraz zdarzeniach związanych z rejestracją czasu pracy. Dzięki szerokim możliwościom konfiguracji pozwala dostosować charakterystykę wygenerowanych danych do różnych scenariuszy testowych. Dodatkowo umożliwia kontrolowane wstrzykiwanie błędów do danych, co pozwala symulować rzeczywiste problemy występujące w systemach RCP.

## Spis treści

* [O projekcie](#o-projekcie)
* [Model danych](#model-danych)
* [Główne funkcje](#główne-funkcje)
* [Generowane pliki CSV](#generowane-pliki-csv)
* [Ustawienia konfiguracji](#ustawienia-konfiguracji)
* [Technologie i narzędzia](#technologie-i-narzędzia)
* [Jak uruchomić](#jak-uruchomić)
* [Możliwości rozwoju](#możliwości-rozwoju)

## O projekcie
System Rejestracji Czasu Pracy (RCP) to system służący do ewidencjonowania czasu pracy pracowników poprzez rejestrowanie zdarzeń wejścia i wyjścia z wykorzystaniem dedykowanych urządzeń. Zebrane dane są wykorzystywane między innymi do rozliczania czasu pracy, nadgodzin oraz obecności pracowników.

Generator został stworzony jako część większego projektu poświęconego transformacji danych pomiędzy systemami RCP. Więcej informacji o całym projekcie znajduje się w głównym repozytorium [Transformacja danych pomiędzy systemami RCP](https://github.com/BartekSliwinski/Transformacja_danych_pomiedzy_systemami_RCP).

Program służy do generowania realistycznych danych testowych w postaci plików **CSV**, które mogą zostać wykorzystane jako źródło danych dla relacyjnej bazy danych, procesów ETL lub analiz.

Generator tworzy spójny model organizacji obejmujący:
- strukturę działów i stanowisk,
- pracowników wraz z podstawowymi informacjami,
- urządzenia rejestrujące,
- zdarzenia wejść i wyjść pracowników.

Podczas generowania danych uwzględniane są zależności pomiędzy encjami oraz kalendarz pracy, w tym weekendy i ustawowe dni wolne od pracy w Polsce. Zachowanie generatora może zostać dostosowane za pomocą pliku konfiguracyjnego, umożliwiającego między innymi zmianę liczby pracowników, zakresu symulacji czy parametrów generowania zdarzeń.

Generator wykorzystuje ziarno losowości (seed), dzięki czemu możliwe jest wielokrotne odtworzenie identycznego zbioru danych.

Projekt zawiera również moduł walidacji wygenerowanych danych oraz możliwość kontrolowanego wstrzykiwania błędów do zdarzeń, co pozwala symulować rzeczywiste problemy spotykane w systemach RCP.

## Model danych

## Główne funkcje

## Generowane dane
![Diagram ERD](images/Diagram_danych.png)

| Plik | Opis |
|---|---|
| departments.csv | Lista działów w firmie |
| positions.csv | Stanowiska przypisane do konkretnych działów |
| employees.csv | Dane pracowników  |
| devices.csv | Urządzenia rejestrujące wydarzenia |
| worklogs.csv | Zdarzenia wejścia i wyjścia pracowników |

## Ustawienia konfiguracji

## Technologie i narzędzia

* **Język:** Python 3.13
* **Biblioteki:** Pandas, Faker <!--dac reszte-->

---
## Jak uruchomić

### Wymagania wstępne

Upewnij się, że masz zainstalowane:

- **Python 3.10** lub nowszy
- **pip** (menedżer pakietów)

### Instalacja i uruchomienie

Podążaj za podanymi poniżej krokami aby uruchomić generator na swojej maszynie. Zwróć uwagę na komendy zależne od systemu operacyjnego.

1. Sklonuj repozytorium Github:

    ```bash
    git clone https://github.com/BartekSliwinski/Transformacja_danych_pomiedzy_systemami_RCP.git
    cd Transformacja_danych_pomiedzy_systemami_RCP/generator
    ```
2. Stwórz środowisko wirtualne

   - Linux/MacOS:

     ```bash
     python -m venv venv
     source venv/bin/activate
     ```
   - Windows:

     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
3. Zainstaluj wymagane pakiety:

    ```bash
    pip install -r requirements.txt
    ```
4. Uruchom aplikację:

    ```bash
    python main.py
    ```


## Możliwości rozwoju

