import datetime
from my_functions import estimate_max_hr

# Elternklasse Person definieren
class Person():
    def __init__(self, name, sex, date_of_birth):
        self.name = name
        self.sex = sex
        self.__date_of_birth = datetime.datetime.strptime(date_of_birth, "%Y-%m-%d").date()  # Private attribute
    def get_age_years(self):
        today = datetime.date.today()
        age_years = datetime.datetime.now().year - self.__date_of_birth.year
        # um zu prüfen, ob der Geburtstag in diesem Jahr bereits war 
        if (today.month, today.day) < (self.__date_of_birth.month, self.__date_of_birth.day):
            age_years -= 1
        return age_years

# Kindklasse Subject und Supervisor definieren
class Subject(Person):
    def __init__(self, name, sex, date_of_birth):
        super().__init__(name, sex, date_of_birth)  # Erben von Elternklasse
    
    # Alter ausrechnen mit dem __date_of_birth private Attribut
    def get_subject_age(self):
        return self.get_age_years()
    
    # estimate_max_hr als Methode definieren
    def estimate_subject_max_hr(self):
        """ Berechnet die maximale Herzfrequenz für das Subject """
        age_years = self.get_subject_age()
        return estimate_max_hr(age_years, self.sex)

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