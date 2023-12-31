# Generated by Django 4.2.2 on 2023-07-24 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("email_sender", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="address",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="customuser",
            name="country",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="customuser",
            name="date_of_birth",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="email",
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
