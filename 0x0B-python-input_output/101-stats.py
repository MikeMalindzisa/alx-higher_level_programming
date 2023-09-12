#!/usr/bin/python3
"""
This script reads stdin line by line and computes metrics.
"""

import sys


def print_metrics(metrics):
    """
    Print the computed metrics.

    Args:
        metrics (dict): A dictionary containing the metrics.
    """
    print("File size: {:d}".format(metrics["total_size"]))
    for status_code in sorted(metrics["status_codes"]):
        count = metrics["status_codes"][status_code]
        print("{:s}: {:d}".format(status_code, count))


def main():
    """
    Main function to compute metrics.
    """
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
    except KeyboardInterrupt:
        pass

    print_metrics(metrics)


if __name__ == "__main__":
    main()
