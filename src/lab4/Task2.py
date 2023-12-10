class AgeGroup:
    def __init__(self, groups, people):
        self.groups = list(map(int, groups.split()))
        self.people = self.load_people(people.split('\n'))

    def load_people(self, people):
        people_list = {}
        for pers in people:
            if pers == 'END':
                break
            person, age = pers.split(',')[0], pers.split(',')[1]
            age = int(age)
            people_list[age] = people_list.get(age, []) + [person]
        return people_list

    def output_group(self, res):
        output, new_item = '', ''
        result = dict(reversed(res.items()))
        for group, people in result.items():
            people = dict(sorted(people.items(), reverse=True))
            if people:
                for age, person in people.items():
                    person = sorted(person)
                    new_item += f"{f' ({age}), '.join([pers for pers in person])} ({age}), "
            if new_item:
                output += f'{group}: {new_item[:-2]}\n'
                new_item = ''
        return output

    def age_group(self):
        result = {}
        for number, elem in enumerate(self.groups):
            if number == 0:
                result[f'0-{elem}'] = {}
            elif number == \
                    len(self.groups) - 1:
                result[f'{elem + 1}+'] = {}
            else:
                result[f'{elem + 1}-{self.groups[number + 1]}'] = {}
        for age, people in self.people.items():
            for group in result.keys():
                if '+' in group:
                    if age >= int(group.replace('+', '')):
                        result[group][age] = people
                elif int(group[:group.index('-')]) <= age < int(group[group.index('-') + 1:]):
                    result[group][age] = people
        return result


groups = '18 25 35 45 60 80 100'
people = '''Соколов Андрей Сергеевич,15
Егоров Алан Петрович,7
Ярилова Розалия Трофимовна,29
Старостин Ростислав Ермолаевич,50
Дьячков Нисон Иринеевич,88
Иванов Варлам Якунович,88
Кошельков Захар Брониславович,105'''
age_group = AgeGroup(groups, people)
result = age_group.age_group()
output_text = age_group.output_group(result)
print(output_text)
