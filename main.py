import random

number = 100

while number > 0:
    print("Ваше количество очков = " + str(number))
    x = int(input("Назовите число от 2 до 12: "))
    if x < 2 or x > 12:
        print ("Вы вышли за границы диапазона, введите данные заново!")
    else:
        y = int(input("Какое количество очков вы хотите поставить? "))
        if y > number:
            print("Вы не обладаете таким количеством очков, введите данные заново!")
        else:
            first_dice = random.randint(1, 6)
            second_dice = random.randint(1,6)
            sum = first_dice + second_dice
            if sum < 7 and x < 7:
                print("Сумма цифр на костях = " + str(sum) + ", вы выиграли ставку!")
                number += y
                n = input("Ваша сумма очков = " + str(number) + ". Вы хотите продолжить? ")
                if n == "Нет":
                    print("Спасибо за игру. Пока!")
                    break
            elif sum > 7 and x > 7:
                print("Сумма цифр на костях = " + str(sum) + ", вы выиграли ставку!")
                number += y
                n = input("Ваша сумма очков = " + str(number) + ". Вы хотите продолжить? ")
                if n == "Нет":
                    print("Спасибо за игру. Пока!")
                    break
            elif sum == x:
                print("Сумма цифр на костях = " + str(sum) + ", вы выиграли ставку, умноженную на 4!")
                number += 4*y
                n = input("Ваша сумма очков = " + str(number) + ". Вы хотите продолжить? ")
                if n == "Нет":
                    print("Спасибо за игру. Пока!")
                    break
            else:
                print("Сумма цифр на костях = " + str(sum) + ", вы проиграли ставку :(")
                number -= y
                if number > 0:
                    n = input("Ваша сумма очков = " + str(number) + ". Вы хотите продолжить? ")
                    if n == "Нет":
                        print("Спасибо за игру. Пока!")
                        break

else:
    print("К сожалению, вы проиграли все очки, игра окончена :( ")
