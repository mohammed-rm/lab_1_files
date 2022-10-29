import unittest

from students import Date, Student


class TestDate(unittest.TestCase):
    def setUp(self) -> None:
        self.date_1 = Date(day=1, month=1, year=2000)
        self.date_2 = Date(day=1, month=1, year=2000)
        self.date_3 = Date(day=15, month=10, year=2001)
        self.date_4 = Date(day=15, month=2, year=2000)
        self.date_5 = Date(day=20, month=1, year=2000)

    def test_eq(self):
        self.assertTrue(self.date_1 == self.date_2)

    def test_lt(self):
        self.assertFalse(self.date_1 < self.date_2)
        self.assertTrue(self.date_1 < self.date_3)
        self.assertTrue(self.date_1 < self.date_4)
        self.assertTrue(self.date_1 < self.date_5)


class TestStudent(unittest.TestCase):
    def setUp(self) -> None:
        self.student_1 = Student(first_name='John', last_name='Doe', date_of_birth=Date(day=22, month=10, year=1975))

    def test_str(self):
        self.assertEqual(str(self.student_1),
                         "First Name : John | Last Name : Doe | Birth : Date(day=22, month=10, year=1975) | Email : john.doe@univ-tours.fr | Age : 47")

    def test_email_adress(self):
        self.assertEqual(self.student_1.email_adress(), "john.doe@univ-tours.fr")

    def test_get_age(self):
        self.assertEqual(self.student_1.get_age(), 47)


if __name__ == '__main__':
    unittest.main(verbosity=2)
