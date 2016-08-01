"""
Done in Python shell:
    a = 10
    b = 2
    c = a + b
    assert c == 12
"""

try:
    1/0
except ZeroDivisionError:
    print "ERROR: Tried to divide by zero"