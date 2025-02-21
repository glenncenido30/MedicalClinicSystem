class Patient:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.medical_history = []  
        self.symptoms = []          

    def add_medical_history(self, history):
        self.medical_history.append(history)

    def add_symptom(self, symptom):
        self.symptoms.append(symptom)

    def display_subjective_info(self):
        print(f"\nPatient Name: {self.name}, Age: {self.age}")
        print("Medical History:", ', '.join(self.medical_history) if self.medical_history else "None")
        print("Symptoms:", ', '.join(self.symptoms) if self.symptoms else "None")
