import tkinter
# 画面作成
root = tkinter.Tk()
root.geometry('300x200')

#「開始」ボタン作成
btn=tkinter.Button(root,text="開始",width=14)
#配置
btn.pack(fill='x',padx=20,side='top')

#「終了」ボタン作成
btn = tkinter.Button(root, text='終了',width=14)
# 配置
btn.pack(fill='x',padx=20,side='top')

root.mainloop()
