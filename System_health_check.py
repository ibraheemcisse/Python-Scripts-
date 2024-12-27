#!/usr/bin/env python3
import shutil
import psutil

def check_disk_usage(disk, threshold=20):
    """
    Check the disk usage for a given disk and compare it with the threshold.

    Args:
    - disk (str): The disk path to check.
    - threshold (int, optional): The free space threshold in percentage. Default is 20%.

    Returns:
    - bool: True if free space is greater than the threshold, False otherwise.
    """
    du = shutil.disk_usage(disk)
    free_percentage = (du.free / du.total) * 100
    return free_percentage > threshold

def check_cpu_usage(threshold=75):
    """
    Check the CPU usage and compare it with the threshold.

    Args:
    - threshold (int, optional): The CPU usage threshold in percentage. Default is 75%.

    Returns:
    - bool: True if CPU usage is less than the threshold, False otherwise.
    """
    usage = psutil.cpu_percent(1)
    return usage < threshold

def main():
    """
    Main function to check system health and print the result.
    """
    if not check_disk_usage("/") or not check_cpu_usage():
        print("ERROR!")
    else:
        print("Everything is OK!")

if __name__ == "__main__":
    main()
