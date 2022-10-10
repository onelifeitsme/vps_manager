import pytest
from vps.models import VPS


@pytest.fixture
def new_vps(db) -> VPS:
    """Фикстура создания объекта сервера"""
    return VPS.objects.create(cpu=4, ram=2048, hdd=120)