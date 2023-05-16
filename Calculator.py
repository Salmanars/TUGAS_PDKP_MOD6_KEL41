import math

class Calculator:
    def __init__(self):
        self.numbers = [0] * 100
        self.index = 0

    def getNumbers(self):
        return self.numbers

    def setNumbers(self, number):
        self.numbers[self.index] = number
        self.index += 1

    def getIndex(self):
        return self.index

    def clear(self):
        self.index = 0
        for i in range(len(self.numbers)):
            self.numbers[i] = 0

class BasicCalculator(Calculator):
    def calculate(self):
        pilihan = 0
        while pilihan != 5:
            print("Jenis operasi perhitungan")
            print("1. Add")
            print("2. Substract")
            print("3. Multiply")
            print("4. Divide")
            print("5. Back")
            pilihan = input("Pilihlah operasi perhitungan (1-5): ")
            try:
                pilihan = int(pilihan)
            except ValueError:
                print("Inputan Anda bukan angka bulat. Silakan masukkan pilihan Anda kembali (1-5):")
                continue
            if pilihan == 1:
                self.add()
            elif pilihan == 2:
                self.subtract()
            elif pilihan == 3:
                self.multiply()
            elif pilihan == 4:
                self.divide()
            elif pilihan == 5:
                return
            else:
                print("Data Eror!!,Inputlah sesuai yang berada dilist :(")

    def getInput(self):
        while True:
            input_string = input("Masukkan bilangan (x untuk berhenti): ")
            if input_string.lower() == "x":
                break
            try:
                number = float(input_string)
                self.setNumbers(number)
            except ValueError:
                print("Inputan salah! masukan bilangan kembali")

    def add(self):
        self.getInput()
        numbers = self.getNumbers()
        result = numbers[0]
        print("Detail = " + str(numbers[0]), end="")
        for i in range(1, self.getIndex()):
            result += numbers[i]
            print(" + " + str(numbers[i]), end="")
        print("")
        print("Hasil = " + str(result))
        print("----------------------------------")
        self.clear()

    def subtract(self):
        self.getInput()
        numbers = self.getNumbers()
        result = numbers[0]
        print("Detail = " + str(numbers[0]), end="")
        for i in range(1, self.getIndex()):
            result -= numbers[i]
            print(" - " + str(numbers[i]), end="")
        print("")
        print("Hasil = " + str(result))
        print("----------------------------------")
        self.clear()
        
    def multiply(self):
        self.getInput()
        numbers = self.getNumbers()
        result = numbers[0]
        print("Detail = " + str(numbers[0]), end="")
        for i in range(1, self.getIndex()):
            result *= numbers[i]
            print(" * " + str(numbers[i]), end="")
        print("")
        print("Hasil = " + str(result))
        print("----------------------------------")
        self.clear()

    def divide(self):
        self.getInput()
        numbers = self.getNumbers()
        result = numbers[0]
        print("Detail = " + str(numbers[0]), end="")
        for i in range(1, self.getIndex()):
            if numbers[i] == 0:
                print(" / " + str(numbers[i]), end="")
                print("")
                print("Hasil = Infinity")
                self.clear()
                return
            result /= numbers[i]
            print(" / " + str(numbers[i]), end="")
        print("")
        print("Hasil = " + str(result))
        print("----------------------------------")
        self.clear()

class ScientificCalculator(Calculator):
    def calculate(self):
        pilihan = 0
        while pilihan != 4:
            print("Silakan pilih jenis operasi perhitungan")
            print("1. squareRoot")
            print("2. exponentiation")
            print("3. factorial")
            print("4. Back")
            pilihan = int(input("Masukkan pilihan Anda (1-4): "))
            
            if pilihan == 1:
                self.squareRoot()
            elif pilihan == 2:
                self.exponentiation()
            elif pilihan == 3:
                self.factorial()
            elif pilihan == 4:
                return
            else:
                print("Data Eror!!,Inputlah sesuai yang berada dilist :(")

    def squareRoot(self):
        print("Masukan bilangan (x untuk keluar):")
        while True:
            try:
                number = float(input())
                break
            except ValueError:
                print("Inputan salah!. Masukkan bilangan kembali: ")
        result = math.sqrt(number)
        print(f"Hasil √{number} = {result}")
        self.clear()

    def exponentiation(self):
        while True:
            try:
                baseNumber = float(input("Inputkan bilangan pokok: "))
                break
            except ValueError:
                print("Input harus berupa angka. Silakan inputkan pokok lagi.")
        while True:
            try:
                exponentNumber = float(input("Inputkan besarnya pangkat: "))
                break
            except ValueError:
                print("Input harus berupa angka. Silakan inputkan besarnya pangkat kembali.")
        result = math.pow(baseNumber, exponentNumber)
        print(f"Hasil {baseNumber}^{exponentNumber} = {result}")
        self.clear()

    def factorial(self):
        while True:
            try:
                number = float(input("Inputkan angka: "))
                break
            except ValueError:
                print("Inputan salah, masukan angka kembali: ")
        result = 1
        for i in range(1, int(number) + 1):
            result *= i
        print(f"Hasil {number}! = {result}")
        self.clear()

class CalculatorMainMenu:
    @staticmethod
    def main():
        while True:
            print("Tugas Kell41 Modul 6")
            print("----------------------------------")
            print("Silakan pilih jenis kalkulator")
            print("1. Basic Calculator")
            print("2. Scientific Calculator")
            print("3. Exit Program")
            pilih_jenis_kalkulator = input("Masukkan pilihan Anda (1-3): ")
            try:
                pilih_jenis_kalkulator = int(pilih_jenis_kalkulator)
            except ValueError:
                print("Inputan Anda bukan angka. Silakan masukkan pilihan Anda kembali (1-3):")
                continue

            if pilih_jenis_kalkulator == 1:
                basic_calculator = BasicCalculator()
                basic_calculator.calculate()
            elif pilih_jenis_kalkulator == 2:
                scientific_calc = ScientificCalculator()
                scientific_calc.calculate()
            elif pilih_jenis_kalkulator == 3:
                print("Semoga Harimu Menyenangkan.")
                break
            else:
                print("Pilihan salah! Silakan masukan pilihan kembali.")

CalculatorMainMenu.main()