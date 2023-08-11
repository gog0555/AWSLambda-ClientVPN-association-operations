import boto3

def lambda_handler(event,context):
    #Client VPN Endpoint 情報
    client_vpn_id = event['client_vpn_id']

    client = boto3.client('ec2')
    
    #Client VPN の Subnet Association ID の取得
    client_vpn_data = client.describe_client_vpn_target_networks(
        ClientVpnEndpointId = client_vpn_id
        )
        
    for i in range(len(client_vpn_data['ClientVpnTargetNetworks'])):
        association_id = client_vpn_data['ClientVpnTargetNetworks'][i]['AssociationId']
    
        #Client VPN の Subnet のデタッチ
        client.disassociate_client_vpn_target_network(
            ClientVpnEndpointId = client_vpn_id,
            AssociationId = association_id
            )