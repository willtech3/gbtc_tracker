import sys
import cloudscraper

class GBTCPage:
  @staticmethod
  def get_source():
    url = "https://grayscale.co/bitcoin-trust/"
    scraper = cloudscraper.create_scraper()
    response = scraper.get(url)
    if response.status_code != 200:
      sys.exit("Fatal Error accessing the Grayscale website")
    return response.content

