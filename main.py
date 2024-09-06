import datetime
import argparse


def read_text_file(file_path):
    """Reads the contents of a text file."""
    with open(file_path, 'r') as file:
        return file.read()


def split_data(text_data):
    """Splits the text data into a list of lists."""
    return [line.split('_') for line in text_data.split('\n') if line]


def sort_data(data):
    """Sorts the data by the first element of each sublist."""
    return sorted(data, key=lambda x: x[0])


def calculate_time_differences(start_log, end_log):
    """Calculates the time differences between start and end logs."""
    time_differences = []
    for start, end in zip(start_log, end_log):
        timestamp_start = datetime.datetime.strptime(start[1], '%H:%M:%S.%f')
        timestamp_end = datetime.datetime.strptime(end[1], '%H:%M:%S.%f')
        difference = timestamp_end - timestamp_start
        time_differences.append(difference)
    return time_differences


def format_timedelta(td):
    """Formats a timedelta object to MM:SS.mmm format."""
    total_seconds = td.total_seconds()
    minutes = int(total_seconds // 60)
    seconds = int(total_seconds % 60)
    milliseconds = int((total_seconds % 1) * 1000)
    return f"{minutes:02}:{seconds:02}.{milliseconds:03}"


def build_report(sorted_abbreviations, time_differences):
    """Combines the sorted abbreviations with the calculated time differences."""
    report = []
    for abbrev, time_diff in zip(sorted_abbreviations, time_differences):
        abbrev.append(time_diff)
        report.append(abbrev)
    return sorted(report, key=lambda x: x[3])  # Sort by time difference


def print_report(report):
    """Prints the formatted race report."""
    for i, entry in enumerate(report):
        if i == 15:
            print("---------------------------------------------------------")
        formatted_time = format_timedelta(entry[3])
        print(f"{i + 1}. {entry[1]} | {entry[2]} | {formatted_time}")


def process_logs():
    # Process start log
    start_log = sort_data(split_data(read_text_file("log/start.log.txt")))

    # Process end log
    end_log = sort_data(split_data(read_text_file("log/end.log.txt")))

    # Process abbreviations
    abbreviations = sort_data(split_data(read_text_file("log/abbreviations.txt")))

    # Calculate time differences
    time_differences = calculate_time_differences(start_log, end_log)

    # Build and print the report
    report = build_report(abbreviations, time_differences)
    print_report(report)


def main():
    parser = argparse.ArgumentParser(description='Generate a race report')
    parser.add_argument('--files', help='Path to the folder containing log files')
    parser.add_argument('--driver', help='Filter report by driver name')
    parser.add_argument('--asc', action='store_true', help='Sort report in ascending order')
    parser.add_argument('--desc', action='store_true', help='Sort report in descending order')
    args = parser.parse_args()

    if args.files:
        # Process start log
        start_log = sort_data(split_data(read_text_file(f"{args.files}/start.log.txt")))

        # Process end log
        end_log = sort_data(split_data(read_text_file(f"{args.files}/end.log.txt")))

        # Process abbreviations
        abbreviations = sort_data(split_data(read_text_file(f"{args.files}/abbreviations.txt")))

        # Calculate time differences
        time_differences = calculate_time_differences(start_log, end_log)

        # Build and print the report
        report = build_report(abbreviations, time_differences)

        if args.driver:
            report = [entry for entry in report if entry[1] == args.driver]

        if args.asc:
            report = sorted(report, key=lambda x: x[3])
        elif args.desc:
            report = sorted(report, key=lambda x: x[3], reverse=True)

        print_report(report)
    else:
        print("Error: --files argument is required")


if __name__ == "__main__":
    main()

