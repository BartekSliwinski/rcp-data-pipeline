# Generator syntetycznych danych do sytemu Rejestracji Czasu Pracy

Program do generowania danych o pracownikach i zdarzeniach wejścia/wyjścia na początek i koniec ich dnia pracy. 

-- zdjęcie z bazy danych połączonych tabel--
## Spis treści

* [O projekcie](#o-projekcie)
* [Główne funkcje](#główne-funkcje)
* [Generowane dane](#generowane-dane)
* [Ustawienia konfiguracji](#ustawienia-konfiguracji)
* [Technologie i narzędzia](#technologie-i-narzędzia)
* [Jak uruchomić](#jak-uruchomić)
* [Możliwości rozwoju](#możliwości-rozwoju)

## O projekcie

Program ten powstał jako część większego projektu. Więcej o nim możesz przeczytać [tutaj](https://github.com/BartekSliwinski/Transformacja_danych_pomiedzy_systemami_RCP).

Służy on do generowania realistycznych danych do systemów RCP. Jego wynikiem końcowym są pliki w formie **csv**, które mogą posłużyć do stworzenia bazy danych lub arkusza.
<!-- aaa -->
<!-- 
Jest konfigurowalny
Bierze pod uwagę weekendy i święta.
-->
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

