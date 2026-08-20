class ICUAllocation:

    def __init__(self, beds):
        self.total_beds = beds
        self.available_beds = beds
        self.patients = {}
        self.waiting_list = []

    def calculate_priority(self, oxygen, heart_rate, blood_pressure,
                           temperature, conditions):

        score = 0

        if oxygen < 90:
            score += 40
        elif oxygen < 94:
            score += 25

        if heart_rate > 120 or heart_rate < 50:
            score += 20

        systolic = blood_pressure[0]

        if systolic < 90 or systolic > 180:
            score += 20

        if temperature >= 39 or temperature <= 35:
            score += 10

        if conditions:
            score += 10

        return score

    def classify(self, score):
        if score >= 70:
            return "CRITICAL"
        elif score >= 50:
            return "HIGH"
        elif score >= 30:
            return "MEDIUM"
        else:
            return "LOW"

    def allocate_patient(self, patient_id, age, oxygen, heart_rate,
                         blood_pressure, temperature, conditions,
                         emergency=False):

        if patient_id in self.patients:
            print("Duplicate patient ID")
            return

        if oxygen < 0 or oxygen > 100:
            print("Invalid oxygen level")
            return

        if heart_rate <= 0:
            print("Invalid heart rate")
            return

        score = self.calculate_priority(
            oxygen,
            heart_rate,
            blood_pressure,
            temperature,
            conditions
        )

        priority = self.classify(score)

        patient = {
            "age": age,
            "oxygen": oxygen,
            "heart_rate": heart_rate,
            "blood_pressure": blood_pressure,
            "temperature": temperature,
            "conditions": conditions,
            "score": score,
            "priority": priority
        }

        self.patients[patient_id] = patient

        if self.available_beds > 0 or emergency:
            if self.available_beds > 0:
                self.available_beds -= 1

            print(patient_id, "allocated ICU bed")
            print("Priority:", priority)

        else:
            self.waiting_list.append(patient_id)
            print(patient_id, "placed in waiting list")

    def show_status(self):
        print("Available ICU beds:", self.available_beds)
        print("Waiting list:", self.waiting_list)


icu = ICUAllocation(2)

icu.allocate_patient(
    "P001", 65, 85, 130, (85, 60), 39.5,
    ["Diabetes"]
)

icu.allocate_patient(
    "P002", 45, 97, 80, (120, 80), 37,
    []
)

icu.allocate_patient(
    "P003", 70, 88, 125, (90, 60), 38.5,
    ["Heart disease"]
)

icu.show_status()
