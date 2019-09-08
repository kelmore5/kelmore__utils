import os
import sys
from typing import Any, Optional, Type


class OperatingSystemCheck:
    """A Python helper class (used in :class:`Utils <kelmore__utils.utils.Utils>`)
        to determine a computer's operating system
    """

    @staticmethod
    def is_linux() -> bool:
        """Checks whether the current operating system is a Linux computer

        Usage::

            >>> Utils.os.is_linux()
            True / False

        :return: True if the current operating system is Linux else False
        :rtype: bool
        """
        return sys.platform == 'linux'

    @staticmethod
    def is_mac() -> bool:
        """Checks whether the current operating system is Mac/OSX

        Usage::

            >>> Utils.os.is_mac()
            True / False

        :return: True if the current operating system is Mac/OSX else False
        :rtype: bool
        """
        return sys.platform == 'darwin'

    @staticmethod
    def is_windows() -> bool:
        """Checks if the current operating system is Windows

        Usage::

            >>> Utils.os.is_windows()
            True / False

        :return: True if the current operating system is Windows else False
        :rtype: bool
        """
        return not (sys.platform == 'linux' or sys.platform == 'darwin')


class CPUTools:
    """A Python helper class (used in :class:`Utils <kelmore__utils.utils.Utils>`)
        to determine details about the computer's CPU"""

    @staticmethod
    def is_32() -> bool:
        """ Checks whether the current processor is a 32-bit (only) CPU

        Usage::

            >>> Utils.cpu.is_32()
            True / False

        :return: True if the current processor is only 32-bit else False
        :rtype: bool
        """
        return CPUTools.processor() == 'x86'

    @staticmethod
    def is_64() -> bool:
        """ Checks whether the current processor is a 64-bit CPU

        Usage::

            >>> Utils.cpu.is_64()
            True / False

        :return: True if the current processor is 64-bit else False
        :rtype: bool
        """
        return CPUTools.processor() == 'x86_64'

    @staticmethod
    def is_arm64() -> bool:
        """ Checks whether the current processor is an arm64 CPU

        Usage::

            >>> Utils.cpu.is_arm64()
            True / False

        :return: True if the current processor is arm64 else False
        :rtype: bool
        """
        return CPUTools.processor() == 'arm64'

    @staticmethod
    def is_arm7l() -> bool:
        """ Checks whether the current processor is an arm7l CPU

        Usage::

            >>> Utils.cpu.is_arm7l()
            True / False

        :return: True if the current process is arm7l else False
        :rtype: bool
        """
        return CPUTools.processor() == 'arm7l'

    @staticmethod
    def processor() -> str:
        """ Returns the current processor

        Usage::

            >>> Utils.cpu.processor()
            'x86_x64'

        :return: The current processor
        :rtype: str
        """
        return os.uname()[4]


class Utils:
    """A Python class to hold extraneous utility functions

    Right now, the only use for this class is to check a computer's CPU and operating system

    Usage::

        >>> from kelmore__utils import Utils
        >>>
        >>> Utils.cpu.is_32()
        >>> Utils.cpu.is_64()
        >>>
        >>> Utils.os.is_linux()
        >>> Utils.os.is_mac()
        >>> Utils.os.is_windows()

        True if the current processor is only 32-bit else False
        True if the current processor is 64-bit else False

        True if the current operating system is Linux else False
        True if the current operating system is Mac/OSX else False
        True if the current operating system is Windows else False

    """

    cpu: Type[CPUTools] = CPUTools
    """Used to determine a computer's processor type"""

    os: Type[OperatingSystemCheck] = OperatingSystemCheck
    """Used to determine a computer's operating system"""

    @staticmethod
    def first_non_none(*items: Any) -> Any:
        """Takes a variable number of items as arguments and returns the first argument that is
        not None

        Usage::

            >>> Utils.first_non_none(None, None, 5, 'hello', None)
            5

        :param items: Any number of arguments that may or may not be None
        :return: The first argument that is not None
        :type items: Any
        :rtype: Any
        """
        for item in items:
            if item is not None:
                return item
        return None

    @staticmethod
    def float_or_none(num: str) -> Optional[float]:
        """ Parses a string into a float. Returns None if the string cannot be parsed
            (instead of raising an error).

        Usage::

            >>> Utils.float_or_none('55.0')
            >>> Utils.float_or_none('54h')
            55
            None

        :param num: A string to parse into a double
        :type num: str
        :return: A float type if the string is a valid float else None
        :rtype: Optional[float]
        """
        if isinstance(num, str):
            num = num.strip()

            if num == '':
                return None

        try:
            return float(num)
        except ValueError:
            return None
        except TypeError:
            return None

    @staticmethod
    def int_or_none(num: str) -> Optional[int]:
        """ Parses a string into an integer. Returns None if the string cannot be parsed
            (instead of raising an error).

        Usage::

            >>> Utils.float_or_none('219')
            >>> Utils.float_or_none('123abc')
            219
            None

        :param num: A string to parse into an integer
        :type num: str
        :return: An int type if the string is a valid integer else None
        :rtype: Optional[int]
        """
        if isinstance(num, str):
            num = num.replace(',', '').strip()

            if num == '':
                return None

        try:
            return int(num)
        except ValueError:
            return None
        except TypeError:
            return None
