#Lab 2 Section 2
#Dustyne Brown
#10/20/11 - 10:45pm - Start
#10/21/11 - 2:20am - Quit
#10/22/2011 - 10:36pm - Start Coding Displays
#10/22/2011 - 11:54pm - Assignment completion



income1 = 0
taxedamount1 = 0
final = 0
deduct = 0
bracket1 = .01
#bracket 1 is 0-15K
bracket2 = .03
#bracket 2 is 15-30
bracket3 = .05
#bracket 3 = 30-75
bracket4 = .1
#bracket 4 =75+
badjobs = 2000
#fast food or retail
living = 1000
#Or with friends
workschool = 200
#fulltime job and school



def main():
    #Retrieves the income from the user.
    incomecollection()
    #Deterimine and apply brackets
    bracketwork()
    #Determine Deducts
    deducts()
    #calculate final results
    calcfinals()
    #display the results
    display()

#display all info
def display():
    global income1
    global taxedamount1
    global deduct
    global final
    global deduct
    income1=format(income1, '.2f')
    taxedamount1=format(taxedamount1, '.2f')
    deduct=format(deduct, '.2f')
    #final=format(final, '.2f')
    print('This year you earned $', income1, '.', sep='')
    print('Due to your tax bracket, your highest possible amount of tax you could pay is $', \
          taxedamount1, '.', sep='')
    if float(deduct)<0:
        deduct=deduct*-1
        print('However, due to your tax credits, your owed amount has been decreased by $', \
          deduct, '.', sep='')
    if float(deduct)==0:
        print('Sorry, your owed amount was not changed at all.')
    else:
        print('However, due to your tax credits, your owed amount has been decreased by $', \
          deduct, '.', sep='')
    if float(final)<0:
        final=final*-1
        print('After your tax credits are applied to your owed amount, you are owed $', format(final, '.2f'), '.', sep='')
    else:
        print('After your tax credits are applied to your owed amount, you now owe $', format(final, '.2f'), '.', sep='')


#calculate the finals on the amount owed
def calcfinals():
    global income1
    global taxedamount1
    global final
    global deduct
    final=taxedamount1-deduct
    #print(final)

#Moduel for calculating deductions
def deducts():
    global income1
    global taxedamount1
    global badjobs
    global living
    global workschool
    global deduct
    print('Do you currently work in Fast Food or Retail for hourly pay?')
    deductone=input()
    if deductone=='Yes':
        #print('finally working')
        deduct=deduct+badjobs
    #else:
        #print('No deduct from work.')
    #print(deduct)
    print('Do you currently live alone or with friends?')
    deducttwo=input()
    if deducttwo=='Yes':
        #print('working 2')
        deduct=deduct+living
    #else:
        #print('No deduct from living conditions.')
    #print(deduct)
    print('Are you currently attending college full time and working full time?')
    deductthree=input()
    if deductthree=='Yes':
        #print('AWWWW YEAH, LAYER THREE WORKING')
        deduct=deduct+workschool
    #else:
        #print('Better work harder if you want more deducts!')
    #print(deduct)
    

        
#applies amount of percents owed
def bracketwork():
    global income1
    global bracket1
    global bracket2
    global bracket3
    global bracket4
    global taxedamount1
    if 0<income1<=15000:
        taxedamount1 = income1*bracket1
        #Test Bracket 1
        #print(taxedamount1)
    if 15000<income1<=30000:
        taxedamount1 = income1*bracket2
        #Test bracket 2
        #print(taxedamount1)
    if 30000<income1<=75000:
        taxedamount1 = income1*bracket3
        #Test 3
        #print(taxedamount1)
    if 75000<income1:
        taxedamount1 = income1*bracket4
        #Test 4
        #print(taxedamount1)
        
    

#Module for collecting income
def incomecollection():
    incomecollect=int(input('How much money did you earn this year? $'))
    global income1
    income1=income1+incomecollect
    #var test1
    #print(income1)
    

main()
