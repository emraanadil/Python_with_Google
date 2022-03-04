import re

def get_pid(log_line):
    regex = r'\[(\d+\)]'
    result = re.search(regex,log_line)
    if result is None:
        return ""
    return result[1]


value = get_pid('hahha this is log line [9999]')
print(value)