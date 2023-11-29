# Generated by Django 4.2.7 on 2023-11-29 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_term', models.DecimalField(decimal_places=2, max_digits=5)),
                ('second_term', models.DecimalField(decimal_places=2, max_digits=5)),
                ('sum', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
            ],
        ),
    ]
