import json

import pytest

from utils import get_formatted_date


def test_json_list(bank_list):
    # преобразование списка JSON в список Python
    data = json.load(bank_list.json)
    # проверка количества элементов списка
    assert len(data) == 5


def test_get_formatted_date(test_data):
    data = get_formatted_date(test_data[1:2])
    assert data[0]['date'] == "2019-08-26T10:50:58.294041"
    assert len(data) == 2


