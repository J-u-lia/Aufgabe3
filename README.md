Sakai-Aufgabe 3: Python-Installation und Funktionen
## Python Installation 
- Installieren Sie Python auf Ihrem Rechner: python.org herunter
- Stellen Sie sicher, den Haken bei Add Python to PATH zu setzen

## VS Code
- Erstellen Sie einem Ordner Aufgabe3 der nicht ein einem Netzwerk oder Cloud-Pfad liegt und legen Sie darin ein Modul (Datei) calculation.py an.
- Öffnen Sie PowerShell (Windows) oder Terminal (Mac) und navigieren Sie in den Ordner indem Sie cd gefolgt von dem Pfad eingeben (z.B. cd       C:\code\temp\Aufgabe3).
- Geben Sie python -V ein, um sicherzustellen, dass Python installiert ist. Sollte eine Fehlermeldung auftreten, dass Python nicht gefunden wurde so haben Sie den Pfad nicht korrekt gesetzt.

- Wir möchten nun eine Funktion in estimate_max_hr() schreiben, die folgende User-Stories erfüllt:

"Als Diagnostiker:in möchte ich die maximale Herzfrequenz eines Patienten auf Basis von Geschlecht und Alter schätzen, um die Leistungsfähigkeit zu beurteilen."

- Erstellen Sie ein Modul my_functions.py mit folgendem Inhalt:
def estimate_max_hr(age_years : int , sex : str) -> int:
  """
  See https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4124545/ Titel anhand dieser PMC-ID in Citavi-Projekt übernehmen for different formulas
  """
  if sex == "male":
    max_hr_bpm =  223 - 0.9 * age_years
  elif sex == "female":
    max_hr_bpm = 226 - 1.0 *  age_years
  else:
    # der input() öffnet ein Eingabefenster für den Nutzer und speichert die Eingabe
    max_hr_bpm  = input("Enter maximum heart rate:")
  return int(max_hr_bpm)

def build_person(first_name, last_name, sex, age) -> dict:
    """Returns a dictionary of information about a supervisor or subject."""
    dict = { "first_name" : first_name,
             "last_name" : last_name,
             "age" : age,
             "estimate_max_hr" : estimate_max_hr(age,sex)}
    return dict

def build_experiment(experiment_name, date, supervisor, subject) -> dict:
    """Returns a dictionary of information about an experiment."""
    dict = {"experiment_name" : experiment_name,
            "date" : date,
            "supervisor" :   supervisor,
            "subject" :   subject
            }
    return dict

- Erstellen Sie ein Modul main.py mit folgendem Inhalt, welches die Funktionen nutzt um ein Dictionary eines Experimentes zu erstellen und zu printen.
- Sie können zum Bearbeiten der Dateien jeden beliebigen Test-Editor oder VSCode verwenden.
- Das Modul main.py sollte die Abfrage if __name__ == "__main__": enthalten.
- Führen Sie das Skript aus, indem Sie python main.py in der Konsole eingeben.
- Laden Sie my_functions.py und main.py in ihrem GitHub-Repository hoch und teilen Sie den Link in Sakai.

## Sakai-Aufgabe 4: VS Code mit Github-Account
# Installieren Sie Visual Studio Code
- Öffnen Sie den Ordner, in dem Sie den Code aus Sakai-Aufgabe 3 gespeichert haben über File -> Open Folder
- Wählen Sie Terminal -> New Terminal und erstellen Sie ein PowerShell-Terminal und geben Sie erneut python main.py ein. Sofern dies zu einem Fehler führt, versuchen Sie die Fehlermeldung zu verstehen und zu beheben, falls das nicht gelingt, kopieren Sie die Fehlermeldung in die Sakai-Aufgabe 4
- Gehen Sie auf das Account-Symbol in der unteren linken Ecke und wählen Sie Sign in with Github ...
- Installieren Sie git auf Ihrem Rechner: git-scm.com
- Nach einem Neustart von Visual Studio Code, sollten Sie in der Lage sein, nun auch eine git-bash-Terminal zu öffnen
- Führen Sie darin folgende Befehle aus
        - Ersetzen Sie "Ihr Name" und "Ihre E-Mail" durch Ihren github account
        - pwd zeigt Ihnen den absoluten Pfad zum Arbeitsverzeichnis
        - git --version zeigt Ihnen die installierte git-Version
        - git config --global user.name "Ihr Name auf github"
        - git config --global user.email "Ihre E-Mail von github"
        - git config --list
- kopieren Sie das Ergebnis oder Fehlermeldungen ebenfalls in die Sakai-Aufgabe 4 Sofern alles Funktioniert hat, schreiben Sie einfach nur ok in die Abgabe, ansonsten posten Sie die Fehlermeldung

## Sakai-Aufgabe 5: Github Repository
- In ihrem Zweier-Team nutzen Sie nun einen PC, um ihr Git-Repository zu klonen
- Sie erstellen ein neues Projekt mit pdm und fügen das numpy-Paket hinzu
- Pushen Sie die Änderungen auf GitHub
- Clonen Sie das Repository auf einem anderen PC und installieren Sie die Pakete mit pdm install
- Nun fügt PC 2 das pandas-Paket hinzu und pusht die Änderungen
- PC 1 kann nun die Änderungen über git pullen und mit pdm install übernehmen
- Kopieren Sie beide den Link zum Repository in die Abgabe
- Bauen Sie Ihre Lösung der letzten Aufgabe oder die Musterlösung in das Projekt ein
- Optional: Mach Sie sich Gedanken, wie man die Musterlösung verbessern könnte (z.B. sicherstellen, dass man bei Diagnostikerinnen keine Daten außer dem Namen erfassen muss)

main.py
from my_functions import estimate_max_hr, build_person, build_experiment, ask_name, ask_number, ask_sex

if __name__ == "__main__":

    # Erstellen eines Leistungstests
    print("Leistungstest wird erstellt")
    print("Bitte geben Sie die Diagnostikerdaten ein:")

    print(" Geben Sie den Vornamen des Diagnostikers ein:")
    first_name = ask_name()
    print(" Geben Sie den Nachnamen des Diagnostikers ein:")    
    last_name = ask_name()

    supervisor = build_person(first_name, last_name, None, None)

    print("Bitte geben Sie die Probandendaten ein:")
    print(" Geben Sie den Vornamen des Probanden ein:")
    first_name = ask_name()
    print(" Geben Sie den Nachnamen des Probanden ein:")
    last_name = ask_name()
    print(" Geben Sie das Alter des Probanden ein:")
    age = ask_number()
    sex = ask_sex()
    # Erstellen einer Person
    subject = build_person(first_name, last_name, sex, age)

    # Erstellen eines Experiments
    experiment = build_experiment("Leistungstest", "2021-01-01", supervisor, subject)

    print("Das Experiment wurde erstellt:")
    print(experiment)
my_functions.py
def ask_name() -> str:
    """Asks the user for their name."""
    try :
        name = input("What is your name? ")
        return name
    except Exception as e:
        print("Please enter a valid name")
        ask_name()

def ask_number() -> int:
    """Asks the user for a number."""
    try:
        number = int(input("Enter a number: "))
        return number
    except Exception as e:
        print("Please enter a valid number")
        ask_number()

def ask_sex() -> str:
    """Ask the user for the sex"""
    sex_string = input("Enter sex (w/m): ")
    if sex_string == "w":
        return "female"
    elif sex_string == "m":
        return "male"
    else:
        print("Please enter 'w' or 'm'")
        ask_sex()

## Sakai-Aufgabe 6.1: Objektorientierung
- nutzen Sie das bestehende Repository aus Sakai-Aufgabe 3 & 5, um die Aufgabe zu bearbeiten. Damit Sie nun wieder unabhängig voneinander arbeiten - können, erstellen Sie jeweils einen neuen Branch mit Ihrem Vornamen und arbeiten Sie alleine in diesem weiter.
- Committen Sie die stabile Lösungen und comitten Sie wieder mit der Commit-Message Aufgabe61, wenn Sie den Code umgeschrieben haben.
- erstellen Sie eine neue Datei my_classes.py in der Sie die Klassen Subject, Supervisor und Experiment anlegen. Diese haben jeweils einen    Konstruktur (__init__()), um die Attribute zu setzen, die bisher im Dictionary gespeichert wurden.
- Das Subject enthält zudem eine Methode estimate_max_hr() basierend auf der Funktion.
- Da wir nicht für jeden Testfall die Daten von Hand eingeben wollen, eine Kopie der main.py namens test.py anlegen (Beispiel, wie das aussehen könnte, finden Sie unten)
- Geben Sie wieder den Link zum Repository in Sakai ab
- Vorschlag für test.py

from my_classes import Subject, Supervisor, Experiment

if __name__ == "__main__":

    # Erstellen eines Leistungstests
    supervisor = Supervisor("FirstName", "LastName")
    subject = Subject("FirstName", "LastName", "female", 30)
    subject.estimate_max_hr()

    experiment = Experiment("Leistungstest", "2021-01-01")
    experiment.add_subject(subject)
    experiment.add_supervisor(supervisor)
    
    print(experiment)

- Startpunkt für my_classes.py
class Subject():
    def __init__(self, first_name, last, sex):
      pass

    def estimate_max_hr(self):
      """A function that estimates the maximum heart rate of a subject"""
      pass

class Supervisor():
    def __init__(self, first_name, last_name):
      pass

class Experiment():
    def __init__(self, name, date):
      pass

    def add_subject(self, subject):
      self.subject = subject

    def add_supervisor(self, supervisor):
      pass

# Code:
- Klasse Subject definieren
- estimate_max_hr als Methode definieren
class Subject():
    def __init__(self, first_name, last_name, sex, age):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.age = age
        pass
    def estimate_max_hr(self):
        """
        A function that estimates the maximum heart rate of a subject"""
        pass





- Klasse Supervisor definieren
class Supervisor():
    def __init__(self, first_name, last_name, sex, age):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.age = age
        pass




- Klasse Experiment definieren
- class subject und subervisor als Parameter übergeben
- Klasse Subject definieren
- estimate_max_hr als Methode definieren
class Subject():
    def __init__(self, first_name, last_name, sex, age):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.age = age
        pass
    def estimate_max_hr(self):
        """
        A function that estimates the maximum heart rate of a subject"""
        pass





- Klasse Supervisor definieren
class Supervisor():
    def __init__(self, first_name, last_name, sex, age):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.age = age
        pass




- Klasse Experiment definieren
- class subject und subervisor als Parameter übergeben
class Experiment():
    def __init__(self, experiment_name, subject, supervisor, experiment_type, date):
        self.experiment_name = experiment_name
        self.subject = subject
        self.supervisor = supervisor
        self.experiment_type = experiment_type
        self.date = date
        pass
    def add_subject(self, subject):
        """
        A function that adds a subject to an experiment"""
        self.subject = subject
        pass
    def add_supervisor(self, supervisor):
        """ 
        A function that adds a supervisor to an experiment"""
        self.supervisor = supervisor
        pass

