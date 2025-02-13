import random

game_var = ["камень", "ножницы", "бумага"]

#ход игрока
print("Слабо выиграть комп в камень, ножницы, бумага?")
human = input("Твой ход: ").lower()
comp_step = random.choice(game_var)
print(f"У нас {comp_step}")

def find_winner(human, comp_step):
    if human == comp_step:
        print("Ничья")
    elif(human == "ножницы" and  comp_step == "камень") or \
        (human == "камень" and  comp_step == "бумага") or \
        (human == "бумага" and  comp_step == "ножницы"):
        print("Упс, вы програли")
    elif human != "камень" and human !="ножницы" and human != "бумага":
        print("Мы не поняли ваш ответ, напишите верно и перезапустите программу")  
    else:
        print("Вау, вам подвернулась удача!")
        
find_winner(human, comp_step)



    



