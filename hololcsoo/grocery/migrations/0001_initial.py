# Generated by Django 4.1.2 on 2022-10-13 21:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("category_name", models.CharField(max_length=100)),
                ("category_id", models.CharField(max_length=20)),
            ],
            options={"verbose_name_plural": "categories",},
        ),
        migrations.CreateModel(
            name="Food",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("price", models.FloatField()),
                ("product_link", models.URLField()),
                ("is_vegan", models.BooleanField()),
                ("is_cooled", models.BooleanField()),
                ("is_local_product", models.BooleanField()),
                ("is_hungarian_product", models.BooleanField()),
                ("is_bio", models.BooleanField()),
                (
                    "categories",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="categories",
                        to="grocery.category",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Grocery",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("grocery_name", models.CharField(max_length=100)),
            ],
            options={"verbose_name_plural": "groceries",},
        ),
        migrations.CreateModel(
            name="Price",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("value", models.FloatField()),
                ("unit", models.CharField(max_length=20)),
                ("unit_price", models.FloatField()),
                ("timestamp", models.TimeField(auto_now=True)),
                (
                    "food",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="foods",
                        to="grocery.food",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="category",
            name="sold_by",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="sold_by",
                to="grocery.grocery",
            ),
        ),
    ]
