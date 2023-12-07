import tkinter as tk
import deepl
from datetime import datetime

auth_key = "you key API"
translator = deepl.Translator(auth_key)
a = "ZH"
b = "EN-us"

def translate():
    word = entry_word.get()
    if choice_language.get().lower() == '中文':
        result = translator.translate_text(word, target_lang=a)
    elif choice_language.get().lower() == '美式英文':
        result = translator.translate_text(word, target_lang=b)
    else:
        result = translator.translate_text(word, target_lang=a)

    translation_result.config(text=result.text)

    save_choice = save_var.get()
    if save_choice.lower() == 'yes':
        today_date = datetime.now().strftime("%Y%m%d")
        file_path = f"C:/yuanD/Honework/{today_date}.txt"
        with open(file_path, "a", encoding="utf-8") as file:
            file.write(f"查询的单词: {word}\n")
            file.write(f"翻译结果: {result.text}\n\n")

# 创建主窗口
root = tk.Tk()
root.title("翻译器")

# 创建并布置控件
label_language = tk.Label(root, text="选择翻译语言：")
label_language.pack()

choice_language = tk.StringVar(root)
choice_language.set("中文")
choices = ["中文", "美式英文"]
language_menu = tk.OptionMenu(root, choice_language, *choices)
language_menu.pack()

label_word = tk.Label(root, text="请输入单词：")
label_word.pack()

entry_word = tk.Entry(root)
entry_word.pack()

translate_button = tk.Button(root, text="翻译", command=translate)
translate_button.pack()

translation_result = tk.Label(root, text="")
translation_result.pack()

label_save = tk.Label(root, text="是否将查询的单词和结果保存到本地的记事本？(yes/no):")
label_save.pack()

save_var = tk.StringVar(root)
save_var.set("no")
save_choices = ["yes", "no"]
save_menu = tk.OptionMenu(root, save_var, *save_choices)
save_menu.pack()

root.mainloop()
