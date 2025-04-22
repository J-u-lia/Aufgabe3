import my_functions as mf
from my_classes import Subject, Supervisor, Experiment

if __name__ == "__main__":
    # Create a supervisor and a subject
    # supervisor = mf.build_person("John", "Doe", "male", 30)
    # leistungstest kreieren
    # supervisor = Supervisor("Max Mustermann", "male", "1980-01-01")
    subject = Subject("Maria Musterfrau", "female", "2000-01-01", id="123456")
    subject.put()    # Person auf Server anlegen
    subject.update_email("MariaMusterfrau@example.com")    # E-Mail-Adresse aktualisieren
    # subject.estimate_max_hr()
#
    # experiment = Experiment("Leistungstest","Maria_Musterfrau", "Max_Mustermann", "max_estimate_hr", "2025-04-16")
    # experiment.add_subject(subject)
    # experiment.add_supervisor(supervisor)



# print(supervisor)
print(subject)
# print(experiment)
