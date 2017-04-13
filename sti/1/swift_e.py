
# SWIFT_E.PY
# Pretend Swift/E controller for Swift/T

import random
import time
import pickle
import logging
from ipyparallel.serialize import pack_apply_message, unpack_apply_message
from base64 import b64encode, b64decode

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
        buf  = f.read()
        sbuf = str(b64encode(buf))

        return sbuf

def task(string_bufs):
    """ Executor.
    Args: name of the inputfile, which is a pickled object that contains
    the function to be executed, it's args, kwargs etc.
    name of the outputfile, where the outputs from the computation are to
    be pickled are written

    """
    #all_names = dir(__builtins__)
    user_ns   = globals()#locals()
    #user_ns.update( {'__builtins__' : {k : getattr(__builtins__, k)  for k in all_names} } )

    log = open("debug.log", 'w+')

    d = eval(string_bufs)
    bufs = pickle.loads(b64decode(d))


    log.write("User_ns : \n")
    for key in user_ns.keys():
        log.write("    key:{0} value:{1}\n".format(key, user_ns[key]))

    log.write( "Got bufs : {0}\n".format( bufs ))


    f, args, kwargs = unpack_apply_message(bufs, user_ns, copy=False)

    log.write( "Got f : {0}\n".format( f ))
    log.write( "Got args : {0}\n".format( args ))
    log.write( "Got kwargs : {0}\n".format( kwargs ))


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


    log.write("Executing code : {0}\n".format(code))

    try:
        print("[RUNNER] Executing : {0}".format(code))
        exec(code, user_ns, user_ns)

    except Exception as e:
        logging.warn("Caught errors but will not handled %s", e)
        #return e
        log.write("Caught exception in  code :{0} \n".format(e))
        log.close()

        ret_value = e

    else :
        #print("Done : {0}".format(locals()))
        print("[RUNNER] Result    : {0}".format(user_ns.get(resultname)))
        #return user_ns.get(resultname)
        ret_value = user_ns.get(resultname)


    ret_sbuf = pickle.dumps(ret_value)
    ret_encoded = str(b64encode(ret_sbuf))

    log.write("Returning : {0}\n".format(ret_encoded))
    log.write("type      : {0}\n".format(type(ret_encoded)))
    log.close()
    return ret_encoded

'''
def task(arguments):
    time.sleep(1) # Simulate computation time
    msg("compute", arguments)
    return sum(tuple(eval(arguments)))
'''
def put_results(results):
    msg("results", results)
    return ""



if __name__ == "__main__":

    sbuf = get_tasks()
    print("Got sbuf from get_task : ", type(sbuf))

    r = task(sbuf)
    print("Got result from task : ", type(r))

    rbuf = eval(r)
    result = pickle.loads(b64decode(rbuf))
    print("Decoded result : ", result)

