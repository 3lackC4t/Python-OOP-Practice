#!/bin/python

import csv
import sys
import personnel



if __name__ == "__main__":
    new_suzy = personnel.Employee('Suzy','Masterson','Admin', 67000)
    print(new_suzy.get_salary())
