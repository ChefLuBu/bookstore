# Generated by Django 4.2 on 2023-04-25 17:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("salespersons", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="salesperson",
            name="pic",
            field=models.ImageField(default="no_picture.jpg", upload_to="salesperson/"),
        ),
    ]
