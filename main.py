import random
import welcome
from replit import clear 

# 印出歡迎畫面
print(welcome.intro)
# TODO: 難度選擇，確認後開始遊戲

# 難度設定：N = 幾位數字
N = 4
NUMBERS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


# the function that generates the answer
def generate_answer():
    # 產生一亂數答案，多一步驟把數字轉為str，做後續判讀：
    ans_num = random.randint(0, 10**N - 1)

    # 如果有少的位數，將前幾格補上"0"
    if ans_num < 10**(N-1):
        return str(ans_num).zfill(N)
    else:
        return str(ans_num)


# check user input, if it's not valid input or command, pop-up error message
def check_input():
    global guess
    guess = input(f"請猜{N}位數字： ")

    if guess == "quit" or guess == "exit" or guess == "answer":
        return False

    if len(guess) != N:
        print("輸入錯誤，請重新輸入")
        return True
    else:
        for x in guess:
            if x not in NUMBERS:
                print(f"請輸入{N}個數字")
                return True
        return False


# compare the user guess with the answer
def compare(guess, answer):
    """比較使用者猜的guess和答案answer後，印出幾A幾B。未猜中的狀況回傳True, 若已經猜中答案則回傳False跳出主程式的猜題迴圈"""
    # 先依照格子跑一次loop找出數字和格子接正確的A，並在answer list 和guess list中標註出來
    a_list = [x for x in answer]
    g_list = [y for y in guess]
    for i, char in enumerate(g_list):
        if char == a_list[i]:
            a_list[i] = "A"
            g_list[i] = "A"
    # 標註數字對位置不對的為B
    for i, num in enumerate(g_list):
        if num in a_list and num != "A":
            for j in range(N):
                if a_list[j] == num:
                    a_list[j] = "B"
                    break

    # print(f"answer: {a_list} / guess: {g_list}")
    a_count = 0
    b_count = 0
    for item in a_list:
        if item == "A":
            a_count += 1
        elif item == "B":
            b_count += 1
    print(f"比對結果：{a_count} A {b_count} B")
    return True


# 定義用來清除畫面的function (for windows)
# def clear(): return system('cls')

# TEST CODE
# answer = '7313'
# guess = '3373'
# compare(guess, answer)


#### 主程式從這裡開始 #######
play = True
while play:
    answer = generate_answer()

    get_guess = True
    game = True
    while game:
        # 確認user輸入正確
        while get_guess:
            get_guess = check_input()
        # 確認輸入沒問題後，開始比對結果
        # 完全正確：恭喜答對！(結束或再玩一次)
        if guess == answer:
            print("答對了！\n")
            game = False
        # 如果輸入隱藏指令則跳出
        elif guess == "quit" or guess == "exit" or guess == "answer":
            break
        else:
            get_guess = compare(guess, answer)

    ### 這部分處理玩完一局或輸入特殊指令跳出後的判定 ###
    # 如果輸入隱藏指令則直接跳出
    if guess == "quit" or guess == "exit":
        break
    # 輸入解答指令answer顯示答案
    elif guess == "answer":
        print(f"\n這局的答案是：{answer}\n")
    # 用play, game和get_guess這三個變數來控制3個層級的迴圈
    replay = input("再玩一次？ (y/n)： ")
    if replay.lower() == "y":
        # 執行自訂function設定一個clear來清除上一局的畫面
        clear()
        game = True
        get_guess = True
    else:
        play = False

clear()
print(welcome.game_over)
