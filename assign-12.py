'''1. Problem Statement
 Hospital Management System :
Stores patient details


Allows doctors to diagnose patients


Calculates hospital bills


Displays complete patient information
2. Input / Output
Doctor Details:
Name: Dr. Sharma
Age: 45
Specialization: Cardiologist

Patient Details:
Name: Rahul
Age: 30
Patient ID: 101
Disease: Heart Problem

Total Hospital Bill: 5000
PS C:\Users\Pravalika kaniganti\Desktop\python-assignment-1> 
3. Logic
🔹 Encapsulation
Patient data (like bill amount) is kept private using double underscore __.


Accessed through getter methods.


🔹 Abstraction
Abstract class Person defines abstract method get_details().


🔹 Inheritance
Patient and Doctor classes inherit from Person.


🔹 Polymorphism
get_details() method behaves differently in Patient and Doctor.
'''
from abc import ABC, abstractmethod

# Abstraction
class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def get_details(self):
        pass


# Inheritance
class Patient(Person):
    def __init__(self, name, age, patient_id, disease):
        super().__init__(name, age)
        self.patient_id = patient_id
        self.disease = disease
        self.__bill = 0   # Encapsulation (private variable)

    # Polymorphism
    def get_details(self):
        print("\nPatient Details:")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Patient ID:", self.patient_id)
        print("Disease:", self.disease)

    def calculate_bill(self, doctor_fee, room_charge):
        self.__bill = doctor_fee + room_charge

    def get_bill(self):   # Getter method
        return self.__bill


class Doctor(Person):
    def __init__(self, name, age, specialization):
        super().__init__(name, age)
        self.specialization = specialization

    # Polymorphism
    def get_details(self):
        print("\nDoctor Details:")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Specialization:", self.specialization)


# Main Program

    # Creating Doctor
doctor = Doctor("Dr. Sharma", 45, "Cardiologist")
doctor.get_details()

    # Creating Patient
patient = Patient("Rahul", 30, 101, "Heart Problem")
patient.get_details()

    # Bill Calculation
patient.calculate_bill(doctor_fee=2000, room_charge=3000)

print("\nTotal Hospital Bill:", patient.get_bill())