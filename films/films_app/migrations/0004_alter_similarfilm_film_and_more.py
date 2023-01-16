# Generated by Django 4.1.5 on 2023-01-16 17:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("films_app", "0003_alter_actor_options_alter_genre_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="similarfilm",
            name="film",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="similar_film",
                to="films_app.film",
                verbose_name="Фильм",
            ),
        ),
        migrations.AlterField(
            model_name="similarfilm",
            name="similar_film",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="films_app.film",
                verbose_name="Похожий фильм",
            ),
        ),
    ]
