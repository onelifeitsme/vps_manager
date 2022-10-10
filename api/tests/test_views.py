from rest_framework.reverse import reverse
from rest_framework.test import APIClient
from vps.models import VPS


def test_create_new_vps(db, client):
    """Тест создания нового сервера"""
    data = {
        "cpu": 2,
        "ram": 2048,
        "hdd": 120,
    }
    client = APIClient()
    response = client.post(path=reverse('vps_list'), data=data)
    assert response.status_code == 201


def test_get_vps_by_uuid(db, client, new_vps):
    """Тест получения сервера по uuid"""
    client = APIClient()
    path = reverse('vps_detail', kwargs={'pk':new_vps.uuid})
    response = client.get(path=path)
    assert response.status_code == 200


def test_get_vps_list_by_params(db, client, new_vps):
    """Тест получения списка серверов по параметрам"""
    client = APIClient()
    params = f'?cpu={new_vps.cpu}&ram={new_vps.ram}'
    path = reverse('vps_list') + params
    response = client.get(path=path)
    assert response.data[0]['uuid'] == str(new_vps.uuid)


def test_change_vps_status(db, client, new_vps):
    """Тест перевода сервера с другой статус"""
    client = APIClient()
    path = reverse('vps_detail', kwargs={'pk': new_vps.uuid})
    data = {
        "status": 1,
    }
    response = client.patch(path=path, data=data)
    assert response.status_code == 200

