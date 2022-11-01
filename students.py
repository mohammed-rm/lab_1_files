from dataclasses import dataclass
from datetime import datetime


@dataclass
class Date:
    day: int
    month: int
    year: int

    def __eq__(self, other):
        return self.day == other.day and self.month == other.month and self.year == other.year

    def __lt__(self, other):
        if self.year < other.year:
            return True
        elif self.year == other.year and self.month < other.month:
            return True
        elif self.year == other.year and self.month == other.month and self.day < other.day:
            return True
        return False


@dataclass
class CSVReader:
    file_name: str

    def read(self):
        with open(self.file_name, 'r') as file:
            lines = file.readlines()
            return lines

    def get_first_name_column(self):
        lines = self.read()
        first_name_column = []
        for line in lines:
            first_name_column.append(line.split(';')[0])
        return first_name_column

    def get_last_name_column(self):
        lines = self.read()
        last_name_column = []
        for line in lines:
            last_name_column.append(line.split(';')[1])
        return last_name_column

    def get_birth_date_column(self):
        lines = self.read()
        birth_dates = []
        for line in lines:
            date = Date(day=int(line.split(';')[2].split('/')[0]),
                        month=int(line.split(';')[2].split('/')[1]),
                        year=int(line.split(';')[2].split('/')[2]))
            birth_dates.append(date)
        return birth_dates


@dataclass
class Student:
    first_name: str
    last_name: str
    date_of_birth: Date

    def __str__(self):
        return f"First Name : {self.first_name}\nLast Name : {self.last_name}\nBirth : {self.date_of_birth}\nEmail : {self.email_adress()}\nAge : {self.get_age()}"

    def email_adress(self):
        return f"{self.first_name.lower()}.{self.last_name.lower()}@univ-tours.fr"

    def get_age(self):
        current_date = datetime.now()
        age = current_date.year - self.date_of_birth.year
        if current_date.month < self.date_of_birth.month:
            age -= 1
        elif current_date.month == self.date_of_birth.month and current_date.day < self.date_of_birth.day:
            age -= 1
        return age


if __name__ == '__main__':
    student_list = []
    csv_reader = CSVReader('students_csv/fichetu.csv')

    students_first_names = csv_reader.get_first_name_column()
    students_last_names = csv_reader.get_last_name_column()
    students_birth_dates = csv_reader.get_birth_date_column()

    for first_name, last_name, birth_date in zip(students_first_names, students_last_names, students_birth_dates):
        student = Student(first_name, last_name, birth_date)
        student_list.append(student)

    for student in student_list:
        print(student)
        print()

