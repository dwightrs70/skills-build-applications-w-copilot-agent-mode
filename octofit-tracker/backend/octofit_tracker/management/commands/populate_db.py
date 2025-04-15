from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.conf import settings
from pymongo import MongoClient
from octofit_tracker import test_data

class Command(BaseCommand):
    help = 'Populate the database with test data for users, teams, activity, leaderboard, and workouts'

    def handle(self, *args, **kwargs):
        # Connect to MongoDB
        client = MongoClient(settings.DATABASES['default']['HOST'], settings.DATABASES['default']['PORT'])
        db = client[settings.DATABASES['default']['NAME']]

        # Drop existing collections
        db.users.drop()
        db.teams.drop()
        db.activity.drop()
        db.leaderboard.drop()
        db.workouts.drop()

        # Load test data
        test_data_content = test_data.get_test_data()

        # Populate collections
        db.users.insert_many(test_data_content['users'])
        db.teams.insert_many(test_data_content['teams'])
        db.activity.insert_many(test_data_content['activities'])
        db.leaderboard.insert_many(test_data_content['leaderboard'])
        db.workouts.insert_many(test_data_content['workouts'])

        self.stdout.write(self.style.SUCCESS('Database populated with test data successfully.'))
