# Python program to demonstrate  
# method overriding 


# Defining parent class 
class Parent(): 

    # Constructor 
    def __init__(self): 
        self.value = "Bathman is bathing"

    # Parent's show method 
    def show(self): 
        print(self.value) 

# Defining child class 
class Child(Parent): 

    # Constructor 
    def __init__(self): 
        self.value = "Blower is blowing"

    # Child's show method 
    def show(self): 
        print(self.value) 


# Driver's code 
obj1 = Parent() 
obj2 = Child() 

obj1.show() 
obj2.show() 