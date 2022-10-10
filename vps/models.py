from django.db import models
from uuid import uuid4


class VPS(models.Model):

    STATUSES = (
        (STARTED := 0, 'Запущен'),
        (BLOCKED := 1, 'Заблокирован'),
        (STOPED := 2, 'Остановлен'),
    )

    uuid = models.UUIDField(verbose_name='uuid', default=uuid4, primary_key=True, editable=False)
    cpu = models.PositiveIntegerField(verbose_name='Количество ядер')
    ram = models.PositiveIntegerField(verbose_name='Объём RAM')
    hdd = models.PositiveIntegerField(verbose_name='Объём HDD')
    status = models.PositiveSmallIntegerField(verbose_name='Статус сервера', choices=STATUSES, default=STOPED)

    def __str__(self):
        return f'{self.uuid} - {self.status}'
