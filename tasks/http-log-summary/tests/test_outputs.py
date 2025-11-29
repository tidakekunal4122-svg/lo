import os
from pathlib import Path

EXPECTED_METHODS = [
    "DELETE 1",
    "GET 6",
    "POST 2",
    "PUT 1",
]

EXPECTED_STATUSES = [
    "200 4",
    "404 2",
    "500 2",
    "201 1",
    "301 1",
]


def project_root() -> Path:
    container_root = Path("/app")
    if container_root.exists():
        return container_root
    return Path(__file__).resolve().parents[1]


def test_method_counts_file_exists():
    root = project_root()
    method_file = root / "reports" / "method_counts.txt"
    assert method_file.exists(), f"Missing {method_file}"
    content = method_file.read_text().strip().splitlines()
    assert content == EXPECTED_METHODS, "Method counts do not match expected ordering or values"


def test_status_counts_file_exists():
    root = project_root()
    status_file = root / "reports" / "status_counts.txt"
    assert status_file.exists(), f"Missing {status_file}"
    content = status_file.read_text().strip().splitlines()
    assert content == EXPECTED_STATUSES, "Status counts do not match expected ordering or values"


def test_log_file_unmodified():
    root = project_root()
    log_file = root / "data" / "access.log"
    assert log_file.exists(), "Access log is missing"
    first_line = log_file.read_text().splitlines()[0]
    assert first_line.startswith("192.168.0.10"), "Log content appears modified"
