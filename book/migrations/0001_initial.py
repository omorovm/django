# Generated by Django 5.0 on 2023-12-12 14:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('author', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('release_at', models.DateTimeField(auto_created=True, null=True)),
                ('title', models.CharField(max_length=40)),
                ('genre', models.CharField(max_length=10)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to='author.author')),
            ],
        ),
    ]
