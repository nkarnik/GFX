CREATE EXTERNAL TABLE IF NOT EXISTS fxhist (
    day INT,
    time INT,
    open FLOAT,
    high FLOAT,
    low FLOAT,
    close FLOAT,
    volume INT,
    a STRING,
    b STRING)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\;'
stored as textfile
LOCATION '/user/ubuntu/FOREX/hist' ;

