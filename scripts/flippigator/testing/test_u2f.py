import os
import time

import pytest
from termcolor import colored

from flippigator.case import BaseCase

os.system("color")


@pytest.mark.u2f
class TestU2f(BaseCase):
    def test_u2f_menu_negative(self, nav):
        nav.u2f.go_into()
        menu = nav.get_menu_list()
        menu_ref = [
            "Connection is active",
            "BTIcon",
        ]
        assert menu == menu_ref, "U2F menu list is wrong"
        nav.go_to_main_screen()