import unittest
from Commission import Commission

class test_Comission(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.commission_calculator = Commission()

    @classmethod
    def tearDownClass(cls):
        print('This is After')


    def setUp(self) -> None:
        return super().setUp()
    

    def tearDown(self) -> None:
        print('\n End of test')

    def test_negative_inputs(self):
        self.assertEqual(self.commission_calculator.check_commission(1, 1, 1), 10000)


if __name__ == '__main__':
    unittest.main()