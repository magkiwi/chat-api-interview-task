from django.db import migrations
import json

def insert_data(apps, schema_editor):
    QuestionAnswer = apps.get_model('chat', 'QuestionAnswer')
    with open('fixture.json') as fixture:
        file_contents = fixture.read()
    data_fixture = json.loads(file_contents)
    for data in data_fixture:
        qa = QuestionAnswer(answers=data["answers"], qText=data["qText"])
        qa.save()

class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_conversation'),
    ]

    operations = [
        migrations.RunPython(insert_data),
    ]