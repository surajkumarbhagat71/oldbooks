# Generated by Django 2.2.6 on 2020-01-10 03:41

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('cat_id', models.AutoField(primary_key=True, serialize=False)),
                ('cat_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('topic_id', models.AutoField(primary_key=True, serialize=False)),
                ('topic_name', models.CharField(max_length=200)),
                ('topic_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datawork.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('book_id', models.AutoField(primary_key=True, serialize=False)),
                ('book_title', models.CharField(max_length=200)),
                ('book_isbn', models.IntegerField()),
                ('book_no_of_page', models.IntegerField()),
                ('book_author', models.CharField(max_length=200)),
                ('book_desc', models.TextField()),
                ('book_quality', models.CharField(choices=[('New Like', 'New Like'), ('Good Condition', 'Good Condition'), ('Too old', 'Too old')], max_length=200)),
                ('book_price', models.IntegerField()),
                ('book_doc', models.DateTimeField(default=django.utils.timezone.now)),
                ('book_status', models.IntegerField(default=0)),
                ('book_cover', models.ImageField(blank=True, default='default.jpg', upload_to='books/')),
                ('book_topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='datawork.Topic')),
            ],
        ),
    ]
