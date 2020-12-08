import pytest
from gbtc_tracker.lib.gbtc_page_retriever import GBTCPage

class TestPageRetriever:

  def test_get_source(self):
    assert GBTCPage.get_source() is not None
