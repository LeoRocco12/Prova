import string as st

while True:
    # Blocco d'inserimento della parola da cercare.
    try:
        word = input("Inserire la parola da cercare (Q per Terminare): ")
    except ValueError:
        print("Tipo di dato inserito Errato!")
    else:
        # Se la parola inserita è q il programma termina subito
        if word.lower() == "q":
            break
        else:
            # Altrimenti creo la che contiene una serie di liste una per ogni riga del file lipsum.txt e nello stesso
            # momento rimuovo tutti i segni di punteggiatura che interferiscono con il programma.
            File_Lipsum = open("Lipsum.txt", "r")
            Testo = [value.split(" ") for value in File_Lipsum]
            Lista_Frasi = [[word.strip(st.punctuation) for word in riga] for riga in Testo]
            File_Lipsum.close()

            # Dopo avere creato questa lista la scorro e cerco se trovo la parola inserita in ingresso.
            Trovata = False
            for righe in Lista_Frasi:
                for value in righe:
                    # Se la parola inserita esiste allora stampo riga e indice della parola
                    if word == value:
                        print(f"POSIZIONE: Riga[{Lista_Frasi.index(righe)}], Colonna[{righe.index(value)}]")
                        Trovata = True

            # Se non ho trovato la parola lo stampo e ricomincia il ciclo
            if Trovata is False:
                print("La parola non è presente nel file!")
