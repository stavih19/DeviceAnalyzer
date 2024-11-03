import os
import copy
import pickle
import Range
import Device
from operates import Range_Component
from utilities import get_valid_devices

dir_path = 'Task example files'

# define component pattern in file lines
component_list = [Range_Component('Volt', Range.Range(0, 0), r"(\d+(?:\.\d+)?)\s*V\s*to\s*(\d+(?:\.\d+)?)\s*V"), 
                  Range_Component('Temperature', Range.Range(0, 0), r"([-+]?\d+)[°�]C\s*to\s*([-+]?\d+)[°�]C")]

# analyze and save the devices into disk
def analyze():
    devices = {}

    # iterate files by givven dir path
    for filename in os.listdir(dir_path):
        file_path = os.path.join(dir_path, filename)
        components = []
    
        # search for component patterns in each file
        for component in component_list:
            with open(file_path, "r", encoding="latin-1") as file:
                # extrac the details by the pattern component
                range = component.extract(file)

                # save in memory
                component.save(range)
                components.append(component)
        file_name_part = filename.split('.')[:-1]
        device_name = '.'.join(file_name_part)

        # store all components by devices in memory
        devices[device_name] = Device.Device(copy.deepcopy(components))

    # store all components by devices in disk
    with open("devices.pkl", "wb") as file:
        pickle.dump(devices, file)


# read devices from disk and filter by parameters
def query(param):
    with open("devices.pkl", "rb") as file:
        devices = pickle.load(file)

    valid_devices = get_valid_devices(devices, param)

    # print filtered devices for comfort
    for device_index in valid_devices:
        print(device_index)
        print(valid_devices[device_index])
        print("\n")


if __name__ == "__main__":
    analyze()

    voltage = 5.6
    tempperature = 0
    query(param=[voltage, tempperature])
