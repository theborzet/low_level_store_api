# Generated by Django 4.2.6 on 2023-10-30 18:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_customuser_token'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={},
        ),
        migrations.AlterUniqueTogether(
            name='customuser',
            unique_together={('username',)},
        ),
    ]