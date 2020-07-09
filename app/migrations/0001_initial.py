# Generated by Django 2.1.2 on 2020-07-08 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User_grade',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
                ('grade', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
    ]