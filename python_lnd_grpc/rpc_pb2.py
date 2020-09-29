import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='rpc.proto',
  package='lnrpc',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\trpc.proto\x12\x05lnrpc\x1a\x1cgoogle/api/annotations.proto\"A\n\x0eGenSeedRequest\x12\x19\n\x11\x61\x65zeed_passphrase\x18\x01 \x01(\x0c\x12\x14\n\x0cseed_entropy\x18\x02 \x01(\x0c\"H\n\x0fGenSeedResponse\x12\x1c\n\x14\x63ipher_seed_mnemonic\x18\x01 \x03(\t\x12\x17\n\x0f\x65nciphered_seed\x18\x02 \x01(\x0c\"~\n\x11InitWalletRequest\x12\x17\n\x0fwallet_password\x18\x01 \x01(\x0c\x12\x1c\n\x14\x63ipher_seed_mnemonic\x18\x02 \x03(\t\x12\x19\n\x11\x61\x65zeed_passphrase\x18\x03 \x01(\x0c\x12\x17\n\x0frecovery_window\x18\x04 \x01(\x05\"\x14\n\x12InitWalletResponse\"G\n\x13UnlockWalletRequest\x12\x17\n\x0fwallet_password\x18\x01 \x01(\x0c\x12\x17\n\x0frecovery_window\x18\x02 \x01(\x05\"\x16\n\x14UnlockWalletResponse\"G\n\x15\x43hangePasswordRequest\x12\x18\n\x10\x63urrent_password\x18\x01 \x01(\x0c\x12\x14\n\x0cnew_password\x18\x02 \x01(\x0c\"\x18\n\x16\x43hangePasswordResponse\"\x99\x02\n\x0bTransaction\x12\x18\n\x07tx_hash\x18\x01 \x01(\tR\x07tx_hash\x12\x16\n\x06\x61mount\x18\x02 \x01(\x03R\x06\x61mount\x12,\n\x11num_confirmations\x18\x03 \x01(\x05R\x11num_confirmations\x12\x1e\n\nblock_hash\x18\x04 \x01(\tR\nblock_hash\x12\"\n\x0c\x62lock_height\x18\x05 \x01(\x05R\x0c\x62lock_height\x12\x1e\n\ntime_stamp\x18\x06 \x01(\x03R\ntime_stamp\x12\x1e\n\ntotal_fees\x18\x07 \x01(\x03R\ntotal_fees\x12&\n\x0e\x64\x65st_addresses\x18\x08 \x03(\tR\x0e\x64\x65st_addresses\"\x18\n\x16GetTransactionsRequest\"L\n\x12TransactionDetails\x12\x36\n\x0ctransactions\x18\x01 \x03(\x0b\x32\x12.lnrpc.TransactionR\x0ctransactions\"7\n\x08\x46\x65\x65Limit\x12\x0f\n\x05\x66ixed\x18\x01 \x01(\x03H\x00\x12\x11\n\x07percent\x18\x02 \x01(\x03H\x00\x42\x07\n\x05limit\"\xc7\x01\n\x0bSendRequest\x12\x0c\n\x04\x64\x65st\x18\x01 \x01(\x0c\x12\x13\n\x0b\x64\x65st_string\x18\x02 \x01(\t\x12\x0b\n\x03\x61mt\x18\x03 \x01(\x03\x12\x14\n\x0cpayment_hash\x18\x04 \x01(\x0c\x12\x1b\n\x13payment_hash_string\x18\x05 \x01(\t\x12\x17\n\x0fpayment_request\x18\x06 \x01(\t\x12\x18\n\x10\x66inal_cltv_delta\x18\x07 \x01(\x05\x12\"\n\tfee_limit\x18\x08 \x01(\x0b\x32\x0f.lnrpc.FeeLimit\"\x94\x01\n\x0cSendResponse\x12$\n\rpayment_error\x18\x01 \x01(\tR\rpayment_error\x12*\n\x10payment_preimage\x18\x02 \x01(\x0cR\x10payment_preimage\x12\x32\n\rpayment_route\x18\x03 \x01(\x0b\x32\x0c.lnrpc.RouteR\rpayment_route\"e\n\x12SendToRouteRequest\x12\x14\n\x0cpayment_hash\x18\x01 \x01(\x0c\x12\x1b\n\x13payment_hash_string\x18\x02 \x01(\t\x12\x1c\n\x06routes\x18\x03 \x03(\x0b\x32\x0c.lnrpc.Route\"\xa2\x01\n\x0c\x43hannelPoint\x12\x30\n\x12\x66unding_txid_bytes\x18\x01 \x01(\x0cH\x00R\x12\x66unding_txid_bytes\x12,\n\x10\x66unding_txid_str\x18\x02 \x01(\tH\x00R\x10\x66unding_txid_str\x12\"\n\x0coutput_index\x18\x03 \x01(\rR\x0coutput_indexB\x0e\n\x0c\x66unding_txid\">\n\x10LightningAddress\x12\x16\n\x06pubkey\x18\x01 \x01(\tR\x06pubkey\x12\x12\n\x04host\x18\x02 \x01(\tR\x04host\"\xb1\x01\n\x0fSendManyRequest\x12>\n\x0c\x41\x64\x64rToAmount\x18\x01 \x03(\x0b\x32(.lnrpc.SendManyRequest.AddrToAmountEntry\x12\x13\n\x0btarget_conf\x18\x03 \x01(\x05\x12\x14\n\x0csat_per_byte\x18\x05 \x01(\x03\x1a\x33\n\x11\x41\x64\x64rToAmountEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x03:\x02\x38\x01\"&\n\x10SendManyResponse\x12\x12\n\x04txid\x18\x01 \x01(\tR\x04txid\"[\n\x10SendCoinsRequest\x12\x0c\n\x04\x61\x64\x64r\x18\x01 \x01(\t\x12\x0e\n\x06\x61mount\x18\x02 \x01(\x03\x12\x13\n\x0btarget_conf\x18\x03 \x01(\x05\x12\x14\n\x0csat_per_byte\x18\x05 \x01(\x03\"\'\n\x11SendCoinsResponse\x12\x12\n\x04txid\x18\x01 \x01(\tR\x04txid\"\x87\x01\n\x11NewAddressRequest\x12\x32\n\x04type\x18\x01 \x01(\x0e\x32$.lnrpc.NewAddressRequest.AddressType\">\n\x0b\x41\x64\x64ressType\x12\x17\n\x13WITNESS_PUBKEY_HASH\x10\x00\x12\x16\n\x12NESTED_PUBKEY_HASH\x10\x01\".\n\x12NewAddressResponse\x12\x18\n\x07\x61\x64\x64ress\x18\x01 \x01(\tR\x07\x61\x64\x64ress\"&\n\x12SignMessageRequest\x12\x10\n\x03msg\x18\x01 \x01(\x0cR\x03msg\"3\n\x13SignMessageResponse\x12\x1c\n\tsignature\x18\x01 \x01(\tR\tsignature\"F\n\x14VerifyMessageRequest\x12\x10\n\x03msg\x18\x01 \x01(\x0cR\x03msg\x12\x1c\n\tsignature\x18\x02 \x01(\tR\tsignature\"E\n\x15VerifyMessageResponse\x12\x14\n\x05valid\x18\x01 \x01(\x08R\x05valid\x12\x16\n\x06pubkey\x18\x02 \x01(\tR\x06pubkey\"I\n\x12\x43onnectPeerRequest\x12%\n\x04\x61\x64\x64r\x18\x01 \x01(\x0b\x32\x17.lnrpc.LightningAddress\x12\x0c\n\x04perm\x18\x02 \x01(\x08\"\x15\n\x13\x43onnectPeerResponse\"1\n\x15\x44isconnectPeerRequest\x12\x18\n\x07pub_key\x18\x01 \x01(\tR\x07pub_key\"\x18\n\x16\x44isconnectPeerResponse\"\x86\x01\n\x04HTLC\x12\x1a\n\x08incoming\x18\x01 \x01(\x08R\x08incoming\x12\x16\n\x06\x61mount\x18\x02 \x01(\x03R\x06\x61mount\x12\x1c\n\thash_lock\x18\x03 \x01(\x0cR\thash_lock\x12,\n\x11\x65xpiration_height\x18\x04 \x01(\rR\x11\x65xpiration_height\"\xfe\x04\n\x07\x43hannel\x12\x16\n\x06\x61\x63tive\x18\x01 \x01(\x08R\x06\x61\x63tive\x12$\n\rremote_pubkey\x18\x02 \x01(\tR\rremote_pubkey\x12$\n\rchannel_point\x18\x03 \x01(\tR\rchannel_point\x12\x18\n\x07\x63han_id\x18\x04 \x01(\x04R\x07\x63han_id\x12\x1a\n\x08\x63\x61pacity\x18\x05 \x01(\x03R\x08\x63\x61pacity\x12$\n\rlocal_balance\x18\x06 \x01(\x03R\rlocal_balance\x12&\n\x0eremote_balance\x18\x07 \x01(\x03R\x0eremote_balance\x12\x1e\n\ncommit_fee\x18\x08 \x01(\x03R\ncommit_fee\x12$\n\rcommit_weight\x18\t \x01(\x03R\rcommit_weight\x12\x1e\n\nfee_per_kw\x18\n \x01(\x03R\nfee_per_kw\x12,\n\x11unsettled_balance\x18\x0b \x01(\x03R\x11unsettled_balance\x12\x30\n\x13total_satoshis_sent\x18\x0c \x01(\x03R\x13total_satoshis_sent\x12\x38\n\x17total_satoshis_received\x18\r \x01(\x03R\x17total_satoshis_received\x12 \n\x0bnum_updates\x18\x0e \x01(\x04R\x0bnum_updates\x12\x31\n\rpending_htlcs\x18\x0f \x03(\x0b\x32\x0b.lnrpc.HTLCR\rpending_htlcs\x12\x1c\n\tcsv_delay\x18\x10 \x01(\rR\tcsv_delay\x12\x18\n\x07private\x18\x11 \x01(\x08R\x07private\"l\n\x13ListChannelsRequest\x12\x13\n\x0b\x61\x63tive_only\x18\x01 \x01(\x08\x12\x15\n\rinactive_only\x18\x02 \x01(\x08\x12\x13\n\x0bpublic_only\x18\x03 \x01(\x08\x12\x14\n\x0cprivate_only\x18\x04 \x01(\x08\"B\n\x14ListChannelsResponse\x12*\n\x08\x63hannels\x18\x0b \x03(\x0b\x32\x0e.lnrpc.ChannelR\x08\x63hannels\"\xb6\x04\n\x13\x43hannelCloseSummary\x12$\n\rchannel_point\x18\x01 \x01(\tR\rchannel_point\x12\x18\n\x07\x63han_id\x18\x02 \x01(\x04R\x07\x63han_id\x12\x1e\n\nchain_hash\x18\x03 \x01(\tR\nchain_hash\x12(\n\x0f\x63losing_tx_hash\x18\x04 \x01(\tR\x0f\x63losing_tx_hash\x12$\n\rremote_pubkey\x18\x05 \x01(\tR\rremote_pubkey\x12\x1a\n\x08\x63\x61pacity\x18\x06 \x01(\x03R\x08\x63\x61pacity\x12\"\n\x0c\x63lose_height\x18\x07 \x01(\rR\x0c\x63lose_height\x12(\n\x0fsettled_balance\x18\x08 \x01(\x03R\x0fsettled_balance\x12\x30\n\x13time_locked_balance\x18\t \x01(\x03R\x13time_locked_balance\x12\x46\n\nclose_type\x18\n \x01(\x0e\x32&.lnrpc.ChannelCloseSummary.ClosureTypeR\nclose_type\"\x8a\x01\n\x0b\x43losureType\x12\x15\n\x11\x43OOPERATIVE_CLOSE\x10\x00\x12\x15\n\x11LOCAL_FORCE_CLOSE\x10\x01\x12\x16\n\x12REMOTE_FORCE_CLOSE\x10\x02\x12\x10\n\x0c\x42REACH_CLOSE\x10\x03\x12\x14\n\x10\x46UNDING_CANCELED\x10\x04\x12\r\n\tABANDONED\x10\x05\"\x94\x01\n\x15\x43losedChannelsRequest\x12\x13\n\x0b\x63ooperative\x18\x01 \x01(\x08\x12\x13\n\x0blocal_force\x18\x02 \x01(\x08\x12\x14\n\x0cremote_force\x18\x03 \x01(\x08\x12\x0e\n\x06\x62reach\x18\x04 \x01(\x08\x12\x18\n\x10\x66unding_canceled\x18\x05 \x01(\x08\x12\x11\n\tabandoned\x18\x06 \x01(\x08\"P\n\x16\x43losedChannelsResponse\x12\x36\n\x08\x63hannels\x18\x01 \x03(\x0b\x32\x1a.lnrpc.ChannelCloseSummaryR\x08\x63hannels\"\xea\x01\n\x04Peer\x12\x18\n\x07pub_key\x18\x01 \x01(\tR\x07pub_key\x12\x18\n\x07\x61\x64\x64ress\x18\x03 \x01(\tR\x07\x61\x64\x64ress\x12\x1e\n\nbytes_sent\x18\x04 \x01(\x04R\nbytes_sent\x12\x1e\n\nbytes_recv\x18\x05 \x01(\x04R\nbytes_recv\x12\x1a\n\x08sat_sent\x18\x06 \x01(\x03R\x08sat_sent\x12\x1a\n\x08sat_recv\x18\x07 \x01(\x03R\x08sat_recv\x12\x18\n\x07inbound\x18\x08 \x01(\x08R\x07inbound\x12\x1c\n\tping_time\x18\t \x01(\x03R\tping_time\"\x12\n\x10ListPeersRequest\"6\n\x11ListPeersResponse\x12!\n\x05peers\x18\x01 \x03(\x0b\x32\x0b.lnrpc.PeerR\x05peers\"\x10\n\x0eGetInfoRequest\"\x8f\x04\n\x0fGetInfoResponse\x12(\n\x0fidentity_pubkey\x18\x01 \x01(\tR\x0fidentity_pubkey\x12\x14\n\x05\x61lias\x18\x02 \x01(\tR\x05\x61lias\x12\x32\n\x14num_pending_channels\x18\x03 \x01(\rR\x14num_pending_channels\x12\x30\n\x13num_active_channels\x18\x04 \x01(\rR\x13num_active_channels\x12\x1c\n\tnum_peers\x18\x05 \x01(\rR\tnum_peers\x12\"\n\x0c\x62lock_height\x18\x06 \x01(\rR\x0c\x62lock_height\x12\x1e\n\nblock_hash\x18\x08 \x01(\tR\nblock_hash\x12(\n\x0fsynced_to_chain\x18\t \x01(\x08R\x0fsynced_to_chain\x12\x18\n\x07testnet\x18\n \x01(\x08R\x07testnet\x12\x16\n\x06\x63hains\x18\x0b \x03(\tR\x06\x63hains\x12\x12\n\x04uris\x18\x0c \x03(\tR\x04uris\x12\x34\n\x15\x62\x65st_header_timestamp\x18\r \x01(\x03R\x15\x62\x65st_header_timestamp\x12\x18\n\x07version\x18\x0e \x01(\tR\x07version\x12\x34\n\x15num_inactive_channels\x18\x0f \x01(\rR\x15num_inactive_channels\"U\n\x12\x43onfirmationUpdate\x12\x11\n\tblock_sha\x18\x01 \x01(\x0c\x12\x14\n\x0c\x62lock_height\x18\x02 \x01(\x05\x12\x16\n\x0enum_confs_left\x18\x03 \x01(\r\"N\n\x11\x43hannelOpenUpdate\x12\x39\n\rchannel_point\x18\x01 \x01(\x0b\x32\x13.lnrpc.ChannelPointR\rchannel_point\"R\n\x12\x43hannelCloseUpdate\x12\"\n\x0c\x63losing_txid\x18\x01 \x01(\x0cR\x0c\x63losing_txid\x12\x18\n\x07success\x18\x02 \x01(\x08R\x07success\"{\n\x13\x43loseChannelRequest\x12*\n\rchannel_point\x18\x01 \x01(\x0b\x32\x13.lnrpc.ChannelPoint\x12\r\n\x05\x66orce\x18\x02 \x01(\x08\x12\x13\n\x0btarget_conf\x18\x03 \x01(\x05\x12\x14\n\x0csat_per_byte\x18\x04 \x01(\x03\"\xd9\x01\n\x11\x43loseStatusUpdate\x12<\n\rclose_pending\x18\x01 \x01(\x0b\x32\x14.lnrpc.PendingUpdateH\x00R\rclose_pending\x12?\n\x0c\x63onfirmation\x18\x02 \x01(\x0b\x32\x19.lnrpc.ConfirmationUpdateH\x00R\x0c\x63onfirmation\x12;\n\nchan_close\x18\x03 \x01(\x0b\x32\x19.lnrpc.ChannelCloseUpdateH\x00R\nchan_closeB\x08\n\x06update\"G\n\rPendingUpdate\x12\x12\n\x04txid\x18\x01 \x01(\x0cR\x04txid\x12\"\n\x0coutput_index\x18\x02 \x01(\rR\x0coutput_index\"\x99\x03\n\x12OpenChannelRequest\x12 \n\x0bnode_pubkey\x18\x02 \x01(\x0cR\x0bnode_pubkey\x12.\n\x12node_pubkey_string\x18\x03 \x01(\tR\x12node_pubkey_string\x12\x32\n\x14local_funding_amount\x18\x04 \x01(\x03R\x14local_funding_amount\x12\x1a\n\x08push_sat\x18\x05 \x01(\x03R\x08push_sat\x12\x13\n\x0btarget_conf\x18\x06 \x01(\x05\x12\x14\n\x0csat_per_byte\x18\x07 \x01(\x03\x12\x18\n\x07private\x18\x08 \x01(\x08R\x07private\x12$\n\rmin_htlc_msat\x18\t \x01(\x03R\rmin_htlc_msat\x12*\n\x10remote_csv_delay\x18\n \x01(\rR\x10remote_csv_delay\x12\x1c\n\tmin_confs\x18\x0b \x01(\x05R\tmin_confs\x12,\n\x11spend_unconfirmed\x18\x0c \x01(\x08R\x11spend_unconfirmed\"\xd3\x01\n\x10OpenStatusUpdate\x12:\n\x0c\x63han_pending\x18\x01 \x01(\x0b\x32\x14.lnrpc.PendingUpdateH\x00R\x0c\x63han_pending\x12?\n\x0c\x63onfirmation\x18\x02 \x01(\x0b\x32\x19.lnrpc.ConfirmationUpdateH\x00R\x0c\x63onfirmation\x12\x38\n\tchan_open\x18\x03 \x01(\x0b\x32\x18.lnrpc.ChannelOpenUpdateH\x00R\tchan_openB\x08\n\x06update\"\xcf\x01\n\x0bPendingHTLC\x12\x1a\n\x08incoming\x18\x01 \x01(\x08R\x08incoming\x12\x16\n\x06\x61mount\x18\x02 \x01(\x03R\x06\x61mount\x12\x1a\n\x08outpoint\x18\x03 \x01(\tR\x08outpoint\x12(\n\x0fmaturity_height\x18\x04 \x01(\rR\x0fmaturity_height\x12\x30\n\x13\x62locks_til_maturity\x18\x05 \x01(\x05R\x13\x62locks_til_maturity\x12\x14\n\x05stage\x18\x06 \x01(\rR\x05stage\"\x18\n\x16PendingChannelsRequest\"\xaa\x0c\n\x17PendingChannelsResponse\x12\x30\n\x13total_limbo_balance\x18\x01 \x01(\x03R\x13total_limbo_balance\x12g\n\x15pending_open_channels\x18\x02 \x03(\x0b\x32\x31.lnrpc.PendingChannelsResponse.PendingOpenChannelR\x15pending_open_channels\x12h\n\x18pending_closing_channels\x18\x03 \x03(\x0b\x32,.lnrpc.PendingChannelsResponse.ClosedChannelR\x18pending_closing_channels\x12y\n\x1epending_force_closing_channels\x18\x04 \x03(\x0b\x32\x31.lnrpc.PendingChannelsResponse.ForceClosedChannelR\x1epending_force_closing_channels\x12j\n\x16waiting_close_channels\x18\x05 \x03(\x0b\x32\x32.lnrpc.PendingChannelsResponse.WaitingCloseChannelR\x16waiting_close_channels\x1a\xca\x01\n\x0ePendingChannel\x12(\n\x0fremote_node_pub\x18\x01 \x01(\tR\x0fremote_node_pub\x12$\n\rchannel_point\x18\x02 \x01(\tR\rchannel_point\x12\x1a\n\x08\x63\x61pacity\x18\x03 \x01(\x03R\x08\x63\x61pacity\x12$\n\rlocal_balance\x18\x04 \x01(\x03R\rlocal_balance\x12&\n\x0eremote_balance\x18\x05 \x01(\x03R\x0eremote_balance\x1a\xf5\x01\n\x12PendingOpenChannel\x12G\n\x07\x63hannel\x18\x01 \x01(\x0b\x32-.lnrpc.PendingChannelsResponse.PendingChannelR\x07\x63hannel\x12\x30\n\x13\x63onfirmation_height\x18\x02 \x01(\rR\x13\x63onfirmation_height\x12\x1e\n\ncommit_fee\x18\x04 \x01(\x03R\ncommit_fee\x12$\n\rcommit_weight\x18\x05 \x01(\x03R\rcommit_weight\x12\x1e\n\nfee_per_kw\x18\x06 \x01(\x03R\nfee_per_kw\x1a{\n\x13WaitingCloseChannel\x12>\n\x07\x63hannel\x18\x01 \x01(\x0b\x32-.lnrpc.PendingChannelsResponse.PendingChannel\x12$\n\rlimbo_balance\x18\x02 \x01(\x03R\rlimbo_balance\x1as\n\rClosedChannel\x12>\n\x07\x63hannel\x18\x01 \x01(\x0b\x32-.lnrpc.PendingChannelsResponse.PendingChannel\x12\"\n\x0c\x63losing_txid\x18\x02 \x01(\tR\x0c\x63losing_txid\x1a\xeb\x02\n\x12\x46orceClosedChannel\x12G\n\x07\x63hannel\x18\x01 \x01(\x0b\x32-.lnrpc.PendingChannelsResponse.PendingChannelR\x07\x63hannel\x12\"\n\x0c\x63losing_txid\x18\x02 \x01(\tR\x0c\x63losing_txid\x12$\n\rlimbo_balance\x18\x03 \x01(\x03R\rlimbo_balance\x12(\n\x0fmaturity_height\x18\x04 \x01(\rR\x0fmaturity_height\x12\x30\n\x13\x62locks_til_maturity\x18\x05 \x01(\x05R\x13\x62locks_til_maturity\x12,\n\x11recovered_balance\x18\x06 \x01(\x03R\x11recovered_balance\x12\x38\n\rpending_htlcs\x18\x08 \x03(\x0b\x32\x12.lnrpc.PendingHTLCR\rpending_htlcs\"\x16\n\x14WalletBalanceRequest\"\x9d\x01\n\x15WalletBalanceResponse\x12$\n\rtotal_balance\x18\x01 \x01(\x03R\rtotal_balance\x12,\n\x11\x63onfirmed_balance\x18\x02 \x01(\x03R\x11\x63onfirmed_balance\x12\x30\n\x13unconfirmed_balance\x18\x03 \x01(\x03R\x13unconfirmed_balance\"\x17\n\x15\x43hannelBalanceRequest\"f\n\x16\x43hannelBalanceResponse\x12\x18\n\x07\x62\x61lance\x18\x01 \x01(\x03R\x07\x62\x61lance\x12\x32\n\x14pending_open_balance\x18\x02 \x01(\x03R\x14pending_open_balance\"\x84\x01\n\x12QueryRoutesRequest\x12\x0f\n\x07pub_key\x18\x01 \x01(\t\x12\x0b\n\x03\x61mt\x18\x02 \x01(\x03\x12\x12\n\nnum_routes\x18\x03 \x01(\x05\x12\x18\n\x10\x66inal_cltv_delta\x18\x04 \x01(\x05\x12\"\n\tfee_limit\x18\x05 \x01(\x0b\x32\x0f.lnrpc.FeeLimit\";\n\x13QueryRoutesResponse\x12$\n\x06routes\x18\x01 \x03(\x0b\x32\x0c.lnrpc.RouteR\x06routes\"\x87\x02\n\x03Hop\x12\x18\n\x07\x63han_id\x18\x01 \x01(\x04R\x07\x63han_id\x12$\n\rchan_capacity\x18\x02 \x01(\x03R\rchan_capacity\x12*\n\x0e\x61mt_to_forward\x18\x03 \x01(\x03\x42\x02\x18\x01R\x0e\x61mt_to_forward\x12\x14\n\x03\x66\x65\x65\x18\x04 \x01(\x03\x42\x02\x18\x01R\x03\x66\x65\x65\x12\x16\n\x06\x65xpiry\x18\x05 \x01(\rR\x06\x65xpiry\x12\x30\n\x13\x61mt_to_forward_msat\x18\x06 \x01(\x03R\x13\x61mt_to_forward_msat\x12\x1a\n\x08\x66\x65\x65_msat\x18\x07 \x01(\x03R\x08\x66\x65\x65_msat\x12\x18\n\x07pub_key\x18\x08 \x01(\tR\x07pub_key\"\xe9\x01\n\x05Route\x12(\n\x0ftotal_time_lock\x18\x01 \x01(\rR\x0ftotal_time_lock\x12\"\n\ntotal_fees\x18\x02 \x01(\x03\x42\x02\x18\x01R\ntotal_fees\x12 \n\ttotal_amt\x18\x03 \x01(\x03\x42\x02\x18\x01R\ttotal_amt\x12\x1e\n\x04hops\x18\x04 \x03(\x0b\x32\n.lnrpc.HopR\x04hops\x12(\n\x0ftotal_fees_msat\x18\x05 \x01(\x03R\x0ftotal_fees_msat\x12&\n\x0etotal_amt_msat\x18\x06 \x01(\x03R\x0etotal_amt_msat\"\"\n\x0fNodeInfoRequest\x12\x0f\n\x07pub_key\x18\x01 \x01(\t\"\x80\x01\n\x08NodeInfo\x12(\n\x04node\x18\x01 \x01(\x0b\x32\x14.lnrpc.LightningNodeR\x04node\x12\"\n\x0cnum_channels\x18\x02 \x01(\rR\x0cnum_channels\x12&\n\x0etotal_capacity\x18\x03 \x01(\x03R\x0etotal_capacity\"\xa9\x01\n\rLightningNode\x12 \n\x0blast_update\x18\x01 \x01(\rR\x0blast_update\x12\x18\n\x07pub_key\x18\x02 \x01(\tR\x07pub_key\x12\x14\n\x05\x61lias\x18\x03 \x01(\tR\x05\x61lias\x12\x30\n\taddresses\x18\x04 \x03(\x0b\x32\x12.lnrpc.NodeAddressR\taddresses\x12\x14\n\x05\x63olor\x18\x05 \x01(\tR\x05\x63olor\";\n\x0bNodeAddress\x12\x18\n\x07network\x18\x01 \x01(\tR\x07network\x12\x12\n\x04\x61\x64\x64r\x18\x02 \x01(\tR\x04\x61\x64\x64r\"\xc9\x01\n\rRoutingPolicy\x12(\n\x0ftime_lock_delta\x18\x01 \x01(\rR\x0ftime_lock_delta\x12\x1a\n\x08min_htlc\x18\x02 \x01(\x03R\x08min_htlc\x12$\n\rfee_base_msat\x18\x03 \x01(\x03R\rfee_base_msat\x12\x30\n\x13\x66\x65\x65_rate_milli_msat\x18\x04 \x01(\x03R\x13\x66\x65\x65_rate_milli_msat\x12\x1a\n\x08\x64isabled\x18\x05 \x01(\x08R\x08\x64isabled\"\xbb\x02\n\x0b\x43hannelEdge\x12\x1e\n\nchannel_id\x18\x01 \x01(\x04R\nchannel_id\x12\x1e\n\nchan_point\x18\x02 \x01(\tR\nchan_point\x12 \n\x0blast_update\x18\x03 \x01(\rR\x0blast_update\x12\x1c\n\tnode1_pub\x18\x04 \x01(\tR\tnode1_pub\x12\x1c\n\tnode2_pub\x18\x05 \x01(\tR\tnode2_pub\x12\x1a\n\x08\x63\x61pacity\x18\x06 \x01(\x03R\x08\x63\x61pacity\x12\x38\n\x0cnode1_policy\x18\x07 \x01(\x0b\x32\x14.lnrpc.RoutingPolicyR\x0cnode1_policy\x12\x38\n\x0cnode2_policy\x18\x08 \x01(\x0b\x32\x14.lnrpc.RoutingPolicyR\x0cnode2_policy\"G\n\x13\x43hannelGraphRequest\x12\x30\n\x13include_unannounced\x18\x01 \x01(\x08R\x13include_unannounced\"d\n\x0c\x43hannelGraph\x12*\n\x05nodes\x18\x01 \x03(\x0b\x32\x14.lnrpc.LightningNodeR\x05nodes\x12(\n\x05\x65\x64ges\x18\x02 \x03(\x0b\x32\x12.lnrpc.ChannelEdgeR\x05\x65\x64ges\"\"\n\x0f\x43hanInfoRequest\x12\x0f\n\x07\x63han_id\x18\x01 \x01(\x04\"\x14\n\x12NetworkInfoRequest\"\x83\x03\n\x0bNetworkInfo\x12&\n\x0egraph_diameter\x18\x01 \x01(\rR\x0egraph_diameter\x12&\n\x0e\x61vg_out_degree\x18\x02 \x01(\x01R\x0e\x61vg_out_degree\x12&\n\x0emax_out_degree\x18\x03 \x01(\rR\x0emax_out_degree\x12\x1c\n\tnum_nodes\x18\x04 \x01(\rR\tnum_nodes\x12\"\n\x0cnum_channels\x18\x05 \x01(\rR\x0cnum_channels\x12\x36\n\x16total_network_capacity\x18\x06 \x01(\x03R\x16total_network_capacity\x12*\n\x10\x61vg_channel_size\x18\x07 \x01(\x01R\x10\x61vg_channel_size\x12*\n\x10min_channel_size\x18\x08 \x01(\x03R\x10min_channel_size\x12*\n\x10max_channel_size\x18\t \x01(\x03R\x10max_channel_size\"\r\n\x0bStopRequest\"\x0e\n\x0cStopResponse\"\x1b\n\x19GraphTopologySubscription\"\xa3\x01\n\x13GraphTopologyUpdate\x12\'\n\x0cnode_updates\x18\x01 \x03(\x0b\x32\x11.lnrpc.NodeUpdate\x12\x31\n\x0f\x63hannel_updates\x18\x02 \x03(\x0b\x32\x18.lnrpc.ChannelEdgeUpdate\x12\x30\n\x0c\x63losed_chans\x18\x03 \x03(\x0b\x32\x1a.lnrpc.ClosedChannelUpdate\"]\n\nNodeUpdate\x12\x11\n\taddresses\x18\x01 \x03(\t\x12\x14\n\x0cidentity_key\x18\x02 \x01(\t\x12\x17\n\x0fglobal_features\x18\x03 \x01(\x0c\x12\r\n\x05\x61lias\x18\x04 \x01(\t\"\xc0\x01\n\x11\x43hannelEdgeUpdate\x12\x0f\n\x07\x63han_id\x18\x01 \x01(\x04\x12\'\n\nchan_point\x18\x02 \x01(\x0b\x32\x13.lnrpc.ChannelPoint\x12\x10\n\x08\x63\x61pacity\x18\x03 \x01(\x03\x12,\n\x0erouting_policy\x18\x04 \x01(\x0b\x32\x14.lnrpc.RoutingPolicy\x12\x18\n\x10\x61\x64vertising_node\x18\x05 \x01(\t\x12\x17\n\x0f\x63onnecting_node\x18\x06 \x01(\t\"x\n\x13\x43losedChannelUpdate\x12\x0f\n\x07\x63han_id\x18\x01 \x01(\x04\x12\x10\n\x08\x63\x61pacity\x18\x02 \x01(\x03\x12\x15\n\rclosed_height\x18\x03 \x01(\r\x12\'\n\nchan_point\x18\x04 \x01(\x0b\x32\x13.lnrpc.ChannelPoint\"\xd3\x01\n\x07HopHint\x12\x18\n\x07node_id\x18\x01 \x01(\tR\x07node_id\x12\x18\n\x07\x63han_id\x18\x02 \x01(\x04R\x07\x63han_id\x12$\n\rfee_base_msat\x18\x03 \x01(\rR\rfee_base_msat\x12@\n\x1b\x66\x65\x65_proportional_millionths\x18\x04 \x01(\rR\x1b\x66\x65\x65_proportional_millionths\x12,\n\x11\x63ltv_expiry_delta\x18\x05 \x01(\rR\x11\x63ltv_expiry_delta\"9\n\tRouteHint\x12,\n\thop_hints\x18\x01 \x03(\x0b\x32\x0e.lnrpc.HopHintR\thop_hints\"\x97\x05\n\x07Invoice\x12\x12\n\x04memo\x18\x01 \x01(\tR\x04memo\x12\x18\n\x07receipt\x18\x02 \x01(\x0cR\x07receipt\x12\x1e\n\nr_preimage\x18\x03 \x01(\x0cR\nr_preimage\x12\x16\n\x06r_hash\x18\x04 \x01(\x0cR\x06r_hash\x12\x14\n\x05value\x18\x05 \x01(\x03R\x05value\x12\x18\n\x07settled\x18\x06 \x01(\x08R\x07settled\x12$\n\rcreation_date\x18\x07 \x01(\x03R\rcreation_date\x12 \n\x0bsettle_date\x18\x08 \x01(\x03R\x0bsettle_date\x12(\n\x0fpayment_request\x18\t \x01(\tR\x0fpayment_request\x12*\n\x10\x64\x65scription_hash\x18\n \x01(\x0cR\x10\x64\x65scription_hash\x12\x16\n\x06\x65xpiry\x18\x0b \x01(\x03R\x06\x65xpiry\x12$\n\rfallback_addr\x18\x0c \x01(\tR\rfallback_addr\x12 \n\x0b\x63ltv_expiry\x18\r \x01(\x04R\x0b\x63ltv_expiry\x12\x32\n\x0broute_hints\x18\x0e \x03(\x0b\x32\x10.lnrpc.RouteHintR\x0broute_hints\x12\x18\n\x07private\x18\x0f \x01(\x08R\x07private\x12\x1c\n\tadd_index\x18\x10 \x01(\x04R\tadd_index\x12\"\n\x0csettle_index\x18\x11 \x01(\x04R\x0csettle_index\x12\x1e\n\x08\x61mt_paid\x18\x12 \x01(\x03\x42\x02\x18\x01R\x08\x61mt_paid\x12\"\n\x0c\x61mt_paid_sat\x18\x13 \x01(\x03R\x0c\x61mt_paid_sat\x12$\n\ramt_paid_msat\x18\x14 \x01(\x03R\ramt_paid_msat\"t\n\x12\x41\x64\x64InvoiceResponse\x12\x16\n\x06r_hash\x18\x01 \x01(\x0cR\x06r_hash\x12(\n\x0fpayment_request\x18\x02 \x01(\tR\x0fpayment_request\x12\x1c\n\tadd_index\x18\x10 \x01(\x04R\tadd_index\"E\n\x0bPaymentHash\x12\x1e\n\nr_hash_str\x18\x01 \x01(\tR\nr_hash_str\x12\x16\n\x06r_hash\x18\x02 \x01(\x0cR\x06r_hash\"\xa4\x01\n\x12ListInvoiceRequest\x12\"\n\x0cpending_only\x18\x01 \x01(\x08R\x0cpending_only\x12\"\n\x0cindex_offset\x18\x04 \x01(\x04R\x0cindex_offset\x12*\n\x10num_max_invoices\x18\x05 \x01(\x04R\x10num_max_invoices\x12\x1a\n\x08reversed\x18\x06 \x01(\x08R\x08reversed\"\x9f\x01\n\x13ListInvoiceResponse\x12*\n\x08invoices\x18\x01 \x03(\x0b\x32\x0e.lnrpc.InvoiceR\x08invoices\x12,\n\x11last_index_offset\x18\x02 \x01(\x04R\x11last_index_offset\x12.\n\x12\x66irst_index_offset\x18\x03 \x01(\x04R\x12\x66irst_index_offset\"W\n\x13InvoiceSubscription\x12\x1c\n\tadd_index\x18\x01 \x01(\x04R\tadd_index\x12\"\n\x0csettle_index\x18\x02 \x01(\x04R\x0csettle_index\"\xfd\x01\n\x07Payment\x12\"\n\x0cpayment_hash\x18\x01 \x01(\tR\x0cpayment_hash\x12\x18\n\x05value\x18\x02 \x01(\x03\x42\x02\x18\x01R\x05value\x12$\n\rcreation_date\x18\x03 \x01(\x03R\rcreation_date\x12\x12\n\x04path\x18\x04 \x03(\tR\x04path\x12\x10\n\x03\x66\x65\x65\x18\x05 \x01(\x03R\x03\x66\x65\x65\x12*\n\x10payment_preimage\x18\x06 \x01(\tR\x10payment_preimage\x12\x1c\n\tvalue_sat\x18\x07 \x01(\x03R\tvalue_sat\x12\x1e\n\nvalue_msat\x18\x08 \x01(\x03R\nvalue_msat\"\x15\n\x13ListPaymentsRequest\"B\n\x14ListPaymentsResponse\x12*\n\x08payments\x18\x01 \x03(\x0b\x32\x0e.lnrpc.PaymentR\x08payments\"\x1a\n\x18\x44\x65leteAllPaymentsRequest\"\x1b\n\x19\x44\x65leteAllPaymentsResponse\"C\n\x15\x41\x62\x61ndonChannelRequest\x12*\n\rchannel_point\x18\x01 \x01(\x0b\x32\x13.lnrpc.ChannelPoint\"\x18\n\x16\x41\x62\x61ndonChannelResponse\"5\n\x11\x44\x65\x62ugLevelRequest\x12\x0c\n\x04show\x18\x01 \x01(\x08\x12\x12\n\nlevel_spec\x18\x02 \x01(\t\"6\n\x12\x44\x65\x62ugLevelResponse\x12 \n\x0bsub_systems\x18\x01 \x01(\tR\x0bsub_systems\"\x1f\n\x0cPayReqString\x12\x0f\n\x07pay_req\x18\x01 \x01(\t\"\xf2\x02\n\x06PayReq\x12 \n\x0b\x64\x65stination\x18\x01 \x01(\tR\x0b\x64\x65stination\x12\"\n\x0cpayment_hash\x18\x02 \x01(\tR\x0cpayment_hash\x12\"\n\x0cnum_satoshis\x18\x03 \x01(\x03R\x0cnum_satoshis\x12\x1c\n\ttimestamp\x18\x04 \x01(\x03R\ttimestamp\x12\x16\n\x06\x65xpiry\x18\x05 \x01(\x03R\x06\x65xpiry\x12 \n\x0b\x64\x65scription\x18\x06 \x01(\tR\x0b\x64\x65scription\x12*\n\x10\x64\x65scription_hash\x18\x07 \x01(\tR\x10\x64\x65scription_hash\x12$\n\rfallback_addr\x18\x08 \x01(\tR\rfallback_addr\x12 \n\x0b\x63ltv_expiry\x18\t \x01(\x03R\x0b\x63ltv_expiry\x12\x32\n\x0broute_hints\x18\n \x03(\x0b\x32\x10.lnrpc.RouteHintR\x0broute_hints\"\x12\n\x10\x46\x65\x65ReportRequest\"\x99\x01\n\x10\x43hannelFeeReport\x12!\n\nchan_point\x18\x01 \x01(\tR\rchannel_point\x12$\n\rbase_fee_msat\x18\x02 \x01(\x03R\rbase_fee_msat\x12 \n\x0b\x66\x65\x65_per_mil\x18\x03 \x01(\x03R\x0b\x66\x65\x65_per_mil\x12\x1a\n\x08\x66\x65\x65_rate\x18\x04 \x01(\x01R\x08\x66\x65\x65_rate\"\xbc\x01\n\x11\x46\x65\x65ReportResponse\x12;\n\x0c\x63hannel_fees\x18\x01 \x03(\x0b\x32\x17.lnrpc.ChannelFeeReportR\x0c\x63hannel_fees\x12 \n\x0b\x64\x61y_fee_sum\x18\x02 \x01(\x04R\x0b\x64\x61y_fee_sum\x12\"\n\x0cweek_fee_sum\x18\x03 \x01(\x04R\x0cweek_fee_sum\x12$\n\rmonth_fee_sum\x18\x04 \x01(\x04R\rmonth_fee_sum\"\xdb\x01\n\x13PolicyUpdateRequest\x12\x18\n\x06global\x18\x01 \x01(\x08H\x00R\x06global\x12\x35\n\nchan_point\x18\x02 \x01(\x0b\x32\x13.lnrpc.ChannelPointH\x00R\nchan_point\x12$\n\rbase_fee_msat\x18\x03 \x01(\x03R\rbase_fee_msat\x12\x1a\n\x08\x66\x65\x65_rate\x18\x04 \x01(\x01R\x08\x66\x65\x65_rate\x12(\n\x0ftime_lock_delta\x18\x05 \x01(\rR\x0ftime_lock_deltaB\x07\n\x05scope\"\x16\n\x14PolicyUpdateResponse\"\xa2\x01\n\x18\x46orwardingHistoryRequest\x12\x1e\n\nstart_time\x18\x01 \x01(\x04R\nstart_time\x12\x1a\n\x08\x65nd_time\x18\x02 \x01(\x04R\x08\x65nd_time\x12\"\n\x0cindex_offset\x18\x03 \x01(\rR\x0cindex_offset\x12&\n\x0enum_max_events\x18\x04 \x01(\rR\x0enum_max_events\"\xb5\x01\n\x0f\x46orwardingEvent\x12\x1c\n\ttimestamp\x18\x01 \x01(\x04R\ttimestamp\x12\x1e\n\nchan_id_in\x18\x02 \x01(\x04R\nchan_id_in\x12 \n\x0b\x63han_id_out\x18\x04 \x01(\x04R\x0b\x63han_id_out\x12\x16\n\x06\x61mt_in\x18\x05 \x01(\x04R\x06\x61mt_in\x12\x18\n\x07\x61mt_out\x18\x06 \x01(\x04R\x07\x61mt_out\x12\x10\n\x03\x66\x65\x65\x18\x07 \x01(\x04R\x03\x66\x65\x65\"\x8f\x01\n\x19\x46orwardingHistoryResponse\x12\x44\n\x11\x66orwarding_events\x18\x01 \x03(\x0b\x32\x16.lnrpc.ForwardingEventR\x11\x66orwarding_events\x12,\n\x11last_offset_index\x18\x02 \x01(\rR\x11last_offset_index2\x91\x03\n\x0eWalletUnlocker\x12M\n\x07GenSeed\x12\x15.lnrpc.GenSeedRequest\x1a\x16.lnrpc.GenSeedResponse\"\x13\x82\xd3\xe4\x93\x02\r\x12\x0b/v1/genseed\x12\\\n\nInitWallet\x12\x18.lnrpc.InitWalletRequest\x1a\x19.lnrpc.InitWalletResponse\"\x19\x82\xd3\xe4\x93\x02\x13\"\x0e/v1/initwallet:\x01*\x12\x64\n\x0cUnlockWallet\x12\x1a.lnrpc.UnlockWalletRequest\x1a\x1b.lnrpc.UnlockWalletResponse\"\x1b\x82\xd3\xe4\x93\x02\x15\"\x10/v1/unlockwallet:\x01*\x12l\n\x0e\x43hangePassword\x12\x1c.lnrpc.ChangePasswordRequest\x1a\x1d.lnrpc.ChangePasswordResponse\"\x1d\x82\xd3\xe4\x93\x02\x17\"\x12/v1/changepassword:\x01*2\xdb\x1e\n\tLightning\x12j\n\rWalletBalance\x12\x1b.lnrpc.WalletBalanceRequest\x1a\x1c.lnrpc.WalletBalanceResponse\"\x1e\x82\xd3\xe4\x93\x02\x18\x12\x16/v1/balance/blockchain\x12k\n\x0e\x43hannelBalance\x12\x1c.lnrpc.ChannelBalanceRequest\x1a\x1d.lnrpc.ChannelBalanceResponse\"\x1c\x82\xd3\xe4\x93\x02\x16\x12\x14/v1/balance/channels\x12\x65\n\x0fGetTransactions\x12\x1d.lnrpc.GetTransactionsRequest\x1a\x19.lnrpc.TransactionDetails\"\x18\x82\xd3\xe4\x93\x02\x12\x12\x10/v1/transactions\x12[\n\tSendCoins\x12\x17.lnrpc.SendCoinsRequest\x1a\x18.lnrpc.SendCoinsResponse\"\x1b\x82\xd3\xe4\x93\x02\x15\"\x10/v1/transactions:\x01*\x12L\n\x15SubscribeTransactions\x12\x1d.lnrpc.GetTransactionsRequest\x1a\x12.lnrpc.Transaction0\x01\x12;\n\x08SendMany\x12\x16.lnrpc.SendManyRequest\x1a\x17.lnrpc.SendManyResponse\x12Y\n\nNewAddress\x12\x18.lnrpc.NewAddressRequest\x1a\x19.lnrpc.NewAddressResponse\"\x16\x82\xd3\xe4\x93\x02\x10\x12\x0e/v1/newaddress\x12\x44\n\x0bSignMessage\x12\x19.lnrpc.SignMessageRequest\x1a\x1a.lnrpc.SignMessageResponse\x12J\n\rVerifyMessage\x12\x1b.lnrpc.VerifyMessageRequest\x1a\x1c.lnrpc.VerifyMessageResponse\x12Z\n\x0b\x43onnectPeer\x12\x19.lnrpc.ConnectPeerRequest\x1a\x1a.lnrpc.ConnectPeerResponse\"\x14\x82\xd3\xe4\x93\x02\x0e\"\t/v1/peers:\x01*\x12j\n\x0e\x44isconnectPeer\x12\x1c.lnrpc.DisconnectPeerRequest\x1a\x1d.lnrpc.DisconnectPeerResponse\"\x1b\x82\xd3\xe4\x93\x02\x15*\x13/v1/peers/{pub_key}\x12Q\n\tListPeers\x12\x17.lnrpc.ListPeersRequest\x1a\x18.lnrpc.ListPeersResponse\"\x11\x82\xd3\xe4\x93\x02\x0b\x12\t/v1/peers\x12M\n\x07GetInfo\x12\x15.lnrpc.GetInfoRequest\x1a\x16.lnrpc.GetInfoResponse\"\x13\x82\xd3\xe4\x93\x02\r\x12\x0b/v1/getinfo\x12n\n\x0fPendingChannels\x12\x1d.lnrpc.PendingChannelsRequest\x1a\x1e.lnrpc.PendingChannelsResponse\"\x1c\x82\xd3\xe4\x93\x02\x16\x12\x14/v1/channels/pending\x12]\n\x0cListChannels\x12\x1a.lnrpc.ListChannelsRequest\x1a\x1b.lnrpc.ListChannelsResponse\"\x14\x82\xd3\xe4\x93\x02\x0e\x12\x0c/v1/channels\x12j\n\x0e\x43losedChannels\x12\x1c.lnrpc.ClosedChannelsRequest\x1a\x1d.lnrpc.ClosedChannelsResponse\"\x1b\x82\xd3\xe4\x93\x02\x15\x12\x13/v1/channels/closed\x12Z\n\x0fOpenChannelSync\x12\x19.lnrpc.OpenChannelRequest\x1a\x13.lnrpc.ChannelPoint\"\x17\x82\xd3\xe4\x93\x02\x11\"\x0c/v1/channels:\x01*\x12\x43\n\x0bOpenChannel\x12\x19.lnrpc.OpenChannelRequest\x1a\x17.lnrpc.OpenStatusUpdate0\x01\x12\x9a\x01\n\x0c\x43loseChannel\x12\x1a.lnrpc.CloseChannelRequest\x1a\x18.lnrpc.CloseStatusUpdate\"R\x82\xd3\xe4\x93\x02L*J/v1/channels/{channel_point.funding_txid_str}/{channel_point.output_index}0\x01\x12\xa9\x01\n\x0e\x41\x62\x61ndonChannel\x12\x1c.lnrpc.AbandonChannelRequest\x1a\x1d.lnrpc.AbandonChannelResponse\"Z\x82\xd3\xe4\x93\x02T*R/v1/channels/abandon/{channel_point.funding_txid_str}/{channel_point.output_index}\x12:\n\x0bSendPayment\x12\x12.lnrpc.SendRequest\x1a\x13.lnrpc.SendResponse(\x01\x30\x01\x12`\n\x0fSendPaymentSync\x12\x12.lnrpc.SendRequest\x1a\x13.lnrpc.SendResponse\"$\x82\xd3\xe4\x93\x02\x1e\"\x19/v1/channels/transactions:\x01*\x12\x41\n\x0bSendToRoute\x12\x19.lnrpc.SendToRouteRequest\x1a\x13.lnrpc.SendResponse(\x01\x30\x01\x12m\n\x0fSendToRouteSync\x12\x19.lnrpc.SendToRouteRequest\x1a\x13.lnrpc.SendResponse\"*\x82\xd3\xe4\x93\x02$\"\x1f/v1/channels/transactions/route:\x01*\x12P\n\nAddInvoice\x12\x0e.lnrpc.Invoice\x1a\x19.lnrpc.AddInvoiceResponse\"\x17\x82\xd3\xe4\x93\x02\x11\"\x0c/v1/invoices:\x01*\x12[\n\x0cListInvoices\x12\x19.lnrpc.ListInvoiceRequest\x1a\x1a.lnrpc.ListInvoiceResponse\"\x14\x82\xd3\xe4\x93\x02\x0e\x12\x0c/v1/invoices\x12U\n\rLookupInvoice\x12\x12.lnrpc.PaymentHash\x1a\x0e.lnrpc.Invoice\" \x82\xd3\xe4\x93\x02\x1a\x12\x18/v1/invoice/{r_hash_str}\x12\x61\n\x11SubscribeInvoices\x12\x1a.lnrpc.InvoiceSubscription\x1a\x0e.lnrpc.Invoice\"\x1e\x82\xd3\xe4\x93\x02\x18\x12\x16/v1/invoices/subscribe0\x01\x12P\n\x0c\x44\x65\x63odePayReq\x12\x13.lnrpc.PayReqString\x1a\r.lnrpc.PayReq\"\x1c\x82\xd3\xe4\x93\x02\x16\x12\x14/v1/payreq/{pay_req}\x12]\n\x0cListPayments\x12\x1a.lnrpc.ListPaymentsRequest\x1a\x1b.lnrpc.ListPaymentsResponse\"\x14\x82\xd3\xe4\x93\x02\x0e\x12\x0c/v1/payments\x12l\n\x11\x44\x65leteAllPayments\x12\x1f.lnrpc.DeleteAllPaymentsRequest\x1a .lnrpc.DeleteAllPaymentsResponse\"\x14\x82\xd3\xe4\x93\x02\x0e*\x0c/v1/payments\x12S\n\rDescribeGraph\x12\x1a.lnrpc.ChannelGraphRequest\x1a\x13.lnrpc.ChannelGraph\"\x11\x82\xd3\xe4\x93\x02\x0b\x12\t/v1/graph\x12[\n\x0bGetChanInfo\x12\x16.lnrpc.ChanInfoRequest\x1a\x12.lnrpc.ChannelEdge\" \x82\xd3\xe4\x93\x02\x1a\x12\x18/v1/graph/edge/{chan_id}\x12X\n\x0bGetNodeInfo\x12\x16.lnrpc.NodeInfoRequest\x1a\x0f.lnrpc.NodeInfo\" \x82\xd3\xe4\x93\x02\x1a\x12\x18/v1/graph/node/{pub_key}\x12n\n\x0bQueryRoutes\x12\x19.lnrpc.QueryRoutesRequest\x1a\x1a.lnrpc.QueryRoutesResponse\"(\x82\xd3\xe4\x93\x02\"\x12 /v1/graph/routes/{pub_key}/{amt}\x12W\n\x0eGetNetworkInfo\x12\x19.lnrpc.NetworkInfoRequest\x1a\x12.lnrpc.NetworkInfo\"\x16\x82\xd3\xe4\x93\x02\x10\x12\x0e/v1/graph/info\x12\x35\n\nStopDaemon\x12\x12.lnrpc.StopRequest\x1a\x13.lnrpc.StopResponse\x12W\n\x15SubscribeChannelGraph\x12 .lnrpc.GraphTopologySubscription\x1a\x1a.lnrpc.GraphTopologyUpdate0\x01\x12\x41\n\nDebugLevel\x12\x18.lnrpc.DebugLevelRequest\x1a\x19.lnrpc.DebugLevelResponse\x12P\n\tFeeReport\x12\x17.lnrpc.FeeReportRequest\x1a\x18.lnrpc.FeeReportResponse\"\x10\x82\xd3\xe4\x93\x02\n\x12\x08/v1/fees\x12i\n\x13UpdateChannelPolicy\x12\x1a.lnrpc.PolicyUpdateRequest\x1a\x1b.lnrpc.PolicyUpdateResponse\"\x19\x82\xd3\xe4\x93\x02\x13\"\x0e/v1/chanpolicy:\x01*\x12m\n\x11\x46orwardingHistory\x12\x1f.lnrpc.ForwardingHistoryRequest\x1a .lnrpc.ForwardingHistoryResponse\"\x15\x82\xd3\xe4\x93\x02\x0f\"\n/v1/switch:\x01*b\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,])



_NEWADDRESSREQUEST_ADDRESSTYPE = _descriptor.EnumDescriptor(
  name='AddressType',
  full_name='lnrpc.NewAddressRequest.AddressType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='WITNESS_PUBKEY_HASH', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NESTED_PUBKEY_HASH', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=2095,
  serialized_end=2157,
)
_sym_db.RegisterEnumDescriptor(_NEWADDRESSREQUEST_ADDRESSTYPE)

_CHANNELCLOSESUMMARY_CLOSURETYPE = _descriptor.EnumDescriptor(
  name='ClosureType',
  full_name='lnrpc.ChannelCloseSummary.ClosureType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='COOPERATIVE_CLOSE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOCAL_FORCE_CLOSE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REMOTE_FORCE_CLOSE', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BREACH_CLOSE', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FUNDING_CANCELED', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ABANDONED', index=5, number=5,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=4003,
  serialized_end=4141,
)
_sym_db.RegisterEnumDescriptor(_CHANNELCLOSESUMMARY_CLOSURETYPE)


_GENSEEDREQUEST = _descriptor.Descriptor(
  name='GenSeedRequest',
  full_name='lnrpc.GenSeedRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='aezeed_passphrase', full_name='lnrpc.GenSeedRequest.aezeed_passphrase', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='seed_entropy', full_name='lnrpc.GenSeedRequest.seed_entropy', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=50,
  serialized_end=115,
)


_GENSEEDRESPONSE = _descriptor.Descriptor(
  name='GenSeedResponse',
  full_name='lnrpc.GenSeedResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cipher_seed_mnemonic', full_name='lnrpc.GenSeedResponse.cipher_seed_mnemonic', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enciphered_seed', full_name='lnrpc.GenSeedResponse.enciphered_seed', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=117,
  serialized_end=189,
)


_INITWALLETREQUEST = _descriptor.Descriptor(
  name='InitWalletRequest',
  full_name='lnrpc.InitWalletRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='wallet_password', full_name='lnrpc.InitWalletRequest.wallet_password', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cipher_seed_mnemonic', full_name='lnrpc.InitWalletRequest.cipher_seed_mnemonic', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='aezeed_passphrase', full_name='lnrpc.InitWalletRequest.aezeed_passphrase', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='recovery_window', full_name='lnrpc.InitWalletRequest.recovery_window', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=191,
  serialized_end=317,
)


_INITWALLETRESPONSE = _descriptor.Descriptor(
  name='InitWalletResponse',
  full_name='lnrpc.InitWalletResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=319,
  serialized_end=339,
)


_UNLOCKWALLETREQUEST = _descriptor.Descriptor(
  name='UnlockWalletRequest',
  full_name='lnrpc.UnlockWalletRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='wallet_password', full_name='lnrpc.UnlockWalletRequest.wallet_password', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='recovery_window', full_name='lnrpc.UnlockWalletRequest.recovery_window', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=341,
  serialized_end=412,
)


_UNLOCKWALLETRESPONSE = _descriptor.Descriptor(
  name='UnlockWalletResponse',
  full_name='lnrpc.UnlockWalletResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=414,
  serialized_end=436,
)


_CHANGEPASSWORDREQUEST = _descriptor.Descriptor(
  name='ChangePasswordRequest',
  full_name='lnrpc.ChangePasswordRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='current_password', full_name='lnrpc.ChangePasswordRequest.current_password', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='new_password', full_name='lnrpc.ChangePasswordRequest.new_password', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=438,
  serialized_end=509,
)


_CHANGEPASSWORDRESPONSE = _descriptor.Descriptor(
  name='ChangePasswordResponse',
  full_name='lnrpc.ChangePasswordResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=511,
  serialized_end=535,
)


_TRANSACTION = _descriptor.Descriptor(
  name='Transaction',
  full_name='lnrpc.Transaction',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tx_hash', full_name='lnrpc.Transaction.tx_hash', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='tx_hash', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='lnrpc.Transaction.amount', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='amount', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_confirmations', full_name='lnrpc.Transaction.num_confirmations', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='num_confirmations', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='block_hash', full_name='lnrpc.Transaction.block_hash', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='block_hash', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='block_height', full_name='lnrpc.Transaction.block_height', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='block_height', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time_stamp', full_name='lnrpc.Transaction.time_stamp', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='time_stamp', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_fees', full_name='lnrpc.Transaction.total_fees', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='total_fees', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dest_addresses', full_name='lnrpc.Transaction.dest_addresses', index=7,
      number=8, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='dest_addresses', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=538,
  serialized_end=819,
)


_GETTRANSACTIONSREQUEST = _descriptor.Descriptor(
  name='GetTransactionsRequest',
  full_name='lnrpc.GetTransactionsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=821,
  serialized_end=845,
)


_TRANSACTIONDETAILS = _descriptor.Descriptor(
  name='TransactionDetails',
  full_name='lnrpc.TransactionDetails',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='transactions', full_name='lnrpc.TransactionDetails.transactions', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='transactions', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=847,
  serialized_end=923,
)


_FEELIMIT = _descriptor.Descriptor(
  name='FeeLimit',
  full_name='lnrpc.FeeLimit',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fixed', full_name='lnrpc.FeeLimit.fixed', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='percent', full_name='lnrpc.FeeLimit.percent', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='limit', full_name='lnrpc.FeeLimit.limit',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=925,
  serialized_end=980,
)


_SENDREQUEST = _descriptor.Descriptor(
  name='SendRequest',
  full_name='lnrpc.SendRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dest', full_name='lnrpc.SendRequest.dest', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='dest_string', full_name='lnrpc.SendRequest.dest_string', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amt', full_name='lnrpc.SendRequest.amt', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payment_hash', full_name='lnrpc.SendRequest.payment_hash', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payment_hash_string', full_name='lnrpc.SendRequest.payment_hash_string', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payment_request', full_name='lnrpc.SendRequest.payment_request', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='final_cltv_delta', full_name='lnrpc.SendRequest.final_cltv_delta', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fee_limit', full_name='lnrpc.SendRequest.fee_limit', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=983,
  serialized_end=1182,
)


_SENDRESPONSE = _descriptor.Descriptor(
  name='SendResponse',
  full_name='lnrpc.SendResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='payment_error', full_name='lnrpc.SendResponse.payment_error', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='payment_error', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payment_preimage', full_name='lnrpc.SendResponse.payment_preimage', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='payment_preimage', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payment_route', full_name='lnrpc.SendResponse.payment_route', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='payment_route', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1185,
  serialized_end=1333,
)


_SENDTOROUTEREQUEST = _descriptor.Descriptor(
  name='SendToRouteRequest',
  full_name='lnrpc.SendToRouteRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='payment_hash', full_name='lnrpc.SendToRouteRequest.payment_hash', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payment_hash_string', full_name='lnrpc.SendToRouteRequest.payment_hash_string', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='routes', full_name='lnrpc.SendToRouteRequest.routes', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1335,
  serialized_end=1436,
)


_CHANNELPOINT = _descriptor.Descriptor(
  name='ChannelPoint',
  full_name='lnrpc.ChannelPoint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='funding_txid_bytes', full_name='lnrpc.ChannelPoint.funding_txid_bytes', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='funding_txid_bytes', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='funding_txid_str', full_name='lnrpc.ChannelPoint.funding_txid_str', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='funding_txid_str', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='output_index', full_name='lnrpc.ChannelPoint.output_index', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='output_index', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='funding_txid', full_name='lnrpc.ChannelPoint.funding_txid',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=1439,
  serialized_end=1601,
)


_LIGHTNINGADDRESS = _descriptor.Descriptor(
  name='LightningAddress',
  full_name='lnrpc.LightningAddress',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pubkey', full_name='lnrpc.LightningAddress.pubkey', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='pubkey', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='host', full_name='lnrpc.LightningAddress.host', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='host', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1603,
  serialized_end=1665,
)


_SENDMANYREQUEST_ADDRTOAMOUNTENTRY = _descriptor.Descriptor(
  name='AddrToAmountEntry',
  full_name='lnrpc.SendManyRequest.AddrToAmountEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='lnrpc.SendManyRequest.AddrToAmountEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='lnrpc.SendManyRequest.AddrToAmountEntry.value', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1794,
  serialized_end=1845,
)

_SENDMANYREQUEST = _descriptor.Descriptor(
  name='SendManyRequest',
  full_name='lnrpc.SendManyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='AddrToAmount', full_name='lnrpc.SendManyRequest.AddrToAmount', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='target_conf', full_name='lnrpc.SendManyRequest.target_conf', index=1,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sat_per_byte', full_name='lnrpc.SendManyRequest.sat_per_byte', index=2,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_SENDMANYREQUEST_ADDRTOAMOUNTENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1668,
  serialized_end=1845,
)


_SENDMANYRESPONSE = _descriptor.Descriptor(
  name='SendManyResponse',
  full_name='lnrpc.SendManyResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='txid', full_name='lnrpc.SendManyResponse.txid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='txid', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1847,
  serialized_end=1885,
)


_SENDCOINSREQUEST = _descriptor.Descriptor(
  name='SendCoinsRequest',
  full_name='lnrpc.SendCoinsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='addr', full_name='lnrpc.SendCoinsRequest.addr', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='lnrpc.SendCoinsRequest.amount', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='target_conf', full_name='lnrpc.SendCoinsRequest.target_conf', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sat_per_byte', full_name='lnrpc.SendCoinsRequest.sat_per_byte', index=3,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1887,
  serialized_end=1978,
)


_SENDCOINSRESPONSE = _descriptor.Descriptor(
  name='SendCoinsResponse',
  full_name='lnrpc.SendCoinsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='txid', full_name='lnrpc.SendCoinsResponse.txid', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='txid', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1980,
  serialized_end=2019,
)


_NEWADDRESSREQUEST = _descriptor.Descriptor(
  name='NewAddressRequest',
  full_name='lnrpc.NewAddressRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='lnrpc.NewAddressRequest.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _NEWADDRESSREQUEST_ADDRESSTYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=2022,
  serialized_end=2157,
)


_NEWADDRESSRESPONSE = _descriptor.Descriptor(
  name='NewAddressResponse',
  full_name='lnrpc.NewAddressResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='address', full_name='lnrpc.NewAddressResponse.address', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='address', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=2159,
  serialized_end=2205,
)


_SIGNMESSAGEREQUEST = _descriptor.Descriptor(
  name='SignMessageRequest',
  full_name='lnrpc.SignMessageRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='msg', full_name='lnrpc.SignMessageRequest.msg', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='msg', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=2207,
  serialized_end=2245,
)


_SIGNMESSAGERESPONSE = _descriptor.Descriptor(
  name='SignMessageResponse',
  full_name='lnrpc.SignMessageResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='signature', full_name='lnrpc.SignMessageResponse.signature', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='signature', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=2247,
  serialized_end=2298,
)


_VERIFYMESSAGEREQUEST = _descriptor.Descriptor(
  name='VerifyMessageRequest',
  full_name='lnrpc.VerifyMessageRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='msg', full_name='lnrpc.VerifyMessageRequest.msg', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='msg', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='signature', full_name='lnrpc.VerifyMessageRequest.signature', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='signature', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=2300,
  serialized_end=2370,
)


_VERIFYMESSAGERESPONSE = _descriptor.Descriptor(
  name='VerifyMessageResponse',
  full_name='lnrpc.VerifyMessageResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='valid', full_name='lnrpc.VerifyMessageResponse.valid', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='valid', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pubkey', full_name='lnrpc.VerifyMessageResponse.pubkey', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='pubkey', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=2372,
  serialized_end=2441,
)


_CONNECTPEERREQUEST = _descriptor.Descriptor(
  name='ConnectPeerRequest',
  full_name='lnrpc.ConnectPeerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='addr', full_name='lnrpc.ConnectPeerRequest.addr', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='perm', full_name='lnrpc.ConnectPeerRequest.perm', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=2443,
  serialized_end=2516,
)


_CONNECTPEERRESPONSE = _descriptor.Descriptor(
  name='ConnectPeerResponse',
  full_name='lnrpc.ConnectPeerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=2518,
  serialized_end=2539,
)


_DISCONNECTPEERREQUEST = _descriptor.Descriptor(
  name='DisconnectPeerRequest',
  full_name='lnrpc.DisconnectPeerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pub_key', full_name='lnrpc.DisconnectPeerRequest.pub_key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='pub_key', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=2541,
  serialized_end=2590,
)


_DISCONNECTPEERRESPONSE = _descriptor.Descriptor(
  name='DisconnectPeerResponse',
  full_name='lnrpc.DisconnectPeerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=2592,
  serialized_end=2616,
)


_HTLC = _descriptor.Descriptor(
  name='HTLC',
  full_name='lnrpc.HTLC',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='incoming', full_name='lnrpc.HTLC.incoming', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='incoming', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='lnrpc.HTLC.amount', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='amount', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hash_lock', full_name='lnrpc.HTLC.hash_lock', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='hash_lock', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='expiration_height', full_name='lnrpc.HTLC.expiration_height', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='expiration_height', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=2619,
  serialized_end=2753,
)


_CHANNEL = _descriptor.Descriptor(
  name='Channel',
  full_name='lnrpc.Channel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='active', full_name='lnrpc.Channel.active', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='active', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='remote_pubkey', full_name='lnrpc.Channel.remote_pubkey', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='remote_pubkey', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='channel_point', full_name='lnrpc.Channel.channel_point', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='channel_point', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chan_id', full_name='lnrpc.Channel.chan_id', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='chan_id', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='capacity', full_name='lnrpc.Channel.capacity', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='capacity', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='local_balance', full_name='lnrpc.Channel.local_balance', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='local_balance', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='remote_balance', full_name='lnrpc.Channel.remote_balance', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='remote_balance', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='commit_fee', full_name='lnrpc.Channel.commit_fee', index=7,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='commit_fee', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='commit_weight', full_name='lnrpc.Channel.commit_weight', index=8,
      number=9, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='commit_weight', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fee_per_kw', full_name='lnrpc.Channel.fee_per_kw', index=9,
      number=10, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='fee_per_kw', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unsettled_balance', full_name='lnrpc.Channel.unsettled_balance', index=10,
      number=11, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='unsettled_balance', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_satoshis_sent', full_name='lnrpc.Channel.total_satoshis_sent', index=11,
      number=12, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='total_satoshis_sent', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_satoshis_received', full_name='lnrpc.Channel.total_satoshis_received', index=12,
      number=13, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='total_satoshis_received', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_updates', full_name='lnrpc.Channel.num_updates', index=13,
      number=14, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='num_updates', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pending_htlcs', full_name='lnrpc.Channel.pending_htlcs', index=14,
      number=15, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='pending_htlcs', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='csv_delay', full_name='lnrpc.Channel.csv_delay', index=15,
      number=16, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='csv_delay', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='private', full_name='lnrpc.Channel.private', index=16,
      number=17, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='private', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=2756,
  serialized_end=3394,
)


_LISTCHANNELSREQUEST = _descriptor.Descriptor(
  name='ListChannelsRequest',
  full_name='lnrpc.ListChannelsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='active_only', full_name='lnrpc.ListChannelsRequest.active_only', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='inactive_only', full_name='lnrpc.ListChannelsRequest.inactive_only', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='public_only', full_name='lnrpc.ListChannelsRequest.public_only', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='private_only', full_name='lnrpc.ListChannelsRequest.private_only', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=3396,
  serialized_end=3504,
)


_LISTCHANNELSRESPONSE = _descriptor.Descriptor(
  name='ListChannelsResponse',
  full_name='lnrpc.ListChannelsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='channels', full_name='lnrpc.ListChannelsResponse.channels', index=0,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='channels', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=3506,
  serialized_end=3572,
)


_CHANNELCLOSESUMMARY = _descriptor.Descriptor(
  name='ChannelCloseSummary',
  full_name='lnrpc.ChannelCloseSummary',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='channel_point', full_name='lnrpc.ChannelCloseSummary.channel_point', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='channel_point', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chan_id', full_name='lnrpc.ChannelCloseSummary.chan_id', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='chan_id', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chain_hash', full_name='lnrpc.ChannelCloseSummary.chain_hash', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='chain_hash', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='closing_tx_hash', full_name='lnrpc.ChannelCloseSummary.closing_tx_hash', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='closing_tx_hash', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='remote_pubkey', full_name='lnrpc.ChannelCloseSummary.remote_pubkey', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='remote_pubkey', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='capacity', full_name='lnrpc.ChannelCloseSummary.capacity', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='capacity', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='close_height', full_name='lnrpc.ChannelCloseSummary.close_height', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='close_height', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='settled_balance', full_name='lnrpc.ChannelCloseSummary.settled_balance', index=7,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='settled_balance', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time_locked_balance', full_name='lnrpc.ChannelCloseSummary.time_locked_balance', index=8,
      number=9, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='time_locked_balance', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='close_type', full_name='lnrpc.ChannelCloseSummary.close_type', index=9,
      number=10, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='close_type', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _CHANNELCLOSESUMMARY_CLOSURETYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=3575,
  serialized_end=4141,
)


_CLOSEDCHANNELSREQUEST = _descriptor.Descriptor(
  name='ClosedChannelsRequest',
  full_name='lnrpc.ClosedChannelsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cooperative', full_name='lnrpc.ClosedChannelsRequest.cooperative', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='local_force', full_name='lnrpc.ClosedChannelsRequest.local_force', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='remote_force', full_name='lnrpc.ClosedChannelsRequest.remote_force', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='breach', full_name='lnrpc.ClosedChannelsRequest.breach', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='funding_canceled', full_name='lnrpc.ClosedChannelsRequest.funding_canceled', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='abandoned', full_name='lnrpc.ClosedChannelsRequest.abandoned', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=4144,
  serialized_end=4292,
)


_CLOSEDCHANNELSRESPONSE = _descriptor.Descriptor(
  name='ClosedChannelsResponse',
  full_name='lnrpc.ClosedChannelsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='channels', full_name='lnrpc.ClosedChannelsResponse.channels', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='channels', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=4294,
  serialized_end=4374,
)


_PEER = _descriptor.Descriptor(
  name='Peer',
  full_name='lnrpc.Peer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pub_key', full_name='lnrpc.Peer.pub_key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='pub_key', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='address', full_name='lnrpc.Peer.address', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='address', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bytes_sent', full_name='lnrpc.Peer.bytes_sent', index=2,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='bytes_sent', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bytes_recv', full_name='lnrpc.Peer.bytes_recv', index=3,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='bytes_recv', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sat_sent', full_name='lnrpc.Peer.sat_sent', index=4,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='sat_sent', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sat_recv', full_name='lnrpc.Peer.sat_recv', index=5,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='sat_recv', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='inbound', full_name='lnrpc.Peer.inbound', index=6,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='inbound', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ping_time', full_name='lnrpc.Peer.ping_time', index=7,
      number=9, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='ping_time', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=4377,
  serialized_end=4611,
)


_LISTPEERSREQUEST = _descriptor.Descriptor(
  name='ListPeersRequest',
  full_name='lnrpc.ListPeersRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=4613,
  serialized_end=4631,
)


_LISTPEERSRESPONSE = _descriptor.Descriptor(
  name='ListPeersResponse',
  full_name='lnrpc.ListPeersResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='peers', full_name='lnrpc.ListPeersResponse.peers', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='peers', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=4633,
  serialized_end=4687,
)


_GETINFOREQUEST = _descriptor.Descriptor(
  name='GetInfoRequest',
  full_name='lnrpc.GetInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=4689,
  serialized_end=4705,
)


_GETINFORESPONSE = _descriptor.Descriptor(
  name='GetInfoResponse',
  full_name='lnrpc.GetInfoResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='identity_pubkey', full_name='lnrpc.GetInfoResponse.identity_pubkey', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='identity_pubkey', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='alias', full_name='lnrpc.GetInfoResponse.alias', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='alias', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_pending_channels', full_name='lnrpc.GetInfoResponse.num_pending_channels', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='num_pending_channels', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_active_channels', full_name='lnrpc.GetInfoResponse.num_active_channels', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='num_active_channels', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_peers', full_name='lnrpc.GetInfoResponse.num_peers', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='num_peers', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='block_height', full_name='lnrpc.GetInfoResponse.block_height', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='block_height', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='block_hash', full_name='lnrpc.GetInfoResponse.block_hash', index=6,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='block_hash', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='synced_to_chain', full_name='lnrpc.GetInfoResponse.synced_to_chain', index=7,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='synced_to_chain', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='testnet', full_name='lnrpc.GetInfoResponse.testnet', index=8,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='testnet', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chains', full_name='lnrpc.GetInfoResponse.chains', index=9,
      number=11, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='chains', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uris', full_name='lnrpc.GetInfoResponse.uris', index=10,
      number=12, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='uris', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='best_header_timestamp', full_name='lnrpc.GetInfoResponse.best_header_timestamp', index=11,
      number=13, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='best_header_timestamp', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='lnrpc.GetInfoResponse.version', index=12,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='version', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_inactive_channels', full_name='lnrpc.GetInfoResponse.num_inactive_channels', index=13,
      number=15, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='num_inactive_channels', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=4708,
  serialized_end=5235,
)


_CONFIRMATIONUPDATE = _descriptor.Descriptor(
  name='ConfirmationUpdate',
  full_name='lnrpc.ConfirmationUpdate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='block_sha', full_name='lnrpc.ConfirmationUpdate.block_sha', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='block_height', full_name='lnrpc.ConfirmationUpdate.block_height', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_confs_left', full_name='lnrpc.ConfirmationUpdate.num_confs_left', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=5237,
  serialized_end=5322,
)


_CHANNELOPENUPDATE = _descriptor.Descriptor(
  name='ChannelOpenUpdate',
  full_name='lnrpc.ChannelOpenUpdate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='channel_point', full_name='lnrpc.ChannelOpenUpdate.channel_point', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='channel_point', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=5324,
  serialized_end=5402,
)


_CHANNELCLOSEUPDATE = _descriptor.Descriptor(
  name='ChannelCloseUpdate',
  full_name='lnrpc.ChannelCloseUpdate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='closing_txid', full_name='lnrpc.ChannelCloseUpdate.closing_txid', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='closing_txid', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='success', full_name='lnrpc.ChannelCloseUpdate.success', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='success', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=5404,
  serialized_end=5486,
)


_CLOSECHANNELREQUEST = _descriptor.Descriptor(
  name='CloseChannelRequest',
  full_name='lnrpc.CloseChannelRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='channel_point', full_name='lnrpc.CloseChannelRequest.channel_point', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='force', full_name='lnrpc.CloseChannelRequest.force', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='target_conf', full_name='lnrpc.CloseChannelRequest.target_conf', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sat_per_byte', full_name='lnrpc.CloseChannelRequest.sat_per_byte', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=5488,
  serialized_end=5611,
)


_CLOSESTATUSUPDATE = _descriptor.Descriptor(
  name='CloseStatusUpdate',
  full_name='lnrpc.CloseStatusUpdate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='close_pending', full_name='lnrpc.CloseStatusUpdate.close_pending', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='close_pending', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='confirmation', full_name='lnrpc.CloseStatusUpdate.confirmation', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='confirmation', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chan_close', full_name='lnrpc.CloseStatusUpdate.chan_close', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='chan_close', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='update', full_name='lnrpc.CloseStatusUpdate.update',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=5614,
  serialized_end=5831,
)


_PENDINGUPDATE = _descriptor.Descriptor(
  name='PendingUpdate',
  full_name='lnrpc.PendingUpdate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='txid', full_name='lnrpc.PendingUpdate.txid', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='txid', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='output_index', full_name='lnrpc.PendingUpdate.output_index', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='output_index', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=5833,
  serialized_end=5904,
)


_OPENCHANNELREQUEST = _descriptor.Descriptor(
  name='OpenChannelRequest',
  full_name='lnrpc.OpenChannelRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='node_pubkey', full_name='lnrpc.OpenChannelRequest.node_pubkey', index=0,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='node_pubkey', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='node_pubkey_string', full_name='lnrpc.OpenChannelRequest.node_pubkey_string', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='node_pubkey_string', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='local_funding_amount', full_name='lnrpc.OpenChannelRequest.local_funding_amount', index=2,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='local_funding_amount', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='push_sat', full_name='lnrpc.OpenChannelRequest.push_sat', index=3,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='push_sat', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='target_conf', full_name='lnrpc.OpenChannelRequest.target_conf', index=4,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sat_per_byte', full_name='lnrpc.OpenChannelRequest.sat_per_byte', index=5,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='private', full_name='lnrpc.OpenChannelRequest.private', index=6,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='private', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='min_htlc_msat', full_name='lnrpc.OpenChannelRequest.min_htlc_msat', index=7,
      number=9, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='min_htlc_msat', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='remote_csv_delay', full_name='lnrpc.OpenChannelRequest.remote_csv_delay', index=8,
      number=10, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='remote_csv_delay', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='min_confs', full_name='lnrpc.OpenChannelRequest.min_confs', index=9,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='min_confs', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='spend_unconfirmed', full_name='lnrpc.OpenChannelRequest.spend_unconfirmed', index=10,
      number=12, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='spend_unconfirmed', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=5907,
  serialized_end=6316,
)


_OPENSTATUSUPDATE = _descriptor.Descriptor(
  name='OpenStatusUpdate',
  full_name='lnrpc.OpenStatusUpdate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='chan_pending', full_name='lnrpc.OpenStatusUpdate.chan_pending', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='chan_pending', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='confirmation', full_name='lnrpc.OpenStatusUpdate.confirmation', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='confirmation', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chan_open', full_name='lnrpc.OpenStatusUpdate.chan_open', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='chan_open', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='update', full_name='lnrpc.OpenStatusUpdate.update',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=6319,
  serialized_end=6530,
)


_PENDINGHTLC = _descriptor.Descriptor(
  name='PendingHTLC',
  full_name='lnrpc.PendingHTLC',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='incoming', full_name='lnrpc.PendingHTLC.incoming', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='incoming', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amount', full_name='lnrpc.PendingHTLC.amount', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='amount', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='outpoint', full_name='lnrpc.PendingHTLC.outpoint', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='outpoint', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='maturity_height', full_name='lnrpc.PendingHTLC.maturity_height', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='maturity_height', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='blocks_til_maturity', full_name='lnrpc.PendingHTLC.blocks_til_maturity', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='blocks_til_maturity', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stage', full_name='lnrpc.PendingHTLC.stage', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='stage', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=6533,
  serialized_end=6740,
)


_PENDINGCHANNELSREQUEST = _descriptor.Descriptor(
  name='PendingChannelsRequest',
  full_name='lnrpc.PendingChannelsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=6742,
  serialized_end=6766,
)


_PENDINGCHANNELSRESPONSE_PENDINGCHANNEL = _descriptor.Descriptor(
  name='PendingChannel',
  full_name='lnrpc.PendingChannelsResponse.PendingChannel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='remote_node_pub', full_name='lnrpc.PendingChannelsResponse.PendingChannel.remote_node_pub', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='remote_node_pub', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='channel_point', full_name='lnrpc.PendingChannelsResponse.PendingChannel.channel_point', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='channel_point', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='capacity', full_name='lnrpc.PendingChannelsResponse.PendingChannel.capacity', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='capacity', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='local_balance', full_name='lnrpc.PendingChannelsResponse.PendingChannel.local_balance', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='local_balance', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='remote_balance', full_name='lnrpc.PendingChannelsResponse.PendingChannel.remote_balance', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='remote_balance', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=7289,
  serialized_end=7491,
)

_PENDINGCHANNELSRESPONSE_PENDINGOPENCHANNEL = _descriptor.Descriptor(
  name='PendingOpenChannel',
  full_name='lnrpc.PendingChannelsResponse.PendingOpenChannel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='channel', full_name='lnrpc.PendingChannelsResponse.PendingOpenChannel.channel', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='channel', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='confirmation_height', full_name='lnrpc.PendingChannelsResponse.PendingOpenChannel.confirmation_height', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='confirmation_height', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='commit_fee', full_name='lnrpc.PendingChannelsResponse.PendingOpenChannel.commit_fee', index=2,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='commit_fee', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='commit_weight', full_name='lnrpc.PendingChannelsResponse.PendingOpenChannel.commit_weight', index=3,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='commit_weight', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fee_per_kw', full_name='lnrpc.PendingChannelsResponse.PendingOpenChannel.fee_per_kw', index=4,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='fee_per_kw', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=7494,
  serialized_end=7739,
)

_PENDINGCHANNELSRESPONSE_WAITINGCLOSECHANNEL = _descriptor.Descriptor(
  name='WaitingCloseChannel',
  full_name='lnrpc.PendingChannelsResponse.WaitingCloseChannel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='channel', full_name='lnrpc.PendingChannelsResponse.WaitingCloseChannel.channel', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='limbo_balance', full_name='lnrpc.PendingChannelsResponse.WaitingCloseChannel.limbo_balance', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='limbo_balance', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=7741,
  serialized_end=7864,
)

_PENDINGCHANNELSRESPONSE_CLOSEDCHANNEL = _descriptor.Descriptor(
  name='ClosedChannel',
  full_name='lnrpc.PendingChannelsResponse.ClosedChannel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='channel', full_name='lnrpc.PendingChannelsResponse.ClosedChannel.channel', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='closing_txid', full_name='lnrpc.PendingChannelsResponse.ClosedChannel.closing_txid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='closing_txid', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=7866,
  serialized_end=7981,
)

_PENDINGCHANNELSRESPONSE_FORCECLOSEDCHANNEL = _descriptor.Descriptor(
  name='ForceClosedChannel',
  full_name='lnrpc.PendingChannelsResponse.ForceClosedChannel',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='channel', full_name='lnrpc.PendingChannelsResponse.ForceClosedChannel.channel', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='channel', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='closing_txid', full_name='lnrpc.PendingChannelsResponse.ForceClosedChannel.closing_txid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='closing_txid', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='limbo_balance', full_name='lnrpc.PendingChannelsResponse.ForceClosedChannel.limbo_balance', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='limbo_balance', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='maturity_height', full_name='lnrpc.PendingChannelsResponse.ForceClosedChannel.maturity_height', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='maturity_height', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='blocks_til_maturity', full_name='lnrpc.PendingChannelsResponse.ForceClosedChannel.blocks_til_maturity', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='blocks_til_maturity', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='recovered_balance', full_name='lnrpc.PendingChannelsResponse.ForceClosedChannel.recovered_balance', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='recovered_balance', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pending_htlcs', full_name='lnrpc.PendingChannelsResponse.ForceClosedChannel.pending_htlcs', index=6,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='pending_htlcs', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=7984,
  serialized_end=8347,
)

_PENDINGCHANNELSRESPONSE = _descriptor.Descriptor(
  name='PendingChannelsResponse',
  full_name='lnrpc.PendingChannelsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='total_limbo_balance', full_name='lnrpc.PendingChannelsResponse.total_limbo_balance', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='total_limbo_balance', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pending_open_channels', full_name='lnrpc.PendingChannelsResponse.pending_open_channels', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='pending_open_channels', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pending_closing_channels', full_name='lnrpc.PendingChannelsResponse.pending_closing_channels', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='pending_closing_channels', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pending_force_closing_channels', full_name='lnrpc.PendingChannelsResponse.pending_force_closing_channels', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='pending_force_closing_channels', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='waiting_close_channels', full_name='lnrpc.PendingChannelsResponse.waiting_close_channels', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='waiting_close_channels', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_PENDINGCHANNELSRESPONSE_PENDINGCHANNEL, _PENDINGCHANNELSRESPONSE_PENDINGOPENCHANNEL, _PENDINGCHANNELSRESPONSE_WAITINGCLOSECHANNEL, _PENDINGCHANNELSRESPONSE_CLOSEDCHANNEL, _PENDINGCHANNELSRESPONSE_FORCECLOSEDCHANNEL, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=6769,
  serialized_end=8347,
)


_WALLETBALANCEREQUEST = _descriptor.Descriptor(
  name='WalletBalanceRequest',
  full_name='lnrpc.WalletBalanceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=8349,
  serialized_end=8371,
)


_WALLETBALANCERESPONSE = _descriptor.Descriptor(
  name='WalletBalanceResponse',
  full_name='lnrpc.WalletBalanceResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='total_balance', full_name='lnrpc.WalletBalanceResponse.total_balance', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='total_balance', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='confirmed_balance', full_name='lnrpc.WalletBalanceResponse.confirmed_balance', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='confirmed_balance', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unconfirmed_balance', full_name='lnrpc.WalletBalanceResponse.unconfirmed_balance', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='unconfirmed_balance', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=8374,
  serialized_end=8531,
)


_CHANNELBALANCEREQUEST = _descriptor.Descriptor(
  name='ChannelBalanceRequest',
  full_name='lnrpc.ChannelBalanceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=8533,
  serialized_end=8556,
)


_CHANNELBALANCERESPONSE = _descriptor.Descriptor(
  name='ChannelBalanceResponse',
  full_name='lnrpc.ChannelBalanceResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='balance', full_name='lnrpc.ChannelBalanceResponse.balance', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='balance', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pending_open_balance', full_name='lnrpc.ChannelBalanceResponse.pending_open_balance', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='pending_open_balance', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=8558,
  serialized_end=8660,
)


_QUERYROUTESREQUEST = _descriptor.Descriptor(
  name='QueryRoutesRequest',
  full_name='lnrpc.QueryRoutesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pub_key', full_name='lnrpc.QueryRoutesRequest.pub_key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amt', full_name='lnrpc.QueryRoutesRequest.amt', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_routes', full_name='lnrpc.QueryRoutesRequest.num_routes', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='final_cltv_delta', full_name='lnrpc.QueryRoutesRequest.final_cltv_delta', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fee_limit', full_name='lnrpc.QueryRoutesRequest.fee_limit', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=8663,
  serialized_end=8795,
)


_QUERYROUTESRESPONSE = _descriptor.Descriptor(
  name='QueryRoutesResponse',
  full_name='lnrpc.QueryRoutesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='routes', full_name='lnrpc.QueryRoutesResponse.routes', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='routes', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=8797,
  serialized_end=8856,
)


_HOP = _descriptor.Descriptor(
  name='Hop',
  full_name='lnrpc.Hop',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='chan_id', full_name='lnrpc.Hop.chan_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='chan_id', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chan_capacity', full_name='lnrpc.Hop.chan_capacity', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='chan_capacity', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amt_to_forward', full_name='lnrpc.Hop.amt_to_forward', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\030\001'), json_name='amt_to_forward', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fee', full_name='lnrpc.Hop.fee', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\030\001'), json_name='fee', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='expiry', full_name='lnrpc.Hop.expiry', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='expiry', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amt_to_forward_msat', full_name='lnrpc.Hop.amt_to_forward_msat', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='amt_to_forward_msat', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fee_msat', full_name='lnrpc.Hop.fee_msat', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='fee_msat', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pub_key', full_name='lnrpc.Hop.pub_key', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='pub_key', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=8859,
  serialized_end=9122,
)


_ROUTE = _descriptor.Descriptor(
  name='Route',
  full_name='lnrpc.Route',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='total_time_lock', full_name='lnrpc.Route.total_time_lock', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='total_time_lock', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_fees', full_name='lnrpc.Route.total_fees', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\030\001'), json_name='total_fees', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_amt', full_name='lnrpc.Route.total_amt', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\030\001'), json_name='total_amt', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hops', full_name='lnrpc.Route.hops', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='hops', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_fees_msat', full_name='lnrpc.Route.total_fees_msat', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='total_fees_msat', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_amt_msat', full_name='lnrpc.Route.total_amt_msat', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='total_amt_msat', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=9125,
  serialized_end=9358,
)


_NODEINFOREQUEST = _descriptor.Descriptor(
  name='NodeInfoRequest',
  full_name='lnrpc.NodeInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pub_key', full_name='lnrpc.NodeInfoRequest.pub_key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=9360,
  serialized_end=9394,
)


_NODEINFO = _descriptor.Descriptor(
  name='NodeInfo',
  full_name='lnrpc.NodeInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='node', full_name='lnrpc.NodeInfo.node', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='node', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_channels', full_name='lnrpc.NodeInfo.num_channels', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='num_channels', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_capacity', full_name='lnrpc.NodeInfo.total_capacity', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='total_capacity', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=9397,
  serialized_end=9525,
)


_LIGHTNINGNODE = _descriptor.Descriptor(
  name='LightningNode',
  full_name='lnrpc.LightningNode',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='last_update', full_name='lnrpc.LightningNode.last_update', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='last_update', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pub_key', full_name='lnrpc.LightningNode.pub_key', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='pub_key', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='alias', full_name='lnrpc.LightningNode.alias', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='alias', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='addresses', full_name='lnrpc.LightningNode.addresses', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='addresses', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='color', full_name='lnrpc.LightningNode.color', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='color', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=9528,
  serialized_end=9697,
)


_NODEADDRESS = _descriptor.Descriptor(
  name='NodeAddress',
  full_name='lnrpc.NodeAddress',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='network', full_name='lnrpc.NodeAddress.network', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='network', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='addr', full_name='lnrpc.NodeAddress.addr', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='addr', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=9699,
  serialized_end=9758,
)


_ROUTINGPOLICY = _descriptor.Descriptor(
  name='RoutingPolicy',
  full_name='lnrpc.RoutingPolicy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='time_lock_delta', full_name='lnrpc.RoutingPolicy.time_lock_delta', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='time_lock_delta', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='min_htlc', full_name='lnrpc.RoutingPolicy.min_htlc', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='min_htlc', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fee_base_msat', full_name='lnrpc.RoutingPolicy.fee_base_msat', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='fee_base_msat', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fee_rate_milli_msat', full_name='lnrpc.RoutingPolicy.fee_rate_milli_msat', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='fee_rate_milli_msat', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='disabled', full_name='lnrpc.RoutingPolicy.disabled', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='disabled', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=9761,
  serialized_end=9962,
)


_CHANNELEDGE = _descriptor.Descriptor(
  name='ChannelEdge',
  full_name='lnrpc.ChannelEdge',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='channel_id', full_name='lnrpc.ChannelEdge.channel_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='channel_id', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chan_point', full_name='lnrpc.ChannelEdge.chan_point', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='chan_point', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_update', full_name='lnrpc.ChannelEdge.last_update', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='last_update', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='node1_pub', full_name='lnrpc.ChannelEdge.node1_pub', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='node1_pub', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='node2_pub', full_name='lnrpc.ChannelEdge.node2_pub', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='node2_pub', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='capacity', full_name='lnrpc.ChannelEdge.capacity', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='capacity', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='node1_policy', full_name='lnrpc.ChannelEdge.node1_policy', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='node1_policy', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='node2_policy', full_name='lnrpc.ChannelEdge.node2_policy', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='node2_policy', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=9965,
  serialized_end=10280,
)


_CHANNELGRAPHREQUEST = _descriptor.Descriptor(
  name='ChannelGraphRequest',
  full_name='lnrpc.ChannelGraphRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='include_unannounced', full_name='lnrpc.ChannelGraphRequest.include_unannounced', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='include_unannounced', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=10282,
  serialized_end=10353,
)


_CHANNELGRAPH = _descriptor.Descriptor(
  name='ChannelGraph',
  full_name='lnrpc.ChannelGraph',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='nodes', full_name='lnrpc.ChannelGraph.nodes', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='nodes', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='edges', full_name='lnrpc.ChannelGraph.edges', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='edges', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=10355,
  serialized_end=10455,
)


_CHANINFOREQUEST = _descriptor.Descriptor(
  name='ChanInfoRequest',
  full_name='lnrpc.ChanInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='chan_id', full_name='lnrpc.ChanInfoRequest.chan_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=10457,
  serialized_end=10491,
)


_NETWORKINFOREQUEST = _descriptor.Descriptor(
  name='NetworkInfoRequest',
  full_name='lnrpc.NetworkInfoRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=10493,
  serialized_end=10513,
)


_NETWORKINFO = _descriptor.Descriptor(
  name='NetworkInfo',
  full_name='lnrpc.NetworkInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='graph_diameter', full_name='lnrpc.NetworkInfo.graph_diameter', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='graph_diameter', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='avg_out_degree', full_name='lnrpc.NetworkInfo.avg_out_degree', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='avg_out_degree', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_out_degree', full_name='lnrpc.NetworkInfo.max_out_degree', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='max_out_degree', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_nodes', full_name='lnrpc.NetworkInfo.num_nodes', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='num_nodes', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_channels', full_name='lnrpc.NetworkInfo.num_channels', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='num_channels', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_network_capacity', full_name='lnrpc.NetworkInfo.total_network_capacity', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='total_network_capacity', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='avg_channel_size', full_name='lnrpc.NetworkInfo.avg_channel_size', index=6,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='avg_channel_size', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='min_channel_size', full_name='lnrpc.NetworkInfo.min_channel_size', index=7,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='min_channel_size', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_channel_size', full_name='lnrpc.NetworkInfo.max_channel_size', index=8,
      number=9, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='max_channel_size', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=10516,
  serialized_end=10903,
)


_STOPREQUEST = _descriptor.Descriptor(
  name='StopRequest',
  full_name='lnrpc.StopRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=10905,
  serialized_end=10918,
)


_STOPRESPONSE = _descriptor.Descriptor(
  name='StopResponse',
  full_name='lnrpc.StopResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=10920,
  serialized_end=10934,
)


_GRAPHTOPOLOGYSUBSCRIPTION = _descriptor.Descriptor(
  name='GraphTopologySubscription',
  full_name='lnrpc.GraphTopologySubscription',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=10936,
  serialized_end=10963,
)


_GRAPHTOPOLOGYUPDATE = _descriptor.Descriptor(
  name='GraphTopologyUpdate',
  full_name='lnrpc.GraphTopologyUpdate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='node_updates', full_name='lnrpc.GraphTopologyUpdate.node_updates', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='channel_updates', full_name='lnrpc.GraphTopologyUpdate.channel_updates', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='closed_chans', full_name='lnrpc.GraphTopologyUpdate.closed_chans', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=10966,
  serialized_end=11129,
)


_NODEUPDATE = _descriptor.Descriptor(
  name='NodeUpdate',
  full_name='lnrpc.NodeUpdate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='addresses', full_name='lnrpc.NodeUpdate.addresses', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='identity_key', full_name='lnrpc.NodeUpdate.identity_key', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='global_features', full_name='lnrpc.NodeUpdate.global_features', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='alias', full_name='lnrpc.NodeUpdate.alias', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=11131,
  serialized_end=11224,
)


_CHANNELEDGEUPDATE = _descriptor.Descriptor(
  name='ChannelEdgeUpdate',
  full_name='lnrpc.ChannelEdgeUpdate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='chan_id', full_name='lnrpc.ChannelEdgeUpdate.chan_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chan_point', full_name='lnrpc.ChannelEdgeUpdate.chan_point', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='capacity', full_name='lnrpc.ChannelEdgeUpdate.capacity', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='routing_policy', full_name='lnrpc.ChannelEdgeUpdate.routing_policy', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='advertising_node', full_name='lnrpc.ChannelEdgeUpdate.advertising_node', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='connecting_node', full_name='lnrpc.ChannelEdgeUpdate.connecting_node', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=11227,
  serialized_end=11419,
)


_CLOSEDCHANNELUPDATE = _descriptor.Descriptor(
  name='ClosedChannelUpdate',
  full_name='lnrpc.ClosedChannelUpdate',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='chan_id', full_name='lnrpc.ClosedChannelUpdate.chan_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='capacity', full_name='lnrpc.ClosedChannelUpdate.capacity', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='closed_height', full_name='lnrpc.ClosedChannelUpdate.closed_height', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chan_point', full_name='lnrpc.ClosedChannelUpdate.chan_point', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=11421,
  serialized_end=11541,
)


_HOPHINT = _descriptor.Descriptor(
  name='HopHint',
  full_name='lnrpc.HopHint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='node_id', full_name='lnrpc.HopHint.node_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='node_id', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chan_id', full_name='lnrpc.HopHint.chan_id', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='chan_id', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fee_base_msat', full_name='lnrpc.HopHint.fee_base_msat', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='fee_base_msat', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fee_proportional_millionths', full_name='lnrpc.HopHint.fee_proportional_millionths', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='fee_proportional_millionths', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cltv_expiry_delta', full_name='lnrpc.HopHint.cltv_expiry_delta', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='cltv_expiry_delta', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=11544,
  serialized_end=11755,
)


_ROUTEHINT = _descriptor.Descriptor(
  name='RouteHint',
  full_name='lnrpc.RouteHint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hop_hints', full_name='lnrpc.RouteHint.hop_hints', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='hop_hints', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=11757,
  serialized_end=11814,
)


_INVOICE = _descriptor.Descriptor(
  name='Invoice',
  full_name='lnrpc.Invoice',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='memo', full_name='lnrpc.Invoice.memo', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='memo', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='receipt', full_name='lnrpc.Invoice.receipt', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='receipt', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='r_preimage', full_name='lnrpc.Invoice.r_preimage', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='r_preimage', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='r_hash', full_name='lnrpc.Invoice.r_hash', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='r_hash', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='lnrpc.Invoice.value', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='value', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='settled', full_name='lnrpc.Invoice.settled', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='settled', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='creation_date', full_name='lnrpc.Invoice.creation_date', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='creation_date', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='settle_date', full_name='lnrpc.Invoice.settle_date', index=7,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='settle_date', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payment_request', full_name='lnrpc.Invoice.payment_request', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='payment_request', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description_hash', full_name='lnrpc.Invoice.description_hash', index=9,
      number=10, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='description_hash', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='expiry', full_name='lnrpc.Invoice.expiry', index=10,
      number=11, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='expiry', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fallback_addr', full_name='lnrpc.Invoice.fallback_addr', index=11,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='fallback_addr', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cltv_expiry', full_name='lnrpc.Invoice.cltv_expiry', index=12,
      number=13, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='cltv_expiry', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='route_hints', full_name='lnrpc.Invoice.route_hints', index=13,
      number=14, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='route_hints', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='private', full_name='lnrpc.Invoice.private', index=14,
      number=15, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='private', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='add_index', full_name='lnrpc.Invoice.add_index', index=15,
      number=16, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='add_index', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='settle_index', full_name='lnrpc.Invoice.settle_index', index=16,
      number=17, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='settle_index', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amt_paid', full_name='lnrpc.Invoice.amt_paid', index=17,
      number=18, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\030\001'), json_name='amt_paid', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amt_paid_sat', full_name='lnrpc.Invoice.amt_paid_sat', index=18,
      number=19, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='amt_paid_sat', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amt_paid_msat', full_name='lnrpc.Invoice.amt_paid_msat', index=19,
      number=20, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='amt_paid_msat', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=11817,
  serialized_end=12480,
)


_ADDINVOICERESPONSE = _descriptor.Descriptor(
  name='AddInvoiceResponse',
  full_name='lnrpc.AddInvoiceResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='r_hash', full_name='lnrpc.AddInvoiceResponse.r_hash', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='r_hash', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payment_request', full_name='lnrpc.AddInvoiceResponse.payment_request', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='payment_request', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='add_index', full_name='lnrpc.AddInvoiceResponse.add_index', index=2,
      number=16, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='add_index', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=12482,
  serialized_end=12598,
)


_PAYMENTHASH = _descriptor.Descriptor(
  name='PaymentHash',
  full_name='lnrpc.PaymentHash',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='r_hash_str', full_name='lnrpc.PaymentHash.r_hash_str', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='r_hash_str', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='r_hash', full_name='lnrpc.PaymentHash.r_hash', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='r_hash', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=12600,
  serialized_end=12669,
)


_LISTINVOICEREQUEST = _descriptor.Descriptor(
  name='ListInvoiceRequest',
  full_name='lnrpc.ListInvoiceRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pending_only', full_name='lnrpc.ListInvoiceRequest.pending_only', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='pending_only', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='index_offset', full_name='lnrpc.ListInvoiceRequest.index_offset', index=1,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='index_offset', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_max_invoices', full_name='lnrpc.ListInvoiceRequest.num_max_invoices', index=2,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='num_max_invoices', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reversed', full_name='lnrpc.ListInvoiceRequest.reversed', index=3,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='reversed', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=12672,
  serialized_end=12836,
)


_LISTINVOICERESPONSE = _descriptor.Descriptor(
  name='ListInvoiceResponse',
  full_name='lnrpc.ListInvoiceResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='invoices', full_name='lnrpc.ListInvoiceResponse.invoices', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='invoices', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_index_offset', full_name='lnrpc.ListInvoiceResponse.last_index_offset', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='last_index_offset', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='first_index_offset', full_name='lnrpc.ListInvoiceResponse.first_index_offset', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='first_index_offset', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=12839,
  serialized_end=12998,
)


_INVOICESUBSCRIPTION = _descriptor.Descriptor(
  name='InvoiceSubscription',
  full_name='lnrpc.InvoiceSubscription',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='add_index', full_name='lnrpc.InvoiceSubscription.add_index', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='add_index', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='settle_index', full_name='lnrpc.InvoiceSubscription.settle_index', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='settle_index', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=13000,
  serialized_end=13087,
)


_PAYMENT = _descriptor.Descriptor(
  name='Payment',
  full_name='lnrpc.Payment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='payment_hash', full_name='lnrpc.Payment.payment_hash', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='payment_hash', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='lnrpc.Payment.value', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\030\001'), json_name='value', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='creation_date', full_name='lnrpc.Payment.creation_date', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='creation_date', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='path', full_name='lnrpc.Payment.path', index=3,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='path', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fee', full_name='lnrpc.Payment.fee', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='fee', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payment_preimage', full_name='lnrpc.Payment.payment_preimage', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='payment_preimage', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value_sat', full_name='lnrpc.Payment.value_sat', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='value_sat', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value_msat', full_name='lnrpc.Payment.value_msat', index=7,
      number=8, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='value_msat', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=13090,
  serialized_end=13343,
)


_LISTPAYMENTSREQUEST = _descriptor.Descriptor(
  name='ListPaymentsRequest',
  full_name='lnrpc.ListPaymentsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=13345,
  serialized_end=13366,
)


_LISTPAYMENTSRESPONSE = _descriptor.Descriptor(
  name='ListPaymentsResponse',
  full_name='lnrpc.ListPaymentsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='payments', full_name='lnrpc.ListPaymentsResponse.payments', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='payments', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=13368,
  serialized_end=13434,
)


_DELETEALLPAYMENTSREQUEST = _descriptor.Descriptor(
  name='DeleteAllPaymentsRequest',
  full_name='lnrpc.DeleteAllPaymentsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=13436,
  serialized_end=13462,
)


_DELETEALLPAYMENTSRESPONSE = _descriptor.Descriptor(
  name='DeleteAllPaymentsResponse',
  full_name='lnrpc.DeleteAllPaymentsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=13464,
  serialized_end=13491,
)


_ABANDONCHANNELREQUEST = _descriptor.Descriptor(
  name='AbandonChannelRequest',
  full_name='lnrpc.AbandonChannelRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='channel_point', full_name='lnrpc.AbandonChannelRequest.channel_point', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=13493,
  serialized_end=13560,
)


_ABANDONCHANNELRESPONSE = _descriptor.Descriptor(
  name='AbandonChannelResponse',
  full_name='lnrpc.AbandonChannelResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=13562,
  serialized_end=13586,
)


_DEBUGLEVELREQUEST = _descriptor.Descriptor(
  name='DebugLevelRequest',
  full_name='lnrpc.DebugLevelRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='show', full_name='lnrpc.DebugLevelRequest.show', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='level_spec', full_name='lnrpc.DebugLevelRequest.level_spec', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=13588,
  serialized_end=13641,
)


_DEBUGLEVELRESPONSE = _descriptor.Descriptor(
  name='DebugLevelResponse',
  full_name='lnrpc.DebugLevelResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='sub_systems', full_name='lnrpc.DebugLevelResponse.sub_systems', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='sub_systems', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=13643,
  serialized_end=13697,
)


_PAYREQSTRING = _descriptor.Descriptor(
  name='PayReqString',
  full_name='lnrpc.PayReqString',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pay_req', full_name='lnrpc.PayReqString.pay_req', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=13699,
  serialized_end=13730,
)


_PAYREQ = _descriptor.Descriptor(
  name='PayReq',
  full_name='lnrpc.PayReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='destination', full_name='lnrpc.PayReq.destination', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='destination', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='payment_hash', full_name='lnrpc.PayReq.payment_hash', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='payment_hash', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_satoshis', full_name='lnrpc.PayReq.num_satoshis', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='num_satoshis', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='lnrpc.PayReq.timestamp', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='timestamp', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='expiry', full_name='lnrpc.PayReq.expiry', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='expiry', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='lnrpc.PayReq.description', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='description', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description_hash', full_name='lnrpc.PayReq.description_hash', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='description_hash', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fallback_addr', full_name='lnrpc.PayReq.fallback_addr', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='fallback_addr', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cltv_expiry', full_name='lnrpc.PayReq.cltv_expiry', index=8,
      number=9, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='cltv_expiry', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='route_hints', full_name='lnrpc.PayReq.route_hints', index=9,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='route_hints', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=13733,
  serialized_end=14103,
)


_FEEREPORTREQUEST = _descriptor.Descriptor(
  name='FeeReportRequest',
  full_name='lnrpc.FeeReportRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=14105,
  serialized_end=14123,
)


_CHANNELFEEREPORT = _descriptor.Descriptor(
  name='ChannelFeeReport',
  full_name='lnrpc.ChannelFeeReport',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='chan_point', full_name='lnrpc.ChannelFeeReport.chan_point', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='channel_point', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='base_fee_msat', full_name='lnrpc.ChannelFeeReport.base_fee_msat', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='base_fee_msat', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fee_per_mil', full_name='lnrpc.ChannelFeeReport.fee_per_mil', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='fee_per_mil', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fee_rate', full_name='lnrpc.ChannelFeeReport.fee_rate', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='fee_rate', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=14126,
  serialized_end=14279,
)


_FEEREPORTRESPONSE = _descriptor.Descriptor(
  name='FeeReportResponse',
  full_name='lnrpc.FeeReportResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='channel_fees', full_name='lnrpc.FeeReportResponse.channel_fees', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='channel_fees', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='day_fee_sum', full_name='lnrpc.FeeReportResponse.day_fee_sum', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='day_fee_sum', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='week_fee_sum', full_name='lnrpc.FeeReportResponse.week_fee_sum', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='week_fee_sum', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='month_fee_sum', full_name='lnrpc.FeeReportResponse.month_fee_sum', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='month_fee_sum', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=14282,
  serialized_end=14470,
)


_POLICYUPDATEREQUEST = _descriptor.Descriptor(
  name='PolicyUpdateRequest',
  full_name='lnrpc.PolicyUpdateRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='global', full_name='lnrpc.PolicyUpdateRequest.global', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='global', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chan_point', full_name='lnrpc.PolicyUpdateRequest.chan_point', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='chan_point', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='base_fee_msat', full_name='lnrpc.PolicyUpdateRequest.base_fee_msat', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='base_fee_msat', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fee_rate', full_name='lnrpc.PolicyUpdateRequest.fee_rate', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='fee_rate', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time_lock_delta', full_name='lnrpc.PolicyUpdateRequest.time_lock_delta', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='time_lock_delta', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='scope', full_name='lnrpc.PolicyUpdateRequest.scope',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=14473,
  serialized_end=14692,
)


_POLICYUPDATERESPONSE = _descriptor.Descriptor(
  name='PolicyUpdateResponse',
  full_name='lnrpc.PolicyUpdateResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=14694,
  serialized_end=14716,
)


_FORWARDINGHISTORYREQUEST = _descriptor.Descriptor(
  name='ForwardingHistoryRequest',
  full_name='lnrpc.ForwardingHistoryRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start_time', full_name='lnrpc.ForwardingHistoryRequest.start_time', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='start_time', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end_time', full_name='lnrpc.ForwardingHistoryRequest.end_time', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='end_time', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='index_offset', full_name='lnrpc.ForwardingHistoryRequest.index_offset', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='index_offset', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_max_events', full_name='lnrpc.ForwardingHistoryRequest.num_max_events', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='num_max_events', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=14719,
  serialized_end=14881,
)


_FORWARDINGEVENT = _descriptor.Descriptor(
  name='ForwardingEvent',
  full_name='lnrpc.ForwardingEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='lnrpc.ForwardingEvent.timestamp', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='timestamp', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chan_id_in', full_name='lnrpc.ForwardingEvent.chan_id_in', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='chan_id_in', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='chan_id_out', full_name='lnrpc.ForwardingEvent.chan_id_out', index=2,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='chan_id_out', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amt_in', full_name='lnrpc.ForwardingEvent.amt_in', index=3,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='amt_in', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='amt_out', full_name='lnrpc.ForwardingEvent.amt_out', index=4,
      number=6, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='amt_out', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fee', full_name='lnrpc.ForwardingEvent.fee', index=5,
      number=7, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='fee', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=14884,
  serialized_end=15065,
)


_FORWARDINGHISTORYRESPONSE = _descriptor.Descriptor(
  name='ForwardingHistoryResponse',
  full_name='lnrpc.ForwardingHistoryResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='forwarding_events', full_name='lnrpc.ForwardingHistoryResponse.forwarding_events', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='forwarding_events', file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_offset_index', full_name='lnrpc.ForwardingHistoryResponse.last_offset_index', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, json_name='last_offset_index', file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=15068,
  serialized_end=15211,
)

_TRANSACTIONDETAILS.fields_by_name['transactions'].message_type = _TRANSACTION
_FEELIMIT.oneofs_by_name['limit'].fields.append(
  _FEELIMIT.fields_by_name['fixed'])
_FEELIMIT.fields_by_name['fixed'].containing_oneof = _FEELIMIT.oneofs_by_name['limit']
_FEELIMIT.oneofs_by_name['limit'].fields.append(
  _FEELIMIT.fields_by_name['percent'])
_FEELIMIT.fields_by_name['percent'].containing_oneof = _FEELIMIT.oneofs_by_name['limit']
_SENDREQUEST.fields_by_name['fee_limit'].message_type = _FEELIMIT
_SENDRESPONSE.fields_by_name['payment_route'].message_type = _ROUTE
_SENDTOROUTEREQUEST.fields_by_name['routes'].message_type = _ROUTE
_CHANNELPOINT.oneofs_by_name['funding_txid'].fields.append(
  _CHANNELPOINT.fields_by_name['funding_txid_bytes'])
_CHANNELPOINT.fields_by_name['funding_txid_bytes'].containing_oneof = _CHANNELPOINT.oneofs_by_name['funding_txid']
_CHANNELPOINT.oneofs_by_name['funding_txid'].fields.append(
  _CHANNELPOINT.fields_by_name['funding_txid_str'])
_CHANNELPOINT.fields_by_name['funding_txid_str'].containing_oneof = _CHANNELPOINT.oneofs_by_name['funding_txid']
_SENDMANYREQUEST_ADDRTOAMOUNTENTRY.containing_type = _SENDMANYREQUEST
_SENDMANYREQUEST.fields_by_name['AddrToAmount'].message_type = _SENDMANYREQUEST_ADDRTOAMOUNTENTRY
_NEWADDRESSREQUEST.fields_by_name['type'].enum_type = _NEWADDRESSREQUEST_ADDRESSTYPE
_NEWADDRESSREQUEST_ADDRESSTYPE.containing_type = _NEWADDRESSREQUEST
_CONNECTPEERREQUEST.fields_by_name['addr'].message_type = _LIGHTNINGADDRESS
_CHANNEL.fields_by_name['pending_htlcs'].message_type = _HTLC
_LISTCHANNELSRESPONSE.fields_by_name['channels'].message_type = _CHANNEL
_CHANNELCLOSESUMMARY.fields_by_name['close_type'].enum_type = _CHANNELCLOSESUMMARY_CLOSURETYPE
_CHANNELCLOSESUMMARY_CLOSURETYPE.containing_type = _CHANNELCLOSESUMMARY
_CLOSEDCHANNELSRESPONSE.fields_by_name['channels'].message_type = _CHANNELCLOSESUMMARY
_LISTPEERSRESPONSE.fields_by_name['peers'].message_type = _PEER
_CHANNELOPENUPDATE.fields_by_name['channel_point'].message_type = _CHANNELPOINT
_CLOSECHANNELREQUEST.fields_by_name['channel_point'].message_type = _CHANNELPOINT
_CLOSESTATUSUPDATE.fields_by_name['close_pending'].message_type = _PENDINGUPDATE
_CLOSESTATUSUPDATE.fields_by_name['confirmation'].message_type = _CONFIRMATIONUPDATE
_CLOSESTATUSUPDATE.fields_by_name['chan_close'].message_type = _CHANNELCLOSEUPDATE
_CLOSESTATUSUPDATE.oneofs_by_name['update'].fields.append(
  _CLOSESTATUSUPDATE.fields_by_name['close_pending'])
_CLOSESTATUSUPDATE.fields_by_name['close_pending'].containing_oneof = _CLOSESTATUSUPDATE.oneofs_by_name['update']
_CLOSESTATUSUPDATE.oneofs_by_name['update'].fields.append(
  _CLOSESTATUSUPDATE.fields_by_name['confirmation'])
_CLOSESTATUSUPDATE.fields_by_name['confirmation'].containing_oneof = _CLOSESTATUSUPDATE.oneofs_by_name['update']
_CLOSESTATUSUPDATE.oneofs_by_name['update'].fields.append(
  _CLOSESTATUSUPDATE.fields_by_name['chan_close'])
_CLOSESTATUSUPDATE.fields_by_name['chan_close'].containing_oneof = _CLOSESTATUSUPDATE.oneofs_by_name['update']
_OPENSTATUSUPDATE.fields_by_name['chan_pending'].message_type = _PENDINGUPDATE
_OPENSTATUSUPDATE.fields_by_name['confirmation'].message_type = _CONFIRMATIONUPDATE
_OPENSTATUSUPDATE.fields_by_name['chan_open'].message_type = _CHANNELOPENUPDATE
_OPENSTATUSUPDATE.oneofs_by_name['update'].fields.append(
  _OPENSTATUSUPDATE.fields_by_name['chan_pending'])
_OPENSTATUSUPDATE.fields_by_name['chan_pending'].containing_oneof = _OPENSTATUSUPDATE.oneofs_by_name['update']
_OPENSTATUSUPDATE.oneofs_by_name['update'].fields.append(
  _OPENSTATUSUPDATE.fields_by_name['confirmation'])
_OPENSTATUSUPDATE.fields_by_name['confirmation'].containing_oneof = _OPENSTATUSUPDATE.oneofs_by_name['update']
_OPENSTATUSUPDATE.oneofs_by_name['update'].fields.append(
  _OPENSTATUSUPDATE.fields_by_name['chan_open'])
_OPENSTATUSUPDATE.fields_by_name['chan_open'].containing_oneof = _OPENSTATUSUPDATE.oneofs_by_name['update']
_PENDINGCHANNELSRESPONSE_PENDINGCHANNEL.containing_type = _PENDINGCHANNELSRESPONSE
_PENDINGCHANNELSRESPONSE_PENDINGOPENCHANNEL.fields_by_name['channel'].message_type = _PENDINGCHANNELSRESPONSE_PENDINGCHANNEL
_PENDINGCHANNELSRESPONSE_PENDINGOPENCHANNEL.containing_type = _PENDINGCHANNELSRESPONSE
_PENDINGCHANNELSRESPONSE_WAITINGCLOSECHANNEL.fields_by_name['channel'].message_type = _PENDINGCHANNELSRESPONSE_PENDINGCHANNEL
_PENDINGCHANNELSRESPONSE_WAITINGCLOSECHANNEL.containing_type = _PENDINGCHANNELSRESPONSE
_PENDINGCHANNELSRESPONSE_CLOSEDCHANNEL.fields_by_name['channel'].message_type = _PENDINGCHANNELSRESPONSE_PENDINGCHANNEL
_PENDINGCHANNELSRESPONSE_CLOSEDCHANNEL.containing_type = _PENDINGCHANNELSRESPONSE
_PENDINGCHANNELSRESPONSE_FORCECLOSEDCHANNEL.fields_by_name['channel'].message_type = _PENDINGCHANNELSRESPONSE_PENDINGCHANNEL
_PENDINGCHANNELSRESPONSE_FORCECLOSEDCHANNEL.fields_by_name['pending_htlcs'].message_type = _PENDINGHTLC
_PENDINGCHANNELSRESPONSE_FORCECLOSEDCHANNEL.containing_type = _PENDINGCHANNELSRESPONSE
_PENDINGCHANNELSRESPONSE.fields_by_name['pending_open_channels'].message_type = _PENDINGCHANNELSRESPONSE_PENDINGOPENCHANNEL
_PENDINGCHANNELSRESPONSE.fields_by_name['pending_closing_channels'].message_type = _PENDINGCHANNELSRESPONSE_CLOSEDCHANNEL
_PENDINGCHANNELSRESPONSE.fields_by_name['pending_force_closing_channels'].message_type = _PENDINGCHANNELSRESPONSE_FORCECLOSEDCHANNEL
_PENDINGCHANNELSRESPONSE.fields_by_name['waiting_close_channels'].message_type = _PENDINGCHANNELSRESPONSE_WAITINGCLOSECHANNEL
_QUERYROUTESREQUEST.fields_by_name['fee_limit'].message_type = _FEELIMIT
_QUERYROUTESRESPONSE.fields_by_name['routes'].message_type = _ROUTE
_ROUTE.fields_by_name['hops'].message_type = _HOP
_NODEINFO.fields_by_name['node'].message_type = _LIGHTNINGNODE
_LIGHTNINGNODE.fields_by_name['addresses'].message_type = _NODEADDRESS
_CHANNELEDGE.fields_by_name['node1_policy'].message_type = _ROUTINGPOLICY
_CHANNELEDGE.fields_by_name['node2_policy'].message_type = _ROUTINGPOLICY
_CHANNELGRAPH.fields_by_name['nodes'].message_type = _LIGHTNINGNODE
_CHANNELGRAPH.fields_by_name['edges'].message_type = _CHANNELEDGE
_GRAPHTOPOLOGYUPDATE.fields_by_name['node_updates'].message_type = _NODEUPDATE
_GRAPHTOPOLOGYUPDATE.fields_by_name['channel_updates'].message_type = _CHANNELEDGEUPDATE
_GRAPHTOPOLOGYUPDATE.fields_by_name['closed_chans'].message_type = _CLOSEDCHANNELUPDATE
_CHANNELEDGEUPDATE.fields_by_name['chan_point'].message_type = _CHANNELPOINT
_CHANNELEDGEUPDATE.fields_by_name['routing_policy'].message_type = _ROUTINGPOLICY
_CLOSEDCHANNELUPDATE.fields_by_name['chan_point'].message_type = _CHANNELPOINT
_ROUTEHINT.fields_by_name['hop_hints'].message_type = _HOPHINT
_INVOICE.fields_by_name['route_hints'].message_type = _ROUTEHINT
_LISTINVOICERESPONSE.fields_by_name['invoices'].message_type = _INVOICE
_LISTPAYMENTSRESPONSE.fields_by_name['payments'].message_type = _PAYMENT
_ABANDONCHANNELREQUEST.fields_by_name['channel_point'].message_type = _CHANNELPOINT
_PAYREQ.fields_by_name['route_hints'].message_type = _ROUTEHINT
_FEEREPORTRESPONSE.fields_by_name['channel_fees'].message_type = _CHANNELFEEREPORT
_POLICYUPDATEREQUEST.fields_by_name['chan_point'].message_type = _CHANNELPOINT
_POLICYUPDATEREQUEST.oneofs_by_name['scope'].fields.append(
  _POLICYUPDATEREQUEST.fields_by_name['global'])
_POLICYUPDATEREQUEST.fields_by_name['global'].containing_oneof = _POLICYUPDATEREQUEST.oneofs_by_name['scope']
_POLICYUPDATEREQUEST.oneofs_by_name['scope'].fields.append(
  _POLICYUPDATEREQUEST.fields_by_name['chan_point'])
_POLICYUPDATEREQUEST.fields_by_name['chan_point'].containing_oneof = _POLICYUPDATEREQUEST.oneofs_by_name['scope']
_FORWARDINGHISTORYRESPONSE.fields_by_name['forwarding_events'].message_type = _FORWARDINGEVENT
DESCRIPTOR.message_types_by_name['GenSeedRequest'] = _GENSEEDREQUEST
DESCRIPTOR.message_types_by_name['GenSeedResponse'] = _GENSEEDRESPONSE
DESCRIPTOR.message_types_by_name['InitWalletRequest'] = _INITWALLETREQUEST
DESCRIPTOR.message_types_by_name['InitWalletResponse'] = _INITWALLETRESPONSE
DESCRIPTOR.message_types_by_name['UnlockWalletRequest'] = _UNLOCKWALLETREQUEST
DESCRIPTOR.message_types_by_name['UnlockWalletResponse'] = _UNLOCKWALLETRESPONSE
DESCRIPTOR.message_types_by_name['ChangePasswordRequest'] = _CHANGEPASSWORDREQUEST
DESCRIPTOR.message_types_by_name['ChangePasswordResponse'] = _CHANGEPASSWORDRESPONSE
DESCRIPTOR.message_types_by_name['Transaction'] = _TRANSACTION
DESCRIPTOR.message_types_by_name['GetTransactionsRequest'] = _GETTRANSACTIONSREQUEST
DESCRIPTOR.message_types_by_name['TransactionDetails'] = _TRANSACTIONDETAILS
DESCRIPTOR.message_types_by_name['FeeLimit'] = _FEELIMIT
DESCRIPTOR.message_types_by_name['SendRequest'] = _SENDREQUEST
DESCRIPTOR.message_types_by_name['SendResponse'] = _SENDRESPONSE
DESCRIPTOR.message_types_by_name['SendToRouteRequest'] = _SENDTOROUTEREQUEST
DESCRIPTOR.message_types_by_name['ChannelPoint'] = _CHANNELPOINT
DESCRIPTOR.message_types_by_name['LightningAddress'] = _LIGHTNINGADDRESS
DESCRIPTOR.message_types_by_name['SendManyRequest'] = _SENDMANYREQUEST
DESCRIPTOR.message_types_by_name['SendManyResponse'] = _SENDMANYRESPONSE
DESCRIPTOR.message_types_by_name['SendCoinsRequest'] = _SENDCOINSREQUEST
DESCRIPTOR.message_types_by_name['SendCoinsResponse'] = _SENDCOINSRESPONSE
DESCRIPTOR.message_types_by_name['NewAddressRequest'] = _NEWADDRESSREQUEST
DESCRIPTOR.message_types_by_name['NewAddressResponse'] = _NEWADDRESSRESPONSE
DESCRIPTOR.message_types_by_name['SignMessageRequest'] = _SIGNMESSAGEREQUEST
DESCRIPTOR.message_types_by_name['SignMessageResponse'] = _SIGNMESSAGERESPONSE
DESCRIPTOR.message_types_by_name['VerifyMessageRequest'] = _VERIFYMESSAGEREQUEST
DESCRIPTOR.message_types_by_name['VerifyMessageResponse'] = _VERIFYMESSAGERESPONSE
DESCRIPTOR.message_types_by_name['ConnectPeerRequest'] = _CONNECTPEERREQUEST
DESCRIPTOR.message_types_by_name['ConnectPeerResponse'] = _CONNECTPEERRESPONSE
DESCRIPTOR.message_types_by_name['DisconnectPeerRequest'] = _DISCONNECTPEERREQUEST
DESCRIPTOR.message_types_by_name['DisconnectPeerResponse'] = _DISCONNECTPEERRESPONSE
DESCRIPTOR.message_types_by_name['HTLC'] = _HTLC
DESCRIPTOR.message_types_by_name['Channel'] = _CHANNEL
DESCRIPTOR.message_types_by_name['ListChannelsRequest'] = _LISTCHANNELSREQUEST
DESCRIPTOR.message_types_by_name['ListChannelsResponse'] = _LISTCHANNELSRESPONSE
DESCRIPTOR.message_types_by_name['ChannelCloseSummary'] = _CHANNELCLOSESUMMARY
DESCRIPTOR.message_types_by_name['ClosedChannelsRequest'] = _CLOSEDCHANNELSREQUEST
DESCRIPTOR.message_types_by_name['ClosedChannelsResponse'] = _CLOSEDCHANNELSRESPONSE
DESCRIPTOR.message_types_by_name['Peer'] = _PEER
DESCRIPTOR.message_types_by_name['ListPeersRequest'] = _LISTPEERSREQUEST
DESCRIPTOR.message_types_by_name['ListPeersResponse'] = _LISTPEERSRESPONSE
DESCRIPTOR.message_types_by_name['GetInfoRequest'] = _GETINFOREQUEST
DESCRIPTOR.message_types_by_name['GetInfoResponse'] = _GETINFORESPONSE
DESCRIPTOR.message_types_by_name['ConfirmationUpdate'] = _CONFIRMATIONUPDATE
DESCRIPTOR.message_types_by_name['ChannelOpenUpdate'] = _CHANNELOPENUPDATE
DESCRIPTOR.message_types_by_name['ChannelCloseUpdate'] = _CHANNELCLOSEUPDATE
DESCRIPTOR.message_types_by_name['CloseChannelRequest'] = _CLOSECHANNELREQUEST
DESCRIPTOR.message_types_by_name['CloseStatusUpdate'] = _CLOSESTATUSUPDATE
DESCRIPTOR.message_types_by_name['PendingUpdate'] = _PENDINGUPDATE
DESCRIPTOR.message_types_by_name['OpenChannelRequest'] = _OPENCHANNELREQUEST
DESCRIPTOR.message_types_by_name['OpenStatusUpdate'] = _OPENSTATUSUPDATE
DESCRIPTOR.message_types_by_name['PendingHTLC'] = _PENDINGHTLC
DESCRIPTOR.message_types_by_name['PendingChannelsRequest'] = _PENDINGCHANNELSREQUEST
DESCRIPTOR.message_types_by_name['PendingChannelsResponse'] = _PENDINGCHANNELSRESPONSE
DESCRIPTOR.message_types_by_name['WalletBalanceRequest'] = _WALLETBALANCEREQUEST
DESCRIPTOR.message_types_by_name['WalletBalanceResponse'] = _WALLETBALANCERESPONSE
DESCRIPTOR.message_types_by_name['ChannelBalanceRequest'] = _CHANNELBALANCEREQUEST
DESCRIPTOR.message_types_by_name['ChannelBalanceResponse'] = _CHANNELBALANCERESPONSE
DESCRIPTOR.message_types_by_name['QueryRoutesRequest'] = _QUERYROUTESREQUEST
DESCRIPTOR.message_types_by_name['QueryRoutesResponse'] = _QUERYROUTESRESPONSE
DESCRIPTOR.message_types_by_name['Hop'] = _HOP
DESCRIPTOR.message_types_by_name['Route'] = _ROUTE
DESCRIPTOR.message_types_by_name['NodeInfoRequest'] = _NODEINFOREQUEST
DESCRIPTOR.message_types_by_name['NodeInfo'] = _NODEINFO
DESCRIPTOR.message_types_by_name['LightningNode'] = _LIGHTNINGNODE
DESCRIPTOR.message_types_by_name['NodeAddress'] = _NODEADDRESS
DESCRIPTOR.message_types_by_name['RoutingPolicy'] = _ROUTINGPOLICY
DESCRIPTOR.message_types_by_name['ChannelEdge'] = _CHANNELEDGE
DESCRIPTOR.message_types_by_name['ChannelGraphRequest'] = _CHANNELGRAPHREQUEST
DESCRIPTOR.message_types_by_name['ChannelGraph'] = _CHANNELGRAPH
DESCRIPTOR.message_types_by_name['ChanInfoRequest'] = _CHANINFOREQUEST
DESCRIPTOR.message_types_by_name['NetworkInfoRequest'] = _NETWORKINFOREQUEST
DESCRIPTOR.message_types_by_name['NetworkInfo'] = _NETWORKINFO
DESCRIPTOR.message_types_by_name['StopRequest'] = _STOPREQUEST
DESCRIPTOR.message_types_by_name['StopResponse'] = _STOPRESPONSE
DESCRIPTOR.message_types_by_name['GraphTopologySubscription'] = _GRAPHTOPOLOGYSUBSCRIPTION
DESCRIPTOR.message_types_by_name['GraphTopologyUpdate'] = _GRAPHTOPOLOGYUPDATE
DESCRIPTOR.message_types_by_name['NodeUpdate'] = _NODEUPDATE
DESCRIPTOR.message_types_by_name['ChannelEdgeUpdate'] = _CHANNELEDGEUPDATE
DESCRIPTOR.message_types_by_name['ClosedChannelUpdate'] = _CLOSEDCHANNELUPDATE
DESCRIPTOR.message_types_by_name['HopHint'] = _HOPHINT
DESCRIPTOR.message_types_by_name['RouteHint'] = _ROUTEHINT
DESCRIPTOR.message_types_by_name['Invoice'] = _INVOICE
DESCRIPTOR.message_types_by_name['AddInvoiceResponse'] = _ADDINVOICERESPONSE
DESCRIPTOR.message_types_by_name['PaymentHash'] = _PAYMENTHASH
DESCRIPTOR.message_types_by_name['ListInvoiceRequest'] = _LISTINVOICEREQUEST
DESCRIPTOR.message_types_by_name['ListInvoiceResponse'] = _LISTINVOICERESPONSE
DESCRIPTOR.message_types_by_name['InvoiceSubscription'] = _INVOICESUBSCRIPTION
DESCRIPTOR.message_types_by_name['Payment'] = _PAYMENT
DESCRIPTOR.message_types_by_name['ListPaymentsRequest'] = _LISTPAYMENTSREQUEST
DESCRIPTOR.message_types_by_name['ListPaymentsResponse'] = _LISTPAYMENTSRESPONSE
DESCRIPTOR.message_types_by_name['DeleteAllPaymentsRequest'] = _DELETEALLPAYMENTSREQUEST
DESCRIPTOR.message_types_by_name['DeleteAllPaymentsResponse'] = _DELETEALLPAYMENTSRESPONSE
DESCRIPTOR.message_types_by_name['AbandonChannelRequest'] = _ABANDONCHANNELREQUEST
DESCRIPTOR.message_types_by_name['AbandonChannelResponse'] = _ABANDONCHANNELRESPONSE
DESCRIPTOR.message_types_by_name['DebugLevelRequest'] = _DEBUGLEVELREQUEST
DESCRIPTOR.message_types_by_name['DebugLevelResponse'] = _DEBUGLEVELRESPONSE
DESCRIPTOR.message_types_by_name['PayReqString'] = _PAYREQSTRING
DESCRIPTOR.message_types_by_name['PayReq'] = _PAYREQ
DESCRIPTOR.message_types_by_name['FeeReportRequest'] = _FEEREPORTREQUEST
DESCRIPTOR.message_types_by_name['ChannelFeeReport'] = _CHANNELFEEREPORT
DESCRIPTOR.message_types_by_name['FeeReportResponse'] = _FEEREPORTRESPONSE
DESCRIPTOR.message_types_by_name['PolicyUpdateRequest'] = _POLICYUPDATEREQUEST
DESCRIPTOR.message_types_by_name['PolicyUpdateResponse'] = _POLICYUPDATERESPONSE
DESCRIPTOR.message_types_by_name['ForwardingHistoryRequest'] = _FORWARDINGHISTORYREQUEST
DESCRIPTOR.message_types_by_name['ForwardingEvent'] = _FORWARDINGEVENT
DESCRIPTOR.message_types_by_name['ForwardingHistoryResponse'] = _FORWARDINGHISTORYRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GenSeedRequest = _reflection.GeneratedProtocolMessageType('GenSeedRequest', (_message.Message,), dict(
  DESCRIPTOR = _GENSEEDREQUEST,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.GenSeedRequest)
  ))
_sym_db.RegisterMessage(GenSeedRequest)

GenSeedResponse = _reflection.GeneratedProtocolMessageType('GenSeedResponse', (_message.Message,), dict(
  DESCRIPTOR = _GENSEEDRESPONSE,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.GenSeedResponse)
  ))
_sym_db.RegisterMessage(GenSeedResponse)

InitWalletRequest = _reflection.GeneratedProtocolMessageType('InitWalletRequest', (_message.Message,), dict(
  DESCRIPTOR = _INITWALLETREQUEST,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.InitWalletRequest)
  ))
_sym_db.RegisterMessage(InitWalletRequest)

InitWalletResponse = _reflection.GeneratedProtocolMessageType('InitWalletResponse', (_message.Message,), dict(
  DESCRIPTOR = _INITWALLETRESPONSE,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.InitWalletResponse)
  ))
_sym_db.RegisterMessage(InitWalletResponse)

UnlockWalletRequest = _reflection.GeneratedProtocolMessageType('UnlockWalletRequest', (_message.Message,), dict(
  DESCRIPTOR = _UNLOCKWALLETREQUEST,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.UnlockWalletRequest)
  ))
_sym_db.RegisterMessage(UnlockWalletRequest)

UnlockWalletResponse = _reflection.GeneratedProtocolMessageType('UnlockWalletResponse', (_message.Message,), dict(
  DESCRIPTOR = _UNLOCKWALLETRESPONSE,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.UnlockWalletResponse)
  ))
_sym_db.RegisterMessage(UnlockWalletResponse)

ChangePasswordRequest = _reflection.GeneratedProtocolMessageType('ChangePasswordRequest', (_message.Message,), dict(
  DESCRIPTOR = _CHANGEPASSWORDREQUEST,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.ChangePasswordRequest)
  ))
_sym_db.RegisterMessage(ChangePasswordRequest)

ChangePasswordResponse = _reflection.GeneratedProtocolMessageType('ChangePasswordResponse', (_message.Message,), dict(
  DESCRIPTOR = _CHANGEPASSWORDRESPONSE,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.ChangePasswordResponse)
  ))
_sym_db.RegisterMessage(ChangePasswordResponse)

Transaction = _reflection.GeneratedProtocolMessageType('Transaction', (_message.Message,), dict(
  DESCRIPTOR = _TRANSACTION,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.Transaction)
  ))
_sym_db.RegisterMessage(Transaction)

GetTransactionsRequest = _reflection.GeneratedProtocolMessageType('GetTransactionsRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETTRANSACTIONSREQUEST,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.GetTransactionsRequest)
  ))
_sym_db.RegisterMessage(GetTransactionsRequest)

TransactionDetails = _reflection.GeneratedProtocolMessageType('TransactionDetails', (_message.Message,), dict(
  DESCRIPTOR = _TRANSACTIONDETAILS,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.TransactionDetails)
  ))
_sym_db.RegisterMessage(TransactionDetails)

FeeLimit = _reflection.GeneratedProtocolMessageType('FeeLimit', (_message.Message,), dict(
  DESCRIPTOR = _FEELIMIT,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.FeeLimit)
  ))
_sym_db.RegisterMessage(FeeLimit)

SendRequest = _reflection.GeneratedProtocolMessageType('SendRequest', (_message.Message,), dict(
  DESCRIPTOR = _SENDREQUEST,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.SendRequest)
  ))
_sym_db.RegisterMessage(SendRequest)

SendResponse = _reflection.GeneratedProtocolMessageType('SendResponse', (_message.Message,), dict(
  DESCRIPTOR = _SENDRESPONSE,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.SendResponse)
  ))
_sym_db.RegisterMessage(SendResponse)

SendToRouteRequest = _reflection.GeneratedProtocolMessageType('SendToRouteRequest', (_message.Message,), dict(
  DESCRIPTOR = _SENDTOROUTEREQUEST,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.SendToRouteRequest)
  ))
_sym_db.RegisterMessage(SendToRouteRequest)

ChannelPoint = _reflection.GeneratedProtocolMessageType('ChannelPoint', (_message.Message,), dict(
  DESCRIPTOR = _CHANNELPOINT,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.ChannelPoint)
  ))
_sym_db.RegisterMessage(ChannelPoint)

LightningAddress = _reflection.GeneratedProtocolMessageType('LightningAddress', (_message.Message,), dict(
  DESCRIPTOR = _LIGHTNINGADDRESS,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.LightningAddress)
  ))
_sym_db.RegisterMessage(LightningAddress)

SendManyRequest = _reflection.GeneratedProtocolMessageType('SendManyRequest', (_message.Message,), dict(

  AddrToAmountEntry = _reflection.GeneratedProtocolMessageType('AddrToAmountEntry', (_message.Message,), dict(
    DESCRIPTOR = _SENDMANYREQUEST_ADDRTOAMOUNTENTRY,
    __module__ = 'rpc_pb2'
    # @@protoc_insertion_point(class_scope:lnrpc.SendManyRequest.AddrToAmountEntry)
    ))
  ,
  DESCRIPTOR = _SENDMANYREQUEST,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.SendManyRequest)
  ))
_sym_db.RegisterMessage(SendManyRequest)
_sym_db.RegisterMessage(SendManyRequest.AddrToAmountEntry)

SendManyResponse = _reflection.GeneratedProtocolMessageType('SendManyResponse', (_message.Message,), dict(
  DESCRIPTOR = _SENDMANYRESPONSE,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.SendManyResponse)
  ))
_sym_db.RegisterMessage(SendManyResponse)

SendCoinsRequest = _reflection.GeneratedProtocolMessageType('SendCoinsRequest', (_message.Message,), dict(
  DESCRIPTOR = _SENDCOINSREQUEST,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.SendCoinsRequest)
  ))
_sym_db.RegisterMessage(SendCoinsRequest)

SendCoinsResponse = _reflection.GeneratedProtocolMessageType('SendCoinsResponse', (_message.Message,), dict(
  DESCRIPTOR = _SENDCOINSRESPONSE,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.SendCoinsResponse)
  ))
_sym_db.RegisterMessage(SendCoinsResponse)

NewAddressRequest = _reflection.GeneratedProtocolMessageType('NewAddressRequest', (_message.Message,), dict(
  DESCRIPTOR = _NEWADDRESSREQUEST,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.NewAddressRequest)
  ))
_sym_db.RegisterMessage(NewAddressRequest)

NewAddressResponse = _reflection.GeneratedProtocolMessageType('NewAddressResponse', (_message.Message,), dict(
  DESCRIPTOR = _NEWADDRESSRESPONSE,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.NewAddressResponse)
  ))
_sym_db.RegisterMessage(NewAddressResponse)

SignMessageRequest = _reflection.GeneratedProtocolMessageType('SignMessageRequest', (_message.Message,), dict(
  DESCRIPTOR = _SIGNMESSAGEREQUEST,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.SignMessageRequest)
  ))
_sym_db.RegisterMessage(SignMessageRequest)

SignMessageResponse = _reflection.GeneratedProtocolMessageType('SignMessageResponse', (_message.Message,), dict(
  DESCRIPTOR = _SIGNMESSAGERESPONSE,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.SignMessageResponse)
  ))
_sym_db.RegisterMessage(SignMessageResponse)

VerifyMessageRequest = _reflection.GeneratedProtocolMessageType('VerifyMessageRequest', (_message.Message,), dict(
  DESCRIPTOR = _VERIFYMESSAGEREQUEST,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.VerifyMessageRequest)
  ))
_sym_db.RegisterMessage(VerifyMessageRequest)

VerifyMessageResponse = _reflection.GeneratedProtocolMessageType('VerifyMessageResponse', (_message.Message,), dict(
  DESCRIPTOR = _VERIFYMESSAGERESPONSE,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.VerifyMessageResponse)
  ))
_sym_db.RegisterMessage(VerifyMessageResponse)

ConnectPeerRequest = _reflection.GeneratedProtocolMessageType('ConnectPeerRequest', (_message.Message,), dict(
  DESCRIPTOR = _CONNECTPEERREQUEST,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.ConnectPeerRequest)
  ))
_sym_db.RegisterMessage(ConnectPeerRequest)

ConnectPeerResponse = _reflection.GeneratedProtocolMessageType('ConnectPeerResponse', (_message.Message,), dict(
  DESCRIPTOR = _CONNECTPEERRESPONSE,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.ConnectPeerResponse)
  ))
_sym_db.RegisterMessage(ConnectPeerResponse)

DisconnectPeerRequest = _reflection.GeneratedProtocolMessageType('DisconnectPeerRequest', (_message.Message,), dict(
  DESCRIPTOR = _DISCONNECTPEERREQUEST,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.DisconnectPeerRequest)
  ))
_sym_db.RegisterMessage(DisconnectPeerRequest)

DisconnectPeerResponse = _reflection.GeneratedProtocolMessageType('DisconnectPeerResponse', (_message.Message,), dict(
  DESCRIPTOR = _DISCONNECTPEERRESPONSE,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.DisconnectPeerResponse)
  ))
_sym_db.RegisterMessage(DisconnectPeerResponse)

HTLC = _reflection.GeneratedProtocolMessageType('HTLC', (_message.Message,), dict(
  DESCRIPTOR = _HTLC,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.HTLC)
  ))
_sym_db.RegisterMessage(HTLC)

Channel = _reflection.GeneratedProtocolMessageType('Channel', (_message.Message,), dict(
  DESCRIPTOR = _CHANNEL,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.Channel)
  ))
_sym_db.RegisterMessage(Channel)

ListChannelsRequest = _reflection.GeneratedProtocolMessageType('ListChannelsRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTCHANNELSREQUEST,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.ListChannelsRequest)
  ))
_sym_db.RegisterMessage(ListChannelsRequest)

ListChannelsResponse = _reflection.GeneratedProtocolMessageType('ListChannelsResponse', (_message.Message,), dict(
  DESCRIPTOR = _LISTCHANNELSRESPONSE,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.ListChannelsResponse)
  ))
_sym_db.RegisterMessage(ListChannelsResponse)

ChannelCloseSummary = _reflection.GeneratedProtocolMessageType('ChannelCloseSummary', (_message.Message,), dict(
  DESCRIPTOR = _CHANNELCLOSESUMMARY,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.ChannelCloseSummary)
  ))
_sym_db.RegisterMessage(ChannelCloseSummary)

ClosedChannelsRequest = _reflection.GeneratedProtocolMessageType('ClosedChannelsRequest', (_message.Message,), dict(
  DESCRIPTOR = _CLOSEDCHANNELSREQUEST,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.ClosedChannelsRequest)
  ))
_sym_db.RegisterMessage(ClosedChannelsRequest)

ClosedChannelsResponse = _reflection.GeneratedProtocolMessageType('ClosedChannelsResponse', (_message.Message,), dict(
  DESCRIPTOR = _CLOSEDCHANNELSRESPONSE,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.ClosedChannelsResponse)
  ))
_sym_db.RegisterMessage(ClosedChannelsResponse)

Peer = _reflection.GeneratedProtocolMessageType('Peer', (_message.Message,), dict(
  DESCRIPTOR = _PEER,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.Peer)
  ))
_sym_db.RegisterMessage(Peer)

ListPeersRequest = _reflection.GeneratedProtocolMessageType('ListPeersRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTPEERSREQUEST,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.ListPeersRequest)
  ))
_sym_db.RegisterMessage(ListPeersRequest)

ListPeersResponse = _reflection.GeneratedProtocolMessageType('ListPeersResponse', (_message.Message,), dict(
  DESCRIPTOR = _LISTPEERSRESPONSE,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.ListPeersResponse)
  ))
_sym_db.RegisterMessage(ListPeersResponse)

GetInfoRequest = _reflection.GeneratedProtocolMessageType('GetInfoRequest', (_message.Message,), dict(
  DESCRIPTOR = _GETINFOREQUEST,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.GetInfoRequest)
  ))
_sym_db.RegisterMessage(GetInfoRequest)

GetInfoResponse = _reflection.GeneratedProtocolMessageType('GetInfoResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETINFORESPONSE,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.GetInfoResponse)
  ))
_sym_db.RegisterMessage(GetInfoResponse)

ConfirmationUpdate = _reflection.GeneratedProtocolMessageType('ConfirmationUpdate', (_message.Message,), dict(
  DESCRIPTOR = _CONFIRMATIONUPDATE,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.ConfirmationUpdate)
  ))
_sym_db.RegisterMessage(ConfirmationUpdate)

ChannelOpenUpdate = _reflection.GeneratedProtocolMessageType('ChannelOpenUpdate', (_message.Message,), dict(
  DESCRIPTOR = _CHANNELOPENUPDATE,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.ChannelOpenUpdate)
  ))
_sym_db.RegisterMessage(ChannelOpenUpdate)

ChannelCloseUpdate = _reflection.GeneratedProtocolMessageType('ChannelCloseUpdate', (_message.Message,), dict(
  DESCRIPTOR = _CHANNELCLOSEUPDATE,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.ChannelCloseUpdate)
  ))
_sym_db.RegisterMessage(ChannelCloseUpdate)

CloseChannelRequest = _reflection.GeneratedProtocolMessageType('CloseChannelRequest', (_message.Message,), dict(
  DESCRIPTOR = _CLOSECHANNELREQUEST,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.CloseChannelRequest)
  ))
_sym_db.RegisterMessage(CloseChannelRequest)

CloseStatusUpdate = _reflection.GeneratedProtocolMessageType('CloseStatusUpdate', (_message.Message,), dict(
  DESCRIPTOR = _CLOSESTATUSUPDATE,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.CloseStatusUpdate)
  ))
_sym_db.RegisterMessage(CloseStatusUpdate)

PendingUpdate = _reflection.GeneratedProtocolMessageType('PendingUpdate', (_message.Message,), dict(
  DESCRIPTOR = _PENDINGUPDATE,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.PendingUpdate)
  ))
_sym_db.RegisterMessage(PendingUpdate)

OpenChannelRequest = _reflection.GeneratedProtocolMessageType('OpenChannelRequest', (_message.Message,), dict(
  DESCRIPTOR = _OPENCHANNELREQUEST,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.OpenChannelRequest)
  ))
_sym_db.RegisterMessage(OpenChannelRequest)

OpenStatusUpdate = _reflection.GeneratedProtocolMessageType('OpenStatusUpdate', (_message.Message,), dict(
  DESCRIPTOR = _OPENSTATUSUPDATE,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.OpenStatusUpdate)
  ))
_sym_db.RegisterMessage(OpenStatusUpdate)

PendingHTLC = _reflection.GeneratedProtocolMessageType('PendingHTLC', (_message.Message,), dict(
  DESCRIPTOR = _PENDINGHTLC,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.PendingHTLC)
  ))
_sym_db.RegisterMessage(PendingHTLC)

PendingChannelsRequest = _reflection.GeneratedProtocolMessageType('PendingChannelsRequest', (_message.Message,), dict(
  DESCRIPTOR = _PENDINGCHANNELSREQUEST,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.PendingChannelsRequest)
  ))
_sym_db.RegisterMessage(PendingChannelsRequest)

PendingChannelsResponse = _reflection.GeneratedProtocolMessageType('PendingChannelsResponse', (_message.Message,), dict(

  PendingChannel = _reflection.GeneratedProtocolMessageType('PendingChannel', (_message.Message,), dict(
    DESCRIPTOR = _PENDINGCHANNELSRESPONSE_PENDINGCHANNEL,
    __module__ = 'rpc_pb2'
    # @@protoc_insertion_point(class_scope:lnrpc.PendingChannelsResponse.PendingChannel)
    ))
  ,

  PendingOpenChannel = _reflection.GeneratedProtocolMessageType('PendingOpenChannel', (_message.Message,), dict(
    DESCRIPTOR = _PENDINGCHANNELSRESPONSE_PENDINGOPENCHANNEL,
    __module__ = 'rpc_pb2'
    # @@protoc_insertion_point(class_scope:lnrpc.PendingChannelsResponse.PendingOpenChannel)
    ))
  ,

  WaitingCloseChannel = _reflection.GeneratedProtocolMessageType('WaitingCloseChannel', (_message.Message,), dict(
    DESCRIPTOR = _PENDINGCHANNELSRESPONSE_WAITINGCLOSECHANNEL,
    __module__ = 'rpc_pb2'
    # @@protoc_insertion_point(class_scope:lnrpc.PendingChannelsResponse.WaitingCloseChannel)
    ))
  ,

  ClosedChannel = _reflection.GeneratedProtocolMessageType('ClosedChannel', (_message.Message,), dict(
    DESCRIPTOR = _PENDINGCHANNELSRESPONSE_CLOSEDCHANNEL,
    __module__ = 'rpc_pb2'
    # @@protoc_insertion_point(class_scope:lnrpc.PendingChannelsResponse.ClosedChannel)
    ))
  ,

  ForceClosedChannel = _reflection.GeneratedProtocolMessageType('ForceClosedChannel', (_message.Message,), dict(
    DESCRIPTOR = _PENDINGCHANNELSRESPONSE_FORCECLOSEDCHANNEL,
    __module__ = 'rpc_pb2'
    # @@protoc_insertion_point(class_scope:lnrpc.PendingChannelsResponse.ForceClosedChannel)
    ))
  ,
  DESCRIPTOR = _PENDINGCHANNELSRESPONSE,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.PendingChannelsResponse)
  ))
_sym_db.RegisterMessage(PendingChannelsResponse)
_sym_db.RegisterMessage(PendingChannelsResponse.PendingChannel)
_sym_db.RegisterMessage(PendingChannelsResponse.PendingOpenChannel)
_sym_db.RegisterMessage(PendingChannelsResponse.WaitingCloseChannel)
_sym_db.RegisterMessage(PendingChannelsResponse.ClosedChannel)
_sym_db.RegisterMessage(PendingChannelsResponse.ForceClosedChannel)

WalletBalanceRequest = _reflection.GeneratedProtocolMessageType('WalletBalanceRequest', (_message.Message,), dict(
  DESCRIPTOR = _WALLETBALANCEREQUEST,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.WalletBalanceRequest)
  ))
_sym_db.RegisterMessage(WalletBalanceRequest)

WalletBalanceResponse = _reflection.GeneratedProtocolMessageType('WalletBalanceResponse', (_message.Message,), dict(
  DESCRIPTOR = _WALLETBALANCERESPONSE,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.WalletBalanceResponse)
  ))
_sym_db.RegisterMessage(WalletBalanceResponse)

ChannelBalanceRequest = _reflection.GeneratedProtocolMessageType('ChannelBalanceRequest', (_message.Message,), dict(
  DESCRIPTOR = _CHANNELBALANCEREQUEST,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.ChannelBalanceRequest)
  ))
_sym_db.RegisterMessage(ChannelBalanceRequest)

ChannelBalanceResponse = _reflection.GeneratedProtocolMessageType('ChannelBalanceResponse', (_message.Message,), dict(
  DESCRIPTOR = _CHANNELBALANCERESPONSE,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.ChannelBalanceResponse)
  ))
_sym_db.RegisterMessage(ChannelBalanceResponse)

QueryRoutesRequest = _reflection.GeneratedProtocolMessageType('QueryRoutesRequest', (_message.Message,), dict(
  DESCRIPTOR = _QUERYROUTESREQUEST,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.QueryRoutesRequest)
  ))
_sym_db.RegisterMessage(QueryRoutesRequest)

QueryRoutesResponse = _reflection.GeneratedProtocolMessageType('QueryRoutesResponse', (_message.Message,), dict(
  DESCRIPTOR = _QUERYROUTESRESPONSE,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.QueryRoutesResponse)
  ))
_sym_db.RegisterMessage(QueryRoutesResponse)

Hop = _reflection.GeneratedProtocolMessageType('Hop', (_message.Message,), dict(
  DESCRIPTOR = _HOP,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.Hop)
  ))
_sym_db.RegisterMessage(Hop)

Route = _reflection.GeneratedProtocolMessageType('Route', (_message.Message,), dict(
  DESCRIPTOR = _ROUTE,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.Route)
  ))
_sym_db.RegisterMessage(Route)

NodeInfoRequest = _reflection.GeneratedProtocolMessageType('NodeInfoRequest', (_message.Message,), dict(
  DESCRIPTOR = _NODEINFOREQUEST,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.NodeInfoRequest)
  ))
_sym_db.RegisterMessage(NodeInfoRequest)

NodeInfo = _reflection.GeneratedProtocolMessageType('NodeInfo', (_message.Message,), dict(
  DESCRIPTOR = _NODEINFO,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.NodeInfo)
  ))
_sym_db.RegisterMessage(NodeInfo)

LightningNode = _reflection.GeneratedProtocolMessageType('LightningNode', (_message.Message,), dict(
  DESCRIPTOR = _LIGHTNINGNODE,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.LightningNode)
  ))
_sym_db.RegisterMessage(LightningNode)

NodeAddress = _reflection.GeneratedProtocolMessageType('NodeAddress', (_message.Message,), dict(
  DESCRIPTOR = _NODEADDRESS,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.NodeAddress)
  ))
_sym_db.RegisterMessage(NodeAddress)

RoutingPolicy = _reflection.GeneratedProtocolMessageType('RoutingPolicy', (_message.Message,), dict(
  DESCRIPTOR = _ROUTINGPOLICY,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.RoutingPolicy)
  ))
_sym_db.RegisterMessage(RoutingPolicy)

ChannelEdge = _reflection.GeneratedProtocolMessageType('ChannelEdge', (_message.Message,), dict(
  DESCRIPTOR = _CHANNELEDGE,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.ChannelEdge)
  ))
_sym_db.RegisterMessage(ChannelEdge)

ChannelGraphRequest = _reflection.GeneratedProtocolMessageType('ChannelGraphRequest', (_message.Message,), dict(
  DESCRIPTOR = _CHANNELGRAPHREQUEST,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.ChannelGraphRequest)
  ))
_sym_db.RegisterMessage(ChannelGraphRequest)

ChannelGraph = _reflection.GeneratedProtocolMessageType('ChannelGraph', (_message.Message,), dict(
  DESCRIPTOR = _CHANNELGRAPH,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.ChannelGraph)
  ))
_sym_db.RegisterMessage(ChannelGraph)

ChanInfoRequest = _reflection.GeneratedProtocolMessageType('ChanInfoRequest', (_message.Message,), dict(
  DESCRIPTOR = _CHANINFOREQUEST,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.ChanInfoRequest)
  ))
_sym_db.RegisterMessage(ChanInfoRequest)

NetworkInfoRequest = _reflection.GeneratedProtocolMessageType('NetworkInfoRequest', (_message.Message,), dict(
  DESCRIPTOR = _NETWORKINFOREQUEST,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.NetworkInfoRequest)
  ))
_sym_db.RegisterMessage(NetworkInfoRequest)

NetworkInfo = _reflection.GeneratedProtocolMessageType('NetworkInfo', (_message.Message,), dict(
  DESCRIPTOR = _NETWORKINFO,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.NetworkInfo)
  ))
_sym_db.RegisterMessage(NetworkInfo)

StopRequest = _reflection.GeneratedProtocolMessageType('StopRequest', (_message.Message,), dict(
  DESCRIPTOR = _STOPREQUEST,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.StopRequest)
  ))
_sym_db.RegisterMessage(StopRequest)

StopResponse = _reflection.GeneratedProtocolMessageType('StopResponse', (_message.Message,), dict(
  DESCRIPTOR = _STOPRESPONSE,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.StopResponse)
  ))
_sym_db.RegisterMessage(StopResponse)

GraphTopologySubscription = _reflection.GeneratedProtocolMessageType('GraphTopologySubscription', (_message.Message,), dict(
  DESCRIPTOR = _GRAPHTOPOLOGYSUBSCRIPTION,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.GraphTopologySubscription)
  ))
_sym_db.RegisterMessage(GraphTopologySubscription)

GraphTopologyUpdate = _reflection.GeneratedProtocolMessageType('GraphTopologyUpdate', (_message.Message,), dict(
  DESCRIPTOR = _GRAPHTOPOLOGYUPDATE,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.GraphTopologyUpdate)
  ))
_sym_db.RegisterMessage(GraphTopologyUpdate)

NodeUpdate = _reflection.GeneratedProtocolMessageType('NodeUpdate', (_message.Message,), dict(
  DESCRIPTOR = _NODEUPDATE,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.NodeUpdate)
  ))
_sym_db.RegisterMessage(NodeUpdate)

ChannelEdgeUpdate = _reflection.GeneratedProtocolMessageType('ChannelEdgeUpdate', (_message.Message,), dict(
  DESCRIPTOR = _CHANNELEDGEUPDATE,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.ChannelEdgeUpdate)
  ))
_sym_db.RegisterMessage(ChannelEdgeUpdate)

ClosedChannelUpdate = _reflection.GeneratedProtocolMessageType('ClosedChannelUpdate', (_message.Message,), dict(
  DESCRIPTOR = _CLOSEDCHANNELUPDATE,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.ClosedChannelUpdate)
  ))
_sym_db.RegisterMessage(ClosedChannelUpdate)

HopHint = _reflection.GeneratedProtocolMessageType('HopHint', (_message.Message,), dict(
  DESCRIPTOR = _HOPHINT,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.HopHint)
  ))
_sym_db.RegisterMessage(HopHint)

RouteHint = _reflection.GeneratedProtocolMessageType('RouteHint', (_message.Message,), dict(
  DESCRIPTOR = _ROUTEHINT,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.RouteHint)
  ))
_sym_db.RegisterMessage(RouteHint)

Invoice = _reflection.GeneratedProtocolMessageType('Invoice', (_message.Message,), dict(
  DESCRIPTOR = _INVOICE,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.Invoice)
  ))
_sym_db.RegisterMessage(Invoice)

AddInvoiceResponse = _reflection.GeneratedProtocolMessageType('AddInvoiceResponse', (_message.Message,), dict(
  DESCRIPTOR = _ADDINVOICERESPONSE,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.AddInvoiceResponse)
  ))
_sym_db.RegisterMessage(AddInvoiceResponse)

PaymentHash = _reflection.GeneratedProtocolMessageType('PaymentHash', (_message.Message,), dict(
  DESCRIPTOR = _PAYMENTHASH,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.PaymentHash)
  ))
_sym_db.RegisterMessage(PaymentHash)

ListInvoiceRequest = _reflection.GeneratedProtocolMessageType('ListInvoiceRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTINVOICEREQUEST,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.ListInvoiceRequest)
  ))
_sym_db.RegisterMessage(ListInvoiceRequest)

ListInvoiceResponse = _reflection.GeneratedProtocolMessageType('ListInvoiceResponse', (_message.Message,), dict(
  DESCRIPTOR = _LISTINVOICERESPONSE,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.ListInvoiceResponse)
  ))
_sym_db.RegisterMessage(ListInvoiceResponse)

InvoiceSubscription = _reflection.GeneratedProtocolMessageType('InvoiceSubscription', (_message.Message,), dict(
  DESCRIPTOR = _INVOICESUBSCRIPTION,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.InvoiceSubscription)
  ))
_sym_db.RegisterMessage(InvoiceSubscription)

Payment = _reflection.GeneratedProtocolMessageType('Payment', (_message.Message,), dict(
  DESCRIPTOR = _PAYMENT,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.Payment)
  ))
_sym_db.RegisterMessage(Payment)

ListPaymentsRequest = _reflection.GeneratedProtocolMessageType('ListPaymentsRequest', (_message.Message,), dict(
  DESCRIPTOR = _LISTPAYMENTSREQUEST,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.ListPaymentsRequest)
  ))
_sym_db.RegisterMessage(ListPaymentsRequest)

ListPaymentsResponse = _reflection.GeneratedProtocolMessageType('ListPaymentsResponse', (_message.Message,), dict(
  DESCRIPTOR = _LISTPAYMENTSRESPONSE,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.ListPaymentsResponse)
  ))
_sym_db.RegisterMessage(ListPaymentsResponse)

DeleteAllPaymentsRequest = _reflection.GeneratedProtocolMessageType('DeleteAllPaymentsRequest', (_message.Message,), dict(
  DESCRIPTOR = _DELETEALLPAYMENTSREQUEST,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.DeleteAllPaymentsRequest)
  ))
_sym_db.RegisterMessage(DeleteAllPaymentsRequest)

DeleteAllPaymentsResponse = _reflection.GeneratedProtocolMessageType('DeleteAllPaymentsResponse', (_message.Message,), dict(
  DESCRIPTOR = _DELETEALLPAYMENTSRESPONSE,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.DeleteAllPaymentsResponse)
  ))
_sym_db.RegisterMessage(DeleteAllPaymentsResponse)

AbandonChannelRequest = _reflection.GeneratedProtocolMessageType('AbandonChannelRequest', (_message.Message,), dict(
  DESCRIPTOR = _ABANDONCHANNELREQUEST,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.AbandonChannelRequest)
  ))
_sym_db.RegisterMessage(AbandonChannelRequest)

AbandonChannelResponse = _reflection.GeneratedProtocolMessageType('AbandonChannelResponse', (_message.Message,), dict(
  DESCRIPTOR = _ABANDONCHANNELRESPONSE,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.AbandonChannelResponse)
  ))
_sym_db.RegisterMessage(AbandonChannelResponse)

DebugLevelRequest = _reflection.GeneratedProtocolMessageType('DebugLevelRequest', (_message.Message,), dict(
  DESCRIPTOR = _DEBUGLEVELREQUEST,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.DebugLevelRequest)
  ))
_sym_db.RegisterMessage(DebugLevelRequest)

DebugLevelResponse = _reflection.GeneratedProtocolMessageType('DebugLevelResponse', (_message.Message,), dict(
  DESCRIPTOR = _DEBUGLEVELRESPONSE,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.DebugLevelResponse)
  ))
_sym_db.RegisterMessage(DebugLevelResponse)

PayReqString = _reflection.GeneratedProtocolMessageType('PayReqString', (_message.Message,), dict(
  DESCRIPTOR = _PAYREQSTRING,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.PayReqString)
  ))
_sym_db.RegisterMessage(PayReqString)

PayReq = _reflection.GeneratedProtocolMessageType('PayReq', (_message.Message,), dict(
  DESCRIPTOR = _PAYREQ,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.PayReq)
  ))
_sym_db.RegisterMessage(PayReq)

FeeReportRequest = _reflection.GeneratedProtocolMessageType('FeeReportRequest', (_message.Message,), dict(
  DESCRIPTOR = _FEEREPORTREQUEST,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.FeeReportRequest)
  ))
_sym_db.RegisterMessage(FeeReportRequest)

ChannelFeeReport = _reflection.GeneratedProtocolMessageType('ChannelFeeReport', (_message.Message,), dict(
  DESCRIPTOR = _CHANNELFEEREPORT,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.ChannelFeeReport)
  ))
_sym_db.RegisterMessage(ChannelFeeReport)

FeeReportResponse = _reflection.GeneratedProtocolMessageType('FeeReportResponse', (_message.Message,), dict(
  DESCRIPTOR = _FEEREPORTRESPONSE,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.FeeReportResponse)
  ))
_sym_db.RegisterMessage(FeeReportResponse)

PolicyUpdateRequest = _reflection.GeneratedProtocolMessageType('PolicyUpdateRequest', (_message.Message,), dict(
  DESCRIPTOR = _POLICYUPDATEREQUEST,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.PolicyUpdateRequest)
  ))
_sym_db.RegisterMessage(PolicyUpdateRequest)

PolicyUpdateResponse = _reflection.GeneratedProtocolMessageType('PolicyUpdateResponse', (_message.Message,), dict(
  DESCRIPTOR = _POLICYUPDATERESPONSE,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.PolicyUpdateResponse)
  ))
_sym_db.RegisterMessage(PolicyUpdateResponse)

ForwardingHistoryRequest = _reflection.GeneratedProtocolMessageType('ForwardingHistoryRequest', (_message.Message,), dict(
  DESCRIPTOR = _FORWARDINGHISTORYREQUEST,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.ForwardingHistoryRequest)
  ))
_sym_db.RegisterMessage(ForwardingHistoryRequest)

ForwardingEvent = _reflection.GeneratedProtocolMessageType('ForwardingEvent', (_message.Message,), dict(
  DESCRIPTOR = _FORWARDINGEVENT,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.ForwardingEvent)
  ))
_sym_db.RegisterMessage(ForwardingEvent)

ForwardingHistoryResponse = _reflection.GeneratedProtocolMessageType('ForwardingHistoryResponse', (_message.Message,), dict(
  DESCRIPTOR = _FORWARDINGHISTORYRESPONSE,
  __module__ = 'rpc_pb2'
  # @@protoc_insertion_point(class_scope:lnrpc.ForwardingHistoryResponse)
  ))
_sym_db.RegisterMessage(ForwardingHistoryResponse)


_SENDMANYREQUEST_ADDRTOAMOUNTENTRY._options = None
_HOP.fields_by_name['amt_to_forward']._options = None
_HOP.fields_by_name['fee']._options = None
_ROUTE.fields_by_name['total_fees']._options = None
_ROUTE.fields_by_name['total_amt']._options = None
_INVOICE.fields_by_name['amt_paid']._options = None
_PAYMENT.fields_by_name['value']._options = None

_WALLETUNLOCKER = _descriptor.ServiceDescriptor(
  name='WalletUnlocker',
  full_name='lnrpc.WalletUnlocker',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=15214,
  serialized_end=15615,
  methods=[
  _descriptor.MethodDescriptor(
    name='GenSeed',
    full_name='lnrpc.WalletUnlocker.GenSeed',
    index=0,
    containing_service=None,
    input_type=_GENSEEDREQUEST,
    output_type=_GENSEEDRESPONSE,
    serialized_options=_b('\202\323\344\223\002\r\022\013/v1/genseed'),
  ),
  _descriptor.MethodDescriptor(
    name='InitWallet',
    full_name='lnrpc.WalletUnlocker.InitWallet',
    index=1,
    containing_service=None,
    input_type=_INITWALLETREQUEST,
    output_type=_INITWALLETRESPONSE,
    serialized_options=_b('\202\323\344\223\002\023\"\016/v1/initwallet:\001*'),
  ),
  _descriptor.MethodDescriptor(
    name='UnlockWallet',
    full_name='lnrpc.WalletUnlocker.UnlockWallet',
    index=2,
    containing_service=None,
    input_type=_UNLOCKWALLETREQUEST,
    output_type=_UNLOCKWALLETRESPONSE,
    serialized_options=_b('\202\323\344\223\002\025\"\020/v1/unlockwallet:\001*'),
  ),
  _descriptor.MethodDescriptor(
    name='ChangePassword',
    full_name='lnrpc.WalletUnlocker.ChangePassword',
    index=3,
    containing_service=None,
    input_type=_CHANGEPASSWORDREQUEST,
    output_type=_CHANGEPASSWORDRESPONSE,
    serialized_options=_b('\202\323\344\223\002\027\"\022/v1/changepassword:\001*'),
  ),
])
_sym_db.RegisterServiceDescriptor(_WALLETUNLOCKER)

DESCRIPTOR.services_by_name['WalletUnlocker'] = _WALLETUNLOCKER


_LIGHTNING = _descriptor.ServiceDescriptor(
  name='Lightning',
  full_name='lnrpc.Lightning',
  file=DESCRIPTOR,
  index=1,
  serialized_options=None,
  serialized_start=15618,
  serialized_end=19549,
  methods=[
  _descriptor.MethodDescriptor(
    name='WalletBalance',
    full_name='lnrpc.Lightning.WalletBalance',
    index=0,
    containing_service=None,
    input_type=_WALLETBALANCEREQUEST,
    output_type=_WALLETBALANCERESPONSE,
    serialized_options=_b('\202\323\344\223\002\030\022\026/v1/balance/blockchain'),
  ),
  _descriptor.MethodDescriptor(
    name='ChannelBalance',
    full_name='lnrpc.Lightning.ChannelBalance',
    index=1,
    containing_service=None,
    input_type=_CHANNELBALANCEREQUEST,
    output_type=_CHANNELBALANCERESPONSE,
    serialized_options=_b('\202\323\344\223\002\026\022\024/v1/balance/channels'),
  ),
  _descriptor.MethodDescriptor(
    name='GetTransactions',
    full_name='lnrpc.Lightning.GetTransactions',
    index=2,
    containing_service=None,
    input_type=_GETTRANSACTIONSREQUEST,
    output_type=_TRANSACTIONDETAILS,
    serialized_options=_b('\202\323\344\223\002\022\022\020/v1/transactions'),
  ),
  _descriptor.MethodDescriptor(
    name='SendCoins',
    full_name='lnrpc.Lightning.SendCoins',
    index=3,
    containing_service=None,
    input_type=_SENDCOINSREQUEST,
    output_type=_SENDCOINSRESPONSE,
    serialized_options=_b('\202\323\344\223\002\025\"\020/v1/transactions:\001*'),
  ),
  _descriptor.MethodDescriptor(
    name='SubscribeTransactions',
    full_name='lnrpc.Lightning.SubscribeTransactions',
    index=4,
    containing_service=None,
    input_type=_GETTRANSACTIONSREQUEST,
    output_type=_TRANSACTION,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SendMany',
    full_name='lnrpc.Lightning.SendMany',
    index=5,
    containing_service=None,
    input_type=_SENDMANYREQUEST,
    output_type=_SENDMANYRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='NewAddress',
    full_name='lnrpc.Lightning.NewAddress',
    index=6,
    containing_service=None,
    input_type=_NEWADDRESSREQUEST,
    output_type=_NEWADDRESSRESPONSE,
    serialized_options=_b('\202\323\344\223\002\020\022\016/v1/newaddress'),
  ),
  _descriptor.MethodDescriptor(
    name='SignMessage',
    full_name='lnrpc.Lightning.SignMessage',
    index=7,
    containing_service=None,
    input_type=_SIGNMESSAGEREQUEST,
    output_type=_SIGNMESSAGERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='VerifyMessage',
    full_name='lnrpc.Lightning.VerifyMessage',
    index=8,
    containing_service=None,
    input_type=_VERIFYMESSAGEREQUEST,
    output_type=_VERIFYMESSAGERESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='ConnectPeer',
    full_name='lnrpc.Lightning.ConnectPeer',
    index=9,
    containing_service=None,
    input_type=_CONNECTPEERREQUEST,
    output_type=_CONNECTPEERRESPONSE,
    serialized_options=_b('\202\323\344\223\002\016\"\t/v1/peers:\001*'),
  ),
  _descriptor.MethodDescriptor(
    name='DisconnectPeer',
    full_name='lnrpc.Lightning.DisconnectPeer',
    index=10,
    containing_service=None,
    input_type=_DISCONNECTPEERREQUEST,
    output_type=_DISCONNECTPEERRESPONSE,
    serialized_options=_b('\202\323\344\223\002\025*\023/v1/peers/{pub_key}'),
  ),
  _descriptor.MethodDescriptor(
    name='ListPeers',
    full_name='lnrpc.Lightning.ListPeers',
    index=11,
    containing_service=None,
    input_type=_LISTPEERSREQUEST,
    output_type=_LISTPEERSRESPONSE,
    serialized_options=_b('\202\323\344\223\002\013\022\t/v1/peers'),
  ),
  _descriptor.MethodDescriptor(
    name='GetInfo',
    full_name='lnrpc.Lightning.GetInfo',
    index=12,
    containing_service=None,
    input_type=_GETINFOREQUEST,
    output_type=_GETINFORESPONSE,
    serialized_options=_b('\202\323\344\223\002\r\022\013/v1/getinfo'),
  ),
  _descriptor.MethodDescriptor(
    name='PendingChannels',
    full_name='lnrpc.Lightning.PendingChannels',
    index=13,
    containing_service=None,
    input_type=_PENDINGCHANNELSREQUEST,
    output_type=_PENDINGCHANNELSRESPONSE,
    serialized_options=_b('\202\323\344\223\002\026\022\024/v1/channels/pending'),
  ),
  _descriptor.MethodDescriptor(
    name='ListChannels',
    full_name='lnrpc.Lightning.ListChannels',
    index=14,
    containing_service=None,
    input_type=_LISTCHANNELSREQUEST,
    output_type=_LISTCHANNELSRESPONSE,
    serialized_options=_b('\202\323\344\223\002\016\022\014/v1/channels'),
  ),
  _descriptor.MethodDescriptor(
    name='ClosedChannels',
    full_name='lnrpc.Lightning.ClosedChannels',
    index=15,
    containing_service=None,
    input_type=_CLOSEDCHANNELSREQUEST,
    output_type=_CLOSEDCHANNELSRESPONSE,
    serialized_options=_b('\202\323\344\223\002\025\022\023/v1/channels/closed'),
  ),
  _descriptor.MethodDescriptor(
    name='OpenChannelSync',
    full_name='lnrpc.Lightning.OpenChannelSync',
    index=16,
    containing_service=None,
    input_type=_OPENCHANNELREQUEST,
    output_type=_CHANNELPOINT,
    serialized_options=_b('\202\323\344\223\002\021\"\014/v1/channels:\001*'),
  ),
  _descriptor.MethodDescriptor(
    name='OpenChannel',
    full_name='lnrpc.Lightning.OpenChannel',
    index=17,
    containing_service=None,
    input_type=_OPENCHANNELREQUEST,
    output_type=_OPENSTATUSUPDATE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='CloseChannel',
    full_name='lnrpc.Lightning.CloseChannel',
    index=18,
    containing_service=None,
    input_type=_CLOSECHANNELREQUEST,
    output_type=_CLOSESTATUSUPDATE,
    serialized_options=_b('\202\323\344\223\002L*J/v1/channels/{channel_point.funding_txid_str}/{channel_point.output_index}'),
  ),
  _descriptor.MethodDescriptor(
    name='AbandonChannel',
    full_name='lnrpc.Lightning.AbandonChannel',
    index=19,
    containing_service=None,
    input_type=_ABANDONCHANNELREQUEST,
    output_type=_ABANDONCHANNELRESPONSE,
    serialized_options=_b('\202\323\344\223\002T*R/v1/channels/abandon/{channel_point.funding_txid_str}/{channel_point.output_index}'),
  ),
  _descriptor.MethodDescriptor(
    name='SendPayment',
    full_name='lnrpc.Lightning.SendPayment',
    index=20,
    containing_service=None,
    input_type=_SENDREQUEST,
    output_type=_SENDRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SendPaymentSync',
    full_name='lnrpc.Lightning.SendPaymentSync',
    index=21,
    containing_service=None,
    input_type=_SENDREQUEST,
    output_type=_SENDRESPONSE,
    serialized_options=_b('\202\323\344\223\002\036\"\031/v1/channels/transactions:\001*'),
  ),
  _descriptor.MethodDescriptor(
    name='SendToRoute',
    full_name='lnrpc.Lightning.SendToRoute',
    index=22,
    containing_service=None,
    input_type=_SENDTOROUTEREQUEST,
    output_type=_SENDRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SendToRouteSync',
    full_name='lnrpc.Lightning.SendToRouteSync',
    index=23,
    containing_service=None,
    input_type=_SENDTOROUTEREQUEST,
    output_type=_SENDRESPONSE,
    serialized_options=_b('\202\323\344\223\002$\"\037/v1/channels/transactions/route:\001*'),
  ),
  _descriptor.MethodDescriptor(
    name='AddInvoice',
    full_name='lnrpc.Lightning.AddInvoice',
    index=24,
    containing_service=None,
    input_type=_INVOICE,
    output_type=_ADDINVOICERESPONSE,
    serialized_options=_b('\202\323\344\223\002\021\"\014/v1/invoices:\001*'),
  ),
  _descriptor.MethodDescriptor(
    name='ListInvoices',
    full_name='lnrpc.Lightning.ListInvoices',
    index=25,
    containing_service=None,
    input_type=_LISTINVOICEREQUEST,
    output_type=_LISTINVOICERESPONSE,
    serialized_options=_b('\202\323\344\223\002\016\022\014/v1/invoices'),
  ),
  _descriptor.MethodDescriptor(
    name='LookupInvoice',
    full_name='lnrpc.Lightning.LookupInvoice',
    index=26,
    containing_service=None,
    input_type=_PAYMENTHASH,
    output_type=_INVOICE,
    serialized_options=_b('\202\323\344\223\002\032\022\030/v1/invoice/{r_hash_str}'),
  ),
  _descriptor.MethodDescriptor(
    name='SubscribeInvoices',
    full_name='lnrpc.Lightning.SubscribeInvoices',
    index=27,
    containing_service=None,
    input_type=_INVOICESUBSCRIPTION,
    output_type=_INVOICE,
    serialized_options=_b('\202\323\344\223\002\030\022\026/v1/invoices/subscribe'),
  ),
  _descriptor.MethodDescriptor(
    name='DecodePayReq',
    full_name='lnrpc.Lightning.DecodePayReq',
    index=28,
    containing_service=None,
    input_type=_PAYREQSTRING,
    output_type=_PAYREQ,
    serialized_options=_b('\202\323\344\223\002\026\022\024/v1/payreq/{pay_req}'),
  ),
  _descriptor.MethodDescriptor(
    name='ListPayments',
    full_name='lnrpc.Lightning.ListPayments',
    index=29,
    containing_service=None,
    input_type=_LISTPAYMENTSREQUEST,
    output_type=_LISTPAYMENTSRESPONSE,
    serialized_options=_b('\202\323\344\223\002\016\022\014/v1/payments'),
  ),
  _descriptor.MethodDescriptor(
    name='DeleteAllPayments',
    full_name='lnrpc.Lightning.DeleteAllPayments',
    index=30,
    containing_service=None,
    input_type=_DELETEALLPAYMENTSREQUEST,
    output_type=_DELETEALLPAYMENTSRESPONSE,
    serialized_options=_b('\202\323\344\223\002\016*\014/v1/payments'),
  ),
  _descriptor.MethodDescriptor(
    name='DescribeGraph',
    full_name='lnrpc.Lightning.DescribeGraph',
    index=31,
    containing_service=None,
    input_type=_CHANNELGRAPHREQUEST,
    output_type=_CHANNELGRAPH,
    serialized_options=_b('\202\323\344\223\002\013\022\t/v1/graph'),
  ),
  _descriptor.MethodDescriptor(
    name='GetChanInfo',
    full_name='lnrpc.Lightning.GetChanInfo',
    index=32,
    containing_service=None,
    input_type=_CHANINFOREQUEST,
    output_type=_CHANNELEDGE,
    serialized_options=_b('\202\323\344\223\002\032\022\030/v1/graph/edge/{chan_id}'),
  ),
  _descriptor.MethodDescriptor(
    name='GetNodeInfo',
    full_name='lnrpc.Lightning.GetNodeInfo',
    index=33,
    containing_service=None,
    input_type=_NODEINFOREQUEST,
    output_type=_NODEINFO,
    serialized_options=_b('\202\323\344\223\002\032\022\030/v1/graph/node/{pub_key}'),
  ),
  _descriptor.MethodDescriptor(
    name='QueryRoutes',
    full_name='lnrpc.Lightning.QueryRoutes',
    index=34,
    containing_service=None,
    input_type=_QUERYROUTESREQUEST,
    output_type=_QUERYROUTESRESPONSE,
    serialized_options=_b('\202\323\344\223\002\"\022 /v1/graph/routes/{pub_key}/{amt}'),
  ),
  _descriptor.MethodDescriptor(
    name='GetNetworkInfo',
    full_name='lnrpc.Lightning.GetNetworkInfo',
    index=35,
    containing_service=None,
    input_type=_NETWORKINFOREQUEST,
    output_type=_NETWORKINFO,
    serialized_options=_b('\202\323\344\223\002\020\022\016/v1/graph/info'),
  ),
  _descriptor.MethodDescriptor(
    name='StopDaemon',
    full_name='lnrpc.Lightning.StopDaemon',
    index=36,
    containing_service=None,
    input_type=_STOPREQUEST,
    output_type=_STOPRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='SubscribeChannelGraph',
    full_name='lnrpc.Lightning.SubscribeChannelGraph',
    index=37,
    containing_service=None,
    input_type=_GRAPHTOPOLOGYSUBSCRIPTION,
    output_type=_GRAPHTOPOLOGYUPDATE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='DebugLevel',
    full_name='lnrpc.Lightning.DebugLevel',
    index=38,
    containing_service=None,
    input_type=_DEBUGLEVELREQUEST,
    output_type=_DEBUGLEVELRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='FeeReport',
    full_name='lnrpc.Lightning.FeeReport',
    index=39,
    containing_service=None,
    input_type=_FEEREPORTREQUEST,
    output_type=_FEEREPORTRESPONSE,
    serialized_options=_b('\202\323\344\223\002\n\022\010/v1/fees'),
  ),
  _descriptor.MethodDescriptor(
    name='UpdateChannelPolicy',
    full_name='lnrpc.Lightning.UpdateChannelPolicy',
    index=40,
    containing_service=None,
    input_type=_POLICYUPDATEREQUEST,
    output_type=_POLICYUPDATERESPONSE,
    serialized_options=_b('\202\323\344\223\002\023\"\016/v1/chanpolicy:\001*'),
  ),
  _descriptor.MethodDescriptor(
    name='ForwardingHistory',
    full_name='lnrpc.Lightning.ForwardingHistory',
    index=41,
    containing_service=None,
    input_type=_FORWARDINGHISTORYREQUEST,
    output_type=_FORWARDINGHISTORYRESPONSE,
    serialized_options=_b('\202\323\344\223\002\017\"\n/v1/switch:\001*'),
  ),
])
_sym_db.RegisterServiceDescriptor(_LIGHTNING)

DESCRIPTOR.services_by_name['Lightning'] = _LIGHTNING

# @@protoc_insertion_point(module_scope)