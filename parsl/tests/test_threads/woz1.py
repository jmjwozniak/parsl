# Import Parsl
import parsl
from parsl import *

#from nose.tools import nottest

import os
import time
import shutil
import argparse

# Let's create a pool of threads to execute our functions
workers = ThreadPoolExecutor(max_workers=4)
# We pass the workers to the DataFlowKernel which will execute our Apps over the workers.
dfk = DataFlowKernel(workers)


parsl.set_stream_logger(format_string="%(message)s")

@App('bash', dfk)
def task1(i=0, dur=0, outputs=None, stdout=None, stderr=None):
    cmd_line = '''
echo "HELLO" {i} > {outputs[0]}
echo "HELLO" {i} > {outputs[1]}
sleep {dur}
'''

# B->D
@App('bash', dfk)
def task2(f=None, dur=0, outputs=None, stdout=None, stderr=None):
    cmd_line = '''
cat {f} > {outputs[0]}
sleep {dur}
'''

app_fu_bc, [B,C] = task1(i=3, dur=1, outputs=["B.txt", "C.txt"])
# Bug: stdout thread collision
app_fu_d,  [D]   = task2(f=B, dur=2, outputs=["D.txt"], stdout="D.log")
app_fu_e,  [E]   = task2(f=C, dur=2, outputs=["E.txt"], stdout="E.log")
