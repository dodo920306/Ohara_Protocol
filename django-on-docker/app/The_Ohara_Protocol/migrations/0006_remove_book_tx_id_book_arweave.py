# Generated by Django 4.2.2 on 2023-06-26 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('The_Ohara_Protocol', '0005_book_tx_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='tx_id',
        ),
        migrations.AddField(
            model_name='book',
            name='Arweave',
            field=models.CharField(default='000000', max_length=65),
            preserve_default=False,
        ),
    ]