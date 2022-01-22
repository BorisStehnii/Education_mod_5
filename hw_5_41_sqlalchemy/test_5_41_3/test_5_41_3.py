import unittest

from hw_5_41_sqlalchemy.hw_5_41_2_query import *


class MyTestCaseAvgSalary(unittest.TestCase):

    def setUp(self) -> None:
        self.session = Session()

    def test_query_table(self):
        # print(avg_salary(session_, Employees, Jobs))
        self.assertEqual(avg_salary(self.session, Employees, Jobs)[0], ('Public Accountant', 8300.0))
        #
        # self.session.commit()
        # self.session.close()

