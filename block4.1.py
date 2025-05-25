>>> def print_arg(arg):
...     print(arg)
...

>>> print_arg("Hello")
Hello

>>> print_arg(123)
123

>>> print_arg([1, 2, 3])
[1, 2, 3]

>>> print_arg({"a": 1, "b": 2})
{'a': 1, 'b': 2}

>>> print_arg()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: print_arg() missing 1 required positional argument: 'arg'

>>> print_arg(1, 2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: print_arg() takes 1 positional argument but 2 were given
