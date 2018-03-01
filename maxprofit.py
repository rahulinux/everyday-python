#!/usr/local/env python


"""
Best time to Buy and Sell stock 
"""


def maxprofit(prices):
   max_profit = 0
   for i in range(1,len(prices)):
      if prices[i] >= prices[i-1]:
         max_profit +=  prices[i] - prices[i-1]
   return max_profit

prices = [1,2,1,3,4]
print maxprofit(prices) 
