# Ewidencja Treningów Sportowych

Aplikacja webowa napisana w języku **Python** z wykorzystaniem frameworka **Flask**, służąca do rejestrowania oraz zaawansowanej analizy aktywności fizycznej. Projekt został przygotowany w ramach zaliczenia laboratorium programowania.

## Główne Funkcje Aplikacji

* **Zarządzanie Treningami:** Możliwość dodawania nowych aktywności oraz usuwania wpisów z historii w czasie rzeczywistym.
* **Inteligentny Backend (Automatyzacja):** System automatycznie szacuje wydatki energetyczne (spalone kalorie) na podstawie wybranego typu sportu oraz czasu trwania, wykorzystując wbudowany w Pythonie algorytm mapujący.Użytkownik może również wpisać własną, precyzyjną wartość.
* **Trwałość Danych:** Dane są trwale zapisywane i serializowane do pliku w formacie tekstowym `JSON`.
* **Panel Statystyk Okresowych:** Automatyczne grupowanie i sumowanie danych na bieżący tydzień, miesiąc oraz rok za pomocą modułu `datetime`.
* **Zaawansowane Filtrowanie Zakresów:** Możliwość wyboru własnego przedziału dat (od-do). System dynamicznie wylicza dla wskazanego okresu liczbę treningów, łączny czas, średni czas pojedynczej sesji oraz generuje szczegółowy podział tekstowy, ile razy dana aktywność została wykonana.
* **UI:** Responsywny interfejs użytkownika.

---

## Struktura Projektu

```text
├── app.py              # Główny serwer Flask, obsługa routingu HTTP i sesji
├── treningi.py         # Logika biznesowa, walidacja danych, silnik analityczny
├── treningi.json       # Plikowa baza danych w formacie JSON
├── requirements.txt    # Lista zależności projektu (Flask)
└── templates/
    └── index.html      # Warstwa prezentacji (Widok HTML5/CSS3 z silnikiem Jinja2)
