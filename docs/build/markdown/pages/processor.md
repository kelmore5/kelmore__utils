<!-- kelmore__utils documentation master file, created by
sphinx-quickstart on Sun Sep  1 18:49:11 2019.
You can adapt this file completely to your liking, but it should at least
contain the root `toctree` directive. -->
# ProcessorCheck


#### class kelmore__utils.utils.CPUTools()
A Python helper class (used in `Utils`)
to determine details about the computer’s CPU


#### static is_32()
Checks whether the current processor is a 32-bit (only) CPU

Usage:

```
>>> Utils.cpu.is_32()
True / False
```


* **Returns**

    True if the current processor is only 32-bit else False



* **Return type**

    bool



#### static is_64()
Checks whether the current processor is a 64-bit CPU

Usage:

```
>>> Utils.cpu.is_64()
True / False
```


* **Returns**

    True if the current processor is 64-bit else False



* **Return type**

    bool



#### static is_arm64()
Checks whether the current processor is an arm64 CPU

Usage:

```
>>> Utils.cpu.is_arm64()
True / False
```


* **Returns**

    True if the current processor is arm64 else False



* **Return type**

    bool



#### static is_arm7l()
Checks whether the current processor is an arm7l CPU

Usage:

```
>>> Utils.cpu.is_arm7l()
True / False
```


* **Returns**

    True if the current process is arm7l else False



* **Return type**

    bool



#### static processor()
Returns the current processor

Usage:

```
>>> Utils.cpu.processor()
'x86_x64'
```


* **Returns**

    The current processor



* **Return type**

    str
