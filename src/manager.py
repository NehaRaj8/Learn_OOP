import pandas as pd
from src.patient import Patient, ChronicPatient


class PatientManager:
    def __init__(self, filepath):
        self.filepath = filepath
        self.patients = []

    def load_data(self):
        df = pd.read_csv(self.filepath)

        for _, row in df.iterrows():
            if row['condition'] == 'chronic':
                patient = ChronicPatient(*row)
            else:
                patient = Patient(*row)

            self.patients.append(patient)

    def get_all_patients(self):
        return self.patients
