from django.test import TestCase

from .models import Film, Actor, Category, Language


class FilmTestCase(TestCase):

    def setUp(self):
        language = Language(name='English')
        language.save()

        actor_a = Actor(first_name='Actor', last_name='A')
        actor_a.save()
        actress_b = Actor(first_name='Actress', last_name='B')
        actress_b.save()

        category_a = Category(name='Test Category')
        category_a.save()

        film_a = Film(
            title='Test Film',
            description='Test Description',
            release_year=2022,
            rental_duration=3,
            rental_rate=5.99,
            length=118,
            replacement_cost=15.99,
            rating='PG-13',
            special_features=['Behind the Scenes','Director\'s Cut']
        )

        film_a.language = language
        film_a.save()

        Film.objects.first().actors.add(*[actor_a, actress_b])
        Film.objects.first().categories.add(*[category_a])

    
    def test_film_exists(self):
        film_count = Film.objects.all().count()
        self.assertEqual(film_count, 1)
    
    def test_film_relations_created(self):
        film = Film.objects.first()
        actors = film.actors.all()
        categories = film.categories.all()

        self.assertEqual(film.language.name, 'English')
        self.assertEqual(actors[0].first_name, 'Actor')
        self.assertEqual(actors[1].first_name, 'Actress')
        self.assertEqual(categories[0].name, 'Test Category')