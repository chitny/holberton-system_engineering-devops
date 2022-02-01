#!/usr/bin/python3
"""
Module: nombre
Descripcion del modulo

"""

import requests
import sys

if __name__ == "__main__":

    userId = sys.argv[1]
    userName = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                            .format(userId))

    name = userName.json().get('name')

    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    totalTodo = 0
    doneTodo = 0

    for task in todos.json():
        if task.get('userId') == int(userId):
            totalTodo += 1
            if task.get('completed'):
                doneTodo += 1

    print('Employee {} is done with tasks({}/{}):'
          .format(name, doneTodo, totalTodo))

    print('\n'.join(["\t " + task.get('title') for task in todos.json()
          if task.get('userId') == int(userId) and task.get('completed')]))
