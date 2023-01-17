import time 
import threading

#For threading we should import the threading module first
#We create a thread as threading.Thread(target=YourFunction, args=ArgumentsToTheFunction).
#After creating the thread, we start it using the start() function.
#We also call the join() function to stop the thread after completion of the task.

#First Method
def greet_them(cars):
    print("Greet starts")
    for car in cars:
        print("Hello Dear "+ car + ". How are you?")
        time.sleep(0.5)
    print("Greet completed")
    

#Second Method
def assign_id(cars):
    print("Assigning starts")
    i=1
    for car in cars:
        print("Hey! {}, your id is {}.".format(car, i))
        i+=1
        time.sleep(0.5)
    print("Assigning completed")

cars =["Tata", "Maruthi", "MG", "Hyundai", "Honda", "Toyota"]

t= time.time()

t1 = threading.Thread(target=greet_them, args=(cars,))
t2 = threading.Thread(target=assign_id, args=(cars,))

t1.start()
t2.start()

# greet_them(cars)
# assign_id(cars)
t1.join()
t2.join()

print("Cars intro finished")
print("I Took "+ str(time.time()-t))
