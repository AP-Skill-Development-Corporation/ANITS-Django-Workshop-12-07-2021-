# Generated by Django 3.0.7 on 2021-07-22 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anitsapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='emailid',
            field=models.EmailField(max_length=30, null=True),
        ),
    ]