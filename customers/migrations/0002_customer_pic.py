# Generated by Django 4.2 on 2023-04-24 19:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("customers", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customer",
            name="pic",
            field=models.ImageField(default="no_picture.jpg", upload_to="customers/"),
        ),
    ]
