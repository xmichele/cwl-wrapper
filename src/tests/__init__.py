import unittest
import tests.subworkflow_test

def subworkflow_test_suite():
    print("Running subworkflow_test_suite")
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(tests.subworkflow_test)
    return suite