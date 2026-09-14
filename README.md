# Dokumentacja kalendarza

**Tytuł:** Dokumentacja kalendarza

**Imię i nazwisko:** XYZ

**PESEL:** XYZ

**Tytuł:** 14.09.2026

---

# Spis treści: 

<!--toc -->
- [Dokumentacja kalendarza](#dokumentacja-kalendarza)
- [Spis treści:](#spis-treści)
- [1. Opis działania aplikacji desktopowej](#1-opis-działania-aplikacji-desktopowej)
- [2. Opis aplikacji desktopowej](#2-opis-aplikacji-desktopowej)
- [3. Uruchomienie aplikacji](#3-uruchomienie-aplikacji)
- [4. Opis funkcji aplikacji](#4-opis-funkcji-aplikacji)

<!--/toc -->

# 1. Opis działania aplikacji desktopowej

Aplikacja desktopowa w języku Python, służy do wyświetlania kalendarza oraz do wyświetlania/dodawania własnych wydarzeń z pliku lub zapisywanie ich do pliku 

# 2. Opis aplikacji desktopowej

Aplikacja desktopowa pozwala na wprowadzanie nowych wydarzeń do kalendarza i  ich zapis albo na wczytywanie wydarzeń z pliku tekstowego

# 3. Uruchomienie aplikacji 

1. Upewnij się że masz zainstalowany Python 3.8 lub wyższy
2. Otwórz terminal w katalogu głownym projektu
3. Wpisz komendę aby zainstalować potrzebną bibliotekę
   ```pip
   pip install tkcalendar
   ```
4. Uruchom program poleceniem python -main.py.CalendarApp lub naciśnij F5 jeśli otwierasz w Visual Studio Code
5. Wczytaj przykładową listę eventów (events.txt)
6. Dodaj nowy event i sprawdź czy się zapiszę do pliku tekstowego

# 4. Opis funkcji aplikacji

+ __funkcja:__ ```__init__(self):```
   
   __działanie:__ funkcja inicializuje aplikacje

   ---

+ __funkcja:__ ```load_events(self):```
   
   __działanie:__ funkcja wczytuje wydarzenia z wybranego pliku tekstowego (obsługuje tylko .txt)

   warunek: wymagany jest format ```dd-mm-yyyy; *nazwa wydarzenia*``` aby moć wczytać wydarzenia

   ---

+ __funkcja:__ ```add_event_manually(self):```
   
   __działanie:__ funkcja pozwala na własnoreczne wpisanie wydarzenia do kalendarza

   warunek: wymagane jest wpisanie poprawnej daty w formacie ```dd-mm-yyyy```

   ---

+ __funkcja:__ ```save_event(self, date_str, event_desc, window):```
   
   __działanie:__ funkcja zapisuję własnorecze wpisanie wydarzenia do pliku events.txt

   warunek: wymagane jest wpisanie poprawnej daty w formacie ```dd-mm-yyyy```

   ---

+ __funkcja:__ ```on_date_selected(self, event):```
   
   __działanie:__ funkcja wyświetla wybraną datę na ekranie

   ---

+ __funkcja:__ ```update_events(self, date_str):```
   
   __działanie:__ funkcja aktualizuje wydarzenia po wybraniu daty lub pokazuje ich brak jeśli w danym dniu nie ma żadnego wydarzenia

   ---

+ __funkcja:__ ```run(self):```
   
   __działanie:__ funkcja odpowiada za właczenie aplikacji
