import re
from Models.User import User
from Models.UserManager import UserManager
from Controllers.MainMenu import MainMenu

class LoginSystem:

    def nameCheck(self, name):
        if name == '':
            return 'Please enter your name... :('
        elif len(name) < 1:
            return 'Username is too short...:('
        elif name.isalnum() is not True:
            return 'Please enter the name without number... :('
        else:
            return True

    def mobCheck(self, mobile):
        if len(str(mobile)) == 10:
            return True
        else:
            return 'Please Enter mobile number correctly... :('

    def mailCheck(self, mailid):
        if "@" not in mailid or "." not in mailid:
            return 'Please enter the email correctly.'
        else:
            return True

    def passwordCheck(self, password):
        if len(password) < 8:
            return 'Password is too short'
        elif password.isalnum() is False:
            return 'Please enter the passwords in alphabets and numbers'
        else:
            return True

    def Login(self):
        mailid = input('Enter your E-mail: ')
        password = input('Enter your Password: ')

        user = UserManager.FindUser(mailid, password)

        if user is not None:
            print('Login successfull... :)')

        else:
            print('Invalid mailid/password... Please retry...')

    def Register(self):

        name = input('Enter your name: ')
        namechecking = self.nameCheck(name)
        if namechecking is True:
            pass
        else:
            print(namechecking)

        mobile = int(input('Enter your Mobile number: '))
        mobchecking = self.mobCheck(mobile)
        if mobchecking is True:
            pass
        else:
            print(mobchecking)

        mailid = input('Enter your E-mail id: ')
        mailChecking = self.mailCheck(mailid)
        if mailChecking is True:
            pass
        else:
            print(mailChecking)

        password = input('Enter your password: ')
        passwordchecking = self.passwordCheck(password)
        if passwordchecking is True:
            pass
        else:
            print(passwordchecking)

        #print(namechecking, mobchecking, passwordchecking)

        if (namechecking is True) and (mailChecking is True) and (mobchecking is True) and (passwordchecking is True):
            user = User(name, mobile, mailid, password)
            UserManager.AddUser(user)

        else:
            print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
            print('Entered wrong Details, Enter the Details again...')
            print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
            registration = self.Register()
            registration


    def GuestLogin(self):
        pass

    def ValidateOptions(self, option):
        if option == 1:
            self.Login()
        elif option == 2:
            self.Register()
        elif option == 3:
            self.GuestLogin()
        elif option == 4:
            print('Thank you for using our FoodApp... :)')
            exit()
        else:
            print('Invalid choice... Please retry')
            FoodApp.Init()


class FoodApp:

    LoginOptions = {1:'Login', 2:'Register', 3: 'Guest', 4: 'Exit'}

    @staticmethod
    def Init():
        print()
        print("<< Welcome to Online Food Ordering App >>")
        print()

        menu = MainMenu()
        Start()

        # loginsystem = LoginSystem()
        #
        # while True:
        #     for option in FoodApp.LoginOptions:
        #         print(f'{option}. {FoodApp.LoginOptions[option]}', end=' ')
        #     print()
        #     try:
        #         choice = int(input('Please enter your choice: '))
        #         loginsystem.ValidateOptions(choice)
        #     except Exception as e:
        #         print('Invalid choice. :( Please enter the correct choice... :)')




