

# Race Report Generator
=======================

## Overview

This script generates a race report from log files containing start and end times, as well as driver abbreviations. The report includes the driver's name, abbreviation, and time difference.

## Usage

To use this script, simply run it from the command line and provide the path to the folder containing the log files using the `--files` argument.

```bash
python script_name.py --files /path/to/log/files
```

You can also filter the report by driver name using the `--driver` argument.

```bash
python script_name.py --files /path/to/log/files --driver "John Doe"
```

Additionally, you can sort the report in ascending or descending order using the `--asc` or `--desc` arguments.

```bash
python script_name.py --files /path/to/log/files --asc
```

## Log File Format

The log files should be in the following format:

* `start.log.txt`: Each line should contain the driver's abbreviation and start time, separated by an underscore.
* `end.log.txt`: Each line should contain the driver's abbreviation and end time, separated by an underscore.
* `abbreviations.txt`: Each line should contain the driver's abbreviation and name, separated by an underscore.

Example:

`start.log.txt`:
```
JD_12:00:00.000
JS_12:00:05.000
```

`end.log.txt`:
```
JD_12:05:00.000
JS_12:05:10.000
```

`abbreviations.txt`:
```
JD_John Doe
JS_Jane Smith
```

## Report Format

The report will be printed to the console in the following format:

```
1. John Doe | JD | 00:05.000
2. Jane Smith | JS | 00:05.000
```

The report will be sorted by time difference in ascending order by default. If the `--asc` or `--desc` arguments are used, the report will be sorted accordingly.