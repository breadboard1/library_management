# Generated by Django 5.1.2 on 2024-10-21 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('borrowings', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrowing',
            name='no',
            field=models.IntegerField(null=True),
        ),
    ]
