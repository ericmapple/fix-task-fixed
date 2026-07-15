# Access-log summary

Analyze the Apache-style access log at `/app/access.log` and write a JSON report to `/app/report.json`.

## Success criteria

1. `/app/report.json` exists and contains one valid JSON object.
2. The object contains exactly these three fields:
   - `total_requests`: an integer equal to the number of non-empty log entries.
   - `unique_ips`: an integer equal to the number of distinct client IP addresses, using the first whitespace-separated field of each log entry.
   - `top_path`: a string containing the most frequently requested path from the HTTP request line.
3. Count requests for every HTTP method present in the log.
4. Do not modify `/app/access.log`, and do not include prose outside the JSON object.
