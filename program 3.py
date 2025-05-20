from tkinter import Tk, Button, Entry, Canvas, Label, Text, Frame, END, W, E

class KonversiSuhu:
    def __init__(self, master):
        self.master = master
        master.title("Konversi Suhu Celcius ke Fahrenheit")
        input_frame = Frame(master)
        input_frame.pack()
        self.label = Label(input_frame, text="Suhu °C:")
        self.label.grid(row=0, column=0)
        self.entry = Entry(input_frame)
        self.entry.grid(row=0, column=1)
        self.konversi_button = Button(input_frame, text="Konversi", command=self.konversi)
        self.konversi_button.grid(row=1, column=0, columnspan=2)

        output_frame = Frame(master)
        output_frame.pack()
        self.hasil_label = Label(output_frame, text="Hasil: ")
        self.hasil_label.pack()
        self.canvas = Canvas(output_frame, width=100, height=30, bg="white")
        self.canvas.pack()
        self.ket_label = Label(output_frame, text="Keterangan:")
        self.ket_label.pack()
        self.text_ket = Text(output_frame, width=30, height=2)
        self.text_ket.pack()

    def konversi(self):
        try:
            C = float(self.entry.get())
            F = C * 9/5 + 32
            self.hasil_label.config(text=f"Hasil: {F:.2f} °F")
            self.canvas.delete("all")
            if C <= 10:
                warna = "blue"
                hawa = "dingin"
            elif C <= 30:
                warna = "green"
                hawa = "normal"
            else:
                warna = "red"
                hawa = "panas"
            self.canvas.create_rectangle(10, 5, 100, 25, fill=warna)
            self.text_ket.delete("1.0", END)
            self.text_ket.insert(END, f"Suhu terasa {hawa}")
        except:
            self.hasil_label.config(text="Masukkan angka yang valid.")
            self.text_ket.delete("1.0", END)
        self.entry.delete(0, END)

root = Tk()
my_gui = KonversiSuhu(root)
root.mainloop()