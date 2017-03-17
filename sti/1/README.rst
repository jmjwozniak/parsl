
Swift/T Interface 1
===================

This workflow demonstrates the simplest way to let Python control a Swift/T workflow.

**Source:** https://github.com/swift-lang/swift-e-lab ``sti/1`` (branch ``rework-executors``)

Files
-----

workflow.swift
  This is the main workflow.  Run with:

::

  $ export PYTHONPATH=$PWD
  $ swift-t workflow.swift

swift_e.py
  This is a set of Python functions called by Swift/T.  There are Swift/T functions with matching names.

Functions
---------

The Python & Swift/T functions are:

get_tasks()
  Gets a set of tasks from Python.

task()
  Computes on a task in Python (does a ``sum()``) with added delay.

put_results()
  Posts the sums back to Python.

TODO
----

The script runs forever.  We could make it stop by having Python return ``"DONE"``.

Transcript
----------

Example usage:

::

  $ swift-t -l -n 5 workflow.swift
  [0] python: new tasks: [6, 1, 6];[5, 1, 6];[4, 0, 4]
  [1] python: compute:   [5, 1, 6]
  [2] python: compute:   [6, 1, 6]
  [3] python: compute:   [4, 0, 4]
  [0] python: results:   13;12;8
  [1] python: new tasks: [9, 0, 3];[7, 7, 5];[1, 5, 5]
  [0] python: compute:   [9, 0, 3]
  [3] python: compute:   [7, 7, 5]
  [2] python: compute:   [1, 5, 5]
  [1] python: results:   12;19;11
  ...

As shown by the MPI rank prefixes, the Python compute tasks run on different ranks.
