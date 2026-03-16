import random
optiuni = ["Piatra", "Hartie", "Foarfeca"]
scor_player = 0
scor_pc = 0
x = "true"
ok = True
while x.lower() == "true":
    calculator = random.choice(optiuni)
    alegere_player = input("Care este alegerea ta?: ")
    if alegere_player.lower() not in ["piatra", "hartie", "foarfeca"]:
        ok_alegere_player = False
        while ok_alegere_player == False:
            alegere_player = input("Nu ai selectat una dintre optiuni! (Piatra / Foarfeca / Hartie): ")
            if alegere_player.lower() == "piatra" or alegere_player.lower() == "foarfeca" or alegere_player.lower() == "hartie":
                ok_alegere_player = True
    if alegere_player.lower() == "piatra" and calculator == "Hartie":
        scor_pc = scor_pc + 1
        print("Alegere PC: " + str(calculator))
        print("PC castigator")
        print("Scor player: " + str(scor_player) + " Scor PC: " + str(scor_pc))
    elif alegere_player.lower() == "hartie" and calculator == "Foarfeca":
        scor_pc = scor_pc + 1
        print("Alegere PC: " + str(calculator))
        print("PC castigator")
        print("Scor player: " + str(scor_player) + " Scor PC: " + str(scor_pc))
    elif alegere_player.lower() == "hartie" and calculator == "Piatra":
        scor_player = scor_player + 1
        print("Alegere PC: " + str(calculator))
        print("Player castigator")
        print("Scor player: " + str(scor_player) + " Scor PC: " + str(scor_pc))
    elif alegere_player.lower() == "foarfeca" and calculator == "Piatra":
        scor_pc = scor_pc + 1
        print("Alegere PC: " + str(calculator))
        print("PC castigator")
        print("Scor player: " + str(scor_player) + " Scor PC: " + str(scor_pc))
    elif alegere_player.lower() == "piatra" and calculator == "Foarfeca":
        scor_player = scor_player + 1
        print("Alegere PC: " + str(calculator))
        print("Player castigator")
        print("Scor player: " + str(scor_player) + " Scor PC: " + str(scor_pc))
    elif alegere_player.lower() == "foarfeca" and calculator == "Hartie":
        scor_player = scor_player + 1
        print("Alegere PC: " + str(calculator))
        print("Player castigator")
        print("Scor player: " + str(scor_player) + " Scor PC: " + str(scor_pc))
    else:
        print("Alegere PC: " + str(calculator))
        print("Egalitate")
        print("Scor player: " + str(scor_player) + " Scor PC: " + str(scor_pc))
    x = input("Doresti sa mai continue jocul? (True/False): ")
    if x.lower() != "true" and x.lower() != "false":
        ok = False
        while ok == False:
            x = input("Ai introdus o optiune invalida! (True/False): ")
            if x.lower() == "true" or x.lower() == "false":
                ok = True
                
            