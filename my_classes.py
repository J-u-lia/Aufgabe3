import datetime
from my_functions import estimate_max_hr
import requests   # davor noch pip install requests im Terminal ausführen, Importiere die requests-Bibliothek für HTTP-Anfragen

# Elternklasse Person definieren
class Person():
    id_counter = 0  # ID-Attribut für die Person, wird automatisch hochgezählt
    def __init__(self, name, sex, date_of_birth, id=None):
        self.name = name
        self.sex = sex
        self.__date_of_birth = datetime.datetime.strptime(date_of_birth, "%Y-%m-%d").date()  # Private attribute
        self.id = id  # ID ist optional, wird aber in der Datenbank benötigt, um die Person zu identifizieren ---> momentan wird nur ein name an den server gesendet, die API-Vorlage versucht aber eine id zu finden
    def get_age_years(self):
        today = datetime.date.today()
        age_years = datetime.datetime.now().year - self.__date_of_birth.year
        # um zu prüfen, ob der Geburtstag in diesem Jahr bereits war 
        if (today.month, today.day) < (self.__date_of_birth.month, self.__date_of_birth.day):
            age_years -= 1
        return age_years
    
    # Person verfügen über eine Methode, die eine neue Person an den Webserver http://127.0.0.1:5000 sendet
    def put(self):
        if self.id is None:  # Wenn die ID nicht gesetzt ist, dann wird sie automatisch hochgezählt
            Person.id_counter += 1
            self.id = Person.id_counter  # ID der Person wird gesetzt
        
        url = "http://127.0.0.1:5000/person/"    # wichtig dass der URL mit /person/ endet, sonst wird die Person nicht angelegt und es kommt ein error heraus, obwohl bei seinem geclonten repository eine meldung kommt das was verscuht worden ist zu putten
        data = {
            "id": self.id,  # ID der Person, die aktualisiert werden soll
            "name": self.name,
            }
        response = requests.post(url, json=data)
        if response.status_code == 201:  # der response.status_code 201 bedeutet, dass eine neue Person erfolgreich created wurde, 200 würde nur bedeutn, dass die Anfrage erfolgreich war
            returned_data = response.json()
            self.id = returned_data.get("id")  # ID von der Antwort speichern
            print("Data sent successfully, ID:, {self.id}")
        else:
            print("Error sending data", response.status_code)

# Kindklasse Subject und Supervisor definieren
class Subject(Person):
    def __init__(self, name, sex, date_of_birth, id=None, email=None):
        super().__init__(name, sex, date_of_birth, id)  # Erben von Elternklasse
        # self.email = email
    
    # Alter ausrechnen mit dem __date_of_birth private Attribut
    def get_subject_age(self):
        return self.get_age_years()
    
    # estimate_max_hr als Methode definieren
    def estimate_subject_max_hr(self):
        """ Berechnet die maximale Herzfrequenz für das Subject """
        age_years = self.get_subject_age()
        return estimate_max_hr(age_years, self.sex)
    
    # Subject hat jetzt eine Methode, die eine PUT-Anfrage an den Webserver sendet, um die E-Mail-Adresse zu aktualisieren mit dem gleichen vornamen wie aus put()
    def update_email(self, email):
        url = "http://127.0.0.1:5000/person/"  # wichtig, dass /person/email dasteht, sonst passiert das gleiche wie vorher bei put()
        data = {
            "id": self.id,  # ID der Person, die aktualisiert werden soll
            "name": self.name,
            "email": email}

        response = requests.put(url, json=data)
        if response.status_code == 200:
            print("Data updated successfully", response.json())
        else:
            print("Error updating data", response.status_code)

class Supervisor(Person):
    def __init__(self, name, sex, date_of_birth):
        super().__init__(name, sex, date_of_birth)
    
    # Alter ausrechnen mit dem __date_of_birth Attribut
    def get_supervisor_age(self):
        return self.get_age_years()


# Klasse Experiment definieren
# class subject und subervisor als Parameter übergeben
class Experiment():
    def __init__(self, experiment_name, subject, supervisor, experiment_type, date):
        self.experiment_name = experiment_name
        self.subject = subject
        self.supervisor = supervisor
        self.experiment_type = experiment_type
        self.date = date
        
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


# Testen der Klassen
p = Subject("Julia", "female", "2006-06-09")
print(f"Alter: {p.get_age_years()} Jahre")
print(f"Maximale Herzfrequenz: {p.estimate_subject_max_hr()} bpm")