from typing import Union

class Group:
    def __init__(self, name) -> None:
        self.name = name
        self.group: dict[int, list[str]] = {}

    def add_person(self, name: str, age: int) -> None:
        if age in self.group:
            self.group[age].append(name)
        else:
            self.group[age] = [name]

    def __repr__(self) -> str:
        ages = self.group.keys()
        if ages:
            return f'{self.name}: ' + ', '.join([f' ({key}), '.join(sorted(self.group[key])) + f' ({key})'
                                                 for key in sorted(ages, reverse=True)])
        return ''

class Groups:
    def __init__(self, ages: list[int]) -> None:
        self.ages = ages
        self.groups = [Group(f'0-{ages[0]}')]
        for age in range(1, len(ages)):
            self.groups.append(Group(f'{ages[age - 1] + 1}-{ages[age]}'))
        self.groups.append(Group(f'{ages[-1] + 1}+'))

    def add_person(self, name: str, age: int) -> None:
        if age > self.ages[-1]:
            self.groups[-1].add_person(name, age)
        elif age <= self.ages[0]:
            self.groups[0].add_person(name, age)
        else:
            for i in range(1, len(self.ages)):
                if self.ages[i - 1] < age <= self.ages[i]:
                    self.groups[i].add_person(name, age)
                    break

    def __repr__(self) -> str:
        groups = []
        for group in self.groups[::-1]:
            people = group.__repr__()
            if people:
                groups.append(people)
        return '\n'.join(groups)

def main(ages: list[int], persons: list[list[Union[int, str]]]) -> str:
    groups = Groups(ages)
    for person in persons:
        groups.add_person(person[0], int(person[1]))
    return groups.__repr__()

if __name__ == '__main__':
    ages = [int(age) for age in input().split()]
    persons = []
    person = input()
    while person != 'END':
        person = person.split(',')
        persons.append([person[0], int(person[1])])
        person = input()
    print(main(ages, persons))


'''
18 25 35 45 60 80 100
Кошельков Захар Брониславович,105
Старостин Ростислав Ермолаевич,50
Дьячков Нисон Иринеевич,88
Иванов Варлам Якунович,88
Соколов Андрей Сергеевич,15
Егоров Алан Петрович,7
Ярилова Розалия Трофимовна,29
END
'''