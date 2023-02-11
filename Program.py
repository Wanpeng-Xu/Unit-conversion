#WanpengXuHomework9
import pandas as pd

df = pd.read_csv('D:/桌面/UnitConversion.csv')
# save rate in doc to make the change easier

def addComment(comment):
    with open(comment_file, 'a', encoding='utf-8') as file:
        file.write(comment)
    
length = [['cm', 'm', 'km'], ['inch', 'foot', 'mile']]
weight = [['g', 'kg'], ['oz', 'lb']]
volume= [['ml', 'l'], ['fl oz', 'gal']]
space = [['sq ft'], ['sq m']]

print('Welcome to the Unit Conversion World!')
restart = 'yes'
while restart == 'yes':
    welcome = input('Please choose what unit you want to convert by entering the number:\nEnter 1 to covert "Lengh/Height" (cm, m, km & inch, foot, mile)\nEnter 2 to covert "Weight" (g, kg & oz, lb)\nEnter 3 to covert "Volume" ( ml, l & fl oz, gal)\nEnter 4 to covert "Space" (sq ft & sq m)\nEnter * to tell me you want to convert more units\n>>>')
    if welcome == '1':
        original = input('Enter the original unit (' + length[0][0] + ', ' + length[0][1] + ', ' + length[0][2]+ ' ,'+ length[1][0] + ', ' + length[1][1] + ', ' + length[1][2] + ')\n>>>')
        
        if original in length[0]:
            current = input('Enter the unit you want to converse to (' + length[1][0] + ', ' + length[1][1] + ', ' + length[1][2] + ')\n>>>')
        elif original in length[1]:
            current = input('Enter the unit you want to converse to (' + length[0][0] + ', ' + length[0][1] + ', ' + length[0][2] + ')\n>>>')
        else:
            original = 'wrong'
            current = 'none'            
        try:
            rateList = df[(df['original units'] == original) & (df['current units'] == current)]
            rate = rateList['rate'].iloc[0]
            oriamount = input('Enter the original number\n>>>')
            result = float(oriamount) * float(rate)
            print(f'{oriamount} {original} is equal to {result} {current}')
            restart = 'no'
        except ValueError:
            print('Please enther number as the original number\nRestarting the program...\t')
            restart = 'yes'
        except IndexError:
            print('Please enter the correct unit\nRestarting the program...\t')
            restart = 'yes'

    elif welcome == '2':
        original = input('Enter the original unit (' + weight[0][0] + ', ' + weight[0][1] + ', ' + weight[1][0] + ', ' + weight[1][1] +  ')\n>>>')
        
        if original in weight[0]:
            current = input('Enter the unit you want to converse to (' + weight[1][0] + ', ' + weight[1][1] + ')\n>>>')
        elif original in weight[1]:
            current = input('Enter the unit you want to converse to (' + weight[0][0] + ', ' + weight[0][1] + ')\n>>>')
        else:
            original = 'wrong'
            current = 'none'
        try:
            rateList = df[(df['original units'] == original) & (df['current units'] == current)]
            rate = rateList['rate'].iloc[0]
            oriamount = input('Enter the original number\n>>>')
            result = float(oriamount) * float(rate)
            print(f'{oriamount} {original} is equal to {result} {current}')
            restart = 'no'
        except ValueError:
            print('Please enther number as the original number\nRestarting the program...\t')
            restart = 'yes'
        except IndexError:
            print('Please enter the correct unit\nRestarting the program...\t')
            restart = 'yes'
        
    elif welcome == '3':
        original = input('Enter the original unit (' + volume[0][0] + ', ' + volume[0][1] +  ', '+ volume[1][0] + ', ' + volume[1][1] +')\n>>>')
        
        if original in volume[0]:
            current = input('Enter the unit you want to converse to (' + volume[1][0] + ', ' + volume[1][1] + ')\n>>>')
        elif original in volume[1]:
            current = input('Enter the unit you want to converse to (' + volume[0][0] + ', ' + volume[0][1] + ')\n>>>')
        else:
            original = 'wrong'
            current = 'none'
        try:
            rateList = df[(df['original units'] == original) & (df['current units'] == current)]
            rate = rateList['rate'].iloc[0]
            oriamount = input('Enter the original number\n>>>')
            result = float(oriamount) * float(rate)
            print(f'{oriamount} {original} is equal to {result} {current}')
            restart = 'no'
        except ValueError:
            print('Please enther number as the original number\nRestarting the program...\t')
            restart = 'yes'
        except IndexError:
            print('Please enter the correct unit\nRestarting the program...\t')
            restart = 'yes'
            
    elif welcome == '4':
        original = input('Enter the original unit (' + space[0][0] + ', '+ space[1][0] + ')\n>>>')
        
        if original in space[0]:
            current =  space[1][0]
        elif original in space[1]:
            current = space[0][0]
        else:
            original = 'wrong'
            current = 'none'
        try:
            rateList = df[(df['original units'] == original) & (df['current units'] == current)]
            rate = rateList['rate'].iloc[0]
            oriamount = input('Enter the original number\n>>>')
            result = float(oriamount) * float(rate)
            print(f'{oriamount} {original} is equal to {result} {current}')
            restart = 'no'
        except ValueError:
            print('Please enther number as the original number\nRestarting the program...\t')
            restart = 'yes'
        except IndexError:
            print('Please enter the correct unit\nRestarting the program...\t')
            restart = 'yes'

        
    elif welcome == '*':
        comment_file = 'D:/桌面/comment_file.text'
        comment = input('What units do you want to convert?\n>>>')
        addComment(comment)
        print('Thank you for your feedback. We will figure it out as soon as possible.')
        
    else:
        print('You entered a wrong number.\nRestarting the program...\t')
        restart = 'yes'
print('Exit!')
exit()
        
