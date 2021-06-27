#user enters their name - introduction
name = str(input('Hello and welcome! Please enter your name: '))
print ('\nHello ', name, ', welcome to HealthMatters, a new text-based interface that allows the user to stay fit, healthy and lead as healthy of a lifestyle as possible! \nWe will speak about audio levels, walking and running distance, diets, and of course BMI! \nWe will give various different recommendations throughout this program.')
print ('\nFirst, we will begin with finding your stride length!')

#step counter
countSteps = int(input('\nPlease input the number of steps you walked this week: '))
findDistance = float(input('\nPlease enter the total number of kilometers you ran or walked this week: '))

#calculate stride length
def stridelength(countSteps,findDistance):
    feet = findDistance * 3281
    while countSteps > findDistance:
        stride = (countSteps / 2) / feet
        print('\nYour stride length is',stride,'feet')
        break
stridelength(countSteps, findDistance)

#how many steps
def steplimit(countSteps):
    if (countSteps < 28000):
        dif = 28000 - countSteps
    else:
        dif = 0
    return dif
print('\nGreat job!\nAs the average adult takes 28,000 steps per week, you should increase your step count by', steplimit(countSteps),'steps')

#audio levels
audioLevel = float(input('\n\nThanks for your input in our step counter. Now we will work with audio levels. \nPlease input your weekly audio levels'))
def exposure(i):
    dif = 0.0
    if i > 85:
        dif = i - 70
    else:
        dif = 0.0
    return dif
print ('\nThanks for your input! Your headphone exposure should be limited by', exposure(audioLevel),'dB.\nThis can be fixed by lowering the volume whenever you are listening to music or watching something with your headphones.')

#calculate bmi
def bmi(value):
    v = True
    if value < 18.5:
        v = False
        return v
    if value >= 18.5 and value <= 24.9:
        v = True
        return v
    else:
        v = False
        return v
value = [18.4, 24.9, 29.9, 40.0]

#print a BMI chart
print('\n--------------BMI CHART------------------')
for v in value:
    print('\nIs a BMI under', v, 'a healthy?', bmi(v))
print('\n--------------BMI CHART------------------')
weight = float(input('\nPlease enter your weight in lbs'))
height = float(input('\nPlease enter your height in cm'))

#determins if healthy or not
def health(weight, height):
    inches = height / 2.54
    inches = inches * inches
    index = weight / inches
    index = index * 703
    if (index < 18.5):
        print('Your BMI is',index,'meaning you are underweight')
    elif(index >= 18.5 and index <= 24.9):
        print('Your BMI is',index,'meaning you are healthy weight')
    elif(index >= 25 and index <= 29.9):
        print('Your BMI is',index,'meaning you are overweight')
    elif(index >= 30):
        print('Your BMI is',index,'meaning you are obese')
health(weight, height)

#different diets
def diets():
    print ('\n\nNow, we will discuss diets! Dieting is when an individual eats certain foods with the main goal of losing weight or becoming healthier.')
    followDiet = str(input('\nDo you follow any diets (y or any other key for no)?'))
    #a quick game
    if (followDiet == "y"):
        dietGame = str(input('\nWell done! Now we will play a little game!\nGuess which diet we recommend for people with a high BMI:'))
        if (dietGame.lower() == 'plant-based diet'):
            print ('\nGreat job you guessed correctly!')
            print('\nThe Plant-based Diet was in fact named the best diet for weight loss, and is recognized as the diet for fastest weight loss')
            print('\nWOW! There are so many locations to find plant-based foods!')
            choice = str(input('\nWhich of the following locations is the most near you?\nReal Canadian Superstore\nWalmart\nCostco'))
            if(choice.lower() == 'real canadian superstore'):
                print('\nIt looks like there are plenty of plant-based foods all around here! Keep checking the location both online and in-person!')
            elif(choice.lower() == 'walmart'):
                print('\nUh oh! Sorry, it looks like there are not many or none plant-based foods here :(')
            elif(choice.lower() == 'costco'):
                print('\nWOW! There are numerous types of plant-based foods here! Check this location for sure :)')
            else:
                print('\nThat location could not be found :(')
        else :
            print ('\nGood guess but thats not correct. The answer we were looking for is The Plant-based Diet')
            print('\nThe Plant-based Diet was in fact named the best diet for weight loss, and is recognized as the diet for fastest weight loss')
            print('\nWOW! There are so many locations to find plant-based foods!')
            choice = str(input('\nWhich of the following locations is the most near you?\nReal Canadian Superstore\nWalmart\nCostco'))
            if (choice.lower() == 'real canadian superstore'):
                print('\nIt looks like there are plenty of plant-based foods all around here! Keep checking the location both online and in-person!')
            elif (choice.lower() == 'walmart'):
                print('\nUh oh! Sorry, it looks like there are not many or none plant-based foods here :(')
            elif (choice.lower() == 'costco'):
                print('\nWOW! There are numerous types of plant-based foods here! Check this location for sure :)')
            else:
                print('\nThat location could not be found :(')
    else:
        #guessing which diet
        dietNew = str(input('\nThat is fine, but guess which diet we recommend for healthy eating:'))
        if (dietNew.lower() == 'mediterranean diet'):
            print ('\nGreat job you guessed correctly!')
            print('\nThe Mediterranean Diet is one of the best diets for staying healthy! It is inspired by individuals living by the Mediterranean Sea.')
            
            #select a location
            print('\nWOW! There are so many locations to find Mediterranean foods, liken salads!')
            choice = str(input('\nWhich of the following locations is the most near you?\nReal Canadian Superstore\nWalmart\nCostco'))
            if (choice.lower() == 'real canadian superstore'):
                print('\nIt looks like there are some Mediterranean foods all around here! Keep checking the location both online and in-person!')
            elif(choice.lower() == 'walmart'):
                print('\nUh oh! Sorry, it looks like there are not many or no Mediterranean foods here :(')
            elif(choice.lower() == 'costco'):
                print('\nWOW! There are plenty of types of Mediterranean foods here! Check out this location for sure :)')
            else:
                print('\nThat location could not be found :(')
        else :
            print ('\nGood guess but thats not correct. The answer we were looking for is The Mediterranean Diet')
            print('\nThe Mediterranean Diet is one of the best diets for staying healthy! It is inspired by individuals living by the Mediterranean Sea.')
            print('\nWOW! There are so many locations to find Mediterranean foods, liken salads!')

            #select a location
            choice = str(input('\nWhich of the following locations is the most near you?\nReal Canadian Superstore\nWalmart\nCostco'))
            if (choice.lower() == 'real canadian superstore'):
                print('\nIt looks like there are some Mediterranean foods all around here! Keep checking the location both online and in-person!')
            elif(choice.lower() == 'walmart'):
                print('\nUh oh! Sorry, it looks like there are not many or no Mediterranean foods here :(')
            elif(choice.lower() == 'costco'):
                print('\nWOW! There are plenty of types of Mediterranean foods here! Check out this location for sure :)')
            else:
                print('\nThat location could not be found :(')
diets()