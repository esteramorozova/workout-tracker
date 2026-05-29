# Ewidencja Treningów Sportowych

Aplikacja webowa napisana w Pythonie z użyciem Flask, która pozwala śledzić i analizować swoje treningi. Projekt powstał jako zaliczenie laboratorium z podstaw programowania.

## Co robi aplikacja

- **Dodawanie i usuwanie treningów** — wpisujesz typ aktywności, czas i kalorie, dane od razu lądują w historii
- **Automatyczne szacowanie kalorii** — na podstawie typu sportu i czasu trwania program sam sugeruje spalone kalorie; możesz też wpisać własną wartość
- **Zapis danych do pliku JSON** — dane zostają po zamknięciu przeglądarki i nie znikają między sesjami
- **Statystyki za bieżący tydzień, miesiąc i rok** — sumy i podsumowania liczone automatycznie przez moduł `datetime`
- **Filtrowanie po własnym zakresie dat** — wybierasz przedział od-do i dostajesz liczbę treningów, łączny czas, średnią i podział według aktywności

## Struktura plików

```
├── app.py           # serwer Flask, routing HTTP
├── treningi.py      # logika aplikacji, walidacja danych, obliczenia
├── treningi.json    # baza danych w formacie JSON
├── requirements.txt # zależności (Flask)
└── templates/
    └── index.html   # interfejs użytkownika (HTML + Jinja2)
```
