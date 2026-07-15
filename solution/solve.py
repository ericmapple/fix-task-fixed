import json
import re
from collections import Counter
from pathlib import Path

LOG_PATH = Path("/app/access.log")
REPORT_PATH = Path("/app/report.json")
REQUEST_RE = re.compile(r'"[A-Z]+\s+(\S+)\s+HTTP/[^\"]+"')


def main() -> None:
    path_counts: Counter[str] = Counter()
    client_ips: set[str] = set()
    total_requests = 0

    with LOG_PATH.open(encoding="utf-8") as log_file:
        for raw_line in log_file:
            line = raw_line.strip()
            if not line:
                continue

            total_requests += 1
            client_ips.add(line.split()[0])

            request_match = REQUEST_RE.search(line)
            if request_match:
                path_counts[request_match.group(1)] += 1

    if not path_counts:
        raise ValueError("No HTTP request paths were found in the access log")

    highest_count = max(path_counts.values())
    top_path = min(
        path for path, count in path_counts.items() if count == highest_count
    )

    report = {
        "total_requests": total_requests,
        "unique_ips": len(client_ips),
        "top_path": top_path,
    }

    with REPORT_PATH.open("w", encoding="utf-8") as report_file:
        json.dump(report, report_file, indent=2)
        report_file.write("\n")


if __name__ == "__main__":
    main()
