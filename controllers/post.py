
from dao import post as postDao
from flask import session

def add(content):
    if not content:
        return (False, "Content cannot be empty")
    postDao.create(content, session["loggedInUserId"])
    return (True, "Post created succesfully")


def findAll():
    return postDao.findAll()
