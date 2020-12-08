from gbtc_tracker.lib.gbtc import GBTC
from gbtc_tracker.lib.gbtc_content_parser import PageParser

class TestPageParser:

  def test_create_gbtc(self):
    with open("gbtc_tracker/test/data/gbtc_page_content", 'rb') as content:
      html = content.read()
      page_parser = PageParser(html)
      gbtc = page_parser.create_gbtc()
      assert type(gbtc) is GBTC
      assert gbtc.sats_per_share > 0
      assert gbtc.shares_outstanding > 0

