#1

class Physician:
    __slots__ = ['id', 'name', 'specialty']
    def __init__(self, id, name, specialty):
        self.id = id
        self.name = name
        self.specialty = specialty

    def get_id(self):
        return self.id 

    def set_id(self, id):
        self.id = id
    
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name
    
    def get_specialty(self):
        return self.specialty

    def set_specialty(self, specialty):
        self.specialty = specialty

    def __repr__(self):
        return "\n ID: " + str(self.id) \
            + "\n Name: " + str(self.name) \
            + "\n Specialty: " +  str(self.specialty) \
            +"\n" 
           

#2

class Patient:
    __slots__ = ['emr_id', 'name', 'gender', 'phone_number']
    def __init__(self, emr_id, name, gender, phone_number):
        self.emr_id = emr_id
        self.name = name
        self.gender = gender
        self.phone_number = phone_number

    def get_emr_id(self):
        return self.emr_id

    def set_emr_id(self, emr_id):
        self.emr_id = emr_id

    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name

    def get_gender(self):
        return self.gender

    def set_gender(self, gender):
        self.gender = gender
    
    def get_phone_number(self):
        return self.phone_number

    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    def __repr__(self):
        return "\n Emirates ID: " + str(self.emr_id) \
            + "\n Name: " + str(self.name) \
            + "\n Gender: " + str(self.gender) \
            + "\n Phone Number: " + str(self.phone_number) \
            

#3

class Encounter:
    __slots__ = ['physician', 'patient', 'date', 'disease', 'medication']
    def __init__(self, physician, patient, date, disease, medication):
        self.physician = physician
        self.patient = patient
        self.date = date
        self.disease = disease
        self.medication = medication
    
    def __repr__(self):
        return "\n Encounter:\n Physician: " + str(self.physician) \
            + "\n Patient: " + str(self.patient) \
            + "\n Date: " + str(self.date) \
            + "\n Disease: " + str(self.disease) \
            + "\n Medication: " + \
            str(self.medication)

import csv

#5

def csv_read():

    with open('patients.csv','r') as file:
        csv_reader = csv.reader(file)
        for read in csv_reader:
            print(read)

    with open('physicians.csv', 'r') as file1:
        csv_reader1 = csv.reader(file1)
        for read_1 in csv_reader1:
            print(read_1)

def csv_write(write1, write2, write3, write4, write5):
    with open('encounter.csv','w') as file2:
        data = str(write1) + '\n' + str(write2) + '\n' + str(write3) + '\n' + str(write4) + '\n' + str(write5)
        file2.write(data)


def main():

    physician1 = Physician('9383984429', 'Hollie Sosa', 'Specialist Radiologist')
    physician2 = Physician('9381603630', 'Kinga Edge', 'Consultant General Surgery')
    physician3 = Physician('9259624392','Shayna Hopper','Consultant of Anesthesia and ICU')

    patient1 = Patient('238741732', 'Mina Ramez', 'Male', '971564720482')
    patient2 = Patient('278332297', 'Omar Morsy', 'Male', '971524230963')
    patient3 = Patient('270005063', 'Helen Sparrow', 'Female', '971561230952')
    patient4 = Patient('265692185', 'Antoine Conrad', 'Male', '971552395710')
    patient5 = Patient('279428910', 'Lillie Sharma', 'Female', '971587609273')
    patient6 = Patient('252920848', 'Steven Avila', 'Male', '971554209450')
    patient7 = Patient('264180135', 'Saarah Mackie', 'Female', '971521209582')
    patient8 = Patient('252483241', 'Emmy Nguyen', 'Female', '971564572342')
    patient9 = Patient('292291579', 'Gino Keller', 'Female', '971552205820')
    patient10 = Patient('299199800', 'Anam Hogg', 'Male', '971585523952')

#6

    encounter1 = Encounter(physician1, patient5, '6-3-2021', 'Alzheimer', 'Donepezil ')
    encounter2 = Encounter(physician3, patient7, '6-7-2017', 'pre-surgery weight management', 'Concentrated Diet')
    encounter3 = Encounter(physician2, patient1, '2-9-2021', 'Abdominal Surgery', 'Analgesic')
    encounter4 = Encounter(physician3, patient3, '10-10-2019', 'Surgery Prep', 'Anesthesia')
    encounter5 = Encounter(physician1, patient10, '1-5-2014', 'Brain Tumor', 'temozolomide')

#7

    print("\n")
    print("Patient information")
    print(patient1)
    print(patient2)
    print(patient3)
    print(patient4)
    print(patient5)
    print(patient6)
    print(patient7)
    print(patient8)
    print(patient9)
    print(patient10)

#8

    print("\n")
    print("Physician information")
    print(physician1)
    print(physician2)
    print(physician3)
    
#9

    print("\n")
    print("Encounters Information")
    print(encounter1)
    print(encounter2)
    print(encounter3)
    print(encounter4)
    print(encounter5)

#10

    csv_read()
    csv_write(encounter1, encounter2, encounter3, encounter4, encounter5)

main()