# define the device with all its components
class Device:
    def __init__(self, components):
        self.components = components

    # get all device's components
    def get_components(self):
        return self.components
    
    # check if the device is valid by the valid parameters
    def is_valid(self, valid_values):
        return all(component.check_if_valid(valid_values[index]) for index, component in enumerate(self.components))
    
    def __str__(self) -> str:
        answer = ""
        for component in self.components:
            answer = answer + str(component) + " | "
        return answer