import random
import welcome
from os import system

# TODO: 設計歡迎畫面
print(welcome.intro)
# TODO: 難度選擇，確認後開始遊戲

# 難度設定：N = 幾位數字
N = 4
NUMBERS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


def clear(): return system('cls')


get_guess = True
game = True
play = True

while play:

    # 產生一亂數答案，多一步驟把數字轉為str，做後續判讀：
    ans_num = random.randint(0, 10**N)

    # 如果有少的位數，將前幾格補上"0"
    if ans_num < 10**(N-1):
        answer = str(ans_num).zfill(N)
    else:
        answer = str(ans_num)

    while game:
        # 用input取得user猜測數字，判定輸入是否合格，若非N位數字擇提示輸入錯誤，重新跳出輸入訊息
        while get_guess:
            guess = input(f"請猜{N}位數字： ")

            # TODO: 設計隱藏指令: 看答案和退出遊戲
            if guess == "quit" or guess == "exit" or guess == "answer":
                break

            if len(guess) != N:
                print("輸入錯誤，請重新輸入")
            else:
                for x in guess:
                    if x not in NUMBERS:
                        print(f"請輸入{N}個數字")
                        get_guess = True
                        break
                    else:
                        get_guess = False

        # 比對答案
        # 還沒猜對：show出xAyB，讓使用者繼續輸入
        # 完全正確：恭喜答對！(結束或再玩一次)
        if guess == answer:
            print("答對了！\n")
            game = False
        elif guess == "quit" or guess == "exit":
            break
        else:
            # 用a_counts代表位置和數字皆正確的數量，用b_counts代表數字正確但位置不正確
            a_counts = 0
            b_counts = 0
            check_a = answer
            for i in range(N):
                if guess[i] == answer[i]:
                    a_counts += 1
                    # 額外設定一個變數check_a來標記已經猜對的格子，這樣檢查b_counts時才不會出錯
                    check_a = check_a.replace(answer[i], "A")
                    # print(check_a)
                elif guess[i] in check_a:
                    # 對數字正確位置不正確的狀況，也用取代的方式建立一個變數check_b，避免檢查時重複計算
                    check_b = check_a.replace(guess[i], "B")
                    b_counts += 1
                    # print(check_b)

            print(f"比對結果：{a_counts} A {b_counts} B")
            get_guess = True

    # 如果輸入隱藏指令則直接跳出
    if guess == "quit" or guess == "exit":
        break
    # 用play, game和get_guess這三個變數來控制3個層級的迴圈
    replay = input("再玩一次？ (y/n)： ")
    if replay.lower() == "y":
        # 用lambda function設定一個clear來清除上一局的畫面
        clear()
        game = True
        get_guess = True
    else:
        play = False

clear()
print(welcome.game_over)
