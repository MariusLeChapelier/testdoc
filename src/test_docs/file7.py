"""
FILE7 HEADER
============

lala
"""

import retico_core
import test_docs
from test_docs import file1


class File7(retico_core.AbstractModule):
    """FILE7 CLASS DOCSTRING"""

    def f1(
        self,
    ):
        """FILE7 FUNCTION DOCSTRING"""
        return file1.File1()
