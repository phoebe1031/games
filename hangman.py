from random import choice
word_list = ["orange","apple","pear","school",'practise',"milk","like","iphone","fruit","busy","middle","good","please","size","show","concert","operation"]
word = choice(word_list)

def hangman(word):

# 第1部分，开始定义参数，字母列表，提示版，猜错次数，初始状态wrong，猜错记录stages
    rletters = list(word)
    board = ["___"] * len(word)
    wrong = 0
    win = False
    stages = [
              "|   ___ ",
              "|    |  ",
              "|    O  ",
              "|   \|/  ",
              "|   / \  ",
              ""]
    print("Welcome to Hangman!")

# 第2部分，开始定义循环，只要wrong小于规定次数，循环以下
    while wrong < len(stages) - 1:
        print("\n")
        msq = "Guess a letter or the word: "
        char = input(msq).lower()

    # 状况一：如果猜测的字母在字母列表里，这样的情况下，开始一个循环，将每个字母都替换掉猜测的字母：
        if char in rletters:
            for item in rletters:
                if item == char:
                    item = rletters.index(char)
                    board[item] = char
                    rletters[item] = '$'

    # 状况二：如果猜测的单词等于单词：
        elif char == word:
            print("\n\n\nYou win")
            print("It's {}.".format(word))
            win = True
            break

    # 状况三：如果没猜到：
        else:
            wrong += 1

        print((" ").join(board))
        print("\n")
        print("\n".join(stages[0:wrong]))

        if "___" not in board:
            print("\n\nYou win! It's {}.".format(word.upper()))
            win = True
            break

    if not win:
        print("You lose! It was {}.".format(word.upper()))

hangman(word)

