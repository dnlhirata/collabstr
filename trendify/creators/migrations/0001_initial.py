# Generated by Django 5.0.4 on 2024-06-13 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Creator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=255)),
                ('rating', models.FloatField()),
                ('platform', models.CharField(choices=[('IG', 'Instagram'), ('TK', 'TikTok'), ('UG', 'User Generated')], default='UG', max_length=255)),
            ],
        ),
    ]