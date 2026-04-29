from src.manager import PatientManager
from src.risk_model import RiskModel


def main():
    manager = PatientManager("data/patients.csv")
    manager.load_data()

    model = RiskModel()

    for patient in manager.get_all_patients():
        score = model.calculate_risk(patient)
        category = model.risk_category(score)

        print(patient.get_summary())
        print(f"Risk Score: {score} | Category: {category}\n")


if __name__ == "__main__":
    main()
