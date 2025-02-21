from patient import Patient
from vitals import VitalSigns
from clinic import Clinic
from utils import get_valid_number, get_valid_temperature


def gather_subjective_data():
    name = input("Enter patient's name: ")
    age = get_valid_number("Enter patient's age: ")
    patient = Patient(name, int(age))

    while True:
        history = input("Enter medical history (or type 'done' to finish): ")
        if history.lower() == 'done':
            break
        patient.add_medical_history(history)

    symptoms = input("Enter symptoms (comma-separated): ").split(',')
    for symptom in symptoms:
        patient.add_symptom(symptom.strip())

    return patient


def gather_objective_data():
    temperature = get_valid_temperature()
    pulse = get_valid_number("Enter pulse: ")
    blood_pressure = input("Enter blood pressure (e.g., 120/80): ")
    return VitalSigns(temperature, int(pulse), blood_pressure)


def main():
    clinic = Clinic()

    print("\n--- Welcome to the Medical Clinic System ---\n")
    
    patient = gather_subjective_data()
    patient.display_subjective_info()
    
    vital_signs = gather_objective_data()
    vital_signs.display()

    assessment_result = clinic.assess_patient(patient)
    print("\n" + assessment_result)

    treatment_plan = clinic.create_treatment_plan(assessment_result)
    print(treatment_plan)

    
    clinic.save_patient_data(patient, vital_signs, assessment_result, treatment_plan)
    print("\nPatient data saved successfully!\n")

    while True:
        follow_up = input("\nWould you like to update patient records? (yes/no): ")
        if follow_up.lower() == 'no':
            print("Exiting system. Stay healthy!")
            break
        else:
            new_symptom = input("Enter new symptom: ")
            patient.add_symptom(new_symptom.strip())
            patient.display_subjective_info()

            vital_signs = gather_objective_data()
            vital_signs.display()

            assessment_result = clinic.assess_patient(patient)
            print("\n" + assessment_result)

            treatment_plan = clinic.create_treatment_plan(assessment_result)
            print(treatment_plan)

            
            clinic.save_patient_data(patient, vital_signs, assessment_result, treatment_plan)
            print("\nUpdated patient data saved!\n")


if __name__ == "__main__":
    main()
