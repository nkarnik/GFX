"""
Welcome to the algogd backtester!!
"""

from algogd import trader, algorithm, run_backtest

#Initialize trader with $100000

dollars = 100000
nikhil = trader(dollars)

#Setup database connection, determine backtesting time period, and add rule triggered by GDELT event
firstalgo = algorithm('mysql')
firstalgo.set_time_period(20000101, 20070601)

firstalgo.add_rule('buy', 
            'EURUSD', 
             100, 
            "select sqldate, sum(NumArticles) from gdv911 where EventLocation != 'RS' and sqldate > '2000-01-01' and sqldate < '2007-06-01' group by sqldate order by sqldate limit 100000", 
             30)

output = run_backtest(nikhil, firstalgo)
