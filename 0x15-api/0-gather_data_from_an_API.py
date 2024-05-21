#!/usr/bin/python3
"""returns information about his/her list progress"""
import requests
import sys


if __name__ == "__main__":
    EMPLOYEE_id = int(sys.argv[1])
    response_a = requests.get(f'https://jsonplaceholder.\
typicode.com/users/{EMPLOYEE_id}', timeout=1)
    html_a = response_a.json()
    EMPLOYEE_NAME = html_a['name']
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    task_list = []
    for i in range(1, 201):
        URL = f'https://jsonplaceholder.typicode.com/todos/{i}'
        try:
            response_b = requests.get(URL, timeout=1)
            try:
                html_b = response_b.json()
                if html_b['userId'] == EMPLOYEE_id:
                    TOTAL_NUMBER_OF_TASKS += 1
                    if html_b['completed'] is True:
                        NUMBER_OF_DONE_TASKS += 1
                        task_list.append(html_b['title'])
            except ValueError:
                print('Not a valid JSON')
        except Exception:
            pass
    print(f'Employee {EMPLOYEE_NAME} is done with tasks({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):')
    for task in task_list:
        print(f'\t {task}')
