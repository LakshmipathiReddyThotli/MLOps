class chatbook:
    user_id = 1
    def __init__(self):
        self.id = chatbook.user_id
        chatbook.user_id += 1
        self.name = ''
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.__private = 'sensitive data'
        # self.menu()
    
    # setter and getter methods for private variables
    def get_private(self):
        return self.__private
    
    def set_private(self, value):
        self.__private = value
    
    @staticmethod
    def get_id():
        return chatbook.user_id
    @staticmethod
    def set_id(val):
        chatbook.user_id = val

    def menu(self):
        user_input = input("""Welcome to chatbook!!
        1. Press 1 to SignUp
        2. Press 2 SignIn
        3. Press 3 to write a post
        4. Press 4 to message a friend
        5. Press any other key to exit""")

        if user_input == '1':
            self.singup()
        elif user_input == '2':
            pass 
        elif user_input == '3':
            pass 
        elif user_input == '4':
            pass 
        else:
            exit()
    def singup(self):
        email = input("Enter you email")
        password = input("Enter your password")
        self.name = email 
        self.password = password 
        print("Sign Up is successful!")
        print("\n")
        self.menu()




# function vs method
# dunder method
# self 
# you can create attribute out of the class also 
# obj.username = "Lakshmipathi"
# print(obj.username)

# Encapsulation - define self.__variable and access using obj._classname__privatevariableName 
# getter and setter 
# static method 

