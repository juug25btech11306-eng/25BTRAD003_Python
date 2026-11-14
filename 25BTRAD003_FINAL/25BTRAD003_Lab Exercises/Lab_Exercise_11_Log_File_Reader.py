def read_log_file(filename):
    counts = {"ERROR": 0, "WARNING": 0, "INFO": 0}
    try:
        with open(filename, encoding="utf-8") as file:
            for line in file:
                for key in counts:
                    if key in line.upper(): counts[key] += 1
        print("Log File Summary")
        for key, count in counts.items(): print(f"{key}: {count}")
    except FileNotFoundError: print("Error: Log file not found.")
    except PermissionError: print("Error: Permission denied.")
    except OSError as error: print("Error reading file:", error)
if __name__ == "__main__": read_log_file(input("Enter log filename: "))
