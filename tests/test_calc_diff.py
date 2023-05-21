from datetime import datetime

import pytest

from src.calc_diff import calc_diff

from freezegun import freeze_time


class TestCalcDiff:

    @pytest.fixture()
    def case_1(self):
        return {
            'start_time': '2021-11-03T09:22:28+00:00',
            'end_time': None
        }

    @pytest.fixture()
    def case_2(self):
        return {
            'start_time': '2021-11-03T09:22:28+00:00',
            'end_time': '2022-11-03T09:22:28+00:00'
        }

    @freeze_time("2022-01-14")
    def test_calc_diff_returns_correct_diff_with_none_as_end_time(self, case_1):
        assert calc_diff(case_1) == 6187052.0

    def test_calc_diff_returns_correct_diff_with_set_time_as_end_time(self, case_2):
        assert calc_diff(case_2) == 31536000.0
