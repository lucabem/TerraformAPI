from AWSTerraform.base_aws import *


class AWSVpc(AWSComponent):
    def __init__(self, component_name, cidr_block, instance_tenacy='default', enable_dns_support=True,
                 enable_dns_hostnames=False, enable_classiclink=False, enable_classiclink_dns_support=None,
                 assign_generated_ipv6_cidr_block=False, tags=None):

        super(AWSVpc, self).__init__(component_name, tags)
        self.cidr_block = cidr_block
        self.instance_tenacy = instance_tenacy
        self.enable_dns_support = enable_dns_support
        self.enable_dns_hostnames = enable_dns_hostnames
        self.enable_classiclink = enable_classiclink
        self.enable_classiclink_dns_support = enable_classiclink_dns_support
        self.assign_generated_ipv6_cidr_block = assign_generated_ipv6_cidr_block

    def to_terraform(self):
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

        dict_tags_str = self.print_tags()
        dict_as_tf += dict_tags_str
        string_resource = " ".join(["resource",
                                    resource_header,
                                    component_name,
                                    "{\n",
                                    dict_as_tf,
                                    "}"])
        return string_resource

    def get_id(self):
        return ".".join(['aws_vpc', self.component_name, 'id'])

    def get_arn(self):
        return ".".join(['aws_vpc', self.component_name, 'arn'])


class AWSSubnet(AWSComponent):

    def __init__(self, component_name, vpc, cidr_block,
                 availability_zone=None, availability_zone_id=None,
                 ipv6_cidr_block=None, map_public_ip_on_launch=False, outpost_arn=None,
                 assign_ipv6_address_on_creation=False, tags=None):

        super(AWSSubnet, self).__init__(component_name, tags)
        self.vpc = vpc
        self.cidr_block = cidr_block
        self.availability_zone = availability_zone
        self.availability_zone_id = availability_zone_id
        self.ipv6_cidr_block = ipv6_cidr_block
        self.map_public_ip_on_launch = map_public_ip_on_launch
        self.outpost_arn = outpost_arn
        self.assign_ipv6_address_on_creation = assign_ipv6_address_on_creation
        self.tags = tags

    def to_terraform(self):
        resource_header = "aws_subnet"

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
                    if key == 'vpc':
                        value = self.vpc.get_id()
                        dict_as_tf += '\t' + key + ' = ' + str(value) + '\n'
                    else:
                        dict_as_tf += '\t' + key + ' = "' + str(value) + '"\n'

        dict_tags_str = self.print_tags()

        dict_as_tf += dict_tags_str
        string_resource = " ".join(["resource",
                                    resource_header,
                                    component_name,
                                    "{\n",
                                    dict_as_tf,
                                    "}"])
        return string_resource

    def get_id(self):
        return ".".join(['aws_subnet', self.component_name, 'id'])

    def get_arn(self):
        return ".".join(['aws_subnet', self.component_name, 'arn'])




