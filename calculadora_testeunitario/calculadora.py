import tkinter
from tkinter import messagebox

def adicao(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

def multi(n1,n2):
    return n1*n2

def div(n1,n2):
    if n2 == 0:
        return "Erro: divisão por zero"
    return n1 / n2

def calcular(operacao):
    try:
        n1 = float(entry1.get())
        n2 = float(entry2.get())
        if operacao == '+':
            resultado = adicao(n1, n2)
        elif operacao == '-':
            resultado = sub(n1, n2)
        elif operacao == '*':
            resultado = multi(n1, n2)
        elif operacao == '/':
            resultado = div(n1, n2)
        label_result.config(text=f"Resultado: {resultado}")
    except ValueError:
        messagebox.showerror("Erro", "Digite números válidos!")

root = tkinter.Tk()
root.title("Calculadora")
root.geometry("400x300")
root.configure(bg="#1e1e1e")  

entry1 = tkinter.Entry(root, font=("Arial", 18), justify='left', bg="#333", fg="#ffffff")
entry1.grid(row=0, column=0, columnspan=4, padx=20, pady=20, sticky="we")

entry2 = tkinter.Entry(root, font=("Arial", 18), justify='left', bg="#333", fg="#ffffff")
entry2.grid(row=1, column=0, columnspan=4, padx=20, pady=20, sticky="we")

btn_adicao = tkinter.Button(root, text="+", width=10, height=2, bg="#47ff22", fg="#000000",
command=lambda: calcular('+'))
btn_adicao.grid(row=2, column=0, padx=10, pady=10)

btn_sub = tkinter.Button(root, text="-", width=10, height=2, bg="#ff2222", fg="#FFFFFF",
command=lambda: calcular('-'))
btn_sub.grid(row=2, column=1, padx=10, pady=10)

btn_multi = tkinter.Button(root, text="*", width=10, height=2, bg="#2238ff", fg="#FFFFFF",
command=lambda: calcular('*'))
btn_multi.grid(row=2, column=2, padx=10, pady=10)

btn_div = tkinter.Button(root, text="/", width=10, height=2, bg="#ff22ff", fg="#FFFFFF",
command=lambda: calcular('/'))
btn_div.grid(row=2, column=3, padx=10, pady=10)

label_result = tkinter.Label(root, text="Resultado:", font=("Arial", 18), bg="#1e1e1e", fg="#FFFFFF")
label_result.grid(row=3, column=0, columnspan=4, pady=20)

root.mainloop()
