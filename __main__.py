from AWSTerraform import *

if __name__ == "__main__":

    aws_vpc = AWSVpc(component_name='vpc_luis', cidr_block='172.10.10.0/16',
                     tags={'Name': 'TFG', 'Billing': 'Test'})
    aws_vpc.to_string()