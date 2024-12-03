"""
FILE4 HEADER
============

lala
"""

import retico_core
import test_docs


class File4(retico_core.AbstractModule):
    """FILE4 CLASS DOCSTRING"""

    def f1(
        self,
    ):
        """FILE4 FUNCTION DOCSTRING"""
        return test_docs.text_class()
