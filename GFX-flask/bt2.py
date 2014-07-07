"""
Welcome to the algogd backtester!!
"""

from algogd import trader, algorithm, run_backtest

dollars = 100000

nikhil = trader(dollars)

firstalgo = algorithm('mysql')
firstalgo.set_time_period(20000101, 20070601)

firstalgo.add_rule('buy', 
            'USDCAD', 
             100, 
            "select sqldate, NumArticles from gdv911 where EventLocation = 'IZ' and sqldate > '2000-01-01' group by sqldate order by sqldate limit 100000", 
             30)


output = run_backtest(nikhil, firstalgo)




