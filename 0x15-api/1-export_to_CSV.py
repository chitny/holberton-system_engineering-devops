#!/usr/bin/python3
"""
Module: nombre
Descripcion del modulo

"""

import csv
import requests
import sys


if __name__ == "__main__":

    userId = sys.argv[1]
    userName = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                            .format(userId))

    name = userName.json().get('username')

    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    totalTodo = 0
    doneTodo = 0

    filename = userId + '.csv'
    with open(filename, mode='w') as f:
        writer = csv.writer(f, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL, lineterminator='\n')
        for task in todos.json():
            if task.get('userId') == int(userId):
                writer.writerow([userId, name, str(task.get('completed')),
                                 task.get('title')])
