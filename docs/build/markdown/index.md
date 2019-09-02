<!-- kelmore__utils documentation master file, created by
sphinx-quickstart on Sun Sep  1 18:49:11 2019.
You can adapt this file completely to your liking, but it should at least
contain the root `toctree` directive. -->
# kelmore_utils

* Utils

* OperatingSystemCheck


## Utils

Utils is a small library of utility functions compiled for personal needs. There’s
nothing too fancy nor anything you can’t find from another library. Utils consists of
smaller functions to be used rather than relying on larger packages.

Right now, this package is very small and only includes function to determine a computer’s operating
system. Hopefully it will be expanded in the future.

### Install

You can install this project directly from Github via:

```
$ pip3.7 install git+https://github.com/kelmore5/python-sub-utilities.git
```

#### Dependencies

* Python 3.7

### Usage

Once installed, you can import the main class like so:

```
>>> from kelmore__utils import Utils
>>>
>>> Utils.os.is_linux()     # True / False
>>> Utils.os.is_mac()       # True / False
>>> Utils.os.is_windows()   # True / False
.
.
.
```

### Documentation

* [Main](docs/build/markdown/index.md)

* [Utils](docs/build/markdown/pages/utils.md)

* [OperatingSystemCheck](docs/build/markdown/pages/operating_system.md)

### Personal Note

Utils is only on Github because I reference it in other projects. I don’t have any plans
to maintain this project, but I will update it from time to time.

<!-- kelmore__utils documentation master file, created by
sphinx-quickstart on Sun Sep  1 18:49:11 2019.
You can adapt this file completely to your liking, but it should at least
contain the root `toctree` directive. -->
## Utils


#### class kelmore__utils.utils.Utils()
A Python class to hold extraneous utility functions

Right now, the only use for this class is to check a computer’s operating system

Usage:

```
>>> from kelmore__utils import Utils
>>>
>>> Utils.os.is_linux()
>>> Utils.os.is_mac()
>>> Utils.os.is_windows()

True if the current operating system is Linux else False
True if the current operating system is Mac/OSX else False
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


Usage:

```
>>> from kelmore__utils import Utils
>>>
>>> Utils.first_non_none(None, None, 5, 'hello', None)

5
```


#### os()
Used to determine a computer’s operating system

alias of `OperatingSystemCheck`
