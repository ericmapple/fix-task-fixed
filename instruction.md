# Access-log summary

Analyze the Apache-style access log located at `/app/access.log`.

Treat each non-empty line as one request. The client IP address is the first whitespace-separated field of each line. The requested path is the path appearing after the HTTP method in the quoted HTTP request line.

Write the result to `/app/report.json`.

## Success criteria

1. `/app/report.json` exists and contains one valid JSON object with exactly these three fields and types: `total_requests` as an integer, `unique_ips` as an integer, and `top_path` as a string.
2. `total_requests` is the number of non-empty requests in the supplied log and equals `6`.
3. `unique_ips` is the number of distinct client IP addresses in the supplied log and equals `3`.
4. `top_path` is the most frequently requested path across all HTTP methods and equals `"/index.html"`.
