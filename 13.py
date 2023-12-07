import random
import tkinter as tk
from tkinter import filedialog
index = 0
words = []  # 添加默认空列表



# 读取文本内容并处理为单词列表
def read_text(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()
        words = []
        word = ""
        translation = ""
        for line in lines:
            if line.startswith("查询的单词:"):
                word = line.split(": ")[1].strip()
            elif line.startswith("翻译结果:"):
                translation = line.split(": ")[1].strip()
                words.append((word, translation))
        return words

# 生成缺少随机数量字母的单词
def generate_incomplete_word(word):
    if len(word) <= 3:  # 如果单词长度小于等于3，不隐藏字母
        return word

    hidden_count = random.randint(1, len(word) - 2)
    indices = random.sample(range(1, len(word) - 1), hidden_count)
    incomplete_word = ''.join([' ' if i in indices else word[i] for i in range(len(word))])
    return incomplete_word

# 显示下一个单词，并验证用户输入是否正确
def show_next_word():
    global index
    global words
    if index < len(words):
        word, translation = words[index]
        incomplete_word = generate_incomplete_word(word)
        lbl_word.config(text=f"单词: {incomplete_word}")
        lbl_translation.config(text=f"翻译结果: {translation}")

        user_input = entry_user_input.get()
        if user_input.strip() == word:
            lbl_feedback.config(text="输入正确！", fg="green")
            entry_user_input.delete(0, 'end')  # 清空输入框内容
            index += 1
            if index < len(words):
                show_next_word()
            else:
                lbl_feedback.config(text="所有单词已显示完毕", fg="blue")
        else:
            lbl_feedback.config(text="输入错误！请重新尝试。", fg="red")
    else:
        lbl_feedback.config(text="所有单词已显示完毕", fg="blue")


# 读取文本内容并准备显示第一个单词（保持不变）

# 创建 GUI 界面
root = tk.Tk()
root.title("单词填空练习")

# 改变字体大小
font_style = ('Arial', 14)

lbl_word = tk.Label(root, text="单词: ", font=font_style)
lbl_word.pack()

lbl_translation = tk.Label(root, text="翻译结果: ", font=font_style)
lbl_translation.pack()

entry_user_input = tk.Entry(root, font=font_style)
entry_user_input.pack()

btn_submit = tk.Button(root, text="提交", command=show_next_word, font=font_style)
btn_submit.pack()

def select_file():
    file_path = filedialog.askopenfilename(initialdir="/", title="选择文件", filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
    if file_path:
        global words
        words = read_text(file_path)
        random.shuffle(words)
        show_next_word()

btn_select_file = tk.Button(root, text="选择文档", command=select_file, font=font_style)
btn_select_file.pack()

lbl_feedback = tk.Label(root, text="", font=font_style)
lbl_feedback.pack()

root.mainloop()