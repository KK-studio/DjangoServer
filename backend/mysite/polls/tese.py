from models import Choice, Question  # Import the model classes we just wrote.



# Create a new Question.
# Support for time zones is enabled in the default settings file, so
# Django expects a datetime with tzinfo for pub_date. Use timezone.now()
# instead of datetime.datetime.now() and it will do the right thing.
from django.utils import timezone
q = Question(question_text="What's new?", pub_date=timezone.now())
q.save()
