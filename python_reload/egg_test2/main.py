import sys
from importlib import reload
import shutil

shutil.copyfile('egg_test_v1.egg', 'egg_test.egg')

sys.path.append('egg_test.egg')

#  --- step 1 ---

import egg_test

from egg_test.func import test_func



# --- step 2 ---

shutil.copyfile('egg_test_v2.egg', 'egg_test.egg')


reload(egg_test)

from egg_test.func import test_func as func2

assert test_func is func2
