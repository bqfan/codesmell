# source: https://dev.to/olatundeadedeji/mastering-solid-principles-in-python-a-guide-to-scalable-coding-bbn

class PatientData:
    def __init__(self, name, age, gender, blood_group, patient_id, medical_history, treatments):
        self.name = name
        self.age = age
        self.gender = gender
        self.blood_group = blood_group
        self.patient_id = patient_id
        self.medical_history = medical_history
        self.treatments = treatments

    def get_patient_data(self):
        # return patient data
        return

    def get_medical_history(self):
        # return medical history
        return

    def get_treatments(self):
        # return treatments
        return

class AppointmentScheduler:
    def __init__(self, patient_data):
        self.patient_data = patient_data
        self.appointments = []

    def get_appointments(self):
        # return appointments
        return

    def schedule_appointment(self, date):
        # schedule an appointment
        return
