# Klasse Subject definieren
# estimate_max_hr als Methode definieren
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





# Klasse Supervisor definieren
class Supervisor():
    def __init__(self, first_name, last_name, sex, age):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.age = age
        pass




# Klasse Experiment definieren
# class subject und subervisor als Parameter übergeben
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
