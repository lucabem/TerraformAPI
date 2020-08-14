
class AWSComponent():
    def __init__(self, component_name, tags=None):
        self.component_name = component_name
        self.tags = tags

    def to_string(self):
        print()

    def print_tags(self):
        dict_tags_str = ""
        if self.tags is not None:
            dict_tags_str += "\ttags = {\n"
            dict_tags = self.tags
            for key_tag in dict_tags:
                dict_tags_str += '\t\t' + key_tag + ' = "' + dict_tags[key_tag] + '"\n'
            dict_tags_str += "\t}\n"

        return dict_tags_str
