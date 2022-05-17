#!/usr/bin/python3
"""
Module holds python script that returns information about an employee todo list
"""
from sys import argv
import requests
import json

if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/todos'
    parameters = (('userId', argv[1]),)
    request_todo = requests.get(url, params=parameters)
    todos = request_todo.json()

    url = 'https://jsonplaceholder.typicode.com/users'
    parameters = argv[1]
    request_user = requests.get(url, params=parameters).json().get('name')

    MyList = []
    for task in todos:
        if task['completed']:
            MyList.append(task)

    print("Employee {} is done with tasks({}/{}):".format(request_user,
          len(MyList), len(todos)))
    if len(MyList) > 0:
        for task in MyList:
            print("\t{}".format(task['title']))
