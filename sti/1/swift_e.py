
# SWIFT_E.PY
# Pretend Swift/E controller for Swift/T

import random
import time

def msg(token, s):
    print("python: %-9s: %s" % (token, s))

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
    msg("new tasks", result)
    return result

def task(arguments):
    time.sleep(1) # Simulate computation time
    msg("compute", arguments)
    return sum(tuple(eval(arguments)))

def put_results(results):
    msg("results", results)
    return ""
