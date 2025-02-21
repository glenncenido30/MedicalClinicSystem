import csv
from patient import Patient

class Clinic:
    DIAGNOSIS_RULES = {
        "fever": "Possible flu or infection. Recommend testing.",
        "cough": "Consider COVID-19 or respiratory infection testing.",
        "chest pain": "Possible heart issue. Seek immediate attention.",
        "headache": "Could be migraine or dehydration. Advise hydration.",
        "sore throat": "Possible throat infection. Recommend medication.",
        "fatigue": "Could indicate anemia or other conditions. Suggest blood tests."
    }

    def __init__(self):
        self.patients = self.load_patient_data()

    def add_patient(self, patient):
        self.patients.append(patient)
        self.save_patient_data(patient)

    def assess_patient(self, patient):
        diagnoses = [self.DIAGNOSIS_RULES.get(symptom, "Unknown condition. Further tests needed.") for symptom in patient.symptoms]
        return " | ".join(set(diagnoses))

    def create_treatment_plan(self, assessment):
        if "flu" in assessment:
            return "Treatment Plan: Rest, hydration, and antiviral medication."
        elif "COVID-19" in assessment:
            return "Treatment Plan: Isolate and get tested."
        elif "heart issue" in assessment:
            return "Treatment Plan: Seek emergency medical attention."
        else:
            return "Treatment Plan: Monitor symptoms and follow up if necessary."

    def save_patient_data(self, patient, vital_signs, assessment_result, treatment_plan):
        with open("patients.csv", "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                patient.name, 
                patient.age, 
                ",".join(patient.medical_history), 
                ",".join(patient.symptoms),
                vital_signs.temperature,
                vital_signs.pulse,
                vital_signs.blood_pressure,
                assessment_result,
                treatment_plan
            ])

    def load_patient_data(self):
        patients = []
        try:
            with open("patients.csv", "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    patient = Patient(row[0], int(row[1]))
                    patient.medical_history = row[2].split(",") if row[2] else []
                    patient.symptoms = row[3].split(",") if row[3] else []
                    patients.append(patient)
        except FileNotFoundError:
            print("No previous patient records found.")
        return patients
