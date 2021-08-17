# Generated by Django 3.2.6 on 2021-08-16 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_authors_app', '0008_auto_20210815_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='books',
            field=models.ManyToManyField(related_name='Authors', to='books_authors_app.Book'),
        ),
    ]
