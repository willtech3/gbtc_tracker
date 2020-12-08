from datetime import date

class GBTC:
  def __init__(self, gbtc_data_hash):
    self.shares_outstanding = self.shares_outstanding(gbtc_data_hash['Shares Outstanding'])
    self.sats_per_share = self.convert_to_sats(gbtc_data_hash['Bitcoin per Share'])
    self.date_recorded = date.today()

  def shares_outstanding(self, shares_outstanding_value):
    no_comma_value = shares_outstanding_value.replace(',', '')[:-1]
    return int(no_comma_value)

  def convert_to_sats(self, btc_str_value):
    btc = btc_str_value[:-1]
    return int(btc.replace('0', '')[1:])
