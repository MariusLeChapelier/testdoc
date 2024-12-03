"""
FILE5 HEADER
============

lala
"""

import retico_core
import test_docs


class File5(retico_core.AbstractModule):
    """FILE5 CLASS DOCSTRING"""

    def f1(
        self,
    ):
        """FILE5 FUNCTION DOCSTRING"""
        return test_docs.file1.File1()
