import my_functions as mf
from my_classes import Subject, Supervisor, Experiment

if __name__ == "__main__":
    # Create a supervisor and a subject
    supervisor = mf.build_person("John", "Doe", "male", 30)
    # leistungstest kreieren
    supervisor = Supervisor("Max", "Mustermann", "male", "35")
    subject = Subject("Maria", "Musterfrau", "female", "30")
    subject.estimate_max_hr()

    experiment = Experiment("Leistungstest","Baum", "Max_Mustermann", "max_estimate_hr", "2025-03-29")
    experiment.add_subject(subject)
    experiment.add_supervisor(supervisor)



print(supervisor)
print(experiment)
