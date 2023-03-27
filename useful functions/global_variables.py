# Global Variables


# In other programming languages, there is the notion of global variables that are accessible to any function.
# We can leverage this ability within Python. In the text editor window, code as follows:

balance = 0


def main():
    print("Balance:", balance)


if __name__ == "__main__":
    main()

# Notice how we create a global variable called balance, outside of any function.
# Since no errors are presented by executing the code above, you’d think all is well. However, it is not! 
# In the text editor window, code as follows:


balance = 0


def main():
    print("Balance:", balance)
    deposit(100)
    withdraw(50)
    print("Balance:", balance)


def deposit(n):
    balance += n


def withdraw(n):
    balance -= n


if __name__ == "__main__":
    main()


# Notice how we now add the functionality to add and withdraw funds to and from balance. 
# However, executing this code, we are presented with an error! We see an error called UnboundLocalError. 
# You might be able to guess that, at least in the way we’ve currently coded balance and our deposit and withdraw functions, 
# we can’t reassign it a value value inside a function.

# To interact with a global variable inside a function, the solution is to use the global keyword. In the text editor window, 
# code as follows:


balance = 0


def main():
    print("Balance:", balance)
    deposit(100)
    withdraw(50)
    print("Balance:", balance)


def deposit(n):
    global balance
    balance += n


def withdraw(n):
    global balance
    balance -= n


if __name__ == "__main__":
    main()

# Notice how the global keyword tells each function that balance does not refer to a local variable: instead, 
# it refers to the global variable we originally placed at the top of our code. Now, our code functions!

# Utilizing our powers from our experience with object-oriented programming, we can modify our code to use a class instead of a 
# global variable. 
# In the text editor window, code as follows:


class Account:
    def __init__(self):
        self._balance = 0

    @property
    def balance(self):
        return self._balance

    def deposit(self, n):
        self._balance += n

    def withdraw(self, n):
        self._balance -= n


def main():
    account = Account()
    print("Balance:", account.balance)
    account.deposit(100)
    account.withdraw(50)
    print("Balance:", account.balance)


if __name__ == "__main__":
    main()

# Notice how we use account = Account() to create an account. Classes allow us to solve this issue of needing a global 
# variable more cleanly because these instance variables are accessible to all the methods of this class utilizing self.

# Generally speaking, global variables should be used quite sparingly, if at all!