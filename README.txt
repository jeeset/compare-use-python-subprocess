# 使用subprocess模組比較程式的正確與錯誤

預先寫好測資，在記憶體中直接比較兩個 Python 程式的輸出結果，不需要將輸出寫入檔案，且不需每次在測試時手動輸入。

---
## 套件列表
- python(3.12.7)
## 說明

| 檔案 | 說明 |
|------|------|
| `compare2.py` | 可多筆測資進行比較 |



## 執行方式

```bash=
python compare2.py <你的程式.py> <答案程式.py>
```

- 第一個引數 <你的程式.py>：你要測試的程式（`file1`）
- 第二個引數 <答案程式.py>：作為正確答案的程式（`file2`）

### 範例

```bash=
python compare2.py my_solution.py answer.py
```



## 測資內容

### compare2.py（可多組輸入）

```
測資 1: 23.12 / 395.30 / 100.46 / 564.33
測資 2: 55.46 / 165.70 / 540.46 / 454.22
測資 3: 14.15 / 315.26 / 115.55 / 2.56
```



## 輸出結果

| 情況 | 輸出訊息 |
|------|----------|
| 所有測資輸出一致 | `Right Answer!` |
| 某組測資輸出不同 | `Wrong Answer!` + 兩支程式的輸出對比 |
| 程式本身有錯誤 | 顯示對應程式的錯誤訊息（stderr） |

### Right Answer 範例輸出

```
Right Answer!
```

### Wrong Answer 範例輸出

```
Wrong Answer!
您的輸出:
（your program output）

答案輸出:
（answer program output）
```



## 自訂測資

若要修改測資，直接編輯compare2.py中的 `test_inputs` 列表內容(input1、input2、、、、、)：

```python
input1 = "你的測資\n"
input2 = "另一筆測資\n"
test_inputs = [input1, input2]
```
如果是要寫入的題目，則測資輸入==""==即可

> **注意**：每個輸入值之間用 `\n` 分隔，模擬使用者逐行輸入的行為。



## 運作原理

1. 使用 `subprocess.run()` 分別執行兩支程式，並傳入測資作為標準輸入（`stdin`）
2. 攔截兩支程式的標準輸出（`stdout`）與錯誤訊息（`stderr`）
3. 逐筆比較輸出，若發現不一致即停止並顯示差異

## 成果
![compare_ex](./compare_ex.png)

**影片**
[compare_video](https://youtu.be/EusF-5M99KE%)