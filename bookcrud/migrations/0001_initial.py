# Generated by Django 5.1.5 on 2025-01-31 08:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookTitle', models.CharField(blank=True, max_length=100, null=True, verbose_name='Book Title')),
                ('bookAuthor', models.CharField(blank=True, max_length=100, null=True, verbose_name='Book Author')),
                ('bookYear', models.CharField(blank=True, max_length=100, null=True, verbose_name='Book Year')),
                ('createdDatetime', models.DateTimeField(auto_now_add=True)),
                ('modifiedDatetime', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
            },
        ),
        migrations.CreateModel(
            name='Favourite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Name')),
                ('createdDatetime', models.DateTimeField(auto_now_add=True)),
                ('modifiedDatetime', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Favourite',
                'verbose_name_plural': 'Favourites',
            },
        ),
        migrations.CreateModel(
            name='UserFavouriteList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createdDatetime', models.DateTimeField(auto_now_add=True)),
                ('modifiedDatetime', models.DateTimeField(auto_now=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookcrud.book')),
                ('favourite', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookcrud.favourite')),
            ],
            options={
                'verbose_name': 'User Favourite List',
                'verbose_name_plural': 'User Favourite Lists',
            },
        ),
    ]
