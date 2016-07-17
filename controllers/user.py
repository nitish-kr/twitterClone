
from dao import user as userDao
from flask import session, redirect, url_for

def login(username, password):
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
    newUserId = userDao.create(username, password, fullName)
    session["loggedInUserId"] = newUserId
