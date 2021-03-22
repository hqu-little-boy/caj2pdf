import tkinter
from cajparser import CAJParser
import tkinter.messagebox
import tkinter.filedialog
import os.path

# caj = CAJParser(args.input)
# caj.convert(args.output)

global caj_address,caj_address_path,caj

def open_dir_func(lei):
    lei.delete(0, tkinter.END)
    dir_name = tkinter.filedialog.askopenfilename()
    lei.insert(0, dir_name)

# def print_caj_address(event):
#     global caj_address
#     open_dir_func(caj_address)
def get_caj_address(event,):
    global caj_address,caj
    open_dir_func(caj_address)
    caj_address_path = str(caj_address.get())
    caj = CAJParser(caj_address_path)

def caj_convert(event,):
    global caj_address,caj
    # open_dir_func(caj_address)
    caj_convert_path = str(caj_address.get())
    if ".caj" in  caj_convert_path:
        caj_convert_path = str(caj_address.get()).replace(".caj",".pdf")
    elif ".CAJ" in caj_convert_path:
        caj_convert_path = str(caj_address.get()).replace(".CAJ", ".pdf")
    else:
        tkinter.messagebox.showinfo(message="该文件不是caj文件")
        return None
    if os.path.isfile(caj_convert_path):
        tkinter.messagebox.showinfo(message="pdf文件已存在")
    else:
        try:
            caj.convert(caj_convert_path)
            tkinter.messagebox.showinfo(message="pdf文件输出完成")
        except:
            tkinter.messagebox.showinfo(message="pdf文件输出失败")

caj2pdf_TK_gui = tkinter.Tk()
caj2pdf_TK_gui.title("caj2pdf")
caj2pdf_TK_gui.geometry("360x100")

pic_address_sign = tkinter.Label(caj2pdf_TK_gui, text="caj原文件地址：")
# pic_address_sign.pack(side = tkinter.LEFT,anchor = tkinter.N)
pic_address_sign.grid(row=0, column=0, sticky=tkinter.W)
caj_address = tkinter.Entry(caj2pdf_TK_gui)
# pic_address.pack(side = tkinter.TOP)
caj_address.grid(row=0, column=1, columnspan=1, sticky=tkinter.W)
caj_address_btn = tkinter.Button(caj2pdf_TK_gui, text="选择文件")
caj_address_btn.bind("<Button-1>", get_caj_address)
# get_dir_btn.pack(side = tkinter.RIGHT,anchor = tkinter.N)
# get_dir_btn.pack()
caj_address_btn.grid(row=0, column=2, sticky=tkinter.W)

caj_convert_btn = tkinter.Button(caj2pdf_TK_gui, text="转换文件")
caj_convert_btn.bind("<Button-1>", caj_convert)
# get_dir_btn.pack(side = tkinter.RIGHT,anchor = tkinter.N)
# get_dir_btn.pack()
caj_convert_btn.grid(row=1, column=2, sticky=tkinter.W)

caj2pdf_TK_gui.mainloop()
