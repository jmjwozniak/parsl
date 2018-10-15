
Support for resource limits #567
================================

https://github.com/Parsl/parsl/issues/567

Examples
--------

Use ``make`` to build ``master.x``

- ``$ python child.py``
  
  will consume memory forever, possibly crashing your system
  
- ``$ ./master.x python child.py``
  
  will limit Python to 16 MB RAM; Python will exit with ``MemoryError``

- ``master.py``
  
  limits itself to 16 MB RAM.  You have to edit it to select whether to
  launch ``child.py`` or not:
  
  - ``master.py`` exits correctly with ``MemoryError``
     when limiting its own memory use
  - ``master.py`` limits the memory use of its subprocess ``child.py``,
     causing it to trigger a ``MemoryError``, which can be caught at the
     ``master.py`` level

Notes
-----

https://linux.die.net/man/2/setrlimit

A child process created via fork(2) inherits its parent's resource
limits. Resource limits are preserved across execve(2).
