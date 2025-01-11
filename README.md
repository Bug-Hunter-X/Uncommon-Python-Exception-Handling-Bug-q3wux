# Uncommon Python Error: General Exception Handling

This repository demonstrates a common mistake in Python exception handling that can make debugging more difficult.  The code in `bug.py` uses a bare `except Exception` block which can catch more than intended and hide the root cause of an error.

The improved code in `bugSolution.py` shows best practices for dealing with exceptions, handling specific types of errors individually, to provide more specific and informative error messages.