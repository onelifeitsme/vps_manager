# Generated by Django 4.1.2 on 2022-10-10 17:06

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VPS',
            fields=[
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, verbose_name='uuid')),
                ('cpu', models.PositiveIntegerField(verbose_name='Количество ядер')),
                ('ram', models.PositiveIntegerField(verbose_name='Объём RAM')),
                ('hdd', models.PositiveIntegerField(verbose_name='Объём HDD')),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'Запущен'), (1, 'Заблокирован'), (2, 'Остановлен')], default=2, verbose_name='Статус сервера')),
            ],
        ),
    ]
