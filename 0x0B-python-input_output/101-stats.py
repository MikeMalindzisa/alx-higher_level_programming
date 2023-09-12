#!/usr/bin/python3
"""
This script computes metrics when piped with another script.
"""

import sys

metrics = {
    "total_size": 0,
    "status_codes": {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0
    }
}

line_count = 0


def print_metrics(metrics):
    """
    Print the computed metrics.

    Args:
        metrics (dict): A dictionary containing the metrics.
    """
    print("File size: {:d}".format(metrics["total_size"]))
    for status_code in sorted(metrics["status_codes"]):
        count = metrics["status_codes"][status_code]
        if count > 0:  # Only print status codes that have appeared
            print("{:s}: {:d}".format(status_code, count))


try:
    for line in sys.stdin:
        line_count += 1
        split_line = line.split()
        if len(split_line) >= 7:
            status_code = split_line[-2]
            file_size = split_line[-1]
            metrics["total_size"] += int(file_size)
            if status_code in metrics["status_codes"]:
                metrics["status_codes"][status_code] += 1
        if line_count % 10 == 0:
            print_metrics(metrics)
except Exception:
    pass
finally:
    print_metrics(metrics)

