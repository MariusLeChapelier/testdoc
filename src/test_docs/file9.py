"""
FILE9 HEADER
============

lala
"""

import retico_core
from test_docs.file1 import File1


class File9(retico_core.AbstractModule):
    """FILE9 CLASS DOCSTRING"""

    def f1(
        self,
    ):
        """FILE9 FUNCTION DOCSTRING"""
        return File1()
