class Patient:
    def __init__(self, patient_id, age, heart_rate, systolic_bp, condition):
        self.patient_id = patient_id
        self.age = age
        self.heart_rate = heart_rate
        self.systolic_bp = systolic_bp
        self.condition = condition

    def get_summary(self):
        return f"Patient {self.patient_id}: Age {self.age}, Condition: {self.condition}"


class ChronicPatient(Patient):
    def __init__(self, patient_id, age, heart_rate, systolic_bp, condition, chronic_flag=True):
        super().__init__(patient_id, age, heart_rate, systolic_bp, condition)
        self.chronic_flag = chronic_flag

    def get_summary(self):
        return super().get_summary() + " (Chronic)"
