import sys

def informatii(lines, lista, cuvant, end):
    index_cuvant = lines.index(cuvant)
    if cuvant == "Transitions:":
        for i in range(index_cuvant + 1, end):
            if "#" not in lines[i]:
                lista.append(tuple(lines[i].strip().strip("\t").split(", ")))
            else:
                lines[i] = lines[i].strip("\t")
                index_oprire = lines[i].index("#") - 1
                aux = lines[i][0:index_oprire]
                lista.append(tuple(aux.strip("\t").split(", ")))
    else:
        for i in range(index_cuvant + 1,end):
            if "#" not in lines[i]:
                lista.append(lines[i].strip().strip("\t"))
            else:
                lines[i] = lines[i].strip("\t")
                index_oprire = lines[i].index("#") - 1
                aux = lines[i][0:index_oprire]
                lista.append(aux.strip("\t"))

def validator(line, init_state, word, fin_state):
    if init_state not in States:
        return f"este invalidă!Greseală la linia {line}: nu există starea {init_state}."
    elif fin_state not in States:
        return f"este invalidă!Greseală la linia {line}: nu există starea {fin_state}."
    elif word not in Sigma:
        return f"este invalidă!Greseală la linia {line}: nu există cuvântul {word}."

    return "este validă!"

def end(lines, cuvant):
    index = lines.index(cuvant)
    for i in range(index, len(lines)):
        if lines[i] == "End":
            return i

# with open("input.txt") as f:
with open(sys.argv[1]) as f:
    lines = f.read().splitlines()
    index_Transitions = lines.index("Transitions:") + 2

    lines = [line for line in lines if line.startswith("#") == 0]

    j = len(lines)-1
    while lines[j] == "":
        del lines[j]
        j -= 1

    lines.append("End")

    # print(lines)

    Sigma = []
    States = []
    Transitions = []


    informatii(lines, Sigma, "Sigma:", end(lines, "Sigma:"))
    informatii(lines, States, "States:", end(lines, "States:"))
    informatii(lines, Transitions, "Transitions:", end(lines, "Transitions:"))

    # print(Sigma)
    # print(States)
    # print(Transitions)

    stare_init = []
    stari_finale = []

    for state in States:
        try:
            if state.split(", ")[1] == "S":
                stare_init.append(state.split(", ")[0])
                States[States.index(state)] = state.split(", ")[0]
            if state.split(", ")[1] == "F":
                stari_finale.append(state.split(", ")[0])
                States[States.index(state)] = state.split(", ")[0]
            if state.split(", ")[2] == "F":
                stari_finale.append(state.split(", ")[0])
                States[States.index(state)] = state.split(", ")[0]
            if state.split(", ")[2] == "S":
                stare_init.append(state.split(", ")[0])
                States[States.index(state)] = state.split(", ")[0]
        except:
            continue

    if len(stare_init) != 1:
        print("Invalid: sunt mai multe stări inițiale.")
    if len(stare_init) == 0:
        print("Invalid: nu există stare inițială.")

    if len(stari_finale) == 0:
        print("Invalid: nu există stare finală.")


    # for transition in Transitions:
    #     if len(transition) != 3:
    #         print(f"Tranziție invalidă {transition}: nu se poate procesa pentru ca nu sunt exact 3 argumente.")
    #     else:
    #         print(f"Tranziția {transition} {validator(index_Transitions, transition[0], transition[1], transition[2])}")
    #     index_Transitions += 1

# print(stare_init)
# print(stari_finale)
# print(f"Sigma: {Sigma}")
# print(f"States: {States}")
# print(f"Transitions: {Transitions}")


def verificare(cuvant):
    if len(stare_init) != 1:
        return "input invalid"
    stare_curenta = stare_init[0]
    index = 0
    while index < len(cuvant):
        ok = 0
        transition = 0
        while transition < len(Transitions):
            if Transitions[transition][0] == stare_curenta and cuvant[index] == Transitions[transition][1]:
                stare_curenta = Transitions[transition][2]
                transition = len(Transitions)
                ok = 1
            else:
                transition += 1
        if ok == 0:
            return "NU ESTE acceptat!"

        index += 1

    if stare_curenta in stari_finale:
        return "ESTE acceptat!"
    return "NU ESTE acceptat!"


print(f"Cuvantul {sys.argv[2]} {verificare(sys.argv[2])}")
# print(verificare("baa"))
