def verificare(cuvant):
    rezultat_coduri = []
    traseu = []
    stare_curenta = stare_init
    traseu.append(stare_curenta)
    rezultat_coduri.append(coduri[int(stare_curenta)])
    index = 0

    while index < len(cuvant):
        ok = 0
        transition = 0
        while transition < len(tranzitii):
            if tranzitii[transition][0] == stare_curenta and cuvant[index] == tranzitii[transition][2]:
                stare_curenta = tranzitii[transition][1]
                transition = len(tranzitii)
                rezultat_coduri.append(coduri[int(stare_curenta)])
                traseu.append(stare_curenta)
                ok = 1
            else:
                transition += 1
        if ok == 0:
            return 0

        index += 1
        
    if stare_curenta in stari_fin:
        return 1, rezultat_coduri, traseu
    return 0


if __name__ == "__main__":
    with open("input.txt") as f:
        line = f.readline().strip()
        nr_noduri, nr_tranzitii = line.split()
        nr_noduri = int(nr_noduri)
        nr_tranzitii = int(nr_tranzitii)
        tranzitii = []

        line = f.readline().strip()
        coduri = [cod for cod in line.split()]

        for i in range(nr_tranzitii):
            line = f.readline().strip()
            stare_init, stare_fin, lit = line.split()
            tranzitii.append((stare_init, stare_fin, lit))

        stare_init = f.readline().strip()
        stari_fin = f.readline().strip().split()
        nr_stari_fin = stari_fin[0]
        stari_fin = stari_fin[1:]
        nr_cuv = int(f.readline().strip())
        cuvinte = []

        for i in range(nr_cuv):
            cuvinte.append(f.readline().strip())

        for cuv in cuvinte:
            if verificare(cuv):
                rezultat = verificare(cuv)
                print("DA")
                print(" ".join(rezultat[1]))
                print("Traseu:", " ".join(rezultat[2]))
            else:
                print("NU")
