class RiskModel:
    def calculate_risk(self, patient):
        score = 0

        if patient.age > 65:
            score += 2
        if patient.heart_rate > 100:
            score += 2
        if patient.systolic_bp > 140:
            score += 2
        if "diabetes" in patient.condition.lower():
            score += 1

        return score

    def risk_category(self, score):
        if score >= 5:
            return "High"
        elif score >= 3:
            return "Medium"
        return "Low"