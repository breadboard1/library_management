# Generated by Django 5.1.2 on 2024-10-21 22:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_alter_book_image'),
        ('borrowings', '0003_remove_borrowing_no'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrowing',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='borrowed_book', to='book.book'),
        ),
    ]