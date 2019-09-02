<!-- kelmore__utils documentation master file, created by
sphinx-quickstart on Sun Sep  1 18:49:11 2019.
You can adapt this file completely to your liking, but it should at least
contain the root `toctree` directive. -->
# Utils


#### class kelmore__utils.utils.Utils()
A Python class to hold extraneous utility functions

Right now, the only use for this class is to check a computer’s operating system

Example:

```
>>> from kelmore__utils import Utils
>>>
>>> Utils.os.is_windows()

True if the current operating system is Windows else False
```


#### static first_non_none(\*items)
Takes a variable number of items as arguments and returns the first argument that is
not None


* **Parameters**

    **items** (*Any*) – Any number of arguments that may or may not be None



* **Returns**

    The first argument that is not None



* **Return type**

    Any


Example:

```
>>> from kelmore__utils import Utils
>>>
>>> Utils.first_non_none(None, None, 5, 'hello', None)

5
```


#### os()
Used to determine a computer’s operating system

alias of `OperatingSystemCheck`
