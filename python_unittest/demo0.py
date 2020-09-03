# -*- coding: utf-8 -*-

import unittest

from HTMLTestRunner import HTMLTestRunner


class demo(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print('i am setup class')

    @classmethod
    def tearDownClass(cls) -> None:
        print('i am teardown class')

    def setUp(self) -> None:
        print('i am setup')

    def tearDown(self) -> None:
        print('i am teardown')

    def test_case0(self):
        print('i am test_case0 in demo')
        self.assertEqual(1, 2, "is 1 equal to 2?")
        self.assertIn('h', 'this', 'is h in this?')

    @unittest.skipUnless(1 < 2, "skip this case")
    def test_case1(self):
        print('i am test_case1 in demo')

    def test_case2(self):
        print('i am test case2 in demo')


class demo1(unittest.TestCase):

    def test_case1(self):
        print("i am test_case1 in demo1")

    def test_case2(self):
        print('i am test_case2 in demo1')


class demo2(unittest.TestCase):
    def test_case1(self):
        print('i am test_case1 in demo2')

    def test_case2(self):
        print('i am test_cases2 in demo2')


if __name__ == '__main__':
    # report_title = 'my unittest report'
    # description = 'this demonstrates the report output by HTMLTestRunner.'
    # report_file = './ExampleReport.html'

    # 01
    #  add test cases to testsuites
    # suite = unittest.TestSuite()
    # suite.addTest(demo('test_case1'))
    # suite.addTest(demo1('test_case1'))
    # unittest.TextTestRunner().run(suite)

    # 02
    # add test class to testsuites
    suite1 = unittest.TestLoader().loadTestsFromTestCase(demo)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(demo2)
    suite = unittest.TestSuite([suite1, suite2])
    unittest.TextTestRunner().run(suite)

    # 03
    ### run test cases in special root
    # discover = unittest.defaultTestLoader.discover('./','demo*.py')
    # unittest.TextTestRunner().run(discover)


    ##04 generate test  report

    # with open('my_report.html', 'wb') as f:
    #     runner = HTMLTestRunner.HTMLTestRunner(stream=f, title=report_title, description=description)
    #     runner.run(suite)
    ## print test report as html
