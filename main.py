import random

def number_gen():
    num =  random.randint(0,2)
    return num


def start_game(score1,score2):
    user1 = number_gen()
    user2 = number_gen()
    if (user1==0):
        pyscript.write("img1","<img src='./assets/rock.jpg' alt='paper image'>")   
    elif(user1==1):
        pyscript.write("img1","<img src='./assets/paper.jpg' alt='paper image'>")  
    elif(user1==2):
        pyscript.write("img1","<img src='./assets/scissor.jpg' alt='paper image'>")  
       
    # dict = {0:'rock', 1:'paper', 2:'scissor'}
    if (user2==0):
        pyscript.write("img2","<img src='./assets/rock.jpg' alt='paper image'>")   
    elif(user2==1):
        pyscript.write("img2","<img src='./assets/paper.jpg' alt='paper image'>")  
    elif(user2==2):
        pyscript.write("img2","<img src='./assets/scissor.jpg' alt='paper image'>")  
      
    a,b = compare(user1,user2,score1, score2)
    #compare(score1, score2, dict)
    return a,b

def compare(user1,user2,score1, score2):

    if(user1 == 0):
        if(user2 == 1):
            #  winner = user2
            score2=score2+1
        elif(user2 == 2):
            # winner = user1
            score1=score1+1
        else:
            print("draw")

    if(user1 == 1):
        if(user2 == 1):
            print("draw")          
        elif(user2 == 2):
            # winner = user2
            score2=score2+1
        else:
            # winner = user1
            score1=score1+1


    if(user1 == 2):
        if(user2 == 1):
            # winner = user1
            score1=score1+1
        elif(user2 == 2):
            print("draw")          
        else:
            # winner = user2
             score2=score2+1
    
    return score1, score2


# score1,score2=start_game(score1,score2)
# print(score1,score2)
score1=0
score2=0

def show_output(*args):
    a,b=start_game(score1,score2)
    pyscript.write("score1",a)
    pyscript.write("score2",b)

def reset_func(*args):
    pyscript.write("score1",0)
    pyscript.write("score2",0)    




