from tkinter import *
from tkinter import ttk
import tkinter.messagebox
from time import strftime


# The class represents the main page of a project prototypes website.

class Project_prototypes_main_page:
    def __init__(self, window):

        self.first_machine = CircularQueue(20)
        self.second_machine = CircularQueue(20)
        self.third_machine = CircularQueue(8)
        self.fouth_machine = CircularQueue(12)
        
        self.fram1 = Frame(window, bg = 'lightgreen')
        self.fram1.grid(row=2, column=1)
        self.fram2 = Frame(window, bg = 'lightgreen')
        self.fram2.grid(row=4, column=1)
        self.fram3 = Frame(window, bg = 'lightgreen')
        self.fram3.grid(row=6, column=1)
        self.fram4 = Frame(window, bg = 'lightgreen')
        self.fram4.grid(row=8, column=1)

        self.menubar = Menu(window, background='blue', fg='white')
        window.config(menu=self.menubar)
        file_menu = Menu(self.menubar, tearoff = False, bg = "pink", fg = "white")
        file_menu.add_command(label = "Login Page", command = self.turnback)
        self.menubar.add_cascade(label = "Return", menu = file_menu, underline=0)

        scale_factor = 5

        # Define image paths (use double backslashes or forward slashes)
        self.image_path_1 = 'C:/Bew colllege learning file all of it/python/HW all/HW python/HW#9/supertrain-gif-maker (1).gif'
        self.image_path_2 = 'C:/Bew colllege learning file all of it/python/HW all/HW python/HW#9/supertrain-gif-maker (2).gif'
        self.image_path_3 = 'C:/Bew colllege learning file all of it/python/HW all/HW python/HW#9/supertrain-gif-maker (3).gif'
        self.image_path_4 = 'C:\Bew colllege learning file all of it\python\project python semester 1 year 1\lung-gif-maker.gif'

        self.image_1 = PhotoImage(file=self.image_path_1)
        self.label_1 = Label(window, image=self.image_1, width=200, height=150, bg='lightgreen')

        self.image_2 = PhotoImage(file=self.image_path_2)
        self.label_2 = Label(window, image=self.image_2, width=200, height=150, bg='lightgreen')

        self.image_3 = PhotoImage(file=self.image_path_3)
        self.label_3 = Label(window, image=self.image_3, width=200, height=150, bg='lightgreen')

        self.image_4 = PhotoImage(file=self.image_path_4)
        self.label_4 = Label(window, image=self.image_4, width=200, height=150, bg='lightgreen')

        self.label_1.grid(row=2, column=0, padx=50)
        self.label_2.grid(row=4, column=0, padx=50)
        self.label_3.grid(row=6, column=0, padx=50)
        self.label_4.grid(row=8, column=0, padx=50)
        
        # Resize images
        self.image_1 = self.image_1.subsample(scale_factor, scale_factor)
        self.image_2 = self.image_2.subsample(scale_factor, scale_factor)
        self.image_3 = self.image_3.subsample(scale_factor, scale_factor)
        self.image_4 = self.image_4.subsample(scale_factor, scale_factor)
        
        # Update labels with resized images
        self.label_1.config(image=self.image_1)
        self.label_2.config(image=self.image_2)
        self.label_3.config(image=self.image_3)
        self.label_4.config(image=self.image_4)

        self.button_1 = Button(self.fram1, text='Book', command= self.command_1, width= 10)
        self.button_2 = Button(self.fram2, text='Book', command= self.command_2, width= 10)
        self.button_3 = Button(self.fram3, text='Book', command= self.command_3, width= 10)
        self.button_4 = Button(self.fram4, text='Book', command= self.command_4, width= 10)
        
        self.button_1.grid(row= 1, column=1)
        self.button_2.grid(row= 1, column=1)
        self.button_3.grid(row= 1, column=1)
        self.button_4.grid(row= 1, column=1)

    
        self.lbl = Label(window, font=('calibri', 18, 'bold'),
            background='lightgreen',
            foreground='black')
        
        self.lbl.grid(row=1, column=1, padx=50, pady=10, sticky=E)

        self.time()

        self.label_countdown_1 = Label(window, font=('calibri', 12, 'bold'),
                background='grey',
                foreground='white')
        self.label_countdown_1.grid(row=1, column=0, padx=50, pady=10, sticky=E)
        self.countdown_1(600)

        
        self.label_countdown_2 = Label(window, font=('calibri', 12, 'bold'),
                background='grey',
                foreground='white')
        self.label_countdown_2.grid(row=3, column=0, padx=50, pady=10, sticky=E)
        self.countdown_2(300)

        
        self.label_countdown_3 = Label(window, font=('calibri', 12, 'bold'),
                background='grey',
                foreground='white')
        self.label_countdown_3.grid(row=5, column=0, padx=50, pady=10, sticky=E)
        self.countdown_3(480)

        
        self.label_countdown_4 = Label(window, font=('calibri', 12, 'bold'),
                background='grey',
                foreground='white')
        self.label_countdown_4.grid(row=7, column=0, padx=50, pady=10, sticky=E)
        self.countdown_4(240)

        self.ima = 'C:\Bew colllege learning file all of it\python\project python semester 1 year 1\people_queue_regular_icon_205081.gif'
        self.im1 = PhotoImage(file=self.ima)
        self.label_101 = Label(self.fram1, image=self.im1, width=50, height=70, bg='lightgreen')
        self.im2 = PhotoImage(file=self.ima)
        self.label_102 = Label(self.fram2, image=self.im2, width=50, height=70, bg='lightgreen')
        self.im3 = PhotoImage(file=self.ima)
        self.label_103 = Label(self.fram3, image=self.im3, width=50, height=70, bg='lightgreen')
        self.im4 = PhotoImage(file=self.ima)
        self.label_104 = Label(self.fram4, image=self.im4, width=50, height=70, bg='lightgreen')
        self.label_101.grid(row= 2, column=1)
        self.label_102.grid(row= 2, column=1)
        self.label_103.grid(row= 2, column=1)
        self.label_104.grid(row= 2, column=1)
        scale = 10
        self.image_101 = self.im1.subsample(scale, scale)
        self.image_102 = self.im2.subsample(scale, scale)
        self.image_103 = self.im3.subsample(scale, scale)
        self.image_104 = self.im4.subsample(scale, scale)
        self.label_101.config(image=self.image_101)
        self.label_102.config(image=self.image_102)
        self.label_103.config(image=self.image_103)
        self.label_104.config(image=self.image_104)

        self.laa1 = Label(self.fram1,bg='lightgreen', text='0', font= ("Arial", 10, 'bold'))
        self.laa2 = Label(self.fram2, bg='lightgreen', text='0', font= ("Arial", 10, 'bold'))
        self.laa3 = Label(self.fram3, bg='lightgreen', text='0', font= ("Arial", 10, 'bold'))
        self.laa4 = Label(self.fram4, bg='lightgreen', text='0', font= ("Arial", 10, 'bold'))
        self.laa1.grid(row= 2, column=2)
        self.laa2.grid(row= 2, column=2)
        self.laa3.grid(row= 2, column=2)
        self.laa4.grid(row= 2, column=2)
        # first_machine = CircularQueue(20)
        # second_machine = CircularQueue(
      

    # def show_queue1(self):
    #     pass
    # def show_queue2(self):
    #     pass
    # def show_queue3(self):
    #     pass
    # def show_queue4(self):
    #     pass

    def set_laa1_text(self, laa1):
        self.laa1.config(text=laa1)
    def set_laa2_text(self, laa2):
        self.laa2.config(text=laa2)
    def set_laa3_text(self, laa3):
        self.laa3.config(text=laa3)
    def set_laa4_text(self, laa4):
        self.laa4.config(text=laa4)


    def turnback(self):
        self.fram1.destroy()
        self.fram2.destroy()
        self.fram3.destroy()
        self.fram4.destroy()

        first_page_login(window)
        self.label_1.destroy()
        self.label_2.destroy()
        self.label_3.destroy()
        self.label_4.destroy()
        self.button_1.destroy()
        self.button_2.destroy()
        self.button_3.destroy()
        self.button_4.destroy()
        self.lbl.destroy()
        self.label_countdown_1.destroy()
        self.label_countdown_2.destroy()
        self.label_countdown_3.destroy()
        self.label_countdown_4.destroy()
        self.menubar.destroy()
       
    def command_1(self):
        Popup_Roller_Coaster_Train(self)

    def command_2(self):
        Popup_Tornado(self)

    def command_3(self):
        Popup_Thunder_Bird(self)

    def command_4(self):
        Popup_Super_Splash(self)

    def time(self):
        string = strftime('%H:%M:%S %p')
        self.lbl.config(text=string)
        self.lbl.after(1000, self.time)

    def countdown_1(self, count):
            hour = 0
            minute = int(count/60)%60
            sec = count % 60

            # change text in label        
            self.label_countdown_1['text'] = f"Ends in: {hour:02}:{minute:02}:{sec:02}"

            if count > 0:
                # call countdown again after 1000ms (1s)
                window.after(1000, self.countdown_1, count-1)

            if count == 0:
                new_count = 600
                self.countdown_1(new_count)

            if count == 0:
                tkinter.messagebox.showinfo("Roller Coaster Train", "This round has ended. The next round please stand by")
                x=[]
                for i in range(20):
                    p = self.first_machine.dequeue()
                    x.append(p)
                return x

    def countdown_2(self, count):
            hour = 0
            minute = int(count/60)%60
            sec = count % 60

            # change text in label        
            self.label_countdown_2['text'] = f"Ends in: {hour:02}:{minute:02}:{sec:02}"

            if count > 0:
                # call countdown again after 1000ms (1s)
                window.after(1000, self.countdown_2, count-1)

            if count == 0:
                new_count = 300
                self.countdown_2(new_count)

            if count == 0:
                tkinter.messagebox.showinfo("Tornado", "This round has ended. The next round please stand by")
                x=[]
                for i in range(20):
                    p = self.first_machine.dequeue()
                    x.append(p)
                return x



    def countdown_3(self, count):
            hour = 0
            minute = int(count/60)%60
            sec = count % 60

            # change text in label        
            self.label_countdown_3['text'] = f"Ends in: {hour:02}:{minute:02}:{sec:02}"

            if count > 0:
                # call countdown again after 1000ms (1s)
                window.after(1000, self.countdown_3, count-1)

            if count == 0:
                new_count = 480
                self.countdown_3(new_count)

            if count == 0:
                tkinter.messagebox.showinfo("Thunder Bird", "This round has ended. The next round please stand by")
                x=[]
                for i in range(8):
                    p = self.first_machine.dequeue()
                    x.append(p)
                return x
            

    def countdown_4(self, count):
            hour = 0
            minute = int(count/60)%60
            sec = count % 60

            # change text in label        
            self.label_countdown_4['text'] = f"Ends in: {hour:02}:{minute:02}:{sec:02}"

            if count > 0:
                # call countdown again after 1000ms (1s)
                window.after(1000, self.countdown_4, count-1)

            if count == 0:
                new_count = 240
                self.countdown_4(new_count)

            if count == 0:
                tkinter.messagebox.showinfo("Super Splash", "This round has ended, The next round please stand by")
                x=[]
                for i in range(12):
                    p = self.first_machine.dequeue()
                    x.append(p)
                return x

# The above class represents a login page for the first page of a website.
            
class first_page_login:
    def __init__(self, window):

            window.title("My Dream World")
            window.geometry("615x1000")
            window.configure(bg='lightpink')
            window.iconbitmap('463407-200.ico')

            self.image = PhotoImage(file='C:\Bew colllege learning file all of it\python\project python semester 1 year 1\logo-removebg-preview.png')

            self.labe = Label(window,text='', padx = 140, pady = 80, bg='lightpink')
            self.labe.grid(row=1, column=2)

            self.label_1 = Label(window, image=self.image, padx = 140, pady = 5, bg='lightpink')
            self.label_1.grid(row=5, column=2)

            self.label_2 = Label(window, text= "Make a Reservation \nTheme Park", font= ("Times New Roman", 20, "bold"), padx = 140, pady = 5, bg='lightpink')
            self.label_2.grid(column=2, row=6)


            self.button1 = Button(window, text= "Click Start", width = 12, command= self.make, font= ("Arial", 10, 'italic'), padx = 140, pady = 10, fg = '#864d9c')
            self.button1.grid(column=2, row=7)

            self.label_4 = Label(window, text= "Please Enjoy", font= ("Georgia", 12, 'bold'), padx = 140, pady = 10, bg='lightpink', fg = '#006db1')
            self.label_4.grid(column=2, row=8)
            self.label_3 = Label(window, text= "- - -  \"Your Dream World\"  - - -", font= ("Verdana", 14, "bold"), padx = 140, bg='lightpink', fg = '#864d9c')
            self.label_3.grid(column=2, row=9)
            self.label_11 = Label(window, text= "Open : 08:00:00 AM", font= ("Verdana", 10, 'bold'), padx = 140, pady = 10, bg='lightpink', fg = '#9a6db1')
            self.label_11.grid(column=2, row=10)
            self.label_12 = Label(window, text= "Close : 18:00:00 PM", font= ("Verdana", 10, "bold"), padx = 140, bg='lightpink', fg = '#9a6db1')
            self.label_12.grid(column=2, row=11)


    def make(self):
        # nw = datetime.now()
        # hrs = nw.hour;mins = nw.minute;secs = nw.second;
        # zero = timedelta(seconds = secs+mins*60+hrs*3600)
        # st = nw - zero # this take me to 0 hours. 
        # time1 = st + timedelta(seconds=8*3600+0*60) # this gives 8:00 AM
        # time2 = st + timedelta(seconds=18*3600+30*60)  # this gives 18:30 PM
       
        # if time2 > nw > time1:
            window.configure(bg='lightgreen')
            self.button1.destroy()
            self.labe.destroy()
            self.label_1.destroy()
            self.label_2.destroy()
            self.label_4.destroy()
            self.label_3.destroy()
            self.label_11.destroy()
            self.label_12.destroy()


            Project_prototypes_main_page(window)
        # else:
        #     tkinter.messagebox.showwarning("My Dream World", "The reservation service is closed.")

# The class is used to create a popup window for making a reservation.

class Popup_make_reservasion_info_main:
    def __init__(self):
        self.name_var = StringVar()
        self.surname_var = StringVar()
        self.amount_var = IntVar()

        self.name_label = None
        self.surname_label = None
        self.amount_label = None

        self.pop = Tk()
        self.pop.geometry("320x300")
        self.pop.iconbitmap('463407-200.ico')

       


    def set_name_label(self, label):
        self.name_label = label

    def set_surname_label(self, label):
        self.surname_label = label

    def set_amount_label(self, label):
        self.amount_label = label

    def get_name_var(self):
        return self.name_var.get()

    def get_surname_var(self):
        return self.surname_var.get()

    def get_amount_var(self):
        return self.amount_var.get()

    def update_name_label(self):
        if self.name_label:
            self.name_label.config(text=f"Name: {self.get_name_var()}")

    def update_surname_label(self):
        if self.surname_label:
            self.surname_label.config(text=f"Surname: {self.get_surname_var()}")

    def update_amount_label(self):
        if self.amount_label:
            self.amount_label.config(text=f"Amount of people: {self.get_amount_var()}")

            #!----------------------------------------------------------------
    def name(self):
        self.label_1 = Label(self.pop, text= "Name:", font= ("Arial", 10, 'bold'))
        self.label_1.grid(row=1,column=1, sticky=W, pady=10, padx=10)

    def surname(self):
        self.label_2 = Label(self.pop, text= "Surname:", font= ("Arial", 10, 'bold'))
        self.label_2.grid(row=2,column=1, sticky=W, pady=10, padx=10)

    def description(self):
        self.label_3 = Label(self.pop, text= "Make a reservation:", font= ("Arial", 10, 'bold'))
        self.label_3.grid(row=4,column=1, sticky=W, pady=10, padx=10)

    def entry_name(self):
        self.entry_1 = Entry(self.pop, textvariable= self.name, font=('calibre',10,'normal'))
        self.entry_1.grid(row=1,column=2, pady=10)

    def entry_surname(self):
        self.entry_2 = Entry(self.pop, textvariable= self.sur_var_1, font=('calibre',10,'normal'))
        self.entry_2.grid(row=2,column=2, pady=10)
        
    def button_click(self):
        self.btn_1 = Button(self.pop, text = "Confirm", font= ("Arial", 10, 'italic'), width = 17)
        self.btn_1.grid(row=4, column = 2, padx=10, pady=5)

    def amount_of_people(self):
        self.label_34 = Label(self.pop, text= "Amount of people:", font= ("Arial", 10, 'bold'))
        self.label_34.grid(row=3,column=1, sticky=W, pady=10, padx=10)

    
# The class `Popup_Roller_Coaster_Train` is a subclass of `Popup_make_reservasion_info_main` and is
# used for making reservations for a roller coaster train.


class Popup_Roller_Coaster_Train(Popup_make_reservasion_info_main):
    def __init__(self, main_page_instance):
        super().__init__()

        self.pop.title("Roller Coaster")

        self.name_var_1 = StringVar()
        self.sur_var_1 = StringVar()
        self.amount_1 = IntVar()

        self.main_page_instance = main_page_instance

        super().name()
        self.entry_1 = Entry(self.pop, textvariable= self.name_var_1, font=('calibre',10,'normal'))
        self.entry_1.grid(row=1,column=2)

        super().surname()
        self.entry_2 = Entry(self.pop, textvariable= self.sur_var_1, font=('calibre',10,'normal'))
        self.entry_2.grid(row=2,column=2)
        
        super().amount_of_people()
        self.spinbox_people_1 = ttk.Spinbox(self.pop, textvariable= self.amount_1, from_ = 1, to = 20, width = 5, wrap =True)
        self.spinbox_people_1.grid(row=3,column=2,padx=6, sticky=W)
    
        super().description()
        self.btn_1 = Button(self.pop, text = "Confirm", font= ("Arial", 10, 'italic'), width = 17, command=self.add_queue_1)
        self.btn_1.grid(row=4, column = 2, padx=5, pady=5)
        # , command= queue_of_Popup_Roller_Coaster_Train(20)

    @staticmethod
    def get_data_1(self):
        full_name = self.name_var_1.get() +' '+ self.sur_var_1.get()
        tup = (full_name, self.amount_1.get())
        return tup
        
    def add_queue_1(self):
        amount = self.amount_1.get()
        for _ in range(amount):
            self.main_page_instance.first_machine.enqueue(self.get_data_1)
        self.main_page_instance.set_laa1_text(self.main_page_instance.first_machine.get_size_element())
        self.pop.destroy()

    def set_name_label(self, label):
        self.name_label = label

    def set_surname_label(self, label):
        self.surname_label = label

    def set_amount_label(self, label):
        self.amount_label = label

    def get_name_var(self):
        return self.name_var.get()

    def get_surname_var(self):
        return self.surname_var.get()

    def get_amount_var(self):
        return self.amount_var.get()

    def update_name_label(self):
        if self.name_label:
            self.name_label.config(text=f"Name: {self.get_name_var()}")

    def update_surname_label(self):
        if self.surname_label:
            self.surname_label.config(text=f"Surname: {self.get_surname_var()}")

    def update_amount_label(self):
        if self.amount_label:
            self.amount_label.config(text=f"Amount of people: {self.get_amount_var()}")

    # def delete_queue_1(self):
    #     x1 = []
    #     for i in range(20):
    #         x1.append(self.first_machine.dequeue())
    #     return x1
                

    # def get_fullname_var_1(self):
    #         return self.name_var_1.get() + self.sur_var_1.get()
    
    # def get_amount_1(self):
    #       return self.amount_1.get()

# The class Popup_Tornado is a subclass of the class Popup_make_reservasion_info_main.

class Popup_Tornado(Popup_make_reservasion_info_main):
    def __init__(self, main_page_instance):
        super().__init__()
        
        self.pop.title("Tornado")

        self.name_var_2 = StringVar()
        self.sur_var_2 = StringVar()
        self.amount_2 = IntVar()

        self.main_page_instance = main_page_instance



        super().name()
        self.entry_1 = Entry(self.pop, textvariable= self.name_var_2, font=('calibre',10,'normal'))
        self.entry_1.grid(row=1,column=2)

        super().surname()
        self.entry_2 = Entry(self.pop, textvariable= self.sur_var_2, font=('calibre',10,'normal'))
        self.entry_2.grid(row=2,column=2)
        
        super().amount_of_people()
        self.spinbox_people_2 = ttk.Spinbox(self.pop, textvariable= self.amount_2, from_ = 1, to = 20, width = 5, wrap =True)
        self.spinbox_people_2.grid(row=3,column=2,padx=6, sticky=W)

        super().description()
        self.btn_2 = Button(self.pop, text = "Confirm", font= ("Arial", 10, 'italic'), width = 17, command=self.add_queue_2)
        self.btn_2.grid(row=4, column = 2, padx=5, pady=5)

     
    
    @staticmethod
    def get_data_2(self):
        full_name = self.name_var_2.get() +' '+ self.sur_var_2.get()
        tup = (full_name, self.amount_2)
        return tup
    

    def add_queue_2(self):
        self.main_page_instance.second_machine.enqueue(self.get_data_2)
        self.main_page_instance.set_laa2_text(self.main_page_instance.second_machine.get_size_element())
        self.pop.destroy()

    def set_name_label(self, label):
        self.name_label = label

    def set_surname_label(self, label):
        self.surname_label = label

    def set_amount_label(self, label):
        self.amount_label = label

    def get_name_var(self):
        return self.name_var.get()

    def get_surname_var(self):
        return self.surname_var.get()

    def get_amount_var(self):
        return self.amount_var.get()

    def update_name_label(self):
        if self.name_label:
            self.name_label.config(text=f"Name: {self.get_name_var()}")

    def update_surname_label(self):
        if self.surname_label:
            self.surname_label.config(text=f"Surname: {self.get_surname_var()}")

    def update_amount_label(self):
        if self.amount_label:
            self.amount_label.config(text=f"Amount of people: {self.get_amount_var()}")


    # def delete_queue_2(self):
    #     x2 = []
    #     for i in range(20):
    #         x2.append(self.second_machine.dequeue())
    #     return x2
                

    # def get_fullname_var_2(self):
    #         return self.name_var_2.get() + self.sur_var_2.get()
    
    # def get_amount_2(self):
    #       return self.amount_2.get()


# The class `Popup_Thunder_Bird` is a subclass of `Popup_make_reservasion_info_main` and likely
# contains additional functionality related to making a reservation.

class Popup_Thunder_Bird(Popup_make_reservasion_info_main):
    def __init__(self, main_page_instance):
        super().__init__()

        self.pop.title("Thunder Bird")

        self.name_var_3 = StringVar()
        self.sur_var_3 = StringVar()
        self.amount_3 = IntVar()

        self.main_page_instance = main_page_instance


        super().name()
        self.entry_1 = Entry(self.pop, textvariable= self.name_var_3, font=('calibre',10,'normal'))
        self.entry_1.grid(row=1,column=2)

        super().surname()
        self.entry_2 = Entry(self.pop, textvariable= self.sur_var_3, font=('calibre',10,'normal'))
        self.entry_2.grid(row=2,column=2)
        
        super().amount_of_people()
        self.spinbox_people_3 = ttk.Spinbox(self.pop, textvariable= self.amount_3, from_ = 1, to = 8, width = 5, wrap =True)
        self.spinbox_people_3.grid(row=3,column=2,padx=6, sticky=W)

        super().description()
        self.btn_3 = Button(self.pop, text = "Confirm", font= ("Arial", 10, 'italic'), width = 17, command=self.add_queue_3)
        self.btn_3.grid(row=4, column = 2, padx=5, pady=5)

    @staticmethod
    def get_data_3(self):
        full_name = self.name_var_3.get() +' '+ self.sur_var_3.get()
        tup = (full_name, self.amount_3)
        return tup

    def add_queue_3(self):
        self.main_page_instance.third_machine.enqueue(self.get_data_3)
        self.main_page_instance.set_laa3_text(self.main_page_instance.third_machine.get_size_element())
        self.pop.destroy()

    def set_name_label(self, label):
        self.name_label = label

    def set_surname_label(self, label):
        self.surname_label = label

    def set_amount_label(self, label):
        self.amount_label = label

    def get_name_var(self):
        return self.name_var.get()

    def get_surname_var(self):
        return self.surname_var.get()

    def get_amount_var(self):
        return self.amount_var.get()

    def update_name_label(self):
        if self.name_label:
            self.name_label.config(text=f"Name: {self.get_name_var()}")

    def update_surname_label(self):
        if self.surname_label:
            self.surname_label.config(text=f"Surname: {self.get_surname_var()}")

    def update_amount_label(self):
        if self.amount_label:
            self.amount_label.config(text=f"Amount of people: {self.get_amount_var()}")

    # def delete_queue_3(self):
    #     x3 = []
    #     for i in range(8):
    #         x3.append(self.third_machine.dequeue())
    #     return x3
                

    # def get_fullname_var_3(self):
    #         return self.name_var_3.get() + self.sur_var_3.get()
    
    # def get_amount_3(self):
    #       return self.amount_3.get()


# The class `Popup_Super_Splash` is a subclass of `Popup_make_reservasion_info_main` and is used for
# creating a popup window for making reservations.

class Popup_Super_Splash(Popup_make_reservasion_info_main):
    def __init__(self, main_page_instance):
        super().__init__()
       

        self.pop.title("Super Splash")

        
        self.name_var_4 = StringVar()
        self.sur_var_4 = StringVar()
        self.amount_4 = IntVar()

        self.main_page_instance = main_page_instance

        super().name()
        self.entry_1 = Entry(self.pop, textvariable= self.name_var_4, font=('calibre',10,'normal'))
        self.entry_1.grid(row=1,column=2)

        super().surname()
        self.entry_2 = Entry(self.pop, textvariable= self.sur_var_4, font=('calibre',10,'normal'))
        self.entry_2.grid(row=2,column=2)
        
        super().amount_of_people()
        self.spinbox_people_4 = ttk.Spinbox(self.pop, textvariable= self.amount_4, from_ = 1, to = 12, width = 5, wrap =True)
        self.spinbox_people_4.grid(row=3,column=2,padx=6, sticky=W)

        super().description()
        self.btn_4 = Button(self.pop, text = "Confirm", font= ("Arial", 10, 'italic'), width = 17, command=self.add_queue_4)
        self.btn_4.grid(row=4, column = 2, padx=5, pady=5)

        

    
    @staticmethod
    def get_data_4(self):
        full_name = self.name_var_4.get() +' '+ self.sur_var_4.get()
        tup = (full_name, self.amount_4)
        return tup
    
    def add_queue_4(self):
        self.main_page_instance.fouth_machine.enqueue(self.get_data_4)
        self.main_page_instance.set_laa4_text(self.main_page_instance.fouth_machine.get_size_element())
        self.pop.destroy()

    def set_name_label(self, label):
        self.name_label = label

    def set_surname_label(self, label):
        self.surname_label = label

    def set_amount_label(self, label):
        self.amount_label = label

    def get_name_var(self):
        return self.name_var.get()

    def get_surname_var(self):
        return self.surname_var.get()

    def get_amount_var(self):
        return self.amount_var.get()

    def update_name_label(self):
        if self.name_label:
            self.name_label.config(text=f"Name: {self.get_name_var()}")

    def update_surname_label(self):
        if self.surname_label:
            self.surname_label.config(text=f"Surname: {self.get_surname_var()}")

    def update_amount_label(self):
        if self.amount_label:
            self.amount_label.config(text=f"Amount of people: {self.get_amount_var()}")

    # def delete_queue_4(self):
    #     x4 = []
    #     for i in range(12):
    #         x4.append(self.fouth_machine.dequeue())
    #     return x4
                

    # def get_fullname_var_4(self):
    #         return self.name_var_4.get() + self.sur_var_4.get()
    
    # def get_amount_4(self):
    #       return self.amount_4.get()

########################################################################
# The CircularQueue class is a data structure that implements a circular queue.

class CircularQueue():
    # constructor
    def __init__(self, size):  # initializing the class
        self.size = size

        # initializing queue with none
        self.queue = [None for i in range(size)]
        self.front = self.rear = -1

    def enqueue(self, data):

        # condition if queue is full
        if ((self.rear + 1) % self.size == self.front):
            print(" Queue is Full\n")

        # condition for empty queue
        elif (self.front == -1):
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = data

        else:

            # next position of rear
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = data

    def dequeue(self):
        if (self.front == -1):  # condition for empty queue
            print("Queue is Empty\n")

        # condition for only one element
        elif (self.front == self.rear):
            temp = self.queue[self.front]
            self.front = -1
            self.rear = -1
            return temp
        else:
            temp = self.queue[self.front]
            self.front = (self.front + 1) % self.size
            return temp

    def display(self):

        # condition for empty queue
        if (self.front == -1):
            print("Queue is Empty")

        elif (self.rear >= self.front):
            print("Elements in the circular queue are:", end=" ")
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")
            print()

        else:
            print("Elements in Circular Queue are:", end=" ")
            for i in range(self.front, self.size):
                print(self.queue[i], end=" ")
            for i in range(0, self.rear + 1):
                print(self.queue[i], end=" ")
            print()

        if ((self.rear + 1) % self.size == self.front):
            print("Queue is Full")

    def get_size_element(self):
        if self.front == -1:
            return 0
        elif self.rear >= self.front:
            return self.rear - self.front + 1
        else:
            return self.size - (self.front - self.rear - 1)
    
    
    
    

# class Queue(CircularQueue):
#     def __init__(self, size, add, time, move):
#         super().__init__(self, size)
#         self.add = add
#         self.time = time
#         self.move = move

#     def add_queue_automatically(self):
#         for i in range(self.time):
#             self.enqueue(self.add)

#     def remove_queue_automatically(self):
#         self.dequeue(self.move)

#     def show_queue(self):
#          self.display()


# first_machine = CircularQueue(20)
# second_machine = CircularQueue(20)
# third_machine = CircularQueue(8)
# fouth_machine = CircularQueue(12)

window = Tk()
first = first_page_login(window)




window.mainloop()