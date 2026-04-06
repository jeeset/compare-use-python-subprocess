#不需要寫入至兩個檔案，而是將兩個輸出直接在記憶體比較
import subprocess
import sys

flag = True

file1 = sys.argv[1] # 讀取第二個argument
file2 = sys.argv[2] # 讀取第三個argument

input1 = "23.12\n395.30\n100.46\n564.33\n" # 測資1
input2 = "55.46\n165.70\n540.46\n454.22\n" # 測資2
input3 = "14.15\n315.26\n115.55\n2.56\n" # 測資3
test_inputs = [input1, input2, input3] # 將測資用list存取

for test in test_inputs:
    c1 = subprocess.run([
        "py",file1
        ],
        input = test, #輸入資料
        text = True, # 表示 input 是文字字串，不是 bytes
        capture_output = True # 將輸出和錯誤訊息攔截，並分別存進stdout和stderr
    )

    c2 = subprocess.run([
        "py",file2
        ],
        input = test, #輸入資料
        text = True,
        capture_output = True
    ) 
    if c1.stderr: # 如果c1有錯誤 ，印出錯誤訊息，並跳出此迴圈
        print(f"{file1} 的錯誤訊息：{c1.stderr}")
        break
    if c2.stderr: # 如果c2有錯誤 ，印出錯誤訊息，並跳出此迴圈
        print(f"{file2} 的錯誤訊息：{c2.stderr}")
        break

    if c1.stdout == c2.stdout: # 比較兩個輸出
        flag = True # 如果一樣，把flag設定True
    else:
        flag = False # 如果一樣，把flag設定False，並跳出此迴圈
        print("Wrong Answer!")
        print(f"您的輸出:\n{c1.stdout}")
        print(f"答案輸出:\n{c2.stdout}")
        break
if flag == True: # 是Flag是True，代表所有測資輸出一樣
    print("Right Answer!")
