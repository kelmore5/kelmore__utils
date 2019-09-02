<!-- kelmore__utils documentation master file, created by
sphinx-quickstart on Sun Sep  1 18:49:11 2019.
You can adapt this file completely to your liking, but it should at least
contain the root `toctree` directive. -->
# kelmore_utils

* Utils

* OperatingSystemCheck


## Utils

This is a small library of array functions I’ve compiled for my own personal needs. This project
doesn’t have anything fancy nor anything you can’t find from another library, but I like to
write out the smaller functions I need rather than relying on packages.

Right now, this package is very small and only includes function to determine a computer’s operating
system, but I hope to expand on it in the future.

This is only on Github as I reference it in other projects I use, but if you’re reading this,
check it out! There may be something you can use for your own projects to simplify using arrays.

I don’t have any plans to maintain this project, but I will add from it from time to time. I may
add more thorough documentation at some point for this, but as of now this suits my needs.

### Install

#### Dependencies

* python 3.7

#### Import

Once installed, you can import the main class like so:

```
from kelmore__utils import Utils

Utils.os.is_linux()
Utils.os.is_mac()
Utils.os.is_windows()
.
.
.
```

<!-- kelmore__utils documentation master file, created by
sphinx-quickstart on Sun Sep  1 18:49:11 2019.
You can adapt this file completely to your liking, but it should at least
contain the root `toctree` directive. -->
## Utils


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
