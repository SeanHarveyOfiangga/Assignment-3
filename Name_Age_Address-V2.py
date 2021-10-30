def getName():
    _name = input("Name: ")
    return _name

def getAge():
    _Age = input("Age: ")
    return _Age
    
def getAddress():
    _Address = input("Address: ")
    return _Address

def display(name_,age_, address_):
    print(f"Hi, my name is {name_}. I am {age_} years old and I live in {address_}.")    

Name = getName()
Age = getAge()
Address = getAddress()
display(Name, Age, Address,)