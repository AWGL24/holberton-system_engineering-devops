#!/usr/bin/python3
"""
Using what you did in the task #0,
extend your Python script to export data in the CSV format.
"""
import csv
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

    with open("{}.csv".format(argv[1]), 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            csv_writer.writerow(
                [int(argv[1]), user[0]['username'],
                 task['completed'], task['title']])
