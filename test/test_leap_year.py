import pytest

from src.year import *
from src.main import *

@pytest.fixture()
def year():
   return Year()

def test_divisible_by_4_but_not_100_pass(year):
    assert True == check_divisible_by_4_but_not_100(year.year2024)

def test_divisible_by_400(year):
    assert True == check_divisible_by_400(year.year2000)


def test_not_divisible_by_4(year):
   assert False == check_not_divisible_by_4(year.year2024)


def test_divisible_by_100_but_not_400(year):
    assert True == isLeapYear(year.year2000)



