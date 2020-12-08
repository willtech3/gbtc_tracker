from gbtc_tracker.lib.gbtc import GBTC
from bs4 import BeautifulSoup

class PageParser:
  def __init__(self, content):
    self.content = content

  def create_gbtc(self):
    html = BeautifulSoup(self.content, 'html.parser')
    gbtc_traits = dict()
    keys = html.findAll('td', {'class': 'key'})
    for key in keys:
      gbtc_traits[key.text] = key.findNextSibling().text
    return GBTC(gbtc_traits)