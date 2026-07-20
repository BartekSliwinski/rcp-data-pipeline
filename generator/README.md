# Generator syntetycznych danych do Systemu Rejestracji Czasu Pracy

Generator syntetycznych danych dla systemów Rejestracji Czasu Pracy (RCP), umożliwiający tworzenie realistycznych zbiorów testowych odwzorowujących strukturę organizacyjną firmy oraz historię zdarzeń wejścia i wyjścia pracowników.

Program pozwala dostosować parametry symulacji do różnych scenariuszy testowych oraz generować dane wykorzystywane podczas projektowania i testowania procesów przetwarzania danych.

## Spis treści

* [O projekcie](#o-projekcie)
* [Model danych](#model-danych)
* [Możliwości generatora](#możliwości-generatora)
* [Generowane pliki CSV](#generowane-pliki-csv)
* [Ustawienia konfiguracji](#ustawienia-konfiguracji)
* [Technologie i narzędzia](#technologie-i-narzędzia)
* [Jak uruchomić](#jak-uruchomić)
* [Możliwości rozwoju](#możliwości-rozwoju)

## O projekcie

System Rejestracji Czasu Pracy (RCP) to system służący do ewidencjonowania czasu pracy pracowników poprzez rejestrowanie zdarzeń wejścia i wyjścia z wykorzystaniem urządzeń rejestrujących. Dane pochodzące z takich systemów mogą być wykorzystywane między innymi do rozliczania czasu pracy, obecności oraz nadgodzin.

Generator został stworzony jako część większego projektu poświęconego transformacji danych pomiędzy systemami RCP. Więcej informacji o całym projekcie znajduje się w głównym repozytorium [Transformacja danych pomiędzy systemami RCP](https://github.com/BartekSliwinski/rcp-data-pipeline).

Celem generatora jest przygotowanie syntetycznych, lecz realistycznych zbiorów danych testowych w formie plików **CSV**, które mogą zostać wykorzystane podczas projektowania, testowania oraz rozwijania procesów przetwarzania danych.

Generator tworzy spójny model danych odwzorowujący podstawowe elementy systemu RCP, obejmujący informacje o strukturze organizacyjnej firmy, pracownikach, urządzeniach rejestrujących oraz zdarzeniach czasu pracy.

## Model danych

Generator tworzy zestaw powiązanych ze sobą tabel reprezentujących uproszczony model danych systemu Rejestracji Czasu Pracy. Diagram poniżej przedstawia relacje pomiędzy poszczególnymi encjami oraz ich najważniejsze atrybuty.

![Model danych](images/Diagram_danych.png)

Model został zaprojektowany w taki sposób, aby zachować spójność referencyjną pomiędzy generowanymi plikami CSV. Dzięki temu mogą one zostać bezpośrednio zaimportowane do relacyjnej bazy danych.

## Możliwości generatora

Generator umożliwia tworzenie spójnych, syntetycznych zbiorów danych dla systemów Rejestracji Czasu Pracy. Najważniejsze możliwości programu:

- **Generowanie kompletnego modelu danych** – tworzenie wszystkich encji wymaganych przez system RCP, między innymi działów, stanowisk, pracowników, urządzeń oraz zdarzeń czasu pracy.

- **Generowanie zdarzeń czasu pracy** – tworzenie historii wejść i wyjść pracowników z uwzględnieniem zależności pomiędzy pracownikiem, urządzeniem oraz czasem wystąpienia zdarzenia.

- **Realistyczna symulacja pracy** – uwzględnianie dni roboczych, weekendów, ustawowych dni wolnych od pracy w Polsce, różnych godzin rozpoczęcia pracy oraz możliwości wystąpienia nadgodzin.

- **Konfigurowalność parametrów symulacji** – możliwość dostosowania między innymi liczby pracowników, zakresu czasowego generowanych danych oraz parametrów wpływających na charakterystykę symulacji.

- **Zachowanie spójności danych** – generowanie powiązanych ze sobą tabel z zachowaniem relacji pomiędzy encjami.

- **Kontrolowane wstrzykiwanie błędów** – możliwość generowania wybranych nieprawidłowości w danych wejścia i wyjścia w celu symulacji rzeczywistych problemów występujących w systemach RCP.

- **Walidacja wygenerowanych danych** – automatyczne sprawdzanie poprawności wygenerowanych plików CSV pod kątem między innymi kompletności, unikalności identyfikatorów oraz poprawności relacji.

- **Powtarzalność generowania danych** – wykorzystanie ziarna losowości, umożliwiającego odtworzenie identycznego zbioru danych przy kolejnych uruchomieniach.

- **Raportowanie wykonania** – zapisywanie podstawowych informacji o przebiegu generowania danych, takich jak czas wykonania, zużycie pamięci, liczba wygenerowanych zdarzeń oraz rozmiar plików wynikowych.

## Generowane pliki CSV

Wynikiem działania generatora jest zestaw plików CSV reprezentujących poszczególne elementy systemu Rejestracji Czasu Pracy. Każdy plik odpowiada osobnej encji modelu danych i zawiera informacje niezbędne do zachowania spójności pomiędzy wygenerowanymi zbiorami.

Wygenerowane pliki mogą zostać wykorzystane jako źródło danych do utworzenia relacyjnej bazy danych, przeprowadzenia testów procesów ETL lub wykonania analiz.

Relacje pomiędzy plikami są odwzorowane za pomocą identyfikatorów kluczy głównych oraz obcych. Dzięki temu możliwe jest odtworzenie struktury organizacji oraz powiązanie zdarzeń czasu pracy z konkretnymi pracownikami i urządzeniami rejestrującymi.

| Plik | Opis |
|---|---|
| departments.csv | Zawiera informacje o działach organizacji, takie jak identyfikator działu oraz jego nazwa. Stanowi podstawę struktury organizacyjnej firmy. |
| positions.csv | Przechowuje informacje o stanowiskach oraz ich przypisaniu do konkretnych działów poprzez identyfikator działu. |
| employees.csv | Zawiera dane pracowników, między innymi dane identyfikacyjne, kontaktowe, informacje o stanowisku oraz statusie zatrudnienia. |
| devices.csv | Zawiera informacje o urządzeniach wykorzystywanych do rejestracji zdarzeń wejścia i wyjścia pracowników. |
| events.csv | Przechowuje historię zdarzeń czasu pracy, zawierając informacje o pracowniku, urządzeniu, typie zdarzenia oraz czasie jego wystąpienia. |

## Ustawienia konfiguracji

Zachowanie generatora kontrolowane jest za pomocą pliku `config.py`, który zawiera najważniejsze parametry wpływające na sposób generowania danych.

Zmiana wartości w pliku konfiguracyjnym pozwala dostosować między innymi rozmiar wygenerowanego zbioru, okres symulacji, strukturę organizacji oraz charakterystykę generowanych zdarzeń czasu pracy.

### Podstawowe ustawienia

| Parametr | Opis |
|---|---|
| `CSV_OUTPUT_DIRECTORY` | Folder, w którym zapisywane są wygenerowane pliki CSV. |
| `RUN_VALIDATIONS` | Określa, czy po zakończeniu generowania danych mają zostać automatycznie uruchomione walidatory. |
| `NUM_OF_EMPLOYEES` | Liczba pracowników generowanych w ramach symulacji. Wpływa bezpośrednio na ilość wygenerowanych danych. |
| `ACTIVE_EMPLOYEE_RATIO` | Określa udział aktywnych pracowników w całej populacji. Pozostali pracownicy otrzymują status nieaktywny. Pole ostatniej modyfikacji w ich przypadku oznacza date zwolnienia. Do tej daty takiemu pracownikowi generowane są zdarzenia.|
| `HIRING_STARTING_DATE` | Najwcześniejsza możliwa data zatrudnienia pracownika. |
| `SIMULATION_START_DATE` | Początek okresu, dla którego generowane są zdarzenia czasu pracy. |
| `SIMULATION_END_DATE` | Koniec okresu, dla którego generowane są zdarzenia czasu pracy. |
| `SEED` | Ziarno generatora losowości umożliwiające ponowne wygenerowanie identycznego zestawu danych. |

Podczas testowania procesów przetwarzania danych zalecane jest zachowanie stałej wartości **SEED**, ponieważ pozwala to porównywać wyniki kolejnych uruchomień programu. Zmiana wartości tego parametru powoduje wygenerowanie nowego, losowego zestawu danych.

### Parametry czasu pracy

Parametry znajdujące się w tej sekcji wpływają na sposób generowania zdarzeń wejścia i wyjścia pracowników.

| Parametr | Opis |
|---|---|
| `WORKING_HOURS_START` | Godzina rozpoczęcia standardowego dnia pracy wykorzystywana podczas generowania zmian. |
| `OVERTIME_PROBABILITY` | Prawdopodobieństwo wystąpienia nadgodzin podczas generowania dnia pracy. |
| `SHIFT_DURATION_MEAN` | Średnia długość standardowej zmiany pracownika wyrażona w godzinach. |
| `SHIFT_DURATION_STD` | Odchylenie od średniej długości zmiany, pozwalające uzyskać naturalne różnice pomiędzy poszczególnymi dniami pracy. |

Zmiana parametrów związanych z czasem pracy wpływa przede wszystkim na dane znajdujące się w pliku `events.csv`, ponieważ określa charakterystykę generowanych zdarzeń wejścia i wyjścia.

### Struktura organizacji

Struktura organizacyjna firmy definiowana jest za pomocą słownika `POSITIONS_IN_DEPARTMENTS`.

Każdy klucz słownika reprezentuje nazwę działu, natomiast przypisana lista zawiera stanowiska dostępne w danym dziale.

Przykład:

```python
"IT": [
    "Data Engineer",
    "Data Analyst",
    "Software Developer"
]
```

Na podstawie tej konfiguracji generator automatycznie tworzy:
- działy organizacyjne,
- stanowiska,
- powiązania pomiędzy stanowiskami a działami.

Liczba działów oraz stanowisk wyznaczana jest automatycznie na podstawie zawartości słownika:

```python
NUM_OF_DEPARTMENTS
NUM_OF_POSITIONS
```

Zmiana zawartości `POSITIONS_IN_DEPARTMENTS` pozwala dostosować profil generowanej organizacji do konkretnego scenariusza testowego.

### Urządzenia rejestrujące

Lista `DEVICES` określa urządzenia dostępne w systemie RCP.

Każde urządzenie posiada własny identyfikator wykorzystywany podczas generowania zdarzeń wejścia i wyjścia.

Liczba urządzeń jest wyznaczana automatycznie:

```python
NUM_OF_DEVICES
```

na podstawie liczby elementów znajdujących się w liście `DEVICES`.

### Przypisanie urządzeń do działów

Słownik `DEPARTMENT_DEVICES` określa, z których urządzeń mogą korzystać pracownicy poszczególnych działów.

Pozwala to ograniczyć losowanie urządzeń podczas generowania zdarzeń i zachować większą spójność pomiędzy strukturą organizacji a historią rejestracji czasu pracy.

Przypisanie odbywa się na podstawie identyfikatorów urządzeń z pliku `devices.csv`
### Generowanie błędów

Generator umożliwia kontrolowane wprowadzanie nieprawidłowości do danych wejścia i wyjścia. Funkcja ta pozwala symulować rzeczywiste problemy występujące w systemach Rejestracji Czasu Pracy oraz testować procesy walidacji i transformacji danych.

| Parametr | Opis |
|---|---|
| `ADD_ERRORS` | Włącza lub wyłącza mechanizm generowania błędów. |
| `MISSING_EVENT_RATIO` | Określa prawdopodobieństwo wygenerowania brakującego zdarzenia wejścia lub wyjścia. |
| `DUPLICATE_EVENT_RATIO` | Określa prawdopodobieństwo wygenerowania zduplikowanego zdarzenia. |

Przykład:

```python
ADD_ERRORS = True
MISSING_EVENT_RATIO = 0.02
DUPLICATE_EVENT_RATIO = 0.01
```

oznacza, że podczas generowania danych zostanie aktywowany mechanizm błędów, który będzie dodawał wybrane nieprawidłowości z określonym prawdopodobieństwem.

\*\*<span style="color: gray;"> Ustawienie w konfiguracji wartości `ADD_ERRORS` na True razem z `RUN_VALIDATIONS` prowadzi z założenia do negatywnego wyniku dla niektórych z testów walidacyjnych.</span>


## Technologie i narzędzia

Projekt został wykonany w języku Python i wykorzystuje biblioteki wspierające generowanie, przetwarzanie oraz kontrolę jakości danych.

### Język

- **Python 3.12+**

Generator został napisany i przetestowany na wersjach Python 3.12 oraz 3.13.

### Wykorzystane biblioteki

| Biblioteka | Zastosowanie |
|---|---|
| **Pandas** | Tworzenie, przetwarzanie oraz zapis wygenerowanych danych w formacie CSV. Wykorzystywana również podczas walidacji danych. |
| **Faker** | Generowanie realistycznych danych fikcyjnych, takich jak imiona, nazwiska, adresy e-mail czy numery telefonów pracowników. |
| **holidays** | Obsługa kalendarza dni wolnych od pracy w Polsce podczas symulacji czasu pracy. |
| **Unidecode** | Normalizacja znaków podczas generowania danych tekstowych, między innymi na potrzeby tworzenia adresów e-mail. |
| **psutil** | Monitorowanie zużycia pamięci podczas wykonywania generatora i tworzenia raportów wykonania. |

### Narzędzia

- **Git** – kontrola wersji projektu.
- **GitHub** – przechowywanie kodu źródłowego oraz dokumentacji.

## Jak uruchomić

### Wymagania wstępne

Upewnij się, że masz zainstalowane:

- **Python 3.12** lub nowszy
- **pip** (menedżer pakietów)

### Instalacja i uruchomienie

Poniższe kroki pozwalają uruchomić generator lokalnie. Przed rozpoczęciem pracy zalecane jest zapoznanie się z plikiem `config.py` i dostosowanie parametrów symulacji do własnych potrzeb.

1. Sklonuj repozytorium GitHub:

    ```bash
    git clone https://github.com/BartekSliwinski/rcp-data-pipeline.git
    cd rcp-data-pipeline/generator
    ```

2. Utwórz środowisko wirtualne:

   - Linux/MacOS:

     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

   - Windows:

     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```

3. Zainstaluj wymagane biblioteki:

    ```bash
    pip install -r requirements.txt
    ```

4. Uruchom generator:

    ```bash
    python main.py
    ```

   W systemach Linux/MacOS może być wymagane użycie polecenia:

    ```bash
    python3 main.py
    ```

Po zakończeniu działania programu wygenerowane pliki CSV zostaną zapisane w katalogu określonym w parametrze `CSV_OUTPUT_DIRECTORY` w pliku `config.py`.

Domyślnie generator tworzy dane w katalogu `output/`.

## Możliwości rozwoju

Dalszy rozwój projektu może obejmować między innymi:

- **Rozszerzenie obsługi kalendarzy pracy** – możliwość generowania danych dla różnych krajów oraz wykorzystania innych kalendarzy dni wolnych od pracy.

- **Obsługa bardziej zaawansowanych grafików pracy** – dodanie pracy wielozmianowej, indywidualnych grafików pracowników, dni wolnych oraz niestandardowych harmonogramów.

- **Bardziej realistyczny model urządzeń rejestrujących** – rozbudowanie mechanizmu przypisywania urządzeń do pracowników, na przykład poprzez uwzględnienie preferowanych urządzeń lub lokalizacji stanowiska pracy.

- **Rozszerzenie mechanizmu generowania błędów** – dodanie kolejnych typów nieprawidłowości występujących w rzeczywistych systemach RCP, takich jak błędne identyfikatory czy niepoprawna kolejność zdarzeń.

- **Benchmarki wydajnościowe** – przygotowanie automatycznych testów pozwalających analizować czas wykonania, zużycie pamięci oraz skalowanie generatora dla różnych konfiguracji.

- **Optymalizacja generowania dużych zbiorów danych** – poprawa wydajności programu przy pracy z większą liczbą pracowników oraz dłuższymi okresami symulacji.
