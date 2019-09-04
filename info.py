class Patient:

    def __init__(self, SSN, date_of_birth, account_number, first_name, last_name, address):
        self.__SSN = SSN
        self.__date_of_birth = date_of_birth
        self.__account_number = account_number
        self.__first_name = first_name
        self.__last_name = last_name
        self.address = address


    # def __init__(self, first_name, last_name):
    #     self.first_name = first_name
    #     self.last_name = last_name

    def __str__(self):
        return (
            f"Name: {self.full_name} SSN:{self.SSN} DOB:{self.date_of_birth} Account #:{self.account_number} Address:{self.address}"
        )

    @property
    def SSN(self):
        try:
            return self.__SSN
        except AttributeError:
            return 0
    @property
    def date_of_birth(self):
        try:
            return self.__date_of_birth
        except AttributeError:
            return 0
    @property
    def account_number(self):
        try:
            return self.__account_number
        except AttributeError:
            return 0
    @property
    def full_name(self):
        try:
            return f"{self.__first_name} {self.__last_name}"
        except AttributeError:
            return 0

    @property
    def address(self):
        try:
            return self.__address
        except AttributeError:
            return 0

    @address.setter
    def address(self, address):
        if type(address) is str:
            self.__address = address
        else:
            raise TypeError('Value must be a string')

cashew = Patient(
    "097-23-1003", "08/13/92", "7001294103",
    "Daniela", "Agnoletti", "500 Infinity Way"
)

print(cashew)

# This should not change the state of the object
# cashew.SSN = "838-31-2256"

# # Neither should this
# cashew.date_of_birth = "01-30-90"

# # But printing either of them should work
# print(cashew.SSN)   # "097-23-1003"

# # These two statements should output nothing
# print(cashew.first_name)
# print(cashew.last_name)




# But this should output the full name
print(cashew.full_name)   # "Daniela Agnoletti"

