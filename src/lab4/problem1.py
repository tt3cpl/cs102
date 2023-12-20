from typing import Union

PATH_TO_INPUT1 = 'input_1.txt'
PATH_TO_INPUT2 = 'input_2.txt'

class FilmsDB(dict):
    def __init__(self, films_dict: dict[int, str]) -> None:
        super().__init__()
        self.films = films_dict

    def get_film(self, id: int) -> str:
        try:
            return self.films[id]
        except KeyError:
            return 'ERROR: film does not found!'

class User(list):
    def __init__(self, user_films: list[int]) -> None:
        super().__init__()
        self.films = user_films

def count_score(person: User, user: User) -> Union[int, list[Union[float, list[int]]]]:
    person_films = set(person.films)
    user_films = set(user.films)
    if 2 * len(person_films & user_films) >= len(user_films):
        return [len(person_films & user_films) / len(person_films), list(user_films - person_films)]
    return 0

def algorithm(films: FilmsDB, users: list[User], person: User) -> str:
    normal_films = {}
    for user in users:
        score_user = count_score(person, user)
        if type(score_user) == list:
            for film in score_user[1]:
                if film in normal_films:
                    normal_films[film] += score_user[0] * user.films.count(film)
                else:
                    normal_films[film] = score_user[0] * user.films.count(film)
    normal_films_list = [[film, normal_films[film]] for film in normal_films]
    return films.get_film(sorted(normal_films_list, key=lambda x: x[1], reverse=True)[0][0])

if __name__ == '__main__':
    with open(PATH_TO_INPUT1, 'r', encoding='utf-8') as file1_input:
        films = {}
        for line in file1_input.readlines():
            film = line.strip().split(',')
            films[int(film[0])] = film[1]
        films_db = FilmsDB(films)
    with open(PATH_TO_INPUT2, 'r', encoding='utf-8') as file2_input:
        users = []
        for line in file2_input.readlines():
            users.append(User(([int(film) for film in line.strip().split(',')])))
    person = User([int(film_id) for film_id in input().split(',')])
    print(algorithm(films_db, users, person))
