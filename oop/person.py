#A person class that calculates the persons age based on
#their date of birth  and current time

#import date class from the datetime module to work with dates
from datetime  import date

#define the class to work with the person
class Person:
    #initilize the person object with name, country and dateofbirth
    def __init__(self,name,country, dateDeNaissance):
        self.name = name
        self.country = country
        self.dateDeNaissance = dateDeNaissance

    #calculate the persons age based on theier dateDeNaissance
    def calculeAge(self):
        today = date.today()
        age = today.year - self.dateDeNaissance.year
        if today < date(today.year, self.dateDeNaissance.month, self.dateDeNaissance.day):
            age -= 1
        return age
    
#Create person objects with different attributes
person1 = Person("Tchaptchet", "Cameroon", date(2000, 1, 17))

print("Person 1:")
print("Name:", person1.name)
print("Country:", person1.country)
print("Age:", person1.calculeAge())