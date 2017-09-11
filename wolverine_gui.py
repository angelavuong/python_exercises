from Tkinter import *

root = Tk()


label1 = Label(root, text="Sites")
label2 = Label(root, text="P-Identifiers")
label3 = Label(root, text="Products")
label1.grid(row=0, sticky=W)
label2.grid(row=1, sticky=W)
label3.grid(row=2, sticky=W)

sites = Entry(root)
p_codes = Entry(root)
sites.grid(row=0, column=1)
p_codes.grid(row=1, column=1)

product_list = [''' dynamic_group_weather,
                    dynamic_group_sports,
                    dynamic_group_money,
                    dynamic_group_entertainment,
                    inline_ad,
                    inline_728x90,
                    inline_160x600,
                    dodgy_drone''']

# i = 1
# for each in range(len(product_list)):
#     var_value = 'var' + str(i)
#     var_value = IntVar()
#     i += 1
#     Checkbutton(root, text=str(each), variable=var_value).grid(row=i, column=1, sticky=W)

var1 = IntVar()
Checkbutton(root, text="inline_ad", variable=var1).grid(row=2, column=1, sticky=W)
var2 = IntVar()
Checkbutton(root, text="inline_728x90", variable=var2).grid(row=3, column=1, sticky=W)
var3 = IntVar()
Checkbutton(root, text="inline_160x600", variable=var3).grid(row=4, column=1, sticky=W)
var4 = IntVar()
Checkbutton(root, text="dodgy_drone", variable=var4).grid(row=5, column=1, sticky=W)

var5 = IntVar()
Checkbutton(root, text="dynamic_group_weather", variable=var5).grid(row=6, column=1, sticky=W)
var6 = IntVar()
Checkbutton(root, text="dynamic_group_sports", variable=var6).grid(row=7, column=1, sticky=W)
var7 = IntVar()
Checkbutton(root, text="dynamic_group_money", variable=var7).grid(row=8, column=1, sticky=W)
var8 = IntVar()
Checkbutton(root, text="dynamic_group_entertainment", variable=var8).grid(row=9, column=1, sticky=W)




root.mainloop()
