# Generated by Django 5.1.2 on 2024-10-21 18:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        ('book', '0003_alter_book_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Borrowing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='borrower', to='accounts.userbankaccount')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='borrow_book', to='book.book')),
            ],
            options={
                'ordering': ['timestamp'],
            },
        ),
    ]
