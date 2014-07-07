"""
Welcome to the algogd backtester!!
"""

from algogd import trader, algorithm, run_backtest

dollars = 100000

nikhil = trader(dollars)

firstalgo = algorithm('mysql')
firstalgo.set_time_period(20000101, 20080601)

firstalgo.add_rule('buy', 
            'USDCAD', 
             100, 
            "select day, sum(SumArticles)/norm from gdecon2 where (Actor1Code = 'USA' and (Actor2Code = 'EUR' or Actor2Code = 'IGOEU' or Actor2Code = 'DEU' or Actor2Code = 'GRC')) and day > 20010101 group by day order by day limit 100000", 
             0.002)


output = run_backtest(nikhil, firstalgo)




