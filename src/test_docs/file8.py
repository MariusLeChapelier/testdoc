"""
FILE8 HEADER
============

lala
"""

import retico_core
from test_docs import file1


class File8(retico_core.AbstractModule):
    """FILE8 CLASS DOCSTRING"""

    def f1(
        self,
    ):
        """FILE8 FUNCTION DOCSTRING"""
        return file1.File1()
