import unittest


class CalculatorTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEquals('3 + 4', 7)
    def test_2(self):
        self.assertEquals('3 * 4', 7)
    def test_3(self):
        self.assertEquals('3 / 4', 7)
    def test_4(self):
        self.assertEquals('3 // 4', 7)
    def test_5(self):
        self.assertEquals('3 - 4', 7)
    def test_6(self):
        self.assertEquals('3 + 4', 7)
    def test_7(self):
        self.assertEquals('3 % 4', 7)

    # Тест для проверки работы, можно удалить
    def test_one(self):
        self.assertEquals(1, 1)
