import json
from pathlib import Path

REPORT_PATH = Path("/app/report.json")
EXPECTED_KEYS = {"total_requests", "unique_ips", "top_path"}


def load_report() -> dict[str, object]:
    assert REPORT_PATH.is_file(), "Missing /app/report.json"

    try:
        report = json.loads(REPORT_PATH.read_text(encoding="utf-8"))
    except json.JSONDecodeError as error:
        raise AssertionError(f"/app/report.json is not valid JSON: {error}") from error

    assert isinstance(report, dict), "The report must be a JSON object"
    return report


def test_report_schema() -> None:
    report = load_report()

    assert set(report) == EXPECTED_KEYS, (
        f"Expected exactly {sorted(EXPECTED_KEYS)}, got {sorted(report)}"
    )
    assert type(report["total_requests"]) is int
    assert type(report["unique_ips"]) is int
    assert type(report["top_path"]) is str


def test_total_requests() -> None:
    report = load_report()
    assert report["total_requests"] == 6


def test_unique_ips() -> None:
    report = load_report()
    assert report["unique_ips"] == 3


def test_top_path() -> None:
    report = load_report()
    assert report["top_path"] == "/index.html"
