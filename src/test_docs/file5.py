"""
FILE5 HEADER
============

lala
"""

import retico_core
import test_docs
from test_docs import utils
from utils import device_definition


class File5(retico_core.AbstractModule):
    """FILE5 CLASS DOCSTRING"""

    def f1(
        self,
    ):
        """FILE5 FUNCTION DOCSTRING"""
        return device_definition()
