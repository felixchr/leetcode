#!/usr/bin/env python

#coding: utf-8
import sys
import importlib
from copy import copy
def testit(module_name):
    module = importlib.import_module(module_name)
    importlib.reload(module)
    func, test_cases = module.test_args()
    fail = 0
    i = 1
    for in_obj, out_obj in test_cases:
        in_obj_store = copy(in_obj)
        if isinstance(in_obj, (tuple, list)):
            out = func(*in_obj)
        else:
            out = func(in_obj)
        if out != out_obj:
            status = 'BAD'
            fail += 1
        else:
            status = 'OK'
        print(f'Test# {i}, In: {in_obj_store}, expect: {out_obj}, out: {out}, Status: {status}')
        i += 1
    if fail == 0:
        print('All passed!')

if __name__ == '__main__':
    module = sys.argv[1]
    if module.endswith('.py'):
        module = module[:-3]
    testit(module)