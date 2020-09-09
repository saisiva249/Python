# if we dont have a class concept then we have to write the 
# attribute for each objects like Cars_name = [a,b,c,], cars_company=[x,y,z]
# and if we have so many instances and its values it will be difficult to handle, 
#while modifying or deleting a particluar as we have to find the index and delete the same on all
# classes or OOP allows us to write a code once and reuse it many times

#class names should be in camelcase
# class can have () or with out also we can write
class Car():
    def __init__(self, company):
        # this is a class attribute which is dependent on instance
        # this attribnubte can be accessed outside the class
        self.company = company
        
    def get_company(self):
        # if we dont specify the self then error will be thrown, company not defined
        return self.company
        
    def drive(self):
        print("Test deive Started")

#calling a class
car1 = Car("Maruthi")
# after intiantiating we are calling the method
# even though the number of arguments passed in thecall
# internally the object on which the call is made will be sent as a 
# parameter to the method 
car1.drive()
print(car1.company)

# instead of accessing the attribute we can get attributes using methods also
print(car1.get_company())
