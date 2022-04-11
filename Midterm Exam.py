# Program 1
def main():
    class TemperatureConversion:
        def __init__(self, temp=1):
            self._temp = temp

    class CelsiusToFahrenheit(TemperatureConversion):
        def conversion(self):
            return (self._temp * 9) / 5 + 32

    class CelsiusToKelvin(TemperatureConversion):
        def conversion(self):
            return self._temp + 273.15

    # The added two conversion
    class FahrenheittoCelsius(TemperatureConversion):
        def conversion(self):
            return ((self._temp - 32) * 5) / 9

    class KelvintoCelsius(TemperatureConversion):
        def conversion(self):
            return self._temp - 273.15

    # ------------------------------------------------------

    tempInCelsius = float(input("Enter the temperature in Celsius: "))

    convert = CelsiusToKelvin(tempInCelsius)
    print(str(convert.conversion()) + " Kelvin")
    convert = CelsiusToFahrenheit(tempInCelsius)
    print(str(convert.conversion()) + " Fahrenheit")

    # Added object

    tempInFahrenheit = float(input("Enter the temperature in Fahrenheit: "))
    convert = FahrenheittoCelsius(tempInFahrenheit)
    print(str(convert.conversion()) + " Celsius")

    tempInKelvin = float(input("Enter the temperature in Kelvin: "))
    convert = KelvintoCelsius(tempInKelvin)
    print(str(convert.conversion()) + " Celsius")


# ------------------------------------------------------


main()

# Program 2
from tkinter import *

class Fullname:
    def __init__(self, win):
        self.name = Label(win, text="Enter your fullname:", fg="Red")
        self.name.place(x=50, y=100)
        self.txtbox1 = Entry(font= ("calibri", 15), bd=5)
        self.txtbox1.place(x=300, y=100)
        self.btn1 = Button(win, text="Click to display your Fullname", fg="Red", command = self.display)
        self.btn1.place(x=50, y=150)
        self.txtbox2 = Entry(font= ("calibri", 15), bd=5)
        self.txtbox2.place(x=300, y=150)
    def display(self):
        self.txtbox2.delete(0, 'end')
        full = self.txtbox1.get()
        self.txtbox2.insert(END, str(full))

window = Tk()
prob2 = Fullname(window)
window.geometry("606x336+30+30")
window.title("Midterm in OOP")

window.mainloop()


