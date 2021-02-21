###################### Indíce ####################### 
#---- Imports
#---- Funções
#     ---- Opções de Equações
#     ---- Validador de Input Númerico
#     ---- Obter Tempo de N = T(N)
#     ---- Obter N sabendo T
#---- Testes
#---- Calcular Equações 

#===============================================================
#========================= Imports =============================
#===============================================================
import math
import unittest

#===============================================================
#========================= Funções =============================
#===============================================================
#===================== Opções de Equações ======================
def option(text):
    while True:
        print("\n | Type:"+"\u0332".join(str(" 1"))+" to get T value knowing N - T(N).")
        print(" "+"| Type:"+"\u0332".join(str(" 2"))+" to get N value knowing T.")
        print(" "+"| Type:"+"\u0332".join(str(" 3"))+" to exit the program.")
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

#================= Validador de Input Númerico =================
def validateAnswer(text):
    while True:
        user_input = input(text)
        try:
            user_input = float(user_input)
        except ValueError:
            print("\n Input must be a number")
            continue
        if isinstance(user_input, float):
            return user_input
        else:
            print("\n Input must be a number")

#================= Obter Tempo de N = T(N) =====================
def getTimeN(N, TN0, TN1, value_incurve):
    #encontrar T(N)
    #T(N) = a*N**b
    #----- example T(N)=10^(-10)*x^3
    b = math.log(TN1/TN0,2) #b = log(2º TEMPO N[1] / TEMPO N[0])
    a = TN0/(N**b) #a = T(N[0])/(N[0]^b)
    Tn = a*value_incurve**b #T(N) = a*N^b)
    return Tn

#================= Obter N sabendo T =====================
def getN(N, TN0, TN1, TX):
    b = math.log(TN1/TN0,2) #b = log(2º TEMPO N[1] / TEMPO N[0])
    a = TN0/(N**b) #a = T(N[0])/(N[0]^b)
    N = (TX/a)**(1/b) #N = (T(N)/a)^(1/b)
    return N

#===============================================================
#========================= Testes ==============================
#===============================================================
#======================= Test Class  ===========================
class testFunctions(unittest.TestCase):

    def test_getTimeN_with_valid_parameters(self):
        self.assertEqual(getTimeN(1000, 0.1, 0.8, 16000), 409.6)

    def test_getN_with_valid_parameters(self):
        self.assertEqual(getN(1000, 0.1, 0.8, 1800), 26207.41394208895)

unittest.main(argv=['first-arg-is-ignored'], exit=False) #deve retornar ok!


#===============================================================
#==================== Calcular Equações ========================
#===============================================================
#========================= Inputs  =============================
while True:
    choose_option = option("[What would you like to do?] ")
    if choose_option == "1":
        N = validateAnswer("Enter N₀ value: ") #Example: 1000
        TN0 = validateAnswer("Enter T(N₀) value: ") #Example: 0.1
        TN1 = validateAnswer("Enter T(2.N₀) value: ") #Example: 0.8
        value_incurve = validateAnswer("Enter N value you wish to find correspondent Time: ") #Example: 16000
        result_tn = getTimeN(N, TN0, TN1, value_incurve)
        print(result_tn)
        print("\n"+str(value_incurve) +" equivale a "+ str(result_tn/60)+ " minutos")
    elif choose_option == "2":
        N = validateAnswer("Enter N₀ value: ") #Example: 1000
        TN0 = validateAnswer("Enter T(N₀) value: ") #Example: 0.1
        TN1 = validateAnswer("Enter T(2.N₀) value: ") #Example: 0.8
        TX = validateAnswer("Enter Time (T(N)), in seconds, to find correspondent Input (N): ") #Example: 1800
        result_n = getN(N, TN0, TN1, TX)
        print("\n Um tempo de "+str(TX)+" segundos ou "+str(TX/60)+\
              " minutos, equivale a um input de "+ str(int(result_n)))
    elif choose_option == "3":
        break
