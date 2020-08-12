
class AWSComponent():
    def __init__(self, component_name):
        self.component_name = component_name

    def setComponentName(self, component_name):
        self.component_name = component_name

    def getComponentName(self):
        return self.component_name

    def to_string(self):
        print()
