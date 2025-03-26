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