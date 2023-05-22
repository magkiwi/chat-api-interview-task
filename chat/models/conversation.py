from django.db import models
from django.contrib.postgres.fields import ArrayField


class Conversation(models.Model):
    user_question = models.TextField(max_length=512)
    bot_answer = models.TextField(max_length=512)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
