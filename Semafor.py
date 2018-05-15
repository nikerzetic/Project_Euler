import tkinter as tk

okno = tk.Tk()
okno.title('Semafor')

platno = tk.Canvas(okno, bg='white')
platno.grid(column=0, row=1, columnspan=3)
b1 = tk.Button(okno, text='zelena', command=lambda: platno.configure(bg='green'))
b1.grid(column=0, row=0)
b2 = tk.Button(okno, text='rumena', command=lambda: platno.configure(bg='yellow'))
b2.grid(column=1, row=0)
b3 = tk.Button(okno, text='rdeča', command=lambda: platno.configure(bg='red'))
b3.grid(column=2, row=0)

okno.mainloop()
