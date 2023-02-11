import datetime
from django.test import TestCase
from django.utils import timezone
from polls.models import Question

# Create your tests here.

class QuestionModelTestCase(TestCase):

    def test_was_published_recently_with_future_question(self):
        date_tomorrow = timezone.now() + datetime.timedelta(days=1)
        question = Question.objects.create(date_created=date_tomorrow)
        self.assertEqual(question.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        date_over_a_day_ago = timezone.now() - datetime.timedelta(days=1, seconds=1)
        question = Question.objects.create(date_created=date_over_a_day_ago)
        self.assertEqual(question.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        date_recent = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        question = Question.objects.create(date_created=date_recent)
        self.assertEqual(question.was_published_recently(), True)

