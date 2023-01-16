# Generated by Django 4.1.5 on 2023-01-16 17:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("films_app", "0005_alter_similarfilm_film_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="similarfilm",
            name="film",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="film",
                to="films_app.film",
                verbose_name="Фильм",
            ),
        ),
    ]
