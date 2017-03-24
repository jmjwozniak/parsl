# SWIFT_E.PY
# Pretend Swift/E controller for Swift/T

import random
import time
import pickle
from serialize import unpack_apply_message
#from serialize import serialize_object, deserialize_object

def msg(token, s):
    print("python: %-10s %s" % (token+":", s))

def make_task():
    result = []
    for i in range(0,3):
        result.append(random.randint(0,9))
    return result

def get_tasks():
    with open('/home/yadu/src/parsl/parsl/tests/181487ca-9791-4eb4-9431-b7fe9d69b968.pkl', 'rb') as f:
        task = f.read()
        msg("New task : ", task)
        return str(task)


    '''
    task_strings = []
    for i in range(0,3):
        task = make_task()
        task_string = str(task)
        task_strings.append(task_string)
    result = ";".join(task_strings)
    msg("new tasks", result)
    return result
    '''

def task(bufs):
    """ Executor.
    Args: name of the inputfile, which is a pickled object that contains
    the function to be executed, it's args, kwargs etc.
    name of the outputfile, where the outputs from the computation are to
    be pickled are written

    """
    all_names = dir(__builtins__)
    user_ns   = locals()
    user_ns.update( {'__builtins__' : {k : getattr(__builtins__, k)  for k in all_names} } )

    bufs = None

    f, args, kwargs = unpack_apply_message(bufs, user_ns, copy=False)

    print(f)
    print(args)

    #x = f(*args,**kwargs)
    #print(x)
    fname = getattr(f, '__name__', 'f')
    prefix     = "kotta_"
    fname      = prefix+"f"
    argname    = prefix+"args"
    kwargname  = prefix+"kwargs"
    resultname = prefix+"result"

    user_ns.update({ fname : f,
                     argname : args,
                     kwargname : kwargs,
                     resultname : resultname })

    code = "{0} = {1}(*{2}, **{3})".format(resultname, fname,
                                           argname, kwargname)

    try:
        print("[RUNNER] Executing : {0}".format(code))
        exec(code, user_ns, user_ns)

    except Exception as e:
        logger.warn("Caught errors but will not handled %s", e)
        return e

    else :
        #print("Done : {0}".format(locals()))
        print("[RUNNER] Result    : {0}".format(user_ns.get(resultname)))
        return user_ns.get(resultname)

'''
def task(arguments):
    time.sleep(1) # Simulate computation time
    msg("compute", arguments)
    return sum(tuple(eval(arguments)))
'''
def put_results(results):
    msg("results", results)
    return ""
