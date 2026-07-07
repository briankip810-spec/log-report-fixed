# Log Report Task

You are given an Apache‑style access log at `/app/access.log`.

Your task is to analyze the file and produce a JSON summary report.

The report **must** be saved to `/app/report.json` and **must** contain exactly three keys:

- `"total_requests"` – integer, the total number of request lines in the log.
- `"unique_ips"` – integer, the number of distinct client IP addresses.
- `"top_path"` – string, the request path (e.g., `/index.html`) that appears most frequently in the log.

## Success criteria

1. The file `/app/report.json` exists.
2. The value of `total_requests` is the correct integer count.
3. The value of `unique_ips` is the correct integer count.
4. The value of `top_path` is the most frequently requested path in the log.
