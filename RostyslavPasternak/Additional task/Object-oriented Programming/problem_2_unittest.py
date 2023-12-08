import unittest
from Jetpack import Jetpack

class Test_ComplexNumber(unittest.TestCase):
    def test_eq(self):
        first_testpack = Jetpack("Barry", "black")
        second_testpack = Jetpack("Barry", "black")
        self.assertTrue(first_testpack == second_testpack)
    def test_fly(self):
        testpack = Jetpack("Barry", "black")
        testpack.fly(4)
        self.assertAlmostEqual(testpack.amount_of_fuel, 6)
    def test_amount_of_fuel(self):
        testpack = Jetpack("Barry", "black")
        self.assertAlmostEqual(testpack.amount_of_fuel, 10)
    def test_contents_full(self):
        testpack = Jetpack("Barry", "black")
        for item in ["pencil", "pen"]:
            testpack.put(item)
        testpack.put("laptop")
        self.assertListEqual(testpack.contents, ["pencil", "pen"])

    def test_contents(self):
        testpack = Jetpack("Barry", "black")
        for item in ["pencil", "pen"]:
            testpack.put(item)
        self.assertListEqual(testpack.contents, ["pencil", "pen"])
    def test_dump(self):
        testpack = Jetpack("Barry", "black")
        for item in ["pencil", "pen", "paper", "computer"]:
            testpack.put(item)
        testpack.dump()
        self.assertListEqual(testpack.contents, [])
    def test_name(self):
        testpack = Jetpack("Barry", "black")
        self.assertAlmostEqual(testpack.name, "Barry")
    def test_color(self):
        testpack = Jetpack("Barry", "black")
        self.assertAlmostEqual(testpack.color, "black")

    def test_max_size(self):
        testpack = Jetpack("Barry", "black")

        self.assertAlmostEqual(testpack.max_size, 2)

if __name__ == '__main__':
    unittest.main()