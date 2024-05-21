#!/usr/bin/python3
"""returns information about his/her list progress"""
import csv
import requests
import sys


if __name__ == "__main__":
    EMPLOYEE_id = int(sys.argv[1])
    response_a = requests.get(f'https://jsonplaceholder.\
typicode.com/users/{EMPLOYEE_id}', timeout=1)
    html_a = response_a.json()
    EMPLOYEE_NAME = html_a['name']
    attributes = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
    task_list = []
    for i in range(1, 201):
        URL = f'https://jsonplaceholder.typicode.com/todos/{i}'
        try:
            response_b = requests.get(URL, timeout=1)
            try:
                html_b = response_b.json()
                if html_b['userId'] == EMPLOYEE_id:
                    task_list.append({"USER_ID": EMPLOYEE_id,
                                      "USERNAME": f'{EMPLOYEE_NAME}',
                                      "TASK_COMPLETED_STATUS":
                                      f'{html_b["completed"]}',
                                      "TASK_TITLE": f'{html_b["title"]}'})
            except ValueError:
                print('Not a valid JSON')
        except Exception:
            pass
    with open(f'{EMPLOYEE_id}.csv', 'w', encoding='utf-8') as csv_file:
        csv_writer = csv.DictWriter(csv_file, attributes,
                                    quoting=csv.QUOTE_ALL)
        for task in task_list:
            csv_writer.writerow(task)
