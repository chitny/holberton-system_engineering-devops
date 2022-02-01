#!/usr/bin/python3
"""
Module: nombre
Descripcion del modulo

"""

import json
import requests
import sys


if __name__ == "__main__":

    userId = sys.argv[1]
    userName = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                            .format(userId))

    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    todos = todos.json()

    todosUser = {}
    tasksList = []

    for task in todos:
        if task.get('userId') == int(userId):
            taskDict = {"task": task.get('title'),
                        "completed": task.get('completed'),
                        "username": userName.json().get('username')}
            tasksList.append(taskDict)
    todosUser[userId] = tasksList

    filename = userId + '.json'
    with open(filename, mode='w') as f:
        json.dump(todosUser, f)
