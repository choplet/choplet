from datetime import datetime
from abc import ABCMeta, abstractmethod


class ValidatorException(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)


class Validator(metaclass = ABCMeta):

    types = {}

    def __init__(self,data):
        self.data = data

    @abstractmethod
    def validate(self,data):

        """
            validating data
        """

    @classmethod
    def add_type(cls, name, klass):

        if not name:
            raise ValidatorException('Validator must have a name!')
        elif not issubclass(klass, Validator):
            raise ValidatorException('Class "{}" is not Validator!'.format(klass))
        cls.types[name] = klass


    @classmethod
    def get_instance(cls, name):

        klass = cls.types.get(name)

        if klass is None:
            raise ValidatorException('Validator with name "{}" not found'.format(name))

        return klass(name)


class EmailValidator(Validator):
    def __init__(self, data):
        super().__init__(data)

    def validate(self, data):
        if "@" in data and  "." in data:
            is_email_valid = data.split("@")
            is_email_valid = is_email_valid[1].split(".")
            return is_email_valid[0] != "" and is_email_valid[1] != ""
        else:
            return False


class DateTimeValidator(Validator):
    def __init__(self, data):
        super().__init__(data)

    def validate(self, data):
        is_valid = False
        values = ['%Y-%m-%d',          '%Y-%m-%d %H:%M',
                  '%Y-%m-%d %H:%M:%S', '%d.%m.%Y',
                  '%d.%m.%Y %H:%M',    '%d.%m.%Y %H:%M:%S',
                  '%d/%m/%Y',          '%d/%m/%Y %H:%M',
                  '%d/%m/%Y %H:%M:%S']

        for value in values:
            try:
                if datetime.strptime(data,value):
                    is_valid = True
            except ValueError:
                    pass
        return is_valid


Validator.add_type("email", EmailValidator)
Validator.add_type("date", DateTimeValidator)

#validator = Validator.get_instance("mail")
#print(validator.validate("info@itmo-it.org"))
#print(validator.validate("None"))



#validator = Validator.get_instance("date")
#print(validator.validate("1.9.2017"))
#print(validator.validate("01/09/2017 12:00"))
#print(validator.validate("2017-09-01 12:00:00"))
