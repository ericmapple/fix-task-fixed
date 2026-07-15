import json
from pathlib import Path

REPORT_PATH = Path("/app/report.json")
EXPECTED_KEYS = {"total_requests", "unique_ips", "top_path"}


def read_report() -> object:
    return json.loads(REPORT_PATH.read_text(encoding="utf-8"))


def test_success_criterion_1_report_format() -> None:
    """Success criterion 1: the report is valid JSON with the exact required keys and types."""
    assert REPORT_PATH.is_file(), "Missing /app/report.json"

    report = read_report()

    assert isinstance(report, dict), "The report must contain one JSON object"
    assert set(report) == EXPECTED_KEYS, (
        f"Expected exactly {sorted(EXPECTED_KEYS)}, got {sorted(report)}"
    )
    assert type(report["total_requests"]) is int
    assert type(report["unique_ips"]) is int
    assert type(report["top_path"]) is str


def test_success_criterion_2_total_requests() -> None:
    """Success criterion 2: total_requests equals 6."""
    report = read_report()
    assert report["total_requests"] == 6


def test_success_criterion_3_unique_ips() -> None:
    """Success criterion 3: unique_ips equals 3."""
    report = read_report()
    assert report["unique_ips"] == 3


def test_success_criterion_4_top_path() -> None:
    """Success criterion 4: top_path equals /index.html."""
    report = read_report()
    assert report["top_path"] == "/index.html"
