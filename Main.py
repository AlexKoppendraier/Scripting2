import easygui
import Functions as F
logo = 'PowerRent.png'

begin_opties =["Registreer","Inloggen","Stoppen","Admin"]
begin_keuze = easygui.buttonbox("Welkom bij de applicatie van PowerRent, maak uw keuze in het menu hier onder", F.pr, begin_opties,  image=logo)

if begin_keuze == 'Registreer':
    F.Scherm_Registreer()
elif begin_keuze == 'Inloggen':
    F.Scherm_Inloggen()
elif begin_keuze == 'Admin':
    F.Scherm_Inloggen_Admin()
elif begin_keuze == 'Stoppen':
    exit()

