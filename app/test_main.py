import datetime
from unittest.mock import patch, Mock
import pytest

from app.main import outdated_products


@pytest.fixture()
def product_list() -> list[dict]:
    product_list = [
        {
            "name": "salmon",
            "expiration_date": datetime.date(2022, 2, 10),
            "price": 600
        },
        {
            "name": "chicken",
            "expiration_date": datetime.date(2022, 2, 5),
            "price": 120
        },
        {
            "name": "duck",
            "expiration_date": datetime.date(2022, 2, 1),
            "price": 160
        }
    ]
    yield product_list


@pytest.mark.parametrize(
    "today_date, expected", [
        (
            datetime.date(2022, 2, 11),
            ["salmon", "chicken", "duck"]
        ),
        (
            datetime.date(2022, 2, 10),
            ["chicken", "duck"]
        ),
        (
            datetime.date(2022, 2, 5),
            ["duck"]
        ),
        (
            datetime.date(2022, 2, 1),
            []
        ),
    ]
)
@patch("app.main.datetime.date")
def test_outdated_products(
        mock_datetime_today: Mock,
        today_date: datetime.date,
        expected: list[str],
        product_list: list[dict]
) -> None:
    mock_datetime_today.today.return_value = today_date
    assert outdated_products(product_list) == expected
