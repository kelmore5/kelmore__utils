# Utils

Utils is a small library of utility functions compiled for personal needs. There’s
nothing too fancy nor anything you can’t find from another library. Utils consists of
smaller functions to be used rather than relying on larger packages.

Right now, this package is very small and only includes function to determine a computer’s operating
system. Hopefully it will be expanded in the future.

## Install

You can install this project directly from Github via:

```
pip3.7 install git+https://github.com/kelmore5/python-sub-utilities.git
```

### Dependencies

* Python 3.7

### Import

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

## Documentation

* [Main](docs/build/markdown/index.md)

* [Utils](docs/build/markdown/pages/utils.md)

## Personal Note

Utils is only on Github because I reference it in other projects. I don’t have any plans
to maintain this project, but I will update it from time to time.
