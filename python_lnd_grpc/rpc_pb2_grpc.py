import grpc

from python_lnd_grpc import rpc_pb2 as rpc__pb2


class WalletUnlockerStub(object):
  """The WalletUnlocker service is used to set up a wallet password for
  lnd at first startup, and unlock a previously set up wallet.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GenSeed = channel.unary_unary(
        '/lnrpc.WalletUnlocker/GenSeed',
        request_serializer=rpc__pb2.GenSeedRequest.SerializeToString,
        response_deserializer=rpc__pb2.GenSeedResponse.FromString,
        )
    self.InitWallet = channel.unary_unary(
        '/lnrpc.WalletUnlocker/InitWallet',
        request_serializer=rpc__pb2.InitWalletRequest.SerializeToString,
        response_deserializer=rpc__pb2.InitWalletResponse.FromString,
        )
    self.UnlockWallet = channel.unary_unary(
        '/lnrpc.WalletUnlocker/UnlockWallet',
        request_serializer=rpc__pb2.UnlockWalletRequest.SerializeToString,
        response_deserializer=rpc__pb2.UnlockWalletResponse.FromString,
        )
    self.ChangePassword = channel.unary_unary(
        '/lnrpc.WalletUnlocker/ChangePassword',
        request_serializer=rpc__pb2.ChangePasswordRequest.SerializeToString,
        response_deserializer=rpc__pb2.ChangePasswordResponse.FromString,
        )


class WalletUnlockerServicer(object):
  """The WalletUnlocker service is used to set up a wallet password for
  lnd at first startup, and unlock a previously set up wallet.
  """

  def GenSeed(self, request, context):
    """*
    GenSeed is the first method that should be used to instantiate a new lnd
    instance. This method allows a caller to generate a new aezeed cipher seed
    given an optional passphrase. If provided, the passphrase will be necessary
    to decrypt the cipherseed to expose the internal wallet seed.

    Once the cipherseed is obtained and verified by the user, the InitWallet
    method should be used to commit the newly generated seed, and create the
    wallet.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def InitWallet(self, request, context):
    """*
    InitWallet is used when lnd is starting up for the first time to fully
    initialize the daemon and its internal wallet. At the very least a wallet
    password must be provided. This will be used to encrypt sensitive material
    on disk.

    In the case of a recovery scenario, the user can also specify their aezeed
    mnemonic and passphrase. If set, then the daemon will use this prior state
    to initialize its internal wallet.

    Alternatively, this can be used along with the GenSeed RPC to obtain a
    seed, then present it to the user. Once it has been verified by the user,
    the seed can be fed into this RPC in order to commit the new wallet.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UnlockWallet(self, request, context):
    """* lncli: `unlock`
    UnlockWallet is used at startup of lnd to provide a password to unlock
    the wallet database.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ChangePassword(self, request, context):
    """* lncli: `changepassword`
    ChangePassword changes the password of the encrypted wallet. This will
    automatically unlock the wallet database if successful.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_WalletUnlockerServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GenSeed': grpc.unary_unary_rpc_method_handler(
          servicer.GenSeed,
          request_deserializer=rpc__pb2.GenSeedRequest.FromString,
          response_serializer=rpc__pb2.GenSeedResponse.SerializeToString,
      ),
      'InitWallet': grpc.unary_unary_rpc_method_handler(
          servicer.InitWallet,
          request_deserializer=rpc__pb2.InitWalletRequest.FromString,
          response_serializer=rpc__pb2.InitWalletResponse.SerializeToString,
      ),
      'UnlockWallet': grpc.unary_unary_rpc_method_handler(
          servicer.UnlockWallet,
          request_deserializer=rpc__pb2.UnlockWalletRequest.FromString,
          response_serializer=rpc__pb2.UnlockWalletResponse.SerializeToString,
      ),
      'ChangePassword': grpc.unary_unary_rpc_method_handler(
          servicer.ChangePassword,
          request_deserializer=rpc__pb2.ChangePasswordRequest.FromString,
          response_serializer=rpc__pb2.ChangePasswordResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'lnrpc.WalletUnlocker', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class LightningStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.WalletBalance = channel.unary_unary(
        '/lnrpc.Lightning/WalletBalance',
        request_serializer=rpc__pb2.WalletBalanceRequest.SerializeToString,
        response_deserializer=rpc__pb2.WalletBalanceResponse.FromString,
        )
    self.ChannelBalance = channel.unary_unary(
        '/lnrpc.Lightning/ChannelBalance',
        request_serializer=rpc__pb2.ChannelBalanceRequest.SerializeToString,
        response_deserializer=rpc__pb2.ChannelBalanceResponse.FromString,
        )
    self.GetTransactions = channel.unary_unary(
        '/lnrpc.Lightning/GetTransactions',
        request_serializer=rpc__pb2.GetTransactionsRequest.SerializeToString,
        response_deserializer=rpc__pb2.TransactionDetails.FromString,
        )
    self.SendCoins = channel.unary_unary(
        '/lnrpc.Lightning/SendCoins',
        request_serializer=rpc__pb2.SendCoinsRequest.SerializeToString,
        response_deserializer=rpc__pb2.SendCoinsResponse.FromString,
        )
    self.SubscribeTransactions = channel.unary_stream(
        '/lnrpc.Lightning/SubscribeTransactions',
        request_serializer=rpc__pb2.GetTransactionsRequest.SerializeToString,
        response_deserializer=rpc__pb2.Transaction.FromString,
        )
    self.SendMany = channel.unary_unary(
        '/lnrpc.Lightning/SendMany',
        request_serializer=rpc__pb2.SendManyRequest.SerializeToString,
        response_deserializer=rpc__pb2.SendManyResponse.FromString,
        )
    self.NewAddress = channel.unary_unary(
        '/lnrpc.Lightning/NewAddress',
        request_serializer=rpc__pb2.NewAddressRequest.SerializeToString,
        response_deserializer=rpc__pb2.NewAddressResponse.FromString,
        )
    self.SignMessage = channel.unary_unary(
        '/lnrpc.Lightning/SignMessage',
        request_serializer=rpc__pb2.SignMessageRequest.SerializeToString,
        response_deserializer=rpc__pb2.SignMessageResponse.FromString,
        )
    self.VerifyMessage = channel.unary_unary(
        '/lnrpc.Lightning/VerifyMessage',
        request_serializer=rpc__pb2.VerifyMessageRequest.SerializeToString,
        response_deserializer=rpc__pb2.VerifyMessageResponse.FromString,
        )
    self.ConnectPeer = channel.unary_unary(
        '/lnrpc.Lightning/ConnectPeer',
        request_serializer=rpc__pb2.ConnectPeerRequest.SerializeToString,
        response_deserializer=rpc__pb2.ConnectPeerResponse.FromString,
        )
    self.DisconnectPeer = channel.unary_unary(
        '/lnrpc.Lightning/DisconnectPeer',
        request_serializer=rpc__pb2.DisconnectPeerRequest.SerializeToString,
        response_deserializer=rpc__pb2.DisconnectPeerResponse.FromString,
        )
    self.ListPeers = channel.unary_unary(
        '/lnrpc.Lightning/ListPeers',
        request_serializer=rpc__pb2.ListPeersRequest.SerializeToString,
        response_deserializer=rpc__pb2.ListPeersResponse.FromString,
        )
    self.GetInfo = channel.unary_unary(
        '/lnrpc.Lightning/GetInfo',
        request_serializer=rpc__pb2.GetInfoRequest.SerializeToString,
        response_deserializer=rpc__pb2.GetInfoResponse.FromString,
        )
    self.PendingChannels = channel.unary_unary(
        '/lnrpc.Lightning/PendingChannels',
        request_serializer=rpc__pb2.PendingChannelsRequest.SerializeToString,
        response_deserializer=rpc__pb2.PendingChannelsResponse.FromString,
        )
    self.ListChannels = channel.unary_unary(
        '/lnrpc.Lightning/ListChannels',
        request_serializer=rpc__pb2.ListChannelsRequest.SerializeToString,
        response_deserializer=rpc__pb2.ListChannelsResponse.FromString,
        )
    self.ClosedChannels = channel.unary_unary(
        '/lnrpc.Lightning/ClosedChannels',
        request_serializer=rpc__pb2.ClosedChannelsRequest.SerializeToString,
        response_deserializer=rpc__pb2.ClosedChannelsResponse.FromString,
        )
    self.OpenChannelSync = channel.unary_unary(
        '/lnrpc.Lightning/OpenChannelSync',
        request_serializer=rpc__pb2.OpenChannelRequest.SerializeToString,
        response_deserializer=rpc__pb2.ChannelPoint.FromString,
        )
    self.OpenChannel = channel.unary_stream(
        '/lnrpc.Lightning/OpenChannel',
        request_serializer=rpc__pb2.OpenChannelRequest.SerializeToString,
        response_deserializer=rpc__pb2.OpenStatusUpdate.FromString,
        )
    self.CloseChannel = channel.unary_stream(
        '/lnrpc.Lightning/CloseChannel',
        request_serializer=rpc__pb2.CloseChannelRequest.SerializeToString,
        response_deserializer=rpc__pb2.CloseStatusUpdate.FromString,
        )
    self.AbandonChannel = channel.unary_unary(
        '/lnrpc.Lightning/AbandonChannel',
        request_serializer=rpc__pb2.AbandonChannelRequest.SerializeToString,
        response_deserializer=rpc__pb2.AbandonChannelResponse.FromString,
        )
    self.SendPayment = channel.stream_stream(
        '/lnrpc.Lightning/SendPayment',
        request_serializer=rpc__pb2.SendRequest.SerializeToString,
        response_deserializer=rpc__pb2.SendResponse.FromString,
        )
    self.SendPaymentSync = channel.unary_unary(
        '/lnrpc.Lightning/SendPaymentSync',
        request_serializer=rpc__pb2.SendRequest.SerializeToString,
        response_deserializer=rpc__pb2.SendResponse.FromString,
        )
    self.SendToRoute = channel.stream_stream(
        '/lnrpc.Lightning/SendToRoute',
        request_serializer=rpc__pb2.SendToRouteRequest.SerializeToString,
        response_deserializer=rpc__pb2.SendResponse.FromString,
        )
    self.SendToRouteSync = channel.unary_unary(
        '/lnrpc.Lightning/SendToRouteSync',
        request_serializer=rpc__pb2.SendToRouteRequest.SerializeToString,
        response_deserializer=rpc__pb2.SendResponse.FromString,
        )
    self.AddInvoice = channel.unary_unary(
        '/lnrpc.Lightning/AddInvoice',
        request_serializer=rpc__pb2.Invoice.SerializeToString,
        response_deserializer=rpc__pb2.AddInvoiceResponse.FromString,
        )
    self.ListInvoices = channel.unary_unary(
        '/lnrpc.Lightning/ListInvoices',
        request_serializer=rpc__pb2.ListInvoiceRequest.SerializeToString,
        response_deserializer=rpc__pb2.ListInvoiceResponse.FromString,
        )
    self.LookupInvoice = channel.unary_unary(
        '/lnrpc.Lightning/LookupInvoice',
        request_serializer=rpc__pb2.PaymentHash.SerializeToString,
        response_deserializer=rpc__pb2.Invoice.FromString,
        )
    self.SubscribeInvoices = channel.unary_stream(
        '/lnrpc.Lightning/SubscribeInvoices',
        request_serializer=rpc__pb2.InvoiceSubscription.SerializeToString,
        response_deserializer=rpc__pb2.Invoice.FromString,
        )
    self.DecodePayReq = channel.unary_unary(
        '/lnrpc.Lightning/DecodePayReq',
        request_serializer=rpc__pb2.PayReqString.SerializeToString,
        response_deserializer=rpc__pb2.PayReq.FromString,
        )
    self.ListPayments = channel.unary_unary(
        '/lnrpc.Lightning/ListPayments',
        request_serializer=rpc__pb2.ListPaymentsRequest.SerializeToString,
        response_deserializer=rpc__pb2.ListPaymentsResponse.FromString,
        )
    self.DeleteAllPayments = channel.unary_unary(
        '/lnrpc.Lightning/DeleteAllPayments',
        request_serializer=rpc__pb2.DeleteAllPaymentsRequest.SerializeToString,
        response_deserializer=rpc__pb2.DeleteAllPaymentsResponse.FromString,
        )
    self.DescribeGraph = channel.unary_unary(
        '/lnrpc.Lightning/DescribeGraph',
        request_serializer=rpc__pb2.ChannelGraphRequest.SerializeToString,
        response_deserializer=rpc__pb2.ChannelGraph.FromString,
        )
    self.GetChanInfo = channel.unary_unary(
        '/lnrpc.Lightning/GetChanInfo',
        request_serializer=rpc__pb2.ChanInfoRequest.SerializeToString,
        response_deserializer=rpc__pb2.ChannelEdge.FromString,
        )
    self.GetNodeInfo = channel.unary_unary(
        '/lnrpc.Lightning/GetNodeInfo',
        request_serializer=rpc__pb2.NodeInfoRequest.SerializeToString,
        response_deserializer=rpc__pb2.NodeInfo.FromString,
        )
    self.QueryRoutes = channel.unary_unary(
        '/lnrpc.Lightning/QueryRoutes',
        request_serializer=rpc__pb2.QueryRoutesRequest.SerializeToString,
        response_deserializer=rpc__pb2.QueryRoutesResponse.FromString,
        )
    self.GetNetworkInfo = channel.unary_unary(
        '/lnrpc.Lightning/GetNetworkInfo',
        request_serializer=rpc__pb2.NetworkInfoRequest.SerializeToString,
        response_deserializer=rpc__pb2.NetworkInfo.FromString,
        )
    self.StopDaemon = channel.unary_unary(
        '/lnrpc.Lightning/StopDaemon',
        request_serializer=rpc__pb2.StopRequest.SerializeToString,
        response_deserializer=rpc__pb2.StopResponse.FromString,
        )
    self.SubscribeChannelGraph = channel.unary_stream(
        '/lnrpc.Lightning/SubscribeChannelGraph',
        request_serializer=rpc__pb2.GraphTopologySubscription.SerializeToString,
        response_deserializer=rpc__pb2.GraphTopologyUpdate.FromString,
        )
    self.DebugLevel = channel.unary_unary(
        '/lnrpc.Lightning/DebugLevel',
        request_serializer=rpc__pb2.DebugLevelRequest.SerializeToString,
        response_deserializer=rpc__pb2.DebugLevelResponse.FromString,
        )
    self.FeeReport = channel.unary_unary(
        '/lnrpc.Lightning/FeeReport',
        request_serializer=rpc__pb2.FeeReportRequest.SerializeToString,
        response_deserializer=rpc__pb2.FeeReportResponse.FromString,
        )
    self.UpdateChannelPolicy = channel.unary_unary(
        '/lnrpc.Lightning/UpdateChannelPolicy',
        request_serializer=rpc__pb2.PolicyUpdateRequest.SerializeToString,
        response_deserializer=rpc__pb2.PolicyUpdateResponse.FromString,
        )
    self.ForwardingHistory = channel.unary_unary(
        '/lnrpc.Lightning/ForwardingHistory',
        request_serializer=rpc__pb2.ForwardingHistoryRequest.SerializeToString,
        response_deserializer=rpc__pb2.ForwardingHistoryResponse.FromString,
        )


class LightningServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def WalletBalance(self, request, context):
    """* lncli: `walletbalance`
    WalletBalance returns total unspent outputs(confirmed and unconfirmed), all
    confirmed unspent outputs and all unconfirmed unspent outputs under control
    of the wallet.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ChannelBalance(self, request, context):
    """* lncli: `channelbalance`
    ChannelBalance returns the total funds available across all open channels
    in satoshis.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetTransactions(self, request, context):
    """* lncli: `listchaintxns`
    GetTransactions returns a list describing all the known transactions
    relevant to the wallet.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SendCoins(self, request, context):
    """* lncli: `sendcoins`
    SendCoins executes a request to send coins to a particular address. Unlike
    SendMany, this RPC call only allows creating a single output at a time. If
    neither target_conf, or sat_per_byte are set, then the internal wallet will
    consult its fee model to determine a fee for the default confirmation
    target.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SubscribeTransactions(self, request, context):
    """*
    SubscribeTransactions creates a uni-directional stream from the server to
    the client in which any newly discovered transactions relevant to the
    wallet are sent over.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SendMany(self, request, context):
    """* lncli: `sendmany`
    SendMany handles a request for a transaction that creates multiple specified
    outputs in parallel. If neither target_conf, or sat_per_byte are set, then
    the internal wallet will consult its fee model to determine a fee for the
    default confirmation target.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def NewAddress(self, request, context):
    """* lncli: `newaddress`
    NewAddress creates a new address under control of the local wallet.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SignMessage(self, request, context):
    """* lncli: `signmessage`
    SignMessage signs a message with this node's private key. The returned
    signature string is `zbase32` encoded and pubkey recoverable, meaning that
    only the message digest and signature are needed for verification.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def VerifyMessage(self, request, context):
    """* lncli: `verifymessage`
    VerifyMessage verifies a signature over a msg. The signature must be
    zbase32 encoded and signed by an active node in the resident node's
    channel database. In addition to returning the validity of the signature,
    VerifyMessage also returns the recovered pubkey from the signature.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ConnectPeer(self, request, context):
    """* lncli: `connect`
    ConnectPeer attempts to establish a connection to a remote peer. This is at
    the networking level, and is used for communication between nodes. This is
    distinct from establishing a channel with a peer.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DisconnectPeer(self, request, context):
    """* lncli: `disconnect`
    DisconnectPeer attempts to disconnect one peer from another identified by a
    given pubKey. In the case that we currently have a pending or active channel
    with the target peer, then this action will be not be allowed.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListPeers(self, request, context):
    """* lncli: `listpeers`
    ListPeers returns a verbose listing of all currently active peers.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetInfo(self, request, context):
    """* lncli: `getinfo`
    GetInfo returns general information concerning the lightning node including
    it's identity pubkey, alias, the chains it is connected to, and information
    concerning the number of open+pending channels.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def PendingChannels(self, request, context):
    """TODO(roasbeef): merge with below with bool?

    * lncli: `pendingchannels`
    PendingChannels returns a list of all the channels that are currently
    considered "pending". A channel is pending if it has finished the funding
    workflow and is waiting for confirmations for the funding txn, or is in the
    process of closure, either initiated cooperatively or non-cooperatively.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListChannels(self, request, context):
    """* lncli: `listchannels`
    ListChannels returns a description of all the open channels that this node
    is a participant in.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ClosedChannels(self, request, context):
    """* lncli: `closedchannels`
    ClosedChannels returns a description of all the closed channels that
    this node was a participant in.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def OpenChannelSync(self, request, context):
    """*
    OpenChannelSync is a synchronous version of the OpenChannel RPC call. This
    call is meant to be consumed by clients to the REST proxy. As with all
    other sync calls, all byte slices are intended to be populated as hex
    encoded strings.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def OpenChannel(self, request, context):
    """* lncli: `openchannel`
    OpenChannel attempts to open a singly funded channel specified in the
    request to a remote peer. Users are able to specify a target number of
    blocks that the funding transaction should be confirmed in, or a manual fee
    rate to us for the funding transaction. If neither are specified, then a
    lax block confirmation target is used.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def CloseChannel(self, request, context):
    """* lncli: `closechannel`
    CloseChannel attempts to close an active channel identified by its channel
    outpoint (ChannelPoint). The actions of this method can additionally be
    augmented to attempt a force close after a timeout period in the case of an
    inactive peer. If a non-force close (cooperative closure) is requested,
    then the user can specify either a target number of blocks until the
    closure transaction is confirmed, or a manual fee rate. If neither are
    specified, then a default lax, block confirmation target is used.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AbandonChannel(self, request, context):
    """* lncli: `abandonchannel`
    AbandonChannel removes all channel state from the database except for a
    close summary. This method can be used to get rid of permanently unusable
    channels due to bugs fixed in newer versions of lnd. Only available
    when in debug builds of lnd.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SendPayment(self, request_iterator, context):
    """* lncli: `sendpayment`
    SendPayment dispatches a bi-directional streaming RPC for sending payments
    through the Lightning Network. A single RPC invocation creates a persistent
    bi-directional stream allowing clients to rapidly send payments through the
    Lightning Network with a single persistent connection.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SendPaymentSync(self, request, context):
    """*
    SendPaymentSync is the synchronous non-streaming version of SendPayment.
    This RPC is intended to be consumed by clients of the REST proxy.
    Additionally, this RPC expects the destination's public key and the payment
    hash (if any) to be encoded as hex strings.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SendToRoute(self, request_iterator, context):
    """* lncli: `sendtoroute`
    SendToRoute is a bi-directional streaming RPC for sending payment through
    the Lightning Network. This method differs from SendPayment in that it
    allows users to specify a full route manually. This can be used for things
    like rebalancing, and atomic swaps.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SendToRouteSync(self, request, context):
    """*
    SendToRouteSync is a synchronous version of SendToRoute. It Will block
    until the payment either fails or succeeds.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AddInvoice(self, request, context):
    """* lncli: `addinvoice`
    AddInvoice attempts to add a new invoice to the invoice database. Any
    duplicated invoices are rejected, therefore all invoices *must* have a
    unique payment preimage.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListInvoices(self, request, context):
    """* lncli: `listinvoices`
    ListInvoices returns a list of all the invoices currently stored within the
    database. Any active debug invoices are ignored. It has full support for
    paginated responses, allowing users to query for specific invoices through
    their add_index. This can be done by using either the first_index_offset or
    last_index_offset fields included in the response as the index_offset of the
    next request. The reversed flag is set by default in order to paginate
    backwards. If you wish to paginate forwards, you must explicitly set the
    flag to false. If none of the parameters are specified, then the last 100
    invoices will be returned.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def LookupInvoice(self, request, context):
    """* lncli: `lookupinvoice`
    LookupInvoice attempts to look up an invoice according to its payment hash.
    The passed payment hash *must* be exactly 32 bytes, if not, an error is
    returned.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SubscribeInvoices(self, request, context):
    """*
    SubscribeInvoices returns a uni-directional stream (server -> client) for
    notifying the client of newly added/settled invoices. The caller can
    optionally specify the add_index and/or the settle_index. If the add_index
    is specified, then we'll first start by sending add invoice events for all
    invoices with an add_index greater than the specified value.  If the
    settle_index is specified, the next, we'll send out all settle events for
    invoices with a settle_index greater than the specified value.  One or both
    of these fields can be set. If no fields are set, then we'll only send out
    the latest add/settle events.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DecodePayReq(self, request, context):
    """* lncli: `decodepayreq`
    DecodePayReq takes an encoded payment request string and attempts to decode
    it, returning a full description of the conditions encoded within the
    payment request.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListPayments(self, request, context):
    """* lncli: `listpayments`
    ListPayments returns a list of all outgoing payments.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteAllPayments(self, request, context):
    """*
    DeleteAllPayments deletes all outgoing payments from DB.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DescribeGraph(self, request, context):
    """* lncli: `describegraph`
    DescribeGraph returns a description of the latest graph state from the
    point of view of the node. The graph information is partitioned into two
    components: all the nodes/vertexes, and all the edges that connect the
    vertexes themselves.  As this is a directed graph, the edges also contain
    the node directional specific routing policy which includes: the time lock
    delta, fee information, etc.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetChanInfo(self, request, context):
    """* lncli: `getchaninfo`
    GetChanInfo returns the latest authenticated network announcement for the
    given channel identified by its channel ID: an 8-byte integer which
    uniquely identifies the location of transaction's funding output within the
    blockchain.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetNodeInfo(self, request, context):
    """* lncli: `getnodeinfo`
    GetNodeInfo returns the latest advertised, aggregated, and authenticated
    channel information for the specified node identified by its public key.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def QueryRoutes(self, request, context):
    """* lncli: `queryroutes`
    QueryRoutes attempts to query the daemon's Channel Router for a possible
    route to a target destination capable of carrying a specific amount of
    satoshis. The retuned route contains the full details required to craft and
    send an HTLC, also including the necessary information that should be
    present within the Sphinx packet encapsulated within the HTLC.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetNetworkInfo(self, request, context):
    """* lncli: `getnetworkinfo`
    GetNetworkInfo returns some basic stats about the known channel graph from
    the point of view of the node.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def StopDaemon(self, request, context):
    """* lncli: `stop`
    StopDaemon will send a shutdown request to the interrupt handler, triggering
    a graceful shutdown of the daemon.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SubscribeChannelGraph(self, request, context):
    """*
    SubscribeChannelGraph launches a streaming RPC that allows the caller to
    receive notifications upon any changes to the channel graph topology from
    the point of view of the responding node. Events notified include: new
    nodes coming online, nodes updating their authenticated attributes, new
    channels being advertised, updates in the routing policy for a directional
    channel edge, and when channels are closed on-chain.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DebugLevel(self, request, context):
    """* lncli: `debuglevel`
    DebugLevel allows a caller to programmatically set the logging verbosity of
    lnd. The logging can be targeted according to a coarse daemon-wide logging
    level, or in a granular fashion to specify the logging for a target
    sub-system.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def FeeReport(self, request, context):
    """* lncli: `feereport`
    FeeReport allows the caller to obtain a report detailing the current fee
    schedule enforced by the node globally for each channel.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateChannelPolicy(self, request, context):
    """* lncli: `updatechanpolicy`
    UpdateChannelPolicy allows the caller to update the fee schedule and
    channel policies for all channels globally, or a particular channel.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ForwardingHistory(self, request, context):
    """* lncli: `fwdinghistory`
    ForwardingHistory allows the caller to query the htlcswitch for a record of
    all HTLC's forwarded within the target time range, and integer offset
    within that time range. If no time-range is specified, then the first chunk
    of the past 24 hrs of forwarding history are returned.

    A list of forwarding events are returned. The size of each forwarding event
    is 40 bytes, and the max message size able to be returned in gRPC is 4 MiB.
    As a result each message can only contain 50k entries.  Each response has
    the index offset of the last entry. The index offset can be provided to the
    request to allow the caller to skip a series of records.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_LightningServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'WalletBalance': grpc.unary_unary_rpc_method_handler(
          servicer.WalletBalance,
          request_deserializer=rpc__pb2.WalletBalanceRequest.FromString,
          response_serializer=rpc__pb2.WalletBalanceResponse.SerializeToString,
      ),
      'ChannelBalance': grpc.unary_unary_rpc_method_handler(
          servicer.ChannelBalance,
          request_deserializer=rpc__pb2.ChannelBalanceRequest.FromString,
          response_serializer=rpc__pb2.ChannelBalanceResponse.SerializeToString,
      ),
      'GetTransactions': grpc.unary_unary_rpc_method_handler(
          servicer.GetTransactions,
          request_deserializer=rpc__pb2.GetTransactionsRequest.FromString,
          response_serializer=rpc__pb2.TransactionDetails.SerializeToString,
      ),
      'SendCoins': grpc.unary_unary_rpc_method_handler(
          servicer.SendCoins,
          request_deserializer=rpc__pb2.SendCoinsRequest.FromString,
          response_serializer=rpc__pb2.SendCoinsResponse.SerializeToString,
      ),
      'SubscribeTransactions': grpc.unary_stream_rpc_method_handler(
          servicer.SubscribeTransactions,
          request_deserializer=rpc__pb2.GetTransactionsRequest.FromString,
          response_serializer=rpc__pb2.Transaction.SerializeToString,
      ),
      'SendMany': grpc.unary_unary_rpc_method_handler(
          servicer.SendMany,
          request_deserializer=rpc__pb2.SendManyRequest.FromString,
          response_serializer=rpc__pb2.SendManyResponse.SerializeToString,
      ),
      'NewAddress': grpc.unary_unary_rpc_method_handler(
          servicer.NewAddress,
          request_deserializer=rpc__pb2.NewAddressRequest.FromString,
          response_serializer=rpc__pb2.NewAddressResponse.SerializeToString,
      ),
      'SignMessage': grpc.unary_unary_rpc_method_handler(
          servicer.SignMessage,
          request_deserializer=rpc__pb2.SignMessageRequest.FromString,
          response_serializer=rpc__pb2.SignMessageResponse.SerializeToString,
      ),
      'VerifyMessage': grpc.unary_unary_rpc_method_handler(
          servicer.VerifyMessage,
          request_deserializer=rpc__pb2.VerifyMessageRequest.FromString,
          response_serializer=rpc__pb2.VerifyMessageResponse.SerializeToString,
      ),
      'ConnectPeer': grpc.unary_unary_rpc_method_handler(
          servicer.ConnectPeer,
          request_deserializer=rpc__pb2.ConnectPeerRequest.FromString,
          response_serializer=rpc__pb2.ConnectPeerResponse.SerializeToString,
      ),
      'DisconnectPeer': grpc.unary_unary_rpc_method_handler(
          servicer.DisconnectPeer,
          request_deserializer=rpc__pb2.DisconnectPeerRequest.FromString,
          response_serializer=rpc__pb2.DisconnectPeerResponse.SerializeToString,
      ),
      'ListPeers': grpc.unary_unary_rpc_method_handler(
          servicer.ListPeers,
          request_deserializer=rpc__pb2.ListPeersRequest.FromString,
          response_serializer=rpc__pb2.ListPeersResponse.SerializeToString,
      ),
      'GetInfo': grpc.unary_unary_rpc_method_handler(
          servicer.GetInfo,
          request_deserializer=rpc__pb2.GetInfoRequest.FromString,
          response_serializer=rpc__pb2.GetInfoResponse.SerializeToString,
      ),
      'PendingChannels': grpc.unary_unary_rpc_method_handler(
          servicer.PendingChannels,
          request_deserializer=rpc__pb2.PendingChannelsRequest.FromString,
          response_serializer=rpc__pb2.PendingChannelsResponse.SerializeToString,
      ),
      'ListChannels': grpc.unary_unary_rpc_method_handler(
          servicer.ListChannels,
          request_deserializer=rpc__pb2.ListChannelsRequest.FromString,
          response_serializer=rpc__pb2.ListChannelsResponse.SerializeToString,
      ),
      'ClosedChannels': grpc.unary_unary_rpc_method_handler(
          servicer.ClosedChannels,
          request_deserializer=rpc__pb2.ClosedChannelsRequest.FromString,
          response_serializer=rpc__pb2.ClosedChannelsResponse.SerializeToString,
      ),
      'OpenChannelSync': grpc.unary_unary_rpc_method_handler(
          servicer.OpenChannelSync,
          request_deserializer=rpc__pb2.OpenChannelRequest.FromString,
          response_serializer=rpc__pb2.ChannelPoint.SerializeToString,
      ),
      'OpenChannel': grpc.unary_stream_rpc_method_handler(
          servicer.OpenChannel,
          request_deserializer=rpc__pb2.OpenChannelRequest.FromString,
          response_serializer=rpc__pb2.OpenStatusUpdate.SerializeToString,
      ),
      'CloseChannel': grpc.unary_stream_rpc_method_handler(
          servicer.CloseChannel,
          request_deserializer=rpc__pb2.CloseChannelRequest.FromString,
          response_serializer=rpc__pb2.CloseStatusUpdate.SerializeToString,
      ),
      'AbandonChannel': grpc.unary_unary_rpc_method_handler(
          servicer.AbandonChannel,
          request_deserializer=rpc__pb2.AbandonChannelRequest.FromString,
          response_serializer=rpc__pb2.AbandonChannelResponse.SerializeToString,
      ),
      'SendPayment': grpc.stream_stream_rpc_method_handler(
          servicer.SendPayment,
          request_deserializer=rpc__pb2.SendRequest.FromString,
          response_serializer=rpc__pb2.SendResponse.SerializeToString,
      ),
      'SendPaymentSync': grpc.unary_unary_rpc_method_handler(
          servicer.SendPaymentSync,
          request_deserializer=rpc__pb2.SendRequest.FromString,
          response_serializer=rpc__pb2.SendResponse.SerializeToString,
      ),
      'SendToRoute': grpc.stream_stream_rpc_method_handler(
          servicer.SendToRoute,
          request_deserializer=rpc__pb2.SendToRouteRequest.FromString,
          response_serializer=rpc__pb2.SendResponse.SerializeToString,
      ),
      'SendToRouteSync': grpc.unary_unary_rpc_method_handler(
          servicer.SendToRouteSync,
          request_deserializer=rpc__pb2.SendToRouteRequest.FromString,
          response_serializer=rpc__pb2.SendResponse.SerializeToString,
      ),
      'AddInvoice': grpc.unary_unary_rpc_method_handler(
          servicer.AddInvoice,
          request_deserializer=rpc__pb2.Invoice.FromString,
          response_serializer=rpc__pb2.AddInvoiceResponse.SerializeToString,
      ),
      'ListInvoices': grpc.unary_unary_rpc_method_handler(
          servicer.ListInvoices,
          request_deserializer=rpc__pb2.ListInvoiceRequest.FromString,
          response_serializer=rpc__pb2.ListInvoiceResponse.SerializeToString,
      ),
      'LookupInvoice': grpc.unary_unary_rpc_method_handler(
          servicer.LookupInvoice,
          request_deserializer=rpc__pb2.PaymentHash.FromString,
          response_serializer=rpc__pb2.Invoice.SerializeToString,
      ),
      'SubscribeInvoices': grpc.unary_stream_rpc_method_handler(
          servicer.SubscribeInvoices,
          request_deserializer=rpc__pb2.InvoiceSubscription.FromString,
          response_serializer=rpc__pb2.Invoice.SerializeToString,
      ),
      'DecodePayReq': grpc.unary_unary_rpc_method_handler(
          servicer.DecodePayReq,
          request_deserializer=rpc__pb2.PayReqString.FromString,
          response_serializer=rpc__pb2.PayReq.SerializeToString,
      ),
      'ListPayments': grpc.unary_unary_rpc_method_handler(
          servicer.ListPayments,
          request_deserializer=rpc__pb2.ListPaymentsRequest.FromString,
          response_serializer=rpc__pb2.ListPaymentsResponse.SerializeToString,
      ),
      'DeleteAllPayments': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteAllPayments,
          request_deserializer=rpc__pb2.DeleteAllPaymentsRequest.FromString,
          response_serializer=rpc__pb2.DeleteAllPaymentsResponse.SerializeToString,
      ),
      'DescribeGraph': grpc.unary_unary_rpc_method_handler(
          servicer.DescribeGraph,
          request_deserializer=rpc__pb2.ChannelGraphRequest.FromString,
          response_serializer=rpc__pb2.ChannelGraph.SerializeToString,
      ),
      'GetChanInfo': grpc.unary_unary_rpc_method_handler(
          servicer.GetChanInfo,
          request_deserializer=rpc__pb2.ChanInfoRequest.FromString,
          response_serializer=rpc__pb2.ChannelEdge.SerializeToString,
      ),
      'GetNodeInfo': grpc.unary_unary_rpc_method_handler(
          servicer.GetNodeInfo,
          request_deserializer=rpc__pb2.NodeInfoRequest.FromString,
          response_serializer=rpc__pb2.NodeInfo.SerializeToString,
      ),
      'QueryRoutes': grpc.unary_unary_rpc_method_handler(
          servicer.QueryRoutes,
          request_deserializer=rpc__pb2.QueryRoutesRequest.FromString,
          response_serializer=rpc__pb2.QueryRoutesResponse.SerializeToString,
      ),
      'GetNetworkInfo': grpc.unary_unary_rpc_method_handler(
          servicer.GetNetworkInfo,
          request_deserializer=rpc__pb2.NetworkInfoRequest.FromString,
          response_serializer=rpc__pb2.NetworkInfo.SerializeToString,
      ),
      'StopDaemon': grpc.unary_unary_rpc_method_handler(
          servicer.StopDaemon,
          request_deserializer=rpc__pb2.StopRequest.FromString,
          response_serializer=rpc__pb2.StopResponse.SerializeToString,
      ),
      'SubscribeChannelGraph': grpc.unary_stream_rpc_method_handler(
          servicer.SubscribeChannelGraph,
          request_deserializer=rpc__pb2.GraphTopologySubscription.FromString,
          response_serializer=rpc__pb2.GraphTopologyUpdate.SerializeToString,
      ),
      'DebugLevel': grpc.unary_unary_rpc_method_handler(
          servicer.DebugLevel,
          request_deserializer=rpc__pb2.DebugLevelRequest.FromString,
          response_serializer=rpc__pb2.DebugLevelResponse.SerializeToString,
      ),
      'FeeReport': grpc.unary_unary_rpc_method_handler(
          servicer.FeeReport,
          request_deserializer=rpc__pb2.FeeReportRequest.FromString,
          response_serializer=rpc__pb2.FeeReportResponse.SerializeToString,
      ),
      'UpdateChannelPolicy': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateChannelPolicy,
          request_deserializer=rpc__pb2.PolicyUpdateRequest.FromString,
          response_serializer=rpc__pb2.PolicyUpdateResponse.SerializeToString,
      ),
      'ForwardingHistory': grpc.unary_unary_rpc_method_handler(
          servicer.ForwardingHistory,
          request_deserializer=rpc__pb2.ForwardingHistoryRequest.FromString,
          response_serializer=rpc__pb2.ForwardingHistoryResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'lnrpc.Lightning', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))