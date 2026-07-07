import json
from pathlib import Path

REPORT = Path("/app/report.json")


def load_report():
    assert REPORT.exists(), "report.json was not created"
    return json.loads(REPORT.read_text())


def test_report_exists():
    """Success Criterion 1: report.json exists."""
    assert REPORT.exists()


def test_total_requests():
    """Success Criterion 2: report.json contains the correct total_requests."""
    report = load_report()
    assert report["total_requests"] == 6


def test_unique_ips():
    """Success Criterion 3: report.json contains the correct unique_ips."""
    report = load_report()
    assert report["unique_ips"] == 3


def test_top_path():
    """Success Criterion 4: report.json contains the correct top_path."""
    report = load_report()
    assert report["top_path"] == "/index.html"
