import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkcalendar import Calendar
import datetime as dt
import locale
from tkinter import messagebox  # needed for messagebox

class CalendarApp:
    def __init__(self): # inicjalizacja aplikacji
        locale.setlocale(locale.LC_TIME, 'pl_PL')
        self.root = tk.Tk()
        self.root.geometry('400x550')
        self.root.title("Kalendarz")
        self.root.configure(bg="lightblue")
        self.events = {}
        self.current_date = dt.datetime.now()

        self.cal = Calendar(self.root, locale='pl_PL', selectmode='day',
                            year=self.current_date.year, month=self.current_date.month, day=self.current_date.day,
                            background="gray", foreground="black", bordercolor="black",
                            headersbg="lightgray", normalbg="lightblue", weekendbg="lightgreen", othermonthbg="lightyellow")
        self.cal.pack(pady=20)

        self.date_label = tk.Label(self.root, text="Dzisiaj jest:\n" + self.current_date.strftime("%d.%m.%Y, %A"),font=("Arial", 10), bg="pink")
        self.date_label.pack(pady=10, padx=10)

        self.chosendate_label = tk.Label(self.root, text="Wybrana data:\n" + self.cal.get_date(),font=("Arial", 10), bg="lightyellow")
        self.chosendate_label.pack(pady=10, padx=10)

        self.event_label = tk.Label(self.root, text="Wybierz datę, aby zobaczyć wydarzenia",font=("Arial", 10), bg="lightgreen", justify=tk.LEFT)
        self.event_label.pack(pady=10, padx=10)

        add_event_from_file = tk.Button(self.root, text="Dodaj wydarzenie z pliku .txt", command=self.load_events)
        add_event_from_file.pack(pady=10, padx=10)

        add_event_manually = tk.Button(self.root, text="Dodaj wydarzenie ręcznie", command=self.add_event_manually)
        add_event_manually.pack(pady=10, padx=10)

        self.cal.bind("<<CalendarSelected>>", self.on_date_selected)

    def load_events(self): # funkcja wczytująca wydzarzenia z pliku .txt
        filename = askopenfilename(title="Wybierz plik", filetypes=[("Pliki tekstowe", "*.txt")])
        if not filename:
            return
        with open(filename, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    date_str, event_desc = line.split(';', 1)
                    event_date = dt.datetime.strptime(date_str, "%d-%m-%Y").date()
                    self.events.setdefault(date_str, []).append(event_desc)
                    self.cal.calevent_create(event_date, event_desc, 'event')
                except ValueError:
                    print(f"Niepoprawny format linii: {line}")
        self.update_events(self.cal.get_date())

    def add_event_manually(self): # funkcja dodająca wydarzenie ręcznie
        add_window = tk.Toplevel(self.root)
        add_window.title("Dodaj wydarzenie")

        tk.Label(add_window, text="Data wydarzenia (dd-mm-yyyy):").pack(pady=5)
        event_date = tk.Entry(add_window, width=40)
        event_date.pack(pady=10, padx=10)

        tk.Label(add_window, text="Nazwa wydarzenia:").pack(pady=5)
        event_name = tk.Entry(add_window, width=40)
        event_name.pack(pady=10, padx=10)

        tk.Button(add_window, text="Zapisz wydarzenie", command=lambda: self.save_event(event_date.get(), event_name.get(), add_window)).pack(pady=10)

    def save_event(self, date_str, event_desc, window): # funkcja zapisująca wydarzenie
        str_date = date_str.strip()
        str_event = event_desc.strip()
        try:
            event_date_obj = dt.datetime.strptime(str_date, "%d-%m-%Y").date()
            self.events.setdefault(str_date, []).append(str_event)
            self.cal.calevent_create(event_date_obj, str_event, 'event')
            with open("events.txt", "a", encoding='utf-8') as f:
                f.write(f"{str_date};{str_event}\n")
            window.destroy()
            self.update_events(self.cal.get_date())
        except ValueError:
            messagebox.showerror("Błąd", "Niepoprawny format daty. Użyj dd-mm-yyyy.")

    def on_date_selected(self, event): # funkcja wywoływana po wybraniu daty
        selected = self.cal.get_date()
        self.chosendate_label.config(text="Wybrana data:\n" + selected)
        self.update_events(selected)

    def update_events(self, date_str): # funkcja aktualizujaca wydarzenia
        dt_obj = None
        for fmt in ("%m/%d/%y", "%d/%m/%Y", "%Y-%m-%d", "%d.%m.%Y", "%d-%m-%Y"):
            try:
                dt_obj = dt.datetime.strptime(date_str, fmt)
                break
            except ValueError:
                continue
        if not dt_obj:
            self.event_label.config(text="Brak wydarzeń dla wybranej daty.")
            return
        # Normalize date to dd-mm-yyyy string
        norm_date = dt_obj.strftime("%d-%m-%Y")
        events = self.events.get(norm_date, [])
        if events:
            self.event_label.config(text=f"Wydarzenia dla wybranej daty:\n" + "\n".join(f"- {e}" for e in events))
        else:
            self.event_label.config(text=f"Brak wydarzeń dla wybranej daty.")

    def run(self): # funkcja uruchamiająca aplikację
        self.root.mainloop()

if __name__ == "__main__":
    app = CalendarApp()
    app.run()
