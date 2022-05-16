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
    request_todo = requests.get(url)
    todos = request_todo.json()

    url = 'https://jsonplaceholder.typicode.com/users'
    request_user = requests.get(url)
    users = request_user.json()

    user_dict = {}

    for user in users:
        username = user['username']
        user_info = []

        for task in todos:
            if task['userId'] == user['id']:
                dict_info = {}
                dict_info['username'] = username
                dict_info['task'] = task['title']
                dict_info['completed'] = task['completed']
                user_info.append(dict_info)
        user_dict[user['id']] = user_info

    with open("todo_all_employees.json", "w") as f:
        json.dump(user_dict, f)
