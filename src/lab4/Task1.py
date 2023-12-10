'''Recomendation system'''
import collections


class FilmRecommendationSystem:
    def __init__(self, films_file, users_file):
        self.films = self._load_films(films_file)
        self.users = self._load_users(users_file)

    def _load_films(self, file_path):
        '''Make films in a dict'''
        films = {}
        with open(file_path) as f:
            file = f.read().split('\n')[:-1]
            for string in file:
                number, film = string.split(',')[0], string.split(',')[1]
                films[number] = film
        return films

    def _load_users(self, file_path):
        '''Enter users'''
        with open(file_path) as f:
            return [user.split(',') for user in f.read().split('\n')[:-1]]


    def get_recommendation(self, user_history):
        '''Get recommendations'''
        recs = []
        try:
            if user_history:
                for user in self.users:
                    similars = list(set(user).intersection(user_history))
                    if len(similars) >= len(user_history) // 2:
                        recs += user
                for numb in user_history:
                    recs = list(filter((numb).__ne__, recs))
                if recs:
                    rec_film = self.films.get(collections.Counter(recs).most_common(1)[0][0])
                    return rec_film
        except Exception as e:
            pass
        return 'Recommended films were not found'


films_file_path = 'films.txt'
users_file_path = 'users.txt'
film_recommendation_system = FilmRecommendationSystem(films_file_path, users_file_path)
user_input = '1'
recommendation = film_recommendation_system.get_recommendation(user_input)
print(recommendation)
