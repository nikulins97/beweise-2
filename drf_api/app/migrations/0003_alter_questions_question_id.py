# Generated by Django 4.1.6 on 2023-06-06 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_questions_answer_questions_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='question_id',
            field=models.IntegerField(unique=True),
        ),
    ]
