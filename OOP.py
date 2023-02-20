# Write your code below

class Employee():
  new_id = 1                                   # Define a class variable new_id and set it equal to 1
  def __init__(self):
    self.id = Employee.new_id               # class attribute
    Employee.new_id += 1

  def say_id(self):                           # Define a say_id() method  (class method)
    print("My id is {}.".format(self.id))

e1 = Employee()   # Define the variable e1 and set it to an instance of Employee
e2 = Employee()
e1.say_id()
e2.say_id()


# OOP Pillar: Inheritance

class Employee():
  new_id = 1
  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1

  def say_id(self):
    print("My id is {}.".format(self.id))

# Write your code below, create an Admin class that inherits from the Employee class

class Admin(Employee):
  pass

# Admin is now a subclass of Employee

e1 = Employee()
e2 = Employee()
e3 = Admin()
e3.say_id()

# Overriding Methods

# When implementing inheritance, a child class may want to change the behavior of a 
# method from its parent class. In Python, all we have to do is override a method definition. 
# An overriding method in a subclass is one that has the same definition as the parent class but contains 
# different behavior.

class Employee():
  new_id = 1
  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1

  def say_id(self):
    print("My id is {}.".format(self.id))

class Admin(Employee):
  # Write your code below
  def say_id(self):
    print("I am an Admin")
  

e1 = Employee()
e2 = Employee()
e3 = Admin()
e3.say_id()

# Now when you call .say_id() with e3 you should see the .say_id() method output from Admin

# super()
# When overriding methods we sometimes want to still access the behavior of the parent method. 
# In order to do that we need a way to call the method of the parent class. 
# Python gives us a way to do that using super().
# super() gives us a proxy object. With this proxy object, we can invoke the method of an object’s 
# parent class (also called its superclass). We call the required function as a method on super():


class Animal:
  def __init__(self, name, sound="Grrrr"):
    self.name = name
    self.sound = sound
 
  def make_noise(self):
    print("{} says, {}".format(self.name, self.sound))
 
class Cat(Animal):
  def __init__(self, name):
    super().__init__(name, "Meow!") 
 
pet_cat = Cat("Rachel")
pet_cat.make_noise() # Rachel says, Meow

# In the above example, we have the class Animal and the subclass Cat. Animal has 2 attributes, 
# name and sound and one method, .make_noise(). The .make_noise() method outputs the name and sound 
# of an instance.
# The Cat subclass has an .__init__() method which means the .__init__() method of its superclass, 
# Animal will not be called when creating an instance of Cat. The .__init__() method from the subclass 
# is overriding the one from the superclass.
# To still invoke the .__init__() method of Animal, super().__init__(name, "Meow!") 
# is called inside the subclass .__init__() method. This additional logic allows us to add the "Meow"
# sound from within the Cat class, but still use the .__init__() method of the Animal class.
# super() is used in subclasses to invoke a needed behavior from the superclass alongside the behavior 
# of a subclass method.

class Employee():
  new_id = 1
  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1

  def say_id(self):
    print("My id is {}.".format(self.id))

class Admin(Employee):
  def say_id(self):
    super().say_id()           # Add a line that also calls the Employee class .say_id() method
    print("I am an admin.")

e1 = Employee()
e2 = Employee()
e3 = Admin()
e3.say_id()    # Now the output should be the admin’s ID and that they are an admin



# Multiple Inheritance: Part 1
# Let’s now look at a feature allowed by Python called multiple inheritance. 
# As you may have guessed from the name, this is when a subclass inherits from more than one superclass. 
# One form of multiple inheritance is when there are multiple levels of inheritance. 
# This means a class inherits members from its superclass and its super-superclass.

class Animal:
  def __init__(self, name):
    self.name = name
 
  def say_hi(self):
    print("{} says, Hi!".format(self.name))
 
class Cat(Animal):
  pass
 
class Angry_Cat(Cat):
  pass
 
my_pet = Angry_Cat("Mr. Cranky")
my_pet.say_hi() # Mr. Cranky says, Hi!


# In the above example, Angry_Cat inherits from Cat and Cat inherits from Animal. 
# Both Angry_Cat and Cat have access to the Animal class name attribute and .say_hi() method. 
# Any feature added to Cat, Angry_Cat will also have access to.

class Employee():
  new_id = 1
  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1

  def say_id(self):
    print("My id is {}.".format(self.id))

class Admin(Employee):
  def say_id(self):
    super().say_id()
    print("I am an admin.")

# Write your code below
class Manager(Admin):
  def say_id(self):
    super().say_id()             # Call the Admin class .say_id() method
    print("I am in charge")

e1 = Employee()
e2 = Employee()
e3 = Admin()
e4 = Manager()                    # Define a variable e4 and set it to an instance of the Manager class
e4.say_id()                       # Call the .say_id() method of the instance in e4



# Multiple Inheritance: Part 2

# Another form of multiple inhertance involves a subclass that inherits directly from two 
# classes and can use the attributes and methods of both.

class Animal:
  def __init__(self, name):
    self.name = name
 
class Dog(Animal):
  def action(self):
    print("{} wags tail. Awwww".format(self.name))
 
class Wolf(Animal):
  def action(self):
    print("{} bites. OUCH!".format(self.name))
 
class Hybrid(Dog, Wolf):
  def action(self):
    super().action()
    Wolf.action(self)
 
my_pet = Hybrid("Fluffy")
my_pet.action() # Fluffy wags tail. Awwww
                # Fluffy bites. OUCH!


# The above example shows the class Hybrid is a subclass of both Dog and Wolf which are also both subclasses 
# of Animal. All 3 subclasses can use the features in Animal and Hybrid can use the features of Dog and Wolf. 
# But, Dog and Wolf can not use each other’s features.

# Care must be taken when creating an inheritance structure like this, especially when using the super() 
# method. In the above example, calling super().action() inside the Hybrid class invokes the .action() 
# method of the Dog class. This is due to it being listed before Wolf in the Hybrid(Dog, Wolf) definition.

# The line Wolf.action(self) calls the Wolf class .action() method. The important thing to note here is 
# that self is passed as an argument. This ensures that the .action() method in Wolf receives the Hybrid 
# class instance to output the correct name.

class Employee():
  new_id = 1
  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1

  def say_id(self):
    print("My id is {}.".format(self.id))

class User:
  def __init__(self, username, role="Customer"):
    self.username = username
    self.role = role

  def say_user_info(self):
    print("My username is {}".format(self.username))
    print("My role is {}".format(self.role))

# Write your code below
class Admin(Employee, User):
  def __init__(self):
    super().__init__()
    User.__init__(self, self.id, "Admin")  # Call the .__init__() method of the User class
    # Pass the Admin class instance, id and the string "Admin" as arguments to the .__init__() method call

  def say_id(self):
    super().say_id()
    print("I am an admin.")

e1 = Employee()
e2 = Employee()
e3 = Admin()
e3.say_user_info()  # Call the .say_user_info() method using the Admin instance in e3


# OOP Pillar: Polymorphism

# In computer programming, polymorphism is the ability to apply an identical operation onto different types 
# of objects. This can be useful when an object type may not be known at the program runtime. 
# Polymorphism can be applied using Python in multiple ways. We have already experienced a form of 
# it when exploring inheritance.

class Animal:
  def __init__(self, name):
    self.name = name
 
  def make_noise(self):
    print("{} says, Grrrr".format(self.name))
 
class Cat(Animal):
 
  def make_noise(self):
    print("{} says, Meow!".format(self.name))
 
class Robot:
 
  def make_noise(self):
    print("beep.boop...BEEEEP!!!")

# The example above shows an Animal class, its subclass Cat, and another standalone class Robot. 
# Each class has a method .make_noise() with different outputs. The identical method name with different 
# behaviors is a form of polymorphism

an_animal = Animal("Bear")
my_pet = Cat("Maisy")
my_vacuum = Robot()
objects = [an_animal, my_pet, my_vacuum]
for o in objects:
  o.make_noise()
 
# OUTPUT
# "Bear says, Grrrr"
# "Maisy says, Meow!"
# "beep.boop...BEEEEP!!!"

# With the classes instantiated and added to a list, we are able to iterate through the list and call 
# .make_noise(). This is done without needing to know what type of class .make_noise() belongs to

class Employee():
  new_id = 1
  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1

  def say_id(self):
    print("My id is {}.".format(self.id))

class Admin(Employee):
  def say_id(self):
    super().say_id()
    print("I am an admin.")

class Manager(Admin):
  def say_id(self):
    super().say_id()
    print("I am in charge!")

# Write your code below
meeting = [Employee(), Admin(), Manager()] # Define a variable meeting and set it equal to a list that contains an instance of each class, Employee(), Admin() and Manager()

# With the different types of employees in the meeting, have them all say their ID.
for i in meeting:
  i.say_id()


# Dunder Methods

# The code below shows that when working with different object types like, int, str or list, 
# the + operator performs different functions. This is known as operator overloading and is another 
# form of polymorphism.

# For an int and an int, + returns an int
2 + 4 == 6
 
# For a string and a string, + returns a string
"Is this " + "addition?" == "Is this addition?"
 
# For a list and a list, + returns a list
[1, 2] + [3, 4] == [1, 2, 3, 4]

# To implement this behavior, we must first discuss dunder methods. Every defined class in Python 
# has access to a group of these special methods. We’ve explored a few already, the constructor __init__() 
# and the string representation method __repr__(). The name dunder method is derived from the Double 
# UNDERscores that surround the name of each method.
# Recall that the __repr__() method takes only one parameter, self, and must return a string value. 
# The returned value should be a string representation of the class, which can be seen by using print() 
# on an instance of the class. Review the sample code below for an example of how this method is used.
# Defining a class’s dunder methods is a way to perform operator overloading.

class Animal:
  def __init__(self, name):
    self.name = name
 
  def __repr__(self):
    return self.name
 
  def __add__(self, another_animal):
    return Animal(self.name + another_animal.name)
 
a1 = Animal("Horse")
a2 = Animal("Penguin")
a3 = a1 + a2
print(a1) # Prints "Horse"
print(a2) # Prints "Penguin"
print(a3) # Prints "HorsePenguin"

# The above code has the class Animal with a dunder method, .__add__(). This defines the + operator behavior
#  when used on objects of this class type. The method returns a new Animal object with the names of 
# the operand objects concatenated. In this example, we have created a "HorsePenguin"!
# The line of code a3 = a1 + a2 invokes the .__add__() method of the left operand, a1, with the right 
# operand a2 passed as an argument. The name attributes of a1 and a2 are concatenated using the .__add__() 
# parameters, self and another_animal. The resulting string is used as the name of a new Animal object which
# is returned to become the value of a3.

class Employee():
  new_id = 1
  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1

# there is now a Meeting class with an attendees list attribute and an .__add__() dunder method that adds Employee instances to the attendees list. Before we try and add employees to a meeting, we want to make sure we can know how many employees are in a meeting.

class Meeting:
  def __init__(self):
    self.attendees = []
  
  def __add__(self, employee):
    print("ID {} added.".format(employee.id))
    self.attendees.append(employee)

  # Write your code, Overload the len() operation by defining a __len__() dunder method
  # Inside the __len__() definition, return the length of the attribute attendees
  def __len__(self):
    return len(self.attendees)
  
    
e1 = Employee()
e2 = Employee()
e3 = Employee()
m1 = Meeting()
# Using the Meeting instance m1, add each of the employee instances e1, e2, and e3. Use one line for each employee instance.
m1 + e1
m1 + e2
m1 + e3
print(len(m1))  # Output the length of meeting instance m1



# OOP Pillar: Abstraction

# When a program starts to get big, classes might start to share functionality or we may 
# lose sight of the purpose of a class’s inheritance structure. In order to alleviate issues like this, 
# we can use the concept of abstraction.
# Abstraction helps with the design of code by defining necessary behaviors to be implemented within a 
# class structure. By doing so, abstraction also helps avoid leaving out or overlapping class functionality 
# as class hierarchies get larger.

from abc import ABC, abstractmethod
 
class Animal(ABC):
  def __init__(self, name):
    self.name = name
 
  @abstractmethod
  def make_noise(self):
    pass
 
class Cat(Animal):
  def make_noise(self):
    print("{} says, Meow!".format(self.name))
 
class Dog(Animal):
  def make_noise(self):
    print("{} says, Woof!".format(self.name))
 
kitty = Cat("Maisy")
doggy = Dog("Amber")
kitty.make_noise() # "Maisy says, Meow!"
doggy.make_noise() # "Amber says, Woof!"


# Above we have Cat and Dog classes that inherit from Animal. The Animal class now inherits from 
# an imported class ABC, which stands for Abstract Base Class.
# This is the first step to making Animal an abstract class that cannot be instantiated. 
# The second step is using the imported decorator @abstractmethod on the empty method .make_noise().

# The below line of code would throw an error.

an_animal = Animal("Scruffy")
 
# TypeError: Can't instantiate abstract class Animal with abstract method make_noise

# The abstraction process defines what an Animal is but does not allow the creation of one. 
# The .__init__() method still requires a name, since we feel all animals deserve a name.
# The .make_noise() method exists since all animals make some form of noise, but the method is not 
# implemented since each animal makes a different noise. Each subclass of Animal is now required to define 
# their own .make_noise() method or an error will occur.
# These are some of the ways abstraction supports the design of an organized class structure.