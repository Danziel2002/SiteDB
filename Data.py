from pymongo import MongoClient
import gridfs
import smtplib

#---------------------------------------------------------------------------------------------------------

Join = MongoClient('localhost', 27017)
db = Join.MyUsers
fs = gridfs.GridFS(db)
UsersColection = db['Users']
Action = str(input("What you wanna do: "))

#---------------------------------------------------------------------------------------------------------

def SendEmail(msg, receiver, Email, Password):
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(Email,Password)
    server.sendmail(Email,receiver, msg)
    server.quit()

#---------------------------------------------------------------------------------------------------------

def Login():
  
    if __name__ == "__main__":
    
        InputUser = str(input("UserName: "))
        InputPass = str(input("PassWord: ")) 
        NotExist = 0
        AllUsers = 0
        Users = UsersColection.find({"User":InputUser, "Pass":InputPass})
    
        for i in Users:
            if InputUser != i["User"] and InputPass != i["Pass"]:
                NotExist += 1

            AllUsers += 1

        if NotExist == AllUsers:
            print("Not an account!")
            Account = str(input("Wanna make an account?"))

            if Account == "Yes":
                Register()

            else:
                Login()

        else:
            print("Login Succesful")

#---------------------------------------------------------------------------------------------------------

def Register():

    if __name__ == "__main__":
        Exists = False
        InputUser = str(input("UserName: "))
        InputPass = str(input("PassWord: "))
        ConfPass = str(input("Confirm the PassWord: "))
        NotExist = 0
        AllUsers = 0

        if InputPass != ConfPass:

            print("The PassWords do not match: ")
            ConfPass = str(input("Confirm the PassWord: "))
   
        OccupiedUser = UsersColection.find({"User": InputUser})
        Users1 = UsersColection.find({}, {"User": 1})

        for i in Users1:
            print(i)
            if InputUser != i["User"]:
                NotExist += 1

            AllUsers += 1

        if NotExist == AllUsers:
            UsersColection.insert({"User":InputUser, "Pass":InputPass})
        
        else:
            print("Account Exists")

#---------------------------------------------------------------------------------------------------------

def ForgotPass():
    InputUser = str(input("UserName: "))

    PassWords  = UsersColection.find({"User":InputUser})
    for Password in PassWords:
        Message = "{} forgot his password, it is {}".format(InputUser, Password["Pass"])
    SendEmail(Message, "gruescudaniel006@gmail.com", "gruescudaniel006@gmail.com", "Daniel2002!")



#---------------------------------------------------------------------------------------------------------


if Action == "Login":
    Login()
elif Action == "Register":
    Register()
elif Action == "ForgotPass":
    ForgotPass()

