import unittest
import esPrimoTest


def suite():
    suite = unittest.TestSuite()
    suite.addTest(esPrimoTest.esPrimoTest('test_entrynumber'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())