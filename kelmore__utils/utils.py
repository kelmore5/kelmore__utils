import sys
from typing import Any


class OperatingSystemCheck:
    """A Python helper class (used in :class:`Utils <kelmore__utils.utils.Utils>`)
        to determine a computer's operating system
    """

    @staticmethod
    def is_linux() -> bool:
        """Returns True if the current operating system is Linux, else False

        :return: True if the current operating system is Linux else False
        :rtype: bool
        """
        return sys.platform == 'linux'

    @staticmethod
    def is_mac() -> bool:
        """Returns True if the current operating system is Mac/OSX, else False

        :return: True if the current operating system is Mac/OSX else False
        :rtype: bool
        """
        return sys.platform == 'darwin'

    @staticmethod
    def is_windows() -> bool:
        """Returns True if the current operating system is Windows, else False

        :return: True if the current operating system is Windows else False
        :rtype: bool
        """
        return not (sys.platform == 'linux' or sys.platform == 'darwin')


class Utils:
    """A Python class to hold extraneous utility functions

    Right now, the only use for this class is to check a computer's operating system

    Usage::

        >>> from kelmore__utils import Utils
        >>>
        >>> Utils.os.is_linux()
        >>> Utils.os.is_mac()
        >>> Utils.os.is_windows()

        True if the current operating system is Linux else False
        True if the current operating system is Mac/OSX else False
        True if the current operating system is Windows else False

    """

    os: OperatingSystemCheck = OperatingSystemCheck
    """Used to determine a computer's operating system"""

    @staticmethod
    def first_non_none(*items: Any) -> Any:
        """Takes a variable number of items as arguments and returns the first argument that is
        not None

        :param items: Any number of arguments that may or may not be None
        :return: The first argument that is not None
        :type items: Any
        :rtype: Any

        Usage::

            >>> from kelmore__utils import Utils
            >>>
            >>> Utils.first_non_none(None, None, 5, 'hello', None)

            5
        """
        for item in items:
            if item is not None:
                return item
        return None
