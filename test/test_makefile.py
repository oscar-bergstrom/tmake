from unittest import TestCase

from pathlib import Path
import os
import sys


current_path = os.path.realpath(os.path.dirname(__file__))
makefile_1 = Path(current_path, "Makefile.1")
sys.path.append(os.path.dirname(current_path))


import tmake


class ParseMakefileTests(TestCase):
    def test_right_file_returned(self):
        m: tmake.Makefile = tmake.Makefile.parse(makefile_1)
        assert m
        assert isinstance(m, tmake.Makefile)

    def test_make_inc(self):
        m: tmake.Makefile = tmake.Makefile.parse(makefile_1)

        assert m.make_inc == "tests"

