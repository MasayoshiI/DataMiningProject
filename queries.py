#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 13:37:29 2019

@author: benjaminsui
"""

import sqlite3

db_file = ''
rating = input('Enter the rating: ')
cutoff = input('Enter the earnings-rank cutoff: ')
file_name = input('Enter the name of the result file: ')

db = sqlite3.connect(db_file)
cursor = db.cursor()

command = '''SELECT earnings_rank, name, year
             FROM Movie
             WHERE rating = ?
               AND earnings_rank <= ?
             ORDER BY earnings_rank;'''

cursor.execute(command, [rating, cutoff])

result_file = open(file_name, 'w')

count = 0
for row in cursor:
    print((str(row[0]) + ',' + row[1] + ',' + str(row[2])), file = result_file)
    count += 1

if count != 0:
    print('Wrote 8 lines of results to the file.')

else:
    print('There are no movies in the database that match your criteria.')

db.commit()
db.close()