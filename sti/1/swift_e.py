
import random
import time

def make_task():
    result = []
    for i in range(0,3):
        result.append(random.randint(0,9))
    return result

def get_tasks():
    task_strings = []
    for i in range(0,3):
        task = make_task()
        task_string = str(task)
        task_strings.append(task_string)
    result = ";".join(task_strings)
    print("tasks: " + result)
    return result

def task(arguments):
    time.sleep(0.1) # Simulate computation time
    return sum(tuple(eval(arguments)))

def put_results(results):
    print("results: " + results)
    return ""
