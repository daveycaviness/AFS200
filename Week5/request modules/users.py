import requests

class User:
    def __init__(self, firstName, lastName, email, userName, password, uuid, phone, cell, pictureLarge, pictureThumbnail):
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.userName = userName
        self.password = password
        self.uuid = uuid
        self.phone = phone
        self.cell = cell
        self.picturelarge = pictureLarge
        self.picturethumbnail = pictureThumbnail

    def setName(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def setEmail(self, email):
        self.email = email

    def setUserName(self, userName):
        self.userName = userName

    def setPassword(self, password):
        self.password = password

    def setUuid(self, uuid):
        self.uuid = uuid

    def setPhone(self, phone):
        self.phone = phone

    def setCell(self, cell):
        self.cell = cell

    def setPictureLarge(self, picturelarge):
        self.picturelarge = picturelarge

    def setPictureThumbnail(self, picturethumbnail):
        self.picturethumbnail = picturethumbnail

    def getName(self, name):
        return f"{self.firstName} {lastName}"

    def getEmail(self, email):
        self.email = email

    def getUserName(self, userName):
        self.userName = userName

    def getPassword(self, password):
        self.password = password

    def getUuid(self, uuid):
        self.uuid = uuid

    def getPhone(self, phone):
        self.phone = phone

    def getCell(self, cell):
        self.cell = cell

    def getPictureLarge(self, picturelarge):
        self.picturelarge = picturelarge

    def getPictureThumbnail(self, pictureThumbnail):
        self.picturethumbnail = pictureThumbnail

    def __str__(self):
        retStr = f"{self.firstName} {self.lastName}" 
        retStr += f"({self.email})"
        return retStr


class AuthorizedUser():
    def __init__(self):
        self.users = []

    def newUserInfo(self, user):
        self.users.append(user)

    def showAuthorizedUsers(self):
        for user in self.users:
            print(user)

def getUsers():
    URL = "https://randomuser.me/api/?nat=us&results=10"

    try:
        response = requests.get(URL, timeout=5)
        response.raise_for_status()
        response_JSON = response.json()
        return response_JSON
    except requests.exceptions.HTTPError as errh:
        print(errh)
    except requests.exceptions.ConnectionError as errc:
        print(errc)
    except requests.exceptions.Timeout as errt:
        print(errt)
    except requests.exceptions.RequestException as err:
        print(err)

AuthorizedUsers = AuthorizedUser()
newUser = getUsers()

for user in newUser["results"]:
    firstName = user["name"]["first"]
    lastName = user["name"]["last"]
    email = user["email"]
    userName = user["login"]["username"]
    password = user["login"]["password"]
    uuid = user["login"]["uuid"]
    phone = user["phone"]
    cell = user["cell"]
    pictureLarge = user["picture"]["large"]
    pictureThumbnail = user["picture"]["thumbnail"]

    newUser = User(firstName, lastName, email, userName, password, uuid, phone, cell, pictureLarge, pictureThumbnail)
    AuthorizedUsers.newUserInfo(newUser)

AuthorizedUsers.showAuthorizedUsers()