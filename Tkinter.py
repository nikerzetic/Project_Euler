import tkinter as tk


class Vmesnik:
    def __init__(self, master):
        self.master = master
        master.title('Pretvornik iz € v $')

        self.vhod = tk.StringVar()
        self.izhod = tk.StringVar()

        self.vnos = tk.Entry(self.master, textvariable=self.vhod)
        self.vnos.grid(column=0, row=0)

        self.napis = tk.Label(self.master, text='€ =')
        self.napis.grid(column=1, row=0)

        self.okvir = tk.LabelFrame(self.master)
        self.okvir.grid(column=2, row=0)

        self.izpis = tk.Label(self.okvir, textvariable=self.izhod, width=20)
        self.izpis.grid(column=2, row=0)

        self.gumb = tk.Button(self.master, text='Pretvori!', command=self.pretvori)
        self.gumb.grid(column=3, row=0)

    def pretvori(self):
        try:
            euro = self.vhod
            self.izhod.set(str(1.198275 * float(euro)))
            self.osvezi()
        except:
            pass

    def osvezi(self):
        self.izpis.grid_remove()
        self.izpis = tk.Label(self.okvir, textvariable=self.izhod, width=20)
        self.izpis.grid(column=2, row=0)


okno = tk.Tk()
vmesnik = Vmesnik(okno)
okno.mainloop()

