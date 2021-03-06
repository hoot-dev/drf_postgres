# Generated by Django 3.2.13 on 2022-05-15 02:58

import django.contrib.postgres.fields
import django.contrib.postgres.indexes
import django.contrib.postgres.search
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('actor_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(max_length=45)),
                ('last_update', models.DateTimeField()),
            ],
            options={
                'db_table': 'actor',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=25)),
                ('last_update', models.DateTimeField()),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('film_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('release_year', models.IntegerField(blank=True, null=True)),
                ('rental_duration', models.SmallIntegerField()),
                ('rental_rate', models.DecimalField(decimal_places=2, max_digits=4)),
                ('length', models.SmallIntegerField(blank=True, null=True)),
                ('replacement_cost', models.DecimalField(decimal_places=2, max_digits=5)),
                ('rating', models.CharField(blank=True, choices=[('G', 'G'), ('PG', 'PG'), ('PG-13', 'PG-13'), ('R', 'R'), ('NC-17', 'NC-17')], max_length=6, null=True)),
                ('last_update', models.DateTimeField()),
                ('special_features', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=100, null=True), size=None)),
                ('fulltext', django.contrib.postgres.search.SearchVectorField(null=True)),
            ],
            options={
                'db_table': 'film',
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('language_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
                ('last_update', models.DateTimeField()),
            ],
            options={
                'db_table': 'language',
            },
        ),
        migrations.CreateModel(
            name='FilmCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_update', models.DateTimeField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='films.category')),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='films.film')),
            ],
            options={
                'db_table': 'film_category',
                'unique_together': {('film', 'category')},
            },
        ),
        migrations.CreateModel(
            name='FilmActor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_update', models.DateTimeField()),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='films.actor')),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='films.film')),
            ],
            options={
                'db_table': 'film_actor',
                'unique_together': {('actor', 'film')},
            },
        ),
        migrations.AddField(
            model_name='film',
            name='actors',
            field=models.ManyToManyField(related_name='films', through='films.FilmActor', to='films.Actor'),
        ),
        migrations.AddField(
            model_name='film',
            name='categories',
            field=models.ManyToManyField(related_name='films', through='films.FilmCategory', to='films.Category'),
        ),
        migrations.AddField(
            model_name='film',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='films.language'),
        ),
        migrations.AddIndex(
            model_name='film',
            index=django.contrib.postgres.indexes.GinIndex(fields=['fulltext'], name='film_fulltex_f41f0a_gin'),
        ),
    ]
