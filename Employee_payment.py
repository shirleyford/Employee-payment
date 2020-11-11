#Employee management system for a restaurant
#Payments are hourly.

class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age
      
  # Employee positions and payments.
class ExecutiveChef(Employee):
    def pay(self, payment="$45"):
        return f"{self.name} hourly pay is {payment}"
  
class SousChef(Employee):
    def pay(self, payment="$30"):
        return f"{self.name} hourly pay is {payment}" 
    
class KitchenManager(Employee):
    def pay(self, payment="$20"):
        return f"{self.name} hourly pay is {payment}" 
        

class LineCook(Employee):
    def pay(self, payment="$15"):
        return f"{self.name} hourly pay is {payment}"        
     
     
class PastryChef(Employee):
    def pay(self, payment="$25"):
        return f"{self.name} hourly pay is {payment}"
      
class FoodAndBeverageManager(Employee):
    def pay(self, payment="$28"):
        return f"{self.name} hourly pay is {payment}"
      
class Sommelier(Employee):
    def pay(self, payment="$21"):
        return f"{self.name} hourly pay is {payment}"
      
                  #Bartenders are given tips
class Bartender(Employee):
    def pay(self, payment="$8"):
        return f"{self.name} hourly pay is {payment}"
                   
                   #servers are given tips
class Server(Employee):
    def pay(self, payment="$5"):
        return f"{self.name} hourly pay is {payment}"
      
class DriveThruOperator(Employee):
    def pay(self, payment="$11"):
        return f"{self.name} hourly pay is {payment}"      
      
class HostOrHostess(Employee):
    def pay(self, payment="$10"):
        return f"{self.name} hourly pay is {payment}"
      
class Cashier(Employee):
    def pay(self, payment="$4"):
        return f"{self.name} hourly pay is {payment}"      
      
class Dishwasher(Employee):
    def pay(self, payment="$3"):
        return f"{self.name} hourly pay is {payment}"      
      
class Cleaner(Employee):
    def pay(self, payment="$3"):
        return f"{self.name} hourly pay is {payment}"     
 
   # sample

mark = ExecutiveChef("mark john", 49)
print(mark.pay())

grace = SousChef("Grace Luke", 28)
print(grace.pay())