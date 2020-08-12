from AWSTerraform.base_aws import *


class AWSVpc(AWSComponent):
    def __init__(self, component_name, cidr_block, instance_tenacy='default', enable_dns_support=True,
                 enable_dns_hostnames=False, enable_classiclink=False, enable_classiclink_dns_support=None,
                 assign_generated_ipv6_cidr_block=False, tags=None):

        super(AWSVpc, self).__init__(component_name)
        self.cidr_block = cidr_block
        self.instance_tenacy = instance_tenacy
        self.enable_dns_support = enable_dns_support
        self.enable_dns_hostnames = enable_dns_hostnames
        self.enable_classiclink = enable_classiclink
        self.enable_classiclink_dns_support = enable_classiclink_dns_support
        self.assign_generated_ipv6_cidr_block = assign_generated_ipv6_cidr_block
        self.tags = tags

    def to_string(self):
        resource_header = '"aws_vpc"'

        dict_attr = self.__dict__
        dict_as_tf = ""
        component_name = '"' + self.component_name + '"'

        for key in dict_attr.keys():
            if key == 'component_name' or key == 'tags':
                continue
            value = dict_attr[key]
            if value is not None:
                if type(value) is bool:
                    dict_as_tf += '\t' + key + ' = ' + str(value).lower() + '\n'
                else:
                    dict_as_tf += '\t' + key + ' = "' + str(value) + '"\n'

        dict_tags_str = ""
        if dict_attr['tags'] is not None:
            dict_tags_str += "\ttags = {\n"
            dict_tags = dict_attr['tags']
            for key_tag in dict_tags:
                dict_tags_str += '\t\t' + key_tag + ' = "' + dict_tags[key_tag] + '"\n'
            dict_tags_str += "\t}\n"

        dict_as_tf += dict_tags_str
        string_resource = " ".join(["resource",
                                    resource_header,
                                    component_name,
                                    "{\n",
                                    dict_as_tf,
                                    "}"])

        print(string_resource)