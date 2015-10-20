#Lab1
#Dustyne Brown
#Calculate the cost of driving to locations based on user input information
#9/14/11 - First completion - 10:24pm


#Information for Location Names
location1 = 'New York City, New York'
location2 = 'Salmo, British Columbia, Canada'
location3 = 'Sacramento, California'
location4 = 'Dallas, Texas'


#Information for Location Distances
miles1 = 1368
miles2 = 2675
miles3 = 1510
miles4 = 1730
home_miles = 288

#user input for gas prices
gas_price = float(input('At a cost per gallon of $'))


#user input for miles per gallon
mpg = int(input('And miles per gallon of '))


#reads required text line 3
print('Your expected gas cost to ')


#Location1, miles and cost of this line reading
print('\t', location1,  ', ', format(miles1, ','), ' miles away is $',\
      format((((miles1 / mpg) * gas_price) * 2), ',.2f'), sep='')


#Location2, miles and cost of this line reading
print('\t', location2, ', ', format(miles2, ','), ' miles away is $',\
      format((((miles2 / mpg) * gas_price) * 2), ',.2f'), sep='')


#Location3, miles and cost of this line reading
print('\t', location3, ', ', format(miles3, ','), ' miles away is $',\
      format((((miles3 / mpg) * gas_price) * 2), ',.2f'), sep='')


#Location4, miles and cost of this line reading
print('\t', location4, ', ', format(miles4, ','), ' miles away is $',\
      format((((miles4 / mpg) * gas_price) * 2), ',.2f'), sep='')


#Total Milage Readout
print('\nTotal milage for the entire trip will be ', \
      format(((((miles1 + miles2) + miles3) + miles4) * 2), ',.2f'), '.', sep='')


#Total gallons of gas used reading
print('Total gallons of gas used will be around ', \
      format((((((miles1 + miles2) + miles3) + miles4) / mpg) * 2), ',.2f'), '.', sep='' )


#Total gas cost read out
print('Total gas cost for the entire trip will be around $', \
      format(((((((miles1 + miles2) + miles3) + miles4) / mpg) * \
               gas_price) * 2), ',.2f'), '.', sep='' )
