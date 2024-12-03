"""
FILE7 HEADER
============

lala
"""

import retico_core
from test_docs.file1 import File1


class File7(retico_core.AbstractModule):
    """FILE7 CLASS DOCSTRING"""

    def f1(
        self,
    ):
        """FILE7 FUNCTION DOCSTRING"""
        return File1()
