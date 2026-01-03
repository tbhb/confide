import importlib
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pytest_codspeed.plugin import BenchmarkFixture
    from pytest_mock import MockerFixture


class TestBenchImportTime:
    def test_import_time_confide(
        self, benchmark: "BenchmarkFixture", mocker: "MockerFixture"
    ) -> None:
        def import_confide():
            _ = mocker.patch("sys.modules", {})
            _ = importlib.import_module("confide", "test_bench_imports")

        benchmark(import_confide)
