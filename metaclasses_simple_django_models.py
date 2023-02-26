"""
Django is a famous back-end framework written in Python. It has a vast list of features 
including the creation of database tables through "models". You can see an example of such model below:

class Person(models.Model):
    first_name = models.CharField()
    last_name = models.CharField()
Apart from creating a table it can perform validation, generate HTML forms, and so on. 
This is possible thanks to metaclasses. Normally there are better solutions than using metaclasses, 
but they can be of great help in creating powerful framework interfaces. This goal of this kata is to 
learn and understand how such frameworks works.

Your task is to implement a class Model and classes for its fields to support functionality like in the following example:

class User(Model):
    first_name = CharField(max_length=30)
    last_name = CharField(max_length=50)
    email = EmailField()
    is_verified = BooleanField(default=False)
    date_joined = DateTimeField(auto_now=True)
    age = IntegerField(min_value=5, max_value=120, blank=True)


user1 = User(first_name='Liam', last_name='Smith', email='liam@example.com')
user1.validate()

print(user1.date_joined)  # prints date and time when the instance was created
print(user1.is_verified)  # prints False (default value)

user1.age = 256
user1.validate()  # raises ValidationError - age is out of range

user2 = User()
user2.validate()  # raises ValidationError - first three fields are missing and mandatory
The classes which inherit from Model should:

support creation of fields using class-attribute syntax
have a validate method which checks whether all fields are valid
The field types which you should implement are:

CharField - a string with min_length (default 0) and max_length (default None) parameters
IntegerField - an integer with min_value (default None) and max_value (default None) parameters
BooleanField - a boolean
DateTimeField - a datetime with auto_now (default False) parameters which determines whether the 
current time should be set automatically on creation
EmailField - a string in the format of address@subdomain.domain where address, subdomain, 
and domain are sequences of alphabetical characters with min_length (default 0) and max_length (default None) parameters

Also, each field type has parameters blank (default False) which determines whether None 
is allowed as a value, and default (default None) which determines the value to be used if nothing was provided.

Each field type should have its own validate method which checks whether the provided value has 
the correct type and satisfies the length/value constraints.

Notes

min_value/max_value and min_length/max_length bounds are inclusive
if DateTimeField's auto_now flag is set to True, and no default value is specified, 
accessing its default attribute should always yield current time.


"""

import re
from datetime import datetime


class ValidationError:
    pass


class CharField:
    
    def __init__(self,
                 char_value: str = "",
                 min_length: int = 0,
                 max_length: int = None,
                 default: str = None,
                 blank: bool = False) -> None:

        self.min_length = min_length
        self.max_length = max_length
        self.blank = blank

        if char_value == "":
            self.char_value = default

        else:
            self.char_value = char_value

    def __repr__(self) -> str:
        return self.char_value

    def validate(self,
                 char_value: str) -> bool:

        return self.has_correct_length(char_value) and self.has_correct_type(char_value)

    def has_correct_length(self,
                           char_value: str) -> bool:

        if self.max_length:
            return self.min_length <= len(char_value) <= self.max_length
        
        else:
            return self.min_length <= len(char_value)


    def has_correct_type(self,
                         char_value: str) -> bool:
        return isinstance(char_value, str)


class IntegerField:
    
    def __init__(self,
                 min_value: int = None,
                 max_value: int = None,
                 default: int = None,
                 blank: bool = False) -> None:
        self.min_value = min_value
        self.max_value = max_value

    def validate(self) -> bool:
        ...
    
    def has_correct_value(self) -> bool:
        return self.min_value <= self.integer <= self.max_value


class BooleanField:
    
    def __init__(self, default: bool = None, blank: bool = False) -> None:
        ...

    def validate(self) -> bool:
        ...


class DateTimeField:
    
    def __init__(self, auto_now: bool = True, default: str = datetime.now().strftime("%H:%M:%S"), blank: bool = False) -> None:
        self.default = default

    def validate(self) -> bool:
        ...
    

class EmailField:

    def __init__(self, default: str = None, blank: bool = False) -> None:
        ...
    
    def validate(self) -> bool:
        
        """Validate email format of 'testname@testdomain.domain'. Use regex"""
        
        # possible regex for mail check: (([a-zA-Z0-9])@{1}([a-zA-z]).{1}([a-zA-Z]*))
        
        ...


class Model:

    def __init__(self,
                 first_name: str,
                 last_name: str,
                 email: str,
                 default: str = None,
                 blank: bool = False) -> None:
        
        self.first_name = CharField(char_value=first_name)
        self.last_name = CharField(char_value=last_name)
        self.email = EmailField(email)
        self.is_verified = BooleanField()
        self.date_joined = DateTimeField()
        self.age = IntegerField()
        self.default = default
        self.blank = blank
        self.valid_data = []
    
        # create getter and setter methods for the single fields
    
    def validate(self) -> bool:
        
        """
        Check if data is entered correct. Is correct when every single piece of data is entered correct.
        """
        
        return all(self.valid_data)


class User(Model):
    first_name = CharField(max_length=3)
    last_name = CharField(max_length=50)
    email = EmailField()
    is_verified = BooleanField(default=False)
    date_joined = DateTimeField(auto_now=True)
    age = IntegerField(min_value=5, max_value=120, blank=True)

    def __init__(self,
                 first_name: str,
                 last_name: str,
                 email: str, default: str = None,
                 blank: bool = False) -> None:

        self.valid_data: bool = []

        if User.first_name.validate(first_name):
            self.valid_data.append(True)
            self.first_name = first_name
        else:
            self.valid_data.append(False)
            self.first_name = default

        if User.last_name.validate(last_name):
            self.valid_data.append(True)
            self.last_name = last_name
        else:
            self.valid_data.append(False)
            self.last_name = default

        
if __name__ == '__main__':

    user1 = User(first_name='Lia', last_name='Smith', email='liam@example.com')
    print(user1.validate())
    print(user1.last_name, type(user1.last_name))