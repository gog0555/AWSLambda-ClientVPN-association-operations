import boto3
import time

def lambda_handler(event, context):
    #Client VPN Endpoint 情報
    client_vpn_id = event['client_vpn_id']
    
    #関連付けをする Subnet 情報
    subnet_list = event['subnet_list']
    
    #ルートテーブルに登録する送信先 CIDR 情報
    destination_cidr_block_list = event['destination_cidr_block_list']
    
    client = boto3.client('ec2')
    
    for i in range(len(subnet_list)):
        #Client VPN に Subnet をアタッチ
        client.associate_client_vpn_target_network(
            ClientVpnEndpointId = client_vpn_id,
            SubnetId = subnet_list[i]
            )
        
        for j in range(len(destination_cidr_block_list)):
            #設定が入りきらない場合があるので、ウェイトをかける
            time.sleep(3)
            
            #Client VPN の Route Table 設定
            client.create_client_vpn_route(
                ClientVpnEndpointId = client_vpn_id,
                DestinationCidrBlock = destination_cidr_block_list[j],
                TargetVpcSubnetId = subnet_list[i]
                )