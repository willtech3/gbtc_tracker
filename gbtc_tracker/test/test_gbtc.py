from gbtc_tracker.lib.gbtc import GBTC

class TestGBTC:

  def test_instantiation(self):
    gbtc_data_hash = {
      'Shares Outstanding': '574,950,700‡',
      'Bitcoin per Share': '0.00095153‡'
    }
    gbtc = GBTC(gbtc_data_hash)
    assert type(gbtc.sats_per_share) is int
    assert type(gbtc.shares_outstanding) is int