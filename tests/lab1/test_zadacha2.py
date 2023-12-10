import unittest
from src.lab4.Task2 import AgeGroup


class TestAgeGroup(unittest.TestCase):

    def test_age_group_1(self):
        groups = '18 25 35 45 60 80 100'
        people = '''Соколов Андрей Сергеевич,15\nЕгоров Алан Петрович,7\nЯрилова Розалия Трофимовна,29\nСтаростин Ростислав Ермолаевич,50\nДьячков Нисон Иринеевич,88\nИванов Варлам Якунович,88\nКошельков Захар Брониславович,105'''
        age_group = AgeGroup(groups, people)
        result = age_group.age_group()
        expected_output = "101+: Кошельков Захар Брониславович (105)\n81-100: Дьячков Нисон Иринеевич (88), Иванов Варлам Якунович (88)\n46-60: Старостин Ростислав Ермолаевич (50)\n26-35: Ярилова Розалия Трофимовна (29)\n0-18: Соколов Андрей Сергеевич (15), Егоров Алан Петрович (7)\n"
        self.assertEqual(age_group.output_group(result), expected_output)

    def test_age_group_2(self):

        groups = '18 25 35'
        people = '''Соколов Андрей Сергеевич,15\nЕгоров Алан Петрович,7\nЯрилова Розалия Трофимовна,29\nСтаростин Ростислав Ермолаевич,50\nДьячков Нисон Иринеевич,88\nИванов Варлам Якунович,88\nКошельков Захар Брониславович,105'''
        age_group = AgeGroup(groups, people)
        result = age_group.age_group()
        expected_output = "36+: Кошельков Захар Брониславович (105), Дьячков Нисон Иринеевич (88), Иванов Варлам Якунович (88), Старостин Ростислав Ермолаевич (50)\n26-35: Ярилова Розалия Трофимовна (29)\n0-18: Соколов Андрей Сергеевич (15), Егоров Алан Петрович (7)\n"
        self.assertEqual(age_group.output_group(result), expected_output)


if __name__ == '__main__':
    unittest.main()
