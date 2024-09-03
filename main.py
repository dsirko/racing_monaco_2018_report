import datetime


def read_text_file(file_path):
    with open(file_path, 'r') as file:
        contents = file.read()
    return contents

def split_data(text_data):
    split_items = []
    split_data = text_data.split()
    for i in range(len(split_data)):
        split_items.append(split_data[i].split("\n"))
    #   print(split_items[i])
    # print(split_items)
    return split_items

def sort_data(split_items):
    sort_data = []
    sort_data = sorted(split_items, key=lambda x: x[0])
    return sort_data
    # for i in range(len(sort_data)):
    #     print(sort_data[i])

        
# work with start log
text_data_start_log = read_text_file("start.log.txt")
splited_start_log = split_data(text_data_start_log)
# print (f"SPLITED START LOG: \n {splited_start_log}")
sorted_start_log = sort_data(splited_start_log)
print("START\n")
for i in range(len(sorted_start_log)):
    print(sorted_start_log[i])


# work with end log
text_data_end_log = read_text_file("end.log.txt")
splited_end_log = split_data(text_data_end_log)
# print (f"SPLITED END LOG: \n {splited_end_log}")
sorted_end_log = sort_data(splited_end_log)
print("\nEND")
for i in range(len(sorted_end_log)):
    print(sorted_end_log[i])


# work eith abbreviations
text_data_abbreviations = read_text_file("abbreviations.txt")
splited_abbreviations = text_data_abbreviations.split('\n')
# print(splited_abbreviations)
# for i in range(len(splited_abbreviations))
sorted_abbreviations = sorted(splited_abbreviations)
print("\nABB")
# print(sorted_abbreviations)
for i in range(len(sorted_abbreviations)):
    print(sorted_abbreviations[i])\

# cut_names
for name in sorted_abbreviations:
    cut_name = name.replace()

# print("start")
# for i in range(len(sp_t_d)):
#     sp_all_el_start.append(sp_t_d[i].split('_'))
# print(sp_all_el_start)

# start_log_sorted = sorted_data(splited_start_log)
# print (f"SORTED START LOG: \n {start_log_sorted}")
# sorted_list = sorted(sp_all_el_start, key=lambda x: x[1])






file_path_finish = "end.log.txt"
text_data_finish = read_text_file(file_path_finish)
sp_t_d_finish = text_data_finish.split()
sp_all_el_finish = []

print("end")
for i in range(len(sp_t_d_finish)):
    sp_all_el_finish.append(sp_t_d_finish[i].split('_'))
print(sp_all_el_finish)

sp_all_el_finish_sorted = sorted(sp_all_el_finish)
print(sp_all_el_finish_sorted)

tme_res = []

for i in range(len(start_log_sorted)):
    datatipe_start = datetime.datetime.strptime(start_log_sorted[i][1], '%H:%M:%S.%f')
    datatipe_finish = datetime.datetime.strptime(sp_all_el_finish_sorted[i][1], '%H:%M:%S.%f')
    difference = datatipe_finish - datatipe_start
    # Extract minutes and seconds
    minutes = difference.seconds // 60  # Use floor division to get whole minutes
    seconds = difference.seconds % 60  # Use modulo to get remaining seconds
    milliseconds = difference.microseconds // 1000  # Get milliseconds

    formatted_output = f"{minutes}:{seconds:02}.{milliseconds:03}"
    tme_res.append(formatted_output)

print("test", tme_res)
# print(type(formatted_output))

for i in range(len(start_log_sorted)):
    start_log_sorted[i].append(tme_res[i])

    # lap_time = [sp_all_el_start_sorted[i][0]] = formatted_output

    


for i in start_log_sorted:
    print(i)

file_path_finish = "abbreviations.txt"
text_data_finish = read_text_file(file_path_finish)
sp_t_d_finish = text_data_finish.split('\n')
names_of_drivers = []
print(sp_t_d_finish)

for i in range(len(sp_t_d_finish)):
    names_of_drivers.append(sp_t_d_finish[i].split())
print(names_of_drivers)

# print("----")

# for i in sp_all_el_finish_sorted:
#     print(i)



# sorted_from_max_to_min = sorted(sp_all_el_start, key=lambda x: x[1], reverse=True)

timestamp1_str = start_log_sorted[0][1]
timestamp2_str = sp_all_el_finish[0][1]
# Convert strings to datetime objects
timestamp1 = datetime.datetime.strptime(timestamp1_str, '%H:%M:%S.%f')
timestamp2 = datetime.datetime.strptime(timestamp2_str, '%H:%M:%S.%f')
# Calculate the difference
difference = timestamp2 - timestamp1
# Print the difference in seconds
print(difference.total_seconds())
