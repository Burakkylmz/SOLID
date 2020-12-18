# A class should have one and only one reason to change, meaning that a class should only have one job. For example, let's assume that we have a simple application that 
# will save the personal information of the newly recruited personnel in the system, keep the logs of this transaction and send an information e-mail to the manager when 
# the person is registered in the system. We can carry out these operations in a single class. If we do this in this way, we would be at odds with this principle. To comply 
# with this principle, we need to handle all these processes in separate classes. Each class should have only one responsibility. For example, a class should be used for 
# logging, a class to enroll the employee in the database and a class for the information e-mail.

import pymongo

class EmployeeProcess:
    def RegisterUser(self, userName, password):
        client = pymongo.MongoClient('localhost', 27017)
        db = client["AppUserDb"]
        collection = db["Employyes"]

        post = {"UserName":userName,"LastName":password}
        collection.insert_one(post)


class Logger:
    def WriteLogToSystem(self, message):
        logFile = open("IOFile.txt","w")
        logFile.write(message)

class Registrations:
    def RegisterUser(self, userName, password):
        try:
            EmployeeProcess().RegisterUser(userName, password)
        except Exception:
            Logger().WriteLogToSystem('Error While Registering User')

