from tkinter import *
from tkinter import messagebox


class TicketSales(object):
    def __init__(self, window):

        self.window = window
        self.window.title("TicketSales")
        self.window.geometry("500x500")
        self.window.config(bg="grey")

        heading = Label(window, text=' Easyticket', bg="green"  )
        heading["font"] = "Ariel", 30
        heading.place(x=145, y=0)


        self.cell_entry_label = Label(self.window, text="Enter Mobile Number:", bg="yellow")
        self.cell_entry = Entry(self.window)
        self.cell_entry_label.place(x=20, y=55)
        self.cell_entry.place(x=230, y=55)


        self.ticket_label = Label(self.window, text="Select Ticket Category:", bg="yellow")
        self.options = ["Soccer", "Movie", "Theater"]
        self.variable = StringVar(self.window)
        self.variable.set("Select Ticket")
        self.ticket_op = OptionMenu(window, self.variable, *self.options)
        self.ticket_label.place(x=20, y=100)
        self.ticket_op.place(x=230, y=95)


        self.ticket_no_label = Label(self.window, text="Number of Tickets Bought:", bg="yellow")
        self.ticket_spinbox = Spinbox(self.window, width=10, from_=0, to=100)
        self.ticket_no_label.place(x=20, y=150)
        self.ticket_spinbox.place(x=230, y=150)


        self.calc_button = Button(self.window, text='Calculate Ticket', bg="yellow", command=self.calc_prepayment)
        self.clear_button = Button(self.window, text='Clear Entries', bg="yellow", command=self.clear)
        self.calc_button.place(x=100, y=200)
        self.clear_button.place(x=290, y=200)


        self.border1 = Label(self.window, text="Thank you for your support ", bg="yellow")
        self.border2 = Label(self.window, text="Dankie vir jou ondersteuning", bg="yellow")
        self.border1.place(y=260 , x=35)
        self.border2.place(y=450, x=35)

        self.amount_pay = Label(self.window, text="", bg="green")
        self.reserve = Label(self.window, text="", bg="green")
        self.cell_label = Label(self.window, text="", bg="green")
        self.amount_pay.place(x=50, y=300)
        self.reserve.place(x=50, y=350)
        self.cell_label.place(x=50, y=400)

    def calc_prepayment(self):
        ticket_no = int(self.ticket_spinbox.get())
        vat = 0.14
        try:
            int(self.cell_entry.get())
            if len(self.cell_entry.get()) < 10 or len(self.cell_entry.get()) > 10:
                raise ValueError

            elif self.variable.get() == "Select Ticket":
                raise ValueError

            elif int(self.ticket_spinbox.get()) == 0:
                raise ValueError

            elif self.variable.get() == "Soccer":
                price = 40  # in Rands
                price_pay = (price * ticket_no) + (price * ticket_no * vat)
                text = ("Amount Payable: R{}".format(price_pay))
                self.amount_pay.config(text=text)

            elif self.variable.get() == "Movie":
                price = 75  # in Rands
                price_pay = (price * ticket_no) + (price * ticket_no * vat)
                text = ("Amount Payable: R{}".format(price_pay))
                self.amount_pay.config(text=text)

            elif self.variable.get() == "Theater":
                price = 100  # in Rands
                price_pay = (price * ticket_no) + (price * ticket_no * vat)
                text = ("Amount Payable: R{}".format(price_pay))
                self.amount_pay.config(text=text)

            reserve_text = "Reservation for {} for : {} ".format(self.variable.get(), ticket_no)
            cell_text = "Reservation Made By: {}".format(self.cell_entry.get())
            self.reserve.config(text=reserve_text)
            self.cell_label.config(text=cell_text)

        except ValueError:  # Error Message
            messagebox.showerror(message="INVALID - Please Try Again")

    def clear(self):
        self.cell_entry.delete(0, END)
        self.cell_entry.focus()
        self.variable.set("Select Ticket")
        self.ticket_spinbox.delete(0, END)
        self.ticket_spinbox.insert(0, 0)
        self.amount_pay.config(text="")
        self.reserve.config(text="")
        self.cell_label.config(text="")


root = Tk()
TicketSales(root)
root.mainloop()