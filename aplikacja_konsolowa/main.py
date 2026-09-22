import datetime as dt
import locale
import os

class CalendarApp:
    def __init__(self):
        locale.setlocale(locale.LC_TIME, 'pl_PL')
        self.current_date = dt.datetime.now()

    def add_event_manually(self):
        print("hi")

    def add_event(self):
        print("hey")

    def save_event(self):
        print("hello")

    def show_events(self):
        print("bye")

    def exit(self):
        print("o/")

    def run(self):
        print('---')
        print(f"dzisiaj jest {self.current_date}")
        print('---')
        print('1. Dodaj wydarzenie własnoręcznie')
        print('2. Dodaj wydarzenie z pliku')
        print('3. Zapisz wydarzenia do pliku')
        print('4. Zobacz listę zaplanowanych wydarzeń')
        print('5. Wyjście')
        action = int(input("Co chcesz zrobić (1-5)?: "))
        if action == 1:
            self.add_event_manually()
        elif action == 2:
            self.add_event()
        elif action == 3:
            self.save_event()
        elif action == 4:
            self.show_events()
        elif action == 5:
            self.exit()
        else:
            print("Złe wprowadzenie, tylko liczby od 1-5, spróbuj ponownie!")
            action = int(input("Co chcesz zrobić (1-5)?: "))


if __name__ == "__main__":
    app = CalendarApp()
    app.run()