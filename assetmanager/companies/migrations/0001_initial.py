# Generated by Django 3.2 on 2021-04-11 18:55

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('order_id', models.IntegerField(default=1)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, help_text='Unique ID for this Company.', primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(default='', help_text="Enter the Company's Name", max_length=50)),
                ('url', models.CharField(default='', help_text="Enter the Company's Web Site URL", max_length=200)),
            ],
            options={
                'ordering': ['order_id'],
            },
        ),
    ]
