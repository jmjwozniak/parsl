
# SWIFT_E.PY
# Pretend Swift/E controller for Swift/T

import random
import time
import pickle
from ipyparallel.serialize import pack_apply_message, unpack_apply_message
#from serialize import serialize_object, deserialize_object

def msg(token, s):
    print("python: %-10s %s" % (token+":", s))

def make_task():
    result = []
    for i in range(0,3):
        result.append(random.randint(0,9))
    return result

def get_tasks():
    with open('/scratch/midway/yadunand/swift-e-lab/sti/1/5cbd919b-e875-4c8f-9f05-e16acb360d0e.pkl', 'rb') as f:
        data = pickle.load(f)
        return str(data)


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

def task(string_bufs):
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
    with open('/scratch/midway/yadunand/swift-e-lab/sti/1/5cbd919b-e875-4c8f-9f05-e16acb360d0e.pkl', 'rb') as f:
        bufs = pickle.load(f)

    bufs = bytes(string_bufs, 'utf-8')
    print(bufs)

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


if __name__ == '__main__' :

    bufs = None
    with open('/scratch/midway/yadunand/swift-e-lab/sti/1/5cbd919b-e875-4c8f-9f05-e16acb360d0e.pkl', 'rb') as f:
        # Bufs is in bytes
        bufs = pickle.load(f)
        sbuf = pickle.dumps(bufs)

    print("String sbuf")
    print(str(sbuf))

    
    if str(sbuf) == sbuf :
        print("Equal")
    else:
        print("Not equal")
        print("bufs: \n", bufs)
        print("bsbufs: \n", sbuf)


    if bufs == str(bufs, 'utf-8'):
        print("Equal")
    else:
        print("Not equal")
        print("bufs: \n", bufs)
        print("bsbufs: \n", sbuf)

    ##string_buf = get_tasks()
    #print(task(str(bufs)))
