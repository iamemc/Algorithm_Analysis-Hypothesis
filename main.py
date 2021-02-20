import math

def option(text):
    while True:
        print("\n | Type:"+"\u0332".join(str(" 1"))+" to get T value knowing N - T(N).")
        print(" "+"| Type:"+"\u0332".join(str(" 2"))+" to get N value knowing T")
        choose_option = input(text)
        if choose_option in ("1","2","3"):
            if choose_option == "1":
                print("\n\n [Let's find N value]")
                return choose_option
            elif choose_option == "2":
                print("\n\n [Let's find T value]")
                return choose_option
            elif choose_option == "3":
                print("\n\n [Quitting the Program]")
                return choose_option
    else:
        print("Input must be '1', '2' or '3'.")

def validateAnswer(text):
    while True:
        user_input = input(text)
        try:
            user_input = float(user_input)
            return user_input
        except ValueError:
            print("\n Input must be a number")
            continue

def getTimeN(N, TN0, TN1, value_incurve):
    #encontrar T(N)
    #T(N) = a*N**b
    #----- example T(N)=10^(-10)*x^3
    b = math.log(TN1/TN0,2) #b = log(2º TEMPO N[1] / TEMPO N[0])
    a = TN0/(N**b) #a = T(N[0])/(N[0]^b)
    Tn = int(a*value_incurve**b) #T(N) = a*N^b
    return Tn

def getN(N, TN0, TN1, TX):
    b = math.log(TN1/TN0,2) #b = log(2º TEMPO N[1] / TEMPO N[0])
    a = TN0/(N**b) #a = T(N[0])/(N[0]^b)
    N = int((TX/a)**(1/b)) #N = (T(N)/a)^(1/b)
    return N

choose_option = option("[What would you like to do?] ")

while True:
    if choose_option == "1":
        N = validateAnswer("Enter N₀ value: ") #Example: 1000
        TN0 = validateAnswer("Enter T(N₀) value: ") #Example: 0.1
        TN1 = validateAnswer("Enter T(2.N₀) value: ") #Example: 0.8
        value_incurve = validateAnswer("Enter N value you wish to find correspondent Time: ") #Example: 16000
        result_tn = getTimeN(N, TN0, TN1, value_incurve)
        print(str(int(value_incurve)) +" equivale a "+ str(int(result_tn/60))+ " minutos")
    elif choose_option == "2":
        N = validateAnswer("Enter N₀ value: ") #Example: 1000
        TN0 = validateAnswer("Enter T(N₀) value: ") #Example: 0.1
        TN1 = validateAnswer("Enter T(2.N₀) value: ") #Example: 0.8
        TX = validateAnswer("Enter Time (T(N)), in seconds, to find correspondent Input (N): ") #Example: 1800
        result_n = getN(N, TN0, TN1, TX)
        print(str(int(value_incurve)) +" equivale a um input de "+ str(int(result_n)))
    elif choose_option == "3":
        break

# =============================================================================
# start = time.time() #start timer
# end = time.time()
# formatted_float = "{:.2f}".format(end - start)
# print("\n Code took "+formatted_float+" seconds to run.")
# =============================================================================

# =============================================================================
#exercicio 1
#log(2º TEMPO N[1] / TEMPO N[0])
# b = math.log(0.8/0.1,2)
# print(b)
# #T(N[0])/(N[0]^b)
# a = 0.1/(1000**b)
# print(a)
# Tn = int(a*16000**b)
# print(Tn)
# =============================================================================

# =============================================================================
#exercicio 1
#log(TEMPO N[1] / TEMPO N[0])
# b = math.log(20/5,2)
# #print(b)
# a = 5/(1000**b)
# #print(a)
# Tn = int(a*16000**b)
# print("16000 equivale a " + str(Tn/60) + " minutos")
# =============================================================================

#log(2º TEMPO N[1] / TEMPO N[0])
#encontrar N
#N = int((1.8*10**13)**(1/3))
#print(N)