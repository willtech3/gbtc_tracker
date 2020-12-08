
from datetime import date
from sqlalchemy import Integer, Date
from gbtc_tracker.models.db_session import Base 

class GBTC_Writer(Base):
  __tablename__ = 'gbtc_daily'
  id = Column(Integer, primary_key=True)
  outstanding_shares = Column(Integer)
  sats_per_share = Column(Integer)
  date = Column(Date)