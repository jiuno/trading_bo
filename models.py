class Balance:
    def __init__(self,balance_info):
        self.initial_margin = float(balance_info['initialMargin'])
        self.maintenance_margin = float(balance_info['maintMargin'])
        self.margin_balance = float(balance_info['marginBalance'])
        self.wallet_balance = float(balance_info['walletBalance'])
        self.unrealized_pnl = float(balance_info['unrealizedProfit'])

class Candle:
    def __init__(self,candle_info) -> None:
        self.timestamp = candle_info[0]
        self.open = float(candle_info[1])
        self.high = float(candle_info[2])
        self.low = float(candle_info[3])
        self.close = float(candle_info[4])
        self.volume = float(candle_info[5])

class Contract:
    def __init__(self,contract_info) -> None:
        self.symbol = contract_info['symbol']
        self.base_asset = contract_info['baseAsset']
        self.quote_asset = contract_info['quoteAsset']
        self.price_decimals = contract_info['pricePrecision']
        self.quantity_decimals = contract_info['quantityPrecision']

class OrderStatus:
    def __init__(self,order_info) -> None:
        self.order_id = order_info['orderId']
        self.status = order_info['status']
        self.avg_price = float(order_info['avgPrice'])
        