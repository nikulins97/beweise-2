# Generated by Django 4.1.6 on 2023-06-07 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_questions_question_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questions',
            name='answer',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='questions',
            name='question',
            field=models.TextField(),
        ),
    ]
