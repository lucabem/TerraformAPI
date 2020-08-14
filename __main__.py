from AWSTerraform import *

if __name__ == "__main__":

    aws_vpc = AWSVpc(component_name='vpc_luis', cidr_block='172.10.10.0/16',
                     tags={'Name': 'TFG', 'Billing': 'Test'})
    print(aws_vpc.to_terraform())

    print()

    aws_subnet = AWSSubnet(cidr_block='172.10.10.1/24', component_name='subnet_luis_1', vpc=aws_vpc,
                           tags={'Name': 'TFG', 'Billing': 'Test'})
    print(aws_subnet.to_terraform())