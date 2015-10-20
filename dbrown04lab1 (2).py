#Lab1 - Section 2
#Dustyne Brown
#Calculate the cost of driving to locations based on user input information
#9/14/11 - First completion - 10:24pm
#9/17/11 - Edit locations and miles - 10:12pm
#9/20/11 - Calculation Edits - 11:24am - 11:57am


#Information for Location Names
location1 = 'New York City, New York'
location2 = 'Salmo, British Columbia, Canada'
location3 = 'Sacramento, California'
location4 = 'Dallas, Texas'


#Information for Location Distances
miles1 = 1368
miles2 = 2006
miles3 = 1817
miles4 = 289
#Trip plan is for going to location 1, back home, and then the next, and so on.


#user input for gas prices
gas_price = float(input('At a cost per gallon of $'))


#user input for miles per gallon
mpg = int(input('And miles per gallon of '))


#Costs for drives
cost1 = (((miles1 / mpg) * gas_price) * 2)
cost2 = (((miles2 / mpg) * gas_price) * 2)
cost3 = (((miles3 / mpg) * gas_price) * 2)
cost4 = (((miles4 / mpg) * gas_price) * 2)


#Total Milage
milage = ((((miles1 + miles2) + miles3) + miles4) * 2)


#Total Gas
t_gas = milage / mpg


#Total Gas Costs
t_g_cost = t_gas * gas_price


#reads required text line 3
print('Your expected gas cost to ')


#Location1, miles and cost of this line reading
print('\t', location1,  ', ', format(miles1, ','), ' miles away is $',\
      format(cost1, ',.2f'), sep='')


#Location2, miles and cost of this line reading
print('\t', location2, ', ', format(miles2, ','), ' miles away is $',\
      format(cost2, ',.2f'), sep='')


#Location3, miles and cost of this line reading
print('\t', location3, ', ', format(miles3, ','), ' miles away is $',\
      format(cost3, ',.2f'), sep='')


#Location4, miles and cost of this line reading
print('\t', location4, ', ', format(miles4, ','), ' miles away is $',\
      format(cost4, ',.2f'), sep='')


#Total Milage Readout
print('\nTotal milage for the entire trip will be ', \
      format(milage, ',.2f'), '.', sep='')


#Total gallons of gas used reading
print('Total gallons of gas used will be around ', \
      format(t_gas, ',.2f'), '.', sep='' )


#Total gas cost read out
print('Total gas cost for the entire trip will be around $', \
      format(t_g_cost, ',.2f'), '.', sep='' )
      
