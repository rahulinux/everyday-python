#!/usr/local/bin python 

"""
Given the meal price (base cost of a meal), tip percent (the percentage of the meal price being added as tip), and tax percent (the percentage of the meal price being added as tax) for a meal, find and print the meal's total cost.

Note: Be sure to use precise values for your calculations, or you may end up with an incorrectly rounded result!
"""

import sys

def get_percentage(total,value):
    return total*value/100

if __name__ == "__main__":
    meal_cost = float(raw_input().strip())
    tip_percent = int(raw_input().strip())
    tax_percent = int(raw_input().strip())
    total_meal_cost = meal_cost + get_percentage(meal_cost,tip_percent) + get_percentage(meal_cost,tax_percent)
    print "The total meal cost is {} dollars.".format(int(round(total_meal_cost)))
