import tkinter as tk

# ウィンドウの作成
root = tk.Tk()
root.geometry("300x200")

# ボタンの作成
button = tk.Button(root, text="クリックしてください")

# ボタンの配置
button.pack()

# ウィンドウの表示
root.mainloop()