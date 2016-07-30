
from dao import user as userDao
from flask import session

def login(username, password):
    if not (username and password):
        return (False, "Please enter both username & password")
    user = userDao.find(username)
    if not user:
        return (False, "Username '{}' not found".format(username))
    if user["password"] != password:
        return (False, "Incorrect password")
    session["loggedInUserId"] = user["id"]
    return (True, "Login successful")


def logout():
    session.pop("loggedInUserId", None)


def register(username, password, fullName):
    if not (username and password and fullName):
        return (False, "Please enter all details")
    newUserId = userDao.create(username, password, fullName)
    session["loggedInUserId"] = newUserId
    return (True, "Registration successful")


def getLoggedInUserInfo():
    return userDao.findById(session["loggedInUserId"])
