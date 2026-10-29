# ----------------------------------------------------------------------
# C1. Atzīmju kopsavilkums
# ----------------------------------------------------------------------

# Kodā izveido sarakstu ar septiņām atzīmēm. Izvadi to skaitu, summu, vidējo, augstāko un zemāko. Visu kodu raksti pats.
#
# Šis fails ir tukšs. Visu kodu raksti pats zem šīs rindas.
# ----------------------------------------------------------------------                                                                                                Sarakstu, kurā glabā atzīmes, nosauc ar vārdu atzimju_saraksts.

atzimju_saraksts = [7, 8, 9, 8, 7, 10, 9]
print("Vispar atzimes:", len(atzimju_saraksts))
print("Atzimes summa:", sum(atzimju_saraksts))
print("Atzimes videjais:", sum(atzimju_saraksts) / len(atzimju_saraksts))
print("Atzimes augstakais:", sorted(atzimju_saraksts)[-1])
print("Atzimes zemākais:", sorted(atzimju_saraksts)[0])
