#stock profits
priceofstocks=int(input('Current price of stocks '))
invested=int(input('How much have you invested? '))
owned=invested/priceofstocks
print('You own ', owned, 'stocks')
payout=owned^.07
print(payout)
