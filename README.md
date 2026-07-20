# RCP Data Pipeline

Projekt **RCP Data Pipeline** to demonstracyjny pipeline przetwarzania danych systemu Rejestracji Czasu Pracy (RCP). Celem projektu jest zaprezentowanie pełnego przepływu danych od generowania przykładowych rekordów, przez import do lokalnej bazy MS SQL Server, aż po planowane dalsze przetwarzanie w chmurze Microsoft Azure. Scenariusz projektowy (opisany poniżej) jest fikcyjny i służy przede wszystkim do pokazania umiejętności budowy złożonych procesów przetwarzania danych.

## Spis treści

- [O projekcie](#o-projekcie)
- [Założenia projektu](#założenia-projektu)
- [Przepływ danych (architektura)](#przep%C5%82yw-danych-architektura)
- [Komponenty rozwiązania](#komponenty-rozwi%C4%85zania)
- [Możliwości rozwoju](#mo%C5%BCliwo%C5%9Bci-rozwoju)

## O projekcie

System Rejestracji Czasu Pracy (RCP) służy do ewidencjonowania czasu pracy pracowników poprzez rejestrowanie zdarzeń wejścia i wyjścia. W tym projekcie tworzymy **demonstacyjny pipeline danych** pokazujący, jak można przygotować i przetransformować dane z systemów RCP. Pipeline obejmuje:

- **Generator danych** – moduł tworzący syntetyczne pliki CSV z danymi RCP (struktura organizacyjna, lista pracowników, zdarzenia wejść/wyjść).
- **Konektor SQL** – moduł ładujący wygenerowane dane do lokalnej bazy MS SQL Server, automatycznie tworząc potrzebne tabele i relacje.
- **Środowisko chmurowe (Azure)** – planowana faza dalszego przetwarzania danych w chmurze, z użyciem usług takich jak Azure SQL Database, Azure Data Factory czy Azure Databricks.

Każdy z powyższych komponentów posiada własny README z instrukcją uruchomienia i konfiguracji. Niniejsze README opisuje ogólną architekturę i cel całego projektu jako całości.

## Założenia projektu

**Scenariusz:** Firma planuje migrację do nowego systemu Rejestracji Czasu Pracy. W okresie przejściowym oba systemy (stary i nowy) działają równolegle. W związku z tym konieczne jest przygotowanie rozwiązania umożliwiającego automatyczne przenoszenie i transformację danych ze starego systemu do nowego, przy zachowaniu ich spójności i integralności.

**Założenia techniczne:** 

- Stary system przechowuje dane w lokalnej bazie danych na serwerze firmowym (on-premises).
- Nowy system będzie wykorzystywał bazę danych w chmurze (Microsoft Azure).
- Struktury danych w obu systemach różnią się, dlatego potrzebna jest ich transformacja podczas migracji.
- Synchronizacja powinna następować okresowo (np. codziennie) i być w pełni zautomatyzowana.
- Przesyłanie danych musi zapewniać spójność i integralność (zmiany nie mogą powodować niespójności).
- Proces powinien uwzględniać raportowanie i obsługę błędów oraz umożliwiać monitorowanie przebiegu.
- Rozwiązanie musi być gotowe na przyszłe wyłączenie starego systemu bez konieczności zmian po stronie nowego systemu.

## Przepływ danych (architektura)

Poniższy diagram Mermaid ilustruje główne etapy przetwarzania danych w projekcie:

```mermaid
flowchart LR
    Generator[Generator danych (CSV)] --> CSV[Pliki CSV]
    CSV --> Konektor[Konektor SQL]
    Konektor --> OnPrem[MS SQL Server (on-premises)]
    subgraph Azure ["Microsoft Azure"]
        AzureSQL["Azure SQL Database"]
        DataFactory["Azure Data Factory"]
        Databricks["Azure Databricks"]
    end
    OnPrem --> AzureSQL
    AzureSQL --> DataFactory
    DataFactory --> Databricks
