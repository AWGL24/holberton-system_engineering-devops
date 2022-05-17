#!/usr/bin/python3
"""
Using what you did in the task #0,
extend your Python script to export data in the JSON format.
"""
import json
import requests
from sys import argv

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/todos'
    parameters = (('userId', argv[1]),)
    request_todo = requests.get(url, params=parameters)
    todos = request_todo.json()

    url = 'https://jsonplaceholder.typicode.com/users'
    parameters = (('id', argv[1]),)
    request_user = requests.get(url, params=parameters)
    user = request_user.json()

    MyList = []
    for task in todos:
        MyDict = {}
        MyDict["task"] = task['title']
        MyDict["completed"] = task['completed']
        MyDict["username"] = user[0]['username']
        MyList.append(MyDict)
    json_obj = {}
    json_obj[argv[1]] = MyList
    with open("{}.json".format(argv[1]), 'w') as json_file:
        json.dump(json_obj, json_file)
