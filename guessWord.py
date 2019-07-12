# 猜单词游戏
import  random
#创建单词序列
WORDS =("pythod", "what", "apple", "easy", "difficult", "answer", "computer", "bike", "car", "phone", "telephone")

#开始游戏
print("""
    欢迎参加猜单词游戏
    把字母组合成一个正确的单词
""")

iscontinue = "y"
while iscontinue=="y" or iscontinue=="Y":
    #从序列中随机挑出一个单词
    word = random.choice(WORDS)
    #一个用于判断玩家是否猜对的变量
    corrent = word
    #创建乱序后单词
    jumble = ""
    while word:         #word不是空串循环
        #根据word长度产生word的随机位置
        position = random.randrange(len(word))
        #将position位置的字母组合到乱序后单词
        jumble += word[position]
        #通过切片将position位置的字母从原单词中删除
        word = word[:position]+word[(position+1):]
    print("乱序后单词：",jumble)

    guess = input("\n请你猜：")
    while guess != corrent and guess!="":
        print("对不起不正确：")
        guess = input("请继续:")
        if guess == corrent:
            print("真棒，你猜对了！")
        iscontinue = input("\n 是否继续(Y/N)")





