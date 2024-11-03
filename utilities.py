import re


# iterate over the lines file and check if the range is already found
def get_range(file, pattern):
    min_range, max_range = None, None

    for line in file:
        cur_min_vol, cur_max_vol = extract_range(line, pattern)
        if cur_min_vol != 0 and cur_max_vol != 0:
            # in case is the first time found reasenble range
            if min_range == None and max_range == None:
                min_range = cur_min_vol
                max_range = cur_max_vol
            # in case we found the range already
            elif cur_min_vol == min_range and cur_max_vol == max_range:
                continue
            # in case we found two different ranges
            else:
                return None, None

    return min_range, max_range


# extract the range from the text line by pattern and return it
def extract_range(line, pattern):
    start_voltage = 0
    end_voltage = 0

    # search for the pattern in the text
    match = re.search(pattern, line)

    if match:
        # extract the matched values
        start_voltage = match.group(1)
        end_voltage = match.group(2)

    return start_voltage, end_voltage


# filter the devives by given values
def get_valid_devices(devices, valid_values):
    return {index: device for index, device in devices.items() if device.is_valid(valid_values)}
