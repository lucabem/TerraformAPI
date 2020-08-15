from AWSTerraform import *

if __name__ == "__main__":

    aws_vpc = AWSVpc(component_name='vpc_luis', cidr_block='172.10.10.0/16',
                     tags={'Name': 'TFG', 'Billing': 'Test'})

    aws_subnet = AWSSubnet(cidr_block='172.10.10.1/24', component_name='subnet_luis_1', vpc=aws_vpc,
                           tags={'Name': 'TFG', 'Billing': 'Test'})

    aws_internet_gateway = AWSInternetGateway("ig_luis", aws_vpc, tags={'Name': 'TFG', 'Billing': 'Test'})

    aws_eip = AWSEip("eipalloc-luis", vpc=True)

    aws_nat_gateway = AWSNATGateway("nat_luis", aws_eip, aws_subnet, tags={'Name': 'TFG', 'Billing': 'Test'})

    print (aws_nat_gateway.to_terraform())

