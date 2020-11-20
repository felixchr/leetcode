#coding: utf-8
# import sys
import importlib
def testit(module_name):
    module = importlib.import_module(module_name)
    importlib.reload(module)
    module.test_solution()

