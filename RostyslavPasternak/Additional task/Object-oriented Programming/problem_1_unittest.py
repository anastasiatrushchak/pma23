import unittest
from Backpack import Backpack

class Test_ComplexNumber(unittest.TestCase):
    def test_eq(self):
        first_testpack = Backpack("Barry", "black")
        second_testpack = Backpack("Barry", "black")
        self.assertTrue(first_testpack == second_testpack)

    def test_contents_full(self):
        testpack = Backpack("Barry", "black")
        for item in ["pencil", "pen", "paper", "computer","phone"]:
            testpack.put(item)
        testpack.put("laptop")
        self.assertListEqual(testpack.contents, ["pencil", "pen", "paper", "computer","phone"])

    def test_contents(self):
        testpack = Backpack("Barry", "black")
        for item in ["pencil", "pen", "paper", "computer"]:
            testpack.put(item)
        self.assertListEqual(testpack.contents, ["pencil", "pen", "paper", "computer"])
    def test_dump(self):
        testpack = Backpack("Barry", "black")
        for item in ["pencil", "pen", "paper", "computer"]:
            testpack.put(item)
        testpack.dump()
        self.assertListEqual(testpack.contents, [])
    def test_name(self):
        testpack = Backpack("Barry", "black")
        self.assertAlmostEqual(testpack.name, "Barry")
    def test_color(self):
        testpack = Backpack("Barry", "black")
        self.assertAlmostEqual(testpack.color, "black")

    def test_max_size(self):
        testpack = Backpack("Barry", "black")
        self.assertAlmostEqual(testpack.max_size, 5)

if __name__ == '__main__':
    unittest.main()