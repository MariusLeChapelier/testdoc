"""
FILE9 HEADER
============

lala
"""

import retico_core
import test_docs
from test_docs import file1
from file1 import File1


class File9(retico_core.AbstractModule):
    """FILE9 CLASS DOCSTRING"""

    def f1(
        self,
    ):
        """FILE9 FUNCTION DOCSTRING"""
        return File1()
