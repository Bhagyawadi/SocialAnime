# Generated by Django 5.0.6 on 2025-06-26 09:23

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['timestamp']},
        ),
        migrations.AlterField(
            model_name='conversation',
            name='participants',
            field=models.ManyToManyField(related_name='conversations', to=settings.AUTH_USER_MODEL),
        ),
    ]
