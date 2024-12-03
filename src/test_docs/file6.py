"""
FILE6 HEADER
============

lala
"""

import retico_core
import test_docs
import test_docs.file1


class File6(retico_core.AbstractModule):
    """FILE6 CLASS DOCSTRING"""

    def f1(
        self,
    ):
        """FILE6 FUNCTION DOCSTRING"""
        return test_docs.file1.File1()
