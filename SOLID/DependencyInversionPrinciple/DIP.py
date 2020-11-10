# In object-oriented design, the dependency inversion principle is a specific form of decoupling software modules. When following this principle, the conventional dependency relationships established from high-level, policy-setting modules to low-level, dependency modules are reversed, thus rendering high-level modules independent of the low-level module implementation details. The principle states:

# High-level modules should not depend on low-level modules. Both should depend on abstractions (e.g. interfaces).Abstractions should not depend on details. Details (concrete implementations) should depend on abstractions. By dictating that both high-level and low-level objects must depend on the same abstraction, this design principle inverts the way some people may think about object-oriented programming.[2]

# The idea behind points A and B of this principle is that when designing the interaction between a high-level module and a low-level one, the interaction should be thought of as an abstract interaction between them. This not only has implications on the design of the high-level module, but also on the low-level one: the low-level one should be designed with the interaction in mind and it may be necessary to change its usage interface.

# In many cases, thinking about the interaction in itself as an abstract concept allows the coupling of the components to be reduced without introducing additional coding patterns, allowing only a lighter and less implementation-dependent interaction schema.

# When the discovered abstract interaction schema(s) between two modules is/are generic and generalization makes sense, this design principle also leads to the following dependency inversion coding pattern.

class UserAuthentication:
    def __init__(self, className) :
        self._className = className

    def ValidateUser(self, uname, pwd):
        return self._className.ValidateUser(self, uname, pwd)

class FakeServiceAuthentication(UserAuthentication):
    def ValidateUser(self, uname, pwd):
        if(uname == 'guest' and pwd == 'guest'):
            return True
        else:
            return False

import sqlite3
from sqlite3 import Error
class DBServiceAuthentication(UserAuthentication):
    def ValidateUser(self, uname, pwd ):
        try:
            con = sqlite3.connect('sqldb.db')
            sql = f"select count(*) from Users where Username='{uname}' and Password='{pwd}'"
            cursor = con.cursor()
            cursor.execute(sql)
            result = cursor.fetchone()
            if result[0] > 0 :
                return True
            else:
                return False
        except Error:
            print(Error)
        finally:
            con.close()

#ua = UserAuthentication(FakeServiceAuthentication)

import json
import sys
import types

def str_to_class(classname):
    return getattr(sys.modules[__name__], classname)

with open('service.json') as f:
    data = json.load(f)

service = str_to_class(data['name'])

ua = UserAuthentication(service)

uname = input('Enter Username :')
pwd = input('Enter Password :')

result = ua.ValidateUser(uname, pwd)

print(f'Result : {result}')