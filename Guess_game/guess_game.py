from game_data import data
import random
# from replit 
score=0
def get_data(account):
    account_name=account['name']
    account_desc=account['description']
    account_country=account['country']
    return f"{account_name},{account_desc}, {account_country}"
def check_ans(guess,a_account,b_account):
    if a_account['follower']>b_account['follower']:
        return guess=='a'
    else:
        return guess=='b'
        
a_account=random.choice(data)
b_account=random.choice(data)
if a_account==b_account:
    b_account=random.choice(data)
    
end_game=False
while not end_game:
    print(f'Compare A : {get_data(a_account)}')
    print(f'Compare B : {get_data(b_account)}')
    guess=input('Guess who have more Followers? "A" or "B" ').lower()
    is_check=check_ans(guess,a_account,b_account)
    if is_check:
        score+=1
        print(f'You win, your score is {score}')
        # clear()
        a_account,b_account=b_account,random.choice(data)
        while a_account==b_account:
            b_account=random.choice(data) 
    else:
        end_game=True
        print(f'you lose, Your score is {score}')
    
# if guess=='a':
#     if a_account['follower']>b_account['follower']:
#         print('Guess is right')
#     else:
#         print('Sorry wrong guess')
# else:
#     if a_account['follower']<b_account['follower']:
#         print('Guess is right')
#     else:
#         print('Sorry wrong guess')