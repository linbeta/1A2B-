# 1A2B猜數字遊戲

## 更新：已完成可重複數字版本！
已解決重複數字問題，目前的版本是答案和猜都可以有重複的數字，會比較難！
[Play 1A2B Guess Numbers on Replit](https://replit.com/@sb2828sb/1A2BCai-Shu-Zi-You-Xi?v=1)
---

很久沒玩1A2B這種猜數字遊戲了，印象中小時候玩是電子辭典裡面的內建遊戲，好幾年沒玩了，最近突然想到拿來當作Python的練習。


### 不算太難寫，但Debug花了好多時間啊啊啊！

大概寫完以後，發現當輸入重複數字時，一直會出現程式判定錯誤的問題，例如：如果答案是1234，但當使用者輸入：2244 時，用人工判斷會是2A0B，但我寫的判斷邏輯會出現2A2B。

主因是我寫的loop判定方式會導致B的重複計數，我試圖使用check_a和check_b兩個變數來捕捉比對過的數字，排除某些重複計數的狀況，但如果使用者輸入重複數字，還是會在某些狀況的判定重複計算。

```python=
        if guess == answer:
            print("答對了！\n")
            game = False
        # 如果輸入隱藏指令則直接跳出
        elif guess == "quit" or guess == "exit" or guess == "answer":
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
```

### 暫時還沒有辦法解決問題，所以我先Google

做了些search以後才發現，原來1A2B的猜數字，經典款的玩法答案是沒有重複數字的🤣，有重複數字的判定的確會比較複雜，因此接下來有兩種處理方式：

1. **把規則定義清楚**
把遊戲規則寫清楚一些，設定為部重複數字，生成答案時直接排除重複數字的狀況，使用者輸入重複數字時也可以設定題是輸入錯誤，避免進入這些狀況的判定。
2. **找人討論或詢問解決數學和演算法上面的問題**
多寫幾行判斷式和if/else的設定我相信應該是解得出來，只是有點麻煩，目前有點懶XDD，有空再來解決。

### 再來我想練習的是版本控制

目前先寫好一版以後，希望可以練習梳理程式碼，把學到更簡潔的寫法、更優化的處理方式更新上去。

### 其他延伸練習

找資料的過程中發現這款經典遊戲也很適合拿來後續做AI相關的練習，例如說寫個機器人來解題之類的，也有看到另一種玩法是讓人類出題，寫程式讓電腦來猜的反向玩法。但目前我還沒有想法該如何動手，先把想法記下來給未來的自己挑戰吧！


### 參考資料
1. [Wikipedia](https://zh.wikipedia.org/wiki/%E7%8C%9C%E6%95%B0%E5%AD%97#%E5%90%AB%E9%87%8D%E5%A4%8D%E6%95%B0%E5%AD%97%E7%9A%84%E7%8C%9C%E6%95%B0%E5%AD%97)
2. [碼人日誌](https://coder.tw/?p=549)
3. [猜數字1A2B 洗牌 C++ 【中學生九年級自學專區】](https://www.youtube.com/watch?v=pXyLkiMY2Lc)