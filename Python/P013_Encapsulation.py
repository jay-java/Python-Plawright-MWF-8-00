#encapsulation -> Wrapping data into single unit.
#properties in class are private

class User:
    __id = 0
    __name =''
    __contact = 0

    def __init__(self):
        pass

    def setId(self,id):
        self.__id = id

    def getId(self):
        return self.__id

    def setName(self,name):
        self.__name = name

    def getName(self):
        return self.__name

    def setContact(self,contact):
        self.__contact = contact

    def getContact(self):
        return self.__contact


u = User()
u.setId(12)
u.setName('python')
u.setContact(9876543)
print(u.getId())
print(u.getName())
print(u.getContact())



