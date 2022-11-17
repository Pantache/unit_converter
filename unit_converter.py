from tkinter import *
from tkinter.font import BOLD
import number_entry as nent
from tkinter.ttk import Notebook
  


def main():
    
    window = Tk()
    window.geometry('300x200-500+200')  #(Width x Height - X + Y)

    window.title("Welcome")
    window.configure( bg="#CAB8FF")

    label = Label(window, text="Welcome to the Unit Converter", bg="#CAB8FF", font=("Helvetica", 14, BOLD))
        
    def create():
        """Create a new window where will be the unit calculator"""
        win_convert = Toplevel(window)
        win_convert.title("Unit Converter")
        win_convert.geometry("350x220-470+200")

        #Calls to the window different frames, Option buttons, buttons,labels and entrys.
        frames(win_convert)

    btn = Button(window, text="START", command = create, padx=10, pady=10, font=("",10),bd=3, bg="#66DE93", cursor="hand2")
    me = Label(window, text="CSE 111. 2022. Ruth Cardona", bg="#CAB8FF", font=("Arial",8, BOLD))
    window.grid()
    label.grid(row=2, column=3, padx=10, pady=30)
    btn.grid(row=4, column=3, pady=20)
    me.grid(row=5, column=3)

    window.mainloop()

   
def frames(win_convert):
        
        #Creates Notebook and adds Temperature, Length and Mass Frames
        my_notebook = Notebook(win_convert, width=350, height=200)

        temp_frm = Frame(my_notebook, bg="#FFAD87", width=200, height=150)
        length_frm = Frame(my_notebook, bg="#86C6F4", width=200, height=150)
        mass_frm = Frame(my_notebook, bg="#A0D995", width=200, height=150)

        my_notebook.add(temp_frm, text="Temperature")
        my_notebook.add(length_frm, text="Length")
        my_notebook.add(mass_frm, text="Mass")

        #Temperature Frame
        temp_list = ["C°", "F°", "K°"]
        temp_unit = StringVar()
        temp_unit.set('C°')
        temp_unit2 = StringVar()
        temp_unit2.set('F°')

        unit_menu = OptionMenu(temp_frm, temp_unit, *temp_list )
        unit_menu2 = OptionMenu(temp_frm, temp_unit2, *temp_list )
     
        ent_temp = nent.FloatEntry(temp_frm,-999999999999999, 99999999999999999, width=15,relief=("raise"))
        lbl = Label(temp_frm, width=19, relief=("flat"))
        lbl_err = Label(temp_frm, bg="#FFAD87", font=("Helvetica", 12))
        btn_clear = Button(temp_frm, text="Clear",padx=3 ,pady=3, cursor="hand2")
        
        
        # #Length Frame
        length_list = ["Kilometer", "Meter", "Centimeter", "Milimeter", "Mile", "Yard", "Foot", "Inch", "Nautical Mile"]
        length_unit = StringVar()
        length_unit.set('Kilometer')
        length_unit2 = StringVar()
        length_unit2.set('Mile')

        unit_menu3 = OptionMenu(length_frm, length_unit, *length_list )
        unit_menu4 = OptionMenu(length_frm, length_unit2, *length_list )
      
        ent_length = nent.FloatEntry(length_frm,-999999999999999, 99999999999999999, width=15, relief=("raise"))
        lbl_2 = Label(length_frm, width=19, relief=("flat"))
        lbl_err2 = Label(length_frm, bg="#86C6F4", font=("Helvetica", 12))
        btn_clear2 = Button(length_frm, text="Clear",padx=3 ,pady=3,cursor="hand2")

         # #Mass Frame
        mass_list = ["Ton","Kilogram", "Gram", "Miligram", "Pound", "Ounce"]
        mass_unit = StringVar()
        mass_unit.set('Kilogram')
        mass_unit2 = StringVar()
        mass_unit2.set('Pound')

        unit_menu5 = OptionMenu(mass_frm, mass_unit, *mass_list )
        unit_menu6 = OptionMenu(mass_frm, mass_unit2, *mass_list )

        ent_mass = nent.FloatEntry(mass_frm,-999999999999999, 99999999999999999, width=15,relief=("raise"))
        lbl_3 = Label(mass_frm, width=19, relief=("flat"))
        lbl_err3 = Label(mass_frm, bg="#A0D995", font=("Helvetica", 12))
        btn_clear3 = Button(mass_frm, text="Clear",padx=3 ,pady=3,cursor="hand2")
        
        #Grid for Each Frame
        my_notebook.grid()
        unit_menu.grid(row=2, column=2, columnspan=2, pady=10)
        unit_menu2.grid(row=2, column=6, columnspan=4, pady=10)
        ent_temp.grid(row=3, column=3,padx=30, pady=3)
        lbl.grid(row=3, column=5, columnspan=6, rowspan=2, pady=3)
        lbl_err.grid(row=5, column=1, columnspan=3)
        btn_clear.grid(row=6, column=4, pady=20)

        unit_menu3.grid(row=2, column=2, columnspan=2, pady=10)
        unit_menu4.grid(row=2, column=6, columnspan=4, pady=10)
        ent_length.grid(row=3, column=3,padx=30, pady=3)
        lbl_2.grid(row=3, column=5, columnspan=6, rowspan=2, pady=3)
        lbl_err2.grid(row=5, column=1, columnspan=3)
        btn_clear2.grid(row=6, column=4, pady=20)

        unit_menu5.grid(row=2, column=2, columnspan=2, pady=10)
        unit_menu6.grid(row=2, column=6, columnspan=4, pady=10)
        ent_mass.grid(row=3, column=3,padx=30, pady=3)
        lbl_3.grid(row=3, column=5, columnspan=6, rowspan=2, pady=3)
        lbl_err3.grid(row=5, column=1, columnspan=3)
        btn_clear3.grid(row=6, column=4, pady=20)
       
       
        def calculate_temp(event):
            """Receives user entry and units to start conversion and 
                displays the result"""
            try: 
                number = float(ent_temp.get())
                unit = temp_unit.get()
                unit2 = temp_unit2.get()

                result = temp_conversion(number,unit, unit2)
                lbl.config(text=f"{result} {unit2}")
                lbl_err.config(text="")
            except ValueError :
                lbl.config(text="")
                lbl_err.config(text="Introduce a number")

        def calculate_length(event):
            """Receives user entry and units to start conversion and 
                displays the result"""
            try: 
                number = float(ent_length.get())
                unit = length_unit.get()
                unit2 = length_unit2.get()

                result = length_conversion(number,unit, unit2)
                lbl_2.config(text=f"{result}")
                lbl_err2.config(text="")
            except ValueError :
                lbl_2.config(text="")
                lbl_err2.config(text="Introduce a number")

        def calculate_mass(event):
            """Receives user entry and units to start conversion and 
                displays the result"""
            try: 
                number = float(ent_mass.get())
                unit = mass_unit.get()
                unit2 = mass_unit2.get()

                result = mass_conversion(number,unit, unit2)
                lbl_3.config(text=f"{result}")
                lbl_err3.config(text="")
            except ValueError :
                lbl_3.config(text="")
                lbl_err3.config(text="Introduce a number")              

        #Clean button function for each Frame        
        def clear():
            """Clear all the inputs and outputs."""
            ent_temp.delete(0, END)
            ent_length.delete(0,END)
            ent_mass.delete(0,END)
            lbl.config(text="")   
            lbl_2.config(text="")    
            lbl_3.config(text="")  
            lbl_err.config(text="")  
            lbl_err2.config(text="") 
            lbl_err3.config(text="")
            ent_temp.focus()    
            ent_length.focus()
            ent_mass.focus()

        #Called the button Clear when usser press it
        btn_clear.config(command=clear)
        btn_clear2.config(command=clear)
        btn_clear3.config(command=clear)

        ent_temp.bind("<KeyRelease>", calculate_temp)    
        ent_length.bind("<KeyRelease>", calculate_length) 
        ent_mass.bind("<KeyRelease>", calculate_mass) 
        ent_temp.focus()
        ent_length.focus()
        ent_mass.focus()
                

#Functions that makes the conversions.
def temp_conversion(user_number, unit, unit_converter):
    """Receives and converts a unit between Celcius, Fahrenheit or Kelvin. 
    Receives a unit and a number from the user and it converts one into 
    another unit selected by the user.
    For example, if the user enter 12°C to convert to F° it will return 53.6F°

    Parameters: 
        unit: A first unit enter as a capitalized string by the user.
        unit_converter: A second unit enter as a capitalized string by the user to convert the user_number. 
        user_number: a number introduce by the user.
    Return: A number converted to the second unit selected by the user.
    """
    try:
        if unit == "C°":
            if unit_converter == "F°":
                conversion = (user_number * (9 / 5)) + 32
            elif unit_converter == "K°":
                conversion = (user_number + 273.15)
            elif unit_converter == "C°":
                conversion = user_number    
            else:
                conversion = "Value Incorrect or not found"
        elif unit == "F°":
            if unit_converter == "C°":
                conversion = (user_number - 32) * 5/9
            elif unit_converter == "K°":
                conversion = (user_number - 32) * 5/9 + 273.15
            elif unit_converter == "F°":
                    conversion = user_number    
            else:
                conversion = "Value Incorrect or not found"
          
        elif unit == "K°":
            if unit_converter == "C°":
                conversion = (user_number - 273.15)
            elif unit_converter == "F°":
                conversion = (user_number - 273.15) * 9/5 + 32
            elif unit_converter == "K°":
                    conversion = user_number    
            else:
                conversion = "Value Incorrect or not found"
        else:
            conversion = "Value Incorrect or not found"

        return conversion

    except TypeError:
        conversion = "Value Incorrect or not found"
        return conversion

def length_conversion(user_number, unit, unit_converter):
    """Receives and converts a unit between Lenght units. 
    Receives a unit and a number from the user and it converts one into 
    another unit selected by the user.
    For example, if the user enter 1 Kilometer to convert to Miles it will return 0.621371 Miles.

    Parameters: 
        unit: A first unit enter as a capitalized string by the user.
        unit_converter: A second unit enter as a capitalized string by the user to convert the user_number. 
        user_number: a number introduce by the user.
    Return: A number converted to the second unit selected by the user.
    """
    try:
        if unit == "Kilometer":
            if unit_converter == "Meter":
                conversion = user_number * 1000
            elif unit_converter == "Centimeter":
                conversion = user_number * 100000
            elif unit_converter == "Milimeter":
                conversion = user_number * 1000000
            elif unit_converter == "Mile":
                conversion = user_number / 1609
            elif unit_converter == "Yard":
                conversion = user_number * 1093.61
            elif unit_converter == "Foot":
                conversion = user_number * 3280.84
            elif unit_converter == "Inch":
                conversion = user_number * 39370.1
            elif unit_converter == "Nautical Mile":
                conversion = user_number / 1.852     
            elif unit_converter == "Kilometer":
                    conversion = user_number    
            else:
                conversion = "Value Incorrect or not found"

        elif unit == "Meter":
            if unit_converter == "Kilometer":
                conversion = user_number / 1000
            elif unit_converter == "Centimeter":
                conversion = user_number * 100
            elif unit_converter == "Milimeter":
                conversion = user_number * 1000
            elif unit_converter == "Mile":
                conversion = user_number / 1609
            elif unit_converter == "Yard":
                conversion = user_number * 1.09361
            elif unit_converter == "Foot":
                conversion = user_number * 3.28084
            elif unit_converter == "Inch":
                conversion = user_number * 39.3701
            elif unit_converter == "Nautical Mile":
                conversion = user_number / 1852  
            elif unit_converter == "Meter":
                    conversion = user_number    
            else:
                conversion = "Value Incorrect or not found"

        elif unit == "Centimeter":
            if unit_converter == "Kilometer":
                conversion = user_number / 100000
            elif unit_converter == "Meter":
                conversion = user_number / 100
            elif unit_converter == "Milimeter":
                conversion = user_number * 10
            elif unit_converter == "Mile":
                conversion = user_number / 160934
            elif unit_converter == "Yard":
                conversion = user_number / 91.44
            elif unit_converter == "Foot":
                conversion = user_number / 30.48
            elif unit_converter == "Inch":
                conversion = user_number /2.54
            elif unit_converter == "Nautical Mile":
                conversion = user_number / 185200
            elif unit_converter == "Centimeter":
                    conversion = user_number    
            else:
                conversion = "Value Incorrect or not found"

        elif unit == "Milimeter":
            if unit_converter == "Kilometer":
                conversion = user_number / 1000000
            elif unit_converter == "Meter":
                conversion = user_number / 1000
            elif unit_converter == "Centimeter":
                conversion = user_number  / 10
            elif unit_converter == "Mile":
                conversion = user_number / 1609344
            elif unit_converter == "Yard":
                conversion = user_number / 914.4
            elif unit_converter == "Foot":
                conversion = user_number / 304.8
            elif unit_converter == "Inch":
                conversion = user_number / 25.4
            elif unit_converter == "Nautical Mile":
                conversion = user_number / 1852000
            elif unit_converter == "Milimeter":
                    conversion = user_number    
            else:
                conversion = "Value Incorrect or not found"
            
        elif unit == "Mile":
            if unit_converter == "Meter":
                conversion = user_number * 1609.34
            elif unit_converter == "Centimeter":
                conversion = user_number * 160934
            elif unit_converter == "Milimeter":
                conversion = user_number * 1609344
            elif unit_converter == "Kilometer":
                conversion = user_number / 1.60934
            elif unit_converter == "Yard":
                conversion = user_number * 1760
            elif unit_converter == "Foot":
                conversion = user_number * 5280
            elif unit_converter == "Inch":
                conversion = user_number * 63360
            elif unit_converter == "Nautical Mile":
                conversion = user_number / 1.15078
            elif unit_converter == "Mile":
                    conversion = user_number    
            else:
                conversion = "Value Incorrect or not found"

        elif unit == "Yard":
            if unit_converter == "Meter":
                conversion = user_number / 1.094
            elif unit_converter == "Centimeter":
                conversion = user_number * 91.44
            elif unit_converter == "Milimeter":
                conversion = user_number * 914.4
            elif unit_converter == "Kilometer":
                conversion = user_number / 1094
            elif unit_converter == "Mile":
                conversion = user_number / 1760
            elif unit_converter == "Foot":
                conversion = user_number * 3
            elif unit_converter == "Inch":
                conversion = user_number * 36
            elif unit_converter == "Nautical Mile":
                conversion = user_number / 2025.37
            elif unit_converter == "Yard":
                    conversion = user_number    
            else:
                conversion = "Value Incorrect or not found"

        elif unit == "Foot":
            if unit_converter == "Meter":
                conversion = user_number / 3.28084
            elif unit_converter == "Centimeter":
                conversion = user_number * 30.48
            elif unit_converter == "Milimeter":
                conversion = user_number * 304.8
            elif unit_converter == "Kilometer":
                conversion = user_number / 3280.84
            elif unit_converter == "Mile":
                conversion = user_number / 5280
            elif unit_converter == "Yard":
                conversion = user_number / 3
            elif unit_converter == "Inch":
                conversion = user_number * 12
            elif unit_converter == "Nautical Mile":
                conversion = user_number / 6076.12
            elif unit_converter == "Foot":
                    conversion = user_number    
            else:
                conversion = "Value Incorrect or not found"

        elif unit == "Inch":
            if unit_converter == "Meter":
                conversion = user_number / 39.3701
            elif unit_converter == "Centimeter":
                conversion = user_number * 2.54
            elif unit_converter == "Milimeter":
                conversion = user_number * 25.4
            elif unit_converter == "Kilometer":
                conversion = user_number / 39370.1
            elif unit_converter == "Mile":
                conversion = user_number / 63360
            elif unit_converter == "Yard":
                conversion = user_number / 36
            elif unit_converter == "Foot":
                conversion = user_number / 12
            elif unit_converter == "Nautical Mile":
                conversion = user_number / 72913.4
            elif unit_converter == "Inch":
                    conversion = user_number    
            else:
                conversion = "Value Incorrect or not found"

        elif unit == "Nautical Mile":
            if unit_converter == "Meter":
                conversion = user_number * 1852
            elif unit_converter == "Centimeter":
                conversion = user_number * 185200
            elif unit_converter == "Milimeter":
                conversion = user_number * 1852000
            elif unit_converter == "Kilometer":
                conversion = user_number * 1.852
            elif unit_converter == "Mile":
                conversion = user_number * 1.15078
            elif unit_converter == "Yard":
                conversion = user_number * 2025.37
            elif unit_converter == "Inch":
                conversion = user_number * 72913.4
            elif unit_converter == "Foot":
                conversion = user_number * 6076.12
            elif unit_converter == "Nautical Mile":
                    conversion = user_number    
            else:
                conversion = "Value Incorrect or not found"
        else:
            conversion = "Value Incorrect or not found"        
        return conversion
    except TypeError:
        conversion = "Value Incorrect or not found"
        return conversion
    
def mass_conversion(user_number, unit, unit_converter):
    """Receives and converts a unit between Mass units. 
    Receives a unit and a number from the user and it converts one into 
    another unit selected by the user.
    For example, if the user enter 1 Kilogram to convert to Pounds it will return 2.20462 Pounds.

    Parameters: 
        unit: A first unit enter as a capitalized string by the user.
        unit_converter: A second unit enter as a capitalized string by the user to convert the user_number. 
        user_number: a number introduce by the user.
    Return: A number converted to the second unit selected by the user.
    """
    try:
        if unit == "Ton":
            if unit_converter == "Kilogram":
                conversion = user_number * 1000
            elif unit_converter == "Gram":
                conversion = user_number * 1000000
            elif unit_converter == "Miligram":
                conversion = user_number * 1000000000
            elif unit_converter == "Pound":
                conversion = user_number * 2204.62
            elif unit_converter == "Ounce":
                conversion = user_number * 35274
            elif unit_converter == "Ton":
                    conversion = user_number    
            else:
                conversion = "Value Incorrect or not found"

        elif unit == "Kilogram":
            if unit_converter == "Ton":
                conversion = user_number / 1000
            elif unit_converter == "Gram":
                conversion = user_number * 1000
            elif unit_converter == "Miligram":
                conversion = user_number * 100000
            elif unit_converter == "Pound":
                conversion = user_number * 2.20462
            elif unit_converter == "Ounce":
                conversion = user_number * 35.274
            elif unit_converter == "Kilogram":
                    conversion = user_number    
            else:
                conversion = "Value Incorrect or not found"

        elif unit == "Gram":
            if unit_converter == "Kilogram":
                conversion = user_number / 1000
            elif unit_converter == "Ton":
                conversion = user_number / 1000000
            elif unit_converter == "Miligram":
                conversion = user_number * 1000
            elif unit_converter == "Pound":
                conversion = user_number / 453.592
            elif unit_converter == "Ounce":
                conversion = user_number / 28.3495
            elif unit_converter == "Gram":
                    conversion = user_number    
            else:
                conversion = "Value Incorrect or not found"

        elif unit == "Miligram":
            if unit_converter == "Kilogram":
                conversion = user_number / 1000000
            elif unit_converter == "Gram":
                conversion = user_number / 1000
            elif unit_converter == "Ton":
                conversion = user_number / 1000000000
            elif unit_converter == "Pound":
                conversion = user_number / 453592
            elif unit_converter == "Ounce":
                conversion = user_number / 28349.5
            elif unit_converter == "Miligram":
                    conversion = user_number    
            else:
                conversion = "Value Incorrect or not found"

        elif unit == "Pound":
            if unit_converter == "Kilogram":
                conversion = user_number / 2.20462
            elif unit_converter == "Gram":
                conversion = user_number * 453.592
            elif unit_converter == "Miligram":
                conversion = user_number * 453592
            elif unit_converter == "Ton":
                conversion = user_number / 2204.62
            elif unit_converter == "Ounce":
                conversion = user_number * 16
            elif unit_converter == "Pound":
                    conversion = user_number    
            else:
                conversion = "Value Incorrect or not found"

        elif unit == "Ounce":
            if unit_converter == "Kilogram":
                conversion = user_number * 35.274
            elif unit_converter == "Gram":
                conversion = user_number * 28.3495
            elif unit_converter == "Miligram":
                conversion = user_number * 28349.5
            elif unit_converter == "Pound":
                conversion = user_number / 16
            elif unit_converter == "Ton":
                conversion = user_number / 35274
            elif unit_converter == "Ounce":
                    conversion = user_number    
            else:
                conversion = "Value Incorrect or not found"
        else:
            conversion = "Value Incorrect or not found"        
        return conversion
    except TypeError:
        conversion = "Value Incorrect or not found"
        return conversion


#Call the main function to run the program.
if __name__ == "__main__":
    main()