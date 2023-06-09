# Generated by Django 4.2.1 on 2023-05-21 15:55

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('weight', models.CharField(max_length=200)),
                ('shape', models.CharField(choices=[('round', 'round'), ('square', 'square'), ('heart', 'heart')], default='round', max_length=200)),
                ('layer', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3')], default='1', max_length=200)),
                ('price', models.FloatField()),
                ('image', models.ImageField(blank=True, upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='Occasion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('comment', models.TextField(max_length=200)),
                ('rating', models.FloatField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('cake', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.cake')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('address', models.CharField(max_length=300)),
                ('matter', models.CharField(max_length=200)),
                ('cake', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.cake')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('cake', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.cake')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='cake',
            name='occasion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.occasion'),
        ),
    ]
