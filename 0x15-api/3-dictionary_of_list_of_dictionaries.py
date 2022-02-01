#!/usr/bin/python3
"""
Module: nombre
Descripcion del modulo

"""

import json
import requests
import sys

users = requests.get("https://jsonplaceholder.typicode.com/users")
users = users.json()
todos = requests.get('https://jsonplaceholder.typicode.com/todos')
todos = todos.json()
todosAll = {}

   for user in users:
        taskList = []
        for task in todos:
            if task.get('userId') == user.get('id'):
                taskDict = {"username": user.get('username'),
                            "task": task.get('title'),
                            "completed": task.get('completed')}
                taskList.append(taskDict)
        todosAll[user.get('id')] = taskList

    with open('todo_all_employees.json', mode='w') as f:
        json.dump(todoAll, f)
