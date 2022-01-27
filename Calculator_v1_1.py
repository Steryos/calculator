def add(num1, num2):
    return num1 + num2

def substract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def calculate():
    try:
        num1 = int(input("Δώσε τον πρώτο(1o) αριθμό: "))
        num2 = int(input("Δώσε τον δεύτερο(2o) αριθμό: "))
        print("Δήλωσε: \n1. για πρόσθεση \n2. για αφαίρεση \n3. για πολλαπλασιασμό \n4. για διαίρεση")
    except:
        print("Λανθασμένη είσοδος.")
    operation=input("Δοκιμάστε μια από τις διαθέσιμες επιλογές πράξεων: ")
    if operation=="1":
        print(num1,"+", num2,"=", add(num1, num2))
    elif operation=="2":
        print(num1,"-",num2,"=", substract(num1, num2))
    elif operation=="3":
        print(num1,"*",num2,"=", multiply(num1, num2))
    elif operation=="4":
        print(num1,"/",num2,"=", divide(num1, num2))
    else:
        print("Λανθασμένη Δήλωση")
        again()

def again():
    calculate_again = input('Θέλετε να υπολογίσετε κάτι άλλο; \nΠληκτρολογήστε ΝΑΙ ή ΟΧΙ αντίστοιχα: ')
    if calculate_again=='Nai' or calculate_again=='nai' or calculate_again=="NAI":
        calculate()
    elif calculate_again=='Oxi' or calculate_again=='OXI' or calculate_again=='oxi':
        print('Καλή συνέχεια.')
        quit()
    else:
        again()

print('\nWelcome to my calculator')
print('*******************************')
calculate()
again()
