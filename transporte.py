print("É terrestre?")
resposta = input()

if resposta == "s":
    print("Cabe apenas uma pessoa?")
    resposta = input()
    if resposta == "s":
        print("É alto?")
        resposta = input()
        if resposta == "s":
            print("TRATOR")
        else:
            print("BICICLETA")
    else:
        print("Usa capacete?")
        resposta = input()
        if resposta == "s":
            print("MOTO")
        else:
            print("Usa trilho?")
            resposta = input()
            if resposta == "s":
                print("TREM")
            else:
                print("É alto?")
                resposta = input()
                if resposta == "s":
                    print("Usa carroceria?")
                    resposta = input()
                    if resposta == "s":
                        print("CAMINHÃO")
                    else:
                        print("ÔNIBUS")
                else:
                    print("CARRO")
else:
    print("É aéreo?")
    resposta = input()
    if resposta == "s":
        print("Precisa pular?")
        resposta = input()
        if resposta == "s":
            print("ASA DELTA")
        else:
            print("É devagar?")
            resposta = input()
            if resposta == "s":
                print("BALÃO")
            else:
                print("Possui asas fixas?")
                resposta = input()
                if resposta == "s":
                    print("AVIÃO")
                else:
                    print("HELICÓPTERO")
    else:
        print("É coberto de água?")
        resposta = input()
        if resposta == "s":
            print("SUBMARINO")
        else:
            print("Possui vela?")
            resposta = input()
            if resposta == "s":
                print("BARCO")
            else:
                print("É alto?")
                resposta = input()
                if resposta == "s":
                    print("NAVIO")
                else:
                    print("LANCHA")

