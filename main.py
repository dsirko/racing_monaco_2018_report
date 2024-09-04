import datetime
from email.utils import format_datetime


def build_report():
    pass


def print_report():
    pass


def read_text_file(file_path):
    with open(file_path, 'r') as file:
        contents = file.read()
    return contents


def split_data(text_data):
    split_items = []
    split_data = text_data.split('\n')
    for i in range(len(split_data)):
        split_items.append(split_data[i].split("\n"))
    for i in range(len(split_items)):
        split_items[i] = split_items[i][0].split('_')
    return split_items


def sort_data(split_items):
    sort_data = sorted(split_items, key=lambda x: x[0])
    return sort_data

        
# work with start log
text_data_start_log = read_text_file("log/start.log.txt")
splited_start_log = split_data(text_data_start_log)
sorted_start_log = sort_data(splited_start_log)
# print("\nSTART", *sorted_start_log, sep='\n')


# work with end log
text_data_end_log = read_text_file("log/end.log.txt")
splited_end_log = split_data(text_data_end_log)
sorted_end_log = sort_data(splited_end_log)
# print("\nEND", *sorted_end_log, sep='\n')


# work eith abbreviations
text_data_abbreviations = read_text_file("log/abbreviations.txt")
splited_abbreviations = split_data(text_data_abbreviations)
sorted_split_abbreviations = sort_data(splited_abbreviations)
# print("\nABBREVIATIONS", *sorted_split_abbreviations, sep='\n')


# time_res = []
#
# for i in sorted_start_log:
#     datatipe_start = datetime.datetime.strptime(sorted_start_log[i][1], '%H:%M:%S.%f')
#     datatipe_finish = datetime.datetime.strptime(sorted_end_log[i][1], '%H:%M:%S.%f')
#     difference = datatipe_finish - datatipe_start
#     # Extract minutes and seconds
#     minutes = difference.seconds // 60  # Use floor division to get whole minutes
#     seconds = difference.seconds % 60  # Use modulo to get remaining seconds
#     milliseconds = difference.microseconds // 1000  # Get milliseconds
#
#     formatted_output = f"{minutes}:{seconds:02}.{milliseconds:03}"
#     time_res.append(formatted_output)
#
# print("test", time_res)
# # print(type(formatted_output))
#
# for i in range(len(sorted_start_log)):
#     sorted_start_log[i].append(time_res[i])

time_result = []

for i in range(len(sorted_start_log)):
    timestamp_start_str = sorted_start_log[i][1]
    timestamp_end_str = sorted_end_log[i][1]
    # Convert strings to datetime objects
    timestamp1 = datetime.datetime.strptime(timestamp_start_str, '%H:%M:%S.%f')
    timestamp2 = datetime.datetime.strptime(timestamp_end_str,'%H:%M:%S.%f')
    # Calculate the difference
    difference = timestamp2 - timestamp1
    minutes, seconds = divmod(difference.seconds, 60)
    seconds += difference.microseconds / 1e6
    # Print the difference in seconds
    time_result.append(difference)



for abbrev, time in zip(sorted_split_abbreviations, time_result):
    abbrev.append(time)
# for i in range(len(sorted_split_abbreviations)):
#     sorted_split_abbreviations[i].append(time_result[i])

prereport = sorted(sorted_split_abbreviations, key=lambda x: x[3])

print(*prereport, sep='\n')




# last_report = []
# for i in range(len(sorted_split_abbreviations)):
#     last_report.append(f"{i + 1}. {sorted_split_abbreviations[i][1]} | {sorted_split_abbreviations[i][2]} | {time_result[i]}")
#     print(last_report[i])

