import unittest
import HtmlTestRunner

from Test_API import TestApiStatus
from Test_API_Get_Books import TestGetBooks
from Test_Submit_Order import TestSubmitOrder
from Test_Delete_Order import TestDeleteOrder


class TestSuite(unittest.TestCase):
    def test_suite(self):
        suit_tests = unittest.TestSuite()
        suit_tests.addTests([unittest.defaultTestLoader.loadTestsFromTestCase(TestApiStatus),
                              unittest.defaultTestLoader.loadTestsFromTestCase(TestGetBooks),
                              unittest.defaultTestLoader.loadTestsFromTestCase(TestSubmitOrder),
                              unittest.defaultTestLoader.loadTestsFromTestCase(TestDeleteOrder)])

        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_name='Books Api Test Results',
            report_title='Api Test Reporter'
        )

        runner.run(suit_tests)
