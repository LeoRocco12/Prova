# Prendere in ingresso da un file Proverbio.txt un proverbio, creare due file Proverbio pari e dispari che contengono
# le lettere del proverbio divise secondo il loro indice.

# Apro i file che utilizzo per l'ingresso e l'uscita.
File_Proverbio = open("Proverbio.txt", "r")
File_Proverbio_Pari = open("../Proverbio_Pari.txt", "w")
File_Proverbio_Dispari = open("../Proverbio_Dispari.txt", "w")

# Utilizzo la list-comprehension per inserire le singole lettere del proverbio in una lista str_proverbio.
Str_Proverbio = [value for value in File_Proverbio.readline()]

# Scorro la lista con i caratteri del proverbio e utilizzo il loro indice per dividerli tra pari e dispari.
for index, value in enumerate(Str_Proverbio):
    if Str_Proverbio.index(value) % 2 == 0:
        File_Proverbio_Pari.write(f"{index}: {value} \n")
    else:
        File_Proverbio_Dispari.write(f"{index}: {value} \n")

# Chiudo i tre file dopo avere completato tutte le operazioni.
File_Proverbio.close()
File_Proverbio_Pari.close()
File_Proverbio_Dispari.close()
