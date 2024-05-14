MENU={
    'espresso':{
        'ingrediants':{
            'water':50,
            'milk':50,
            'coffee':18,
        },
        'cost':1.5,
    },
    
    'latte':{
        'ingrediants':{
            'water':200,
            'milk':150,
            'coffee':24,
        },'cost':2.5,
    },
    
    'cappuccino':{
        'ingrediants':{
            'water':250,
            'milk':100,
            'coffee':24,
        },'cost':3.0,
    },
    
}
resources={
    'water':300,
'milk':200,
'coffee':100
}
def show_details():
    print(f'WATER: {resources["WATER"]}ml')
    print(f'MILK: {resources["MILK"]}ml')
    print(f'Coffee: {resources["Coffee"]}grams')
def check_resources_sufficient(coffee_name):
    for items in coffee_name:
        if coffee_name[items]>resources[items]:
            return False
    return True
def take_payment():
    print('Enter payment details')
    total=int(input('Amount of Quarters? :'))*0.25
    total+=int(input('Amount of dims? :'))*0.1
    total+=int(input('Amount of nickles? :'))*0.05
    total+=int(input('Amount of pennies? :'))*0.01
    return total

def check_payment_sufficient(enter_amount,coffee_amount):
    if enter_amount>=coffee_amount:
        exchange=round(enter_amount-coffee_amount,2)
        global profit
        profit+=enter_amount
        print(f'Take your coffee, Here is change {exchange}')
        print(f'Profit is {profit}.')
        return True
    else:
        print('Sorry Amount is not enough.Amount is refunded')
        
        print(f'Profit is {profit}.')
        return False
        
def decuct_resources(coffee_resources,resources):
    for items in resources:
        # print(items)
        # coffee_resources[items]
        resources[items]-=coffee_resources[items]
        
        
profit=0
is_on=True
while is_on:
    choice=input('Enter your Choice? Espresso/latte/cappuccino... ').lower()
    if choice=='report':
        show_details()
    elif choice=='off':
        is_on=False
    else:
        choice_details=MENU[choice]
        # print(choice_details)
        coffee_ingrediants=choice_details['ingrediants']
        if check_resources_sufficient(coffee_ingrediants):
            total_amount=take_payment()
            if check_payment_sufficient(total_amount,choice_details['cost']):
             decuct_resources(coffee_ingrediants,resources)
            else:
                is_on=False
            