"""
FILE8 HEADER
============

lala
"""

import retico_core
import test_docs
from test_docs.file1 import File1


class File8(retico_core.AbstractModule):
    """FILE8 CLASS DOCSTRING"""

    def f1(
        self,
    ):
        """FILE8 FUNCTION DOCSTRING"""
        return File1()
