from Models.User import User

class UserManager:
    __Users = []

    @classmethod
    def AddUser(cls, userObj):
        if isinstance(userObj, User):
            cls.__Users.append(userObj)
            print('//////////////////////////////////////////////////////////////////////////////////')
            print('Registration is successfully Done...:)')
            print('//////////////////////////////////////////////////////////////////////////////////')
        else:
            print('Invalid user')

    @classmethod
    def FindUser(cls, mailid, pwd):
        for user in cls.__Users:
            if user.email == mailid and user.password == pwd:
                return user



