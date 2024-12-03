"""
FILE6 HEADER
============

lala
"""

import retico_core
from test_docs import file1


class File6(retico_core.AbstractModule):
    """FILE6 CLASS DOCSTRING"""

    def f1(
        self,
    ):
        """FILE6 FUNCTION DOCSTRING"""
        return file1.File1()
