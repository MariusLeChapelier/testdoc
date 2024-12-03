"""
FILE4 HEADER
============

lala
"""

import retico_core
import test_docs
from test_docs.utils import device_definition


class File4(retico_core.AbstractModule):
    """FILE4 CLASS DOCSTRING"""

    def f1(
        self,
    ):
        """FILE4 FUNCTION DOCSTRING"""
        return device_definition()
