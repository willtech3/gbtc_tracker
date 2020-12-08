--
-- file: migrations/0001.create-gbtc_daily.sql
---
CREATE TABLE gbtc_daily(
  id INT AUTO_INCREMENT,
  outstanding_shares INT,
  sats_per_share INT, 
  date DATE,
  primary key(id)
);
