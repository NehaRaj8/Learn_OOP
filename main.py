from src.manager import PatientManager
from src.risk_model import RiskModel


def display_patient_risk(patient, model):
    """Calculate and display a patient's risk information."""
    score = model.calculate_risk(patient)
    category = model.risk_category(score)

    print("=" * 50)
    print(patient.get_summary())
    print(f"Risk Score : {score}")
    print(f"Category   : {category}")
    print("=" * 50 + "\n")


def main():
    data_path = "data/patients.csv"

    try:
        manager = PatientManager(data_path)
        manager.load_data()

        patients = manager.get_all_patients()

        if not patients:
            print("No patient records found.")
            return

        model = RiskModel()

        print(f"Loaded {len(patients)} patient(s)\n")
        
         # CREATE COUNTERS HERE
        high_count = 0
        medium_count = 0
        low_count = 0
        
        for patient in patients[:5]:
            score = model.calculate_risk(patient)
            category = model.risk_category(score)

            display_patient_risk(patient, model)

            if category == "High":
              high_count += 1
            elif category == "Medium":
              medium_count += 1
            else:
              low_count += 1

          # PRINT SUMMARY AFTER LOOP
        print("SUMMARY")
        print("=" * 30)
        print(f"High Risk Patients   : {high_count}")
        print(f"Medium Risk Patients : {medium_count}")
        print(f"Low Risk Patients    : {low_count}")

    except FileNotFoundError:
        print(f"Error: Could not find file '{data_path}'")
    except Exception as error:
        print(f"Unexpected error: {error}")


if __name__ == "__main__":
    main()