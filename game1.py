import random

number1 = int(input("最小:"))
number2 = int(input("最大:"))
number_to_guess = random.randint(number1, number2)
tries = 0

print("欢迎来到猜数字游戏！我已经想好了一个",number1,"到",number2,"之间的数字，你来猜猜看。")

while True:
    try:
        guess = int(input("请输入你的猜测："))
        tries += 1

        if guess == number_to_guess:
            print(f"恭喜你，猜对了！你一共猜了 {tries} 次。")
            break
        elif guess < number_to_guess:
            print("猜的数字太小了，再试试吧。")
        else:
            print("猜的 数字太大了，再试试吧。")
    except ValueError:
        print("请输入一个有效的整数哦。")