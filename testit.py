#coding: utf-8
# import sys
import importlib
def testit(module_name):
    module = importlib.import_module(module_name)
    importlib.reload(module)
    func, test_cases = module.test_args()
    fail = 0
    for in_obj, out_obj in test_cases:
        out = func(*in_obj)
        if out != out_obj:
            status = 'BAD'
            fail += 1
        else:
            status = 'OK'
        print(f'In: {in_obj}, expect: {out_obj}, out: {out}, Status: {status}')
    if fail == 0:
        print('All passed!')
