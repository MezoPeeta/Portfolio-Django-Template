# Generated by Django 3.0.2 on 2020-01-25 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20190722_1445'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('sys_id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(blank=True, max_length=200, unique=True)),
                ('status', models.CharField(blank=True, max_length=64)),
                ('created_date', models.DateTimeField(blank=True)),
                ('updated_date', models.DateTimeField(blank=True)),
            ],
            options={
                'db_table': 'blog_subscribe',
            },
        ),
    ]