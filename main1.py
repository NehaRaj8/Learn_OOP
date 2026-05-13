from src.manager import PatientManager
from src.risk_model import RiskModel
from src.ml_model import MLModel


def display_patient(patient, risk_score, category, prediction):
    print("=" * 50)
    print(patient.get_summary())
    print(f"Risk Score    : {risk_score}")
    print(f"Risk Category : {category}")
    print(f"ML Prediction : {prediction}")
    print("=" * 50 + "\n")


def main():
    data_path = "data/patients_synthetic_dataset.csv"

    try:
        manager = PatientManager(data_path)
        manager.load_data()

        patients = manager.get_all_patients()

        if not patients:
            print("No patient records found.")
            return

        risk_model = RiskModel()
        ml_model = MLModel()

        print(f"\nLoaded {len(patients)} patients\n")

        # Summary counters
        high_risk = 0
        medium_risk = 0
        low_risk = 0

        # Process patients
        for patient in patients:
            score = risk_model.calculate_risk(patient)
            category = risk_model.risk_category(score)

            if category == "High":
                high_risk += 1
            elif category == "Medium":
                medium_risk += 1
            else:
                low_risk += 1

        # Dashboard Summary
        print("=" * 50)
        print("PATIENT RISK SUMMARY")
        print("=" * 50)

        print(f"High Risk Patients   : {high_risk}")
        print(f"Medium Risk Patients : {medium_risk}")
        print(f"Low Risk Patients    : {low_risk}")

        print("=" * 50)

        # Show only first 5 patients
        print("\nDisplaying first 5 patients:\n")

        for patient in patients[:5]:
            score = risk_model.calculate_risk(patient)
            category = risk_model.risk_category(score)
            prediction = ml_model.predict_condition(patient)

            display_patient(
                patient,
                score,
                category,
                prediction
            )

    except FileNotFoundError:
        print(f"Error: Could not find file '{data_path}'")

    except Exception as error:
        print(f"Unexpected error: {error}")


if __name__ == "__main__":
    main()