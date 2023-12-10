import unittest
from src.lab4.Task1 import FilmRecommendationSystem


class TaskTestCase(unittest.TestCase):
    def setUp(self):
        self.films_file_path = 'films.txt'
        self.users_file_path = 'users.txt'
        self.film_recommendation_system = FilmRecommendationSystem(self.films_file_path, self.users_file_path)

    def test_get_recommendation_1(self):
        user_input = '2,4'
        expected_recommendation = 'Дюна'
        recommendation = self.film_recommendation_system.get_recommendation(user_input)
        self.assertEqual(recommendation, expected_recommendation)

    def test_get_recommendation_2(self):
        user_input = '2'
        expected_recommendation = 'Дюна'
        recommendation = self.film_recommendation_system.get_recommendation(user_input)
        self.assertEqual(recommendation, expected_recommendation)

    def test_get_recommendation_3(self):
        user_input = '1,3'
        expected_recommendation = 'Хатико'
        recommendation = self.film_recommendation_system.get_recommendation(user_input)
        self.assertEqual(recommendation, expected_recommendation)

    def test_get_recommendation_4(self):
        user_input = '1,2,3,4'
        expected_recommendation = 'Recommended films were not found'
        recommendation = self.film_recommendation_system.get_recommendation(user_input)
        self.assertEqual(recommendation, expected_recommendation)

    def test_get_recommendation_5(self):
        user_input = ''
        expected_recommendation = 'Recommended films were not found'
        recommendation = self.film_recommendation_system.get_recommendation(user_input)
        self.assertEqual(recommendation, expected_recommendation)


if __name__ == '__main__':
    unittest.main()
