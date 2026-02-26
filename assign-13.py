from abc import ABC, abstractmethod

# Abstraction
class Person(ABC):
    def __init__(self, name, age):
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be a valid string.")
        if not isinstance(age, int) or age <= 0:
            raise ValueError("Age must be a positive integer.")

        self.name = name
        self.age = age

    @abstractmethod
    def get_details(self):
        pass


# Inheritance
class Patient(Person):
    def __init__(self, name, age, patient_id, disease):
        super().__init__(name, age)

        if not isinstance(patient_id, int):
            raise ValueError("Patient ID must be an integer.")
        if not disease.strip():
            raise ValueError("Disease cannot be empty.")

        self.patient_id = patient_id
        self.disease = disease
        self.__bill = 0   # Encapsulation

    def get_details(self):
        print("\nPatient Details:")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Patient ID:", self.patient_id)
        print("Disease:", self.disease)

    def calculate_bill(self, doctor_fee, room_charge):
        if doctor_fee < 0 or room_charge < 0:
            raise ValueError("Charges cannot be negative.")
        self.__bill = doctor_fee + room_charge

    def get_bill(self):
        return self.__bill


class Doctor(Person):
    def __init__(self, name, age, specialization):
        super().__init__(name, age)

        if not specialization.strip():
            raise ValueError("Specialization cannot be empty.")

        self.specialization = specialization

    def get_details(self):
        print("\nDoctor Details:")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Specialization:", self.specialization)


# Main Program with User Input
try:
    print("----- Enter Doctor Details -----")
    d_name = input("Enter Doctor Name: ")
    d_age = int(input("Enter Doctor Age: "))
    d_spec = input("Enter Specialization: ")

    doctor = Doctor(d_name, d_age, d_spec)
    doctor.get_details()

    print("\n----- Enter Patient Details -----")
    p_name = input("Enter Patient Name: ")
    p_age = int(input("Enter Patient Age: "))
    p_id = int(input("Enter Patient ID: "))
    p_disease = input("Enter Disease: ")

    patient = Patient(p_name, p_age, p_id, p_disease)
    patient.get_details()

    print("\n----- Enter Billing Details -----")
    doctor_fee = float(input("Enter Doctor Fee: "))
    room_charge = float(input("Enter Room Charge: "))

    patient.calculate_bill(doctor_fee, room_charge)

except ValueError as ve:
    print("Input Error:", ve)

except Exception as e:
    print("Unexpected Error:", e)

else:
    print("\nTotal Hospital Bill:", patient.get_bill())

finally:
    print("\nProgram executed successfully.")