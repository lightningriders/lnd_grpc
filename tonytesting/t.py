import python_lnd_grpc 

obj = python_lnd_grpc.LNDMethods(network="mainnet")
info = obj.get_info()
print(info)
feereport = obj.fee_report()
print(feereport)
walletbalance = obj.wallet_balance()
print(walletbalance)
channelbalance = obj.channel_balance()
print(channelbalance)
pubkey = "0390b5d4492dc2f5318e5233ab2cebf6d48914881a33ef6a9c6bcdbb433ad986d0"
ip_addr = "46.229.165.136:9735"
addr = {
    'pubkey' : pubkey,
    'host' : ip_addr
}
# connectpeer = obj.connect_peer(addr, False)