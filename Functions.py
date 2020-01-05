import easygui
import os.path
import re
from shutil import copyfile
pr = "PowerRent"
logo = 'PowerRent.png'
#----------------------------------------------------------------------------------------------------------------------- De functies die ervoor zorgen dat er dingen gedaan kunnen worden met de tekst documenten
#dit leest Database.text
def ReadDatabase():
    ReadDatabase = open("Database.txt", "r")
    print(ReadDatabase.read())
    ReadDatabase.close()
#dit kan schrijven  in Database.txt
def WriteDatabase(S):
    WriteDatabase = open("Database.txt", "w")
    WriteDatabase.write(S)
    WriteDatabase.close()
#Dit zorgt ervoor dat er een structuur gemaakt kan worden in Database.txt
def AppenDatabase(S):
    AppenDatabase = open("Database.txt", "a")
    AppenDatabase.writelines(S)
    AppenDatabase.close()
#dit leest AdminDatabase.text
def ReadDatabase_admin():
    ReadDatabase = open("AdminDatabase.txt", "r")
    print(ReadDatabase.read())
    ReadDatabase.close()
#dit kan schrijven  in AdminDatabase.txt
def WriteDatabase_admin(S):
    WriteDatabase = open("AdminDatabase.txt", "w")
    WriteDatabase.write(S)
    WriteDatabase.close()
#Dit zorgt ervoor dat er een structuur gemaakt kan worden in AdminDatabase.txt
def AppenDatabase_admin(S):
    AppenDatabase = open("AdminDatabase.txt", "a")
    AppenDatabase.writelines(S)
    AppenDatabase.close()

def AppenDatabase_Product(S):
    AppenDatabase = open("ProductDatabase.txt", "a")
    AppenDatabase.writelines(S)
    AppenDatabase.close()
#-----------------------------------------------------------------------------------------------------------------------Het pop-up bericht
#dit zorgt voor een pop-up bericht met een zelf inschaalbaar bericht
def Waarschuwing(S):
    msg = S
    tittle = pr
    easygui.msgbox(msg,tittle)

#-----------------------------------------------------------------------------------------------------------------------Het kunnen inloggen en registeren
#dit is het registratie scherm
def Scherm_Registreer():
    msg = 'Enter your personal details'
    register_screen_fieldnames = ['Username *','Name *', 'last name *', 'Street','Number', 'City', 'State', 'ZipCode', 'Country','E-mail *','Password *']
    register_screen_fieldvalues = easygui.multpasswordbox(msg, title = pr, fields=register_screen_fieldnames)
    while 1:
        if register_screen_fieldvalues is None: break
        error_msg = ""
        for i in range(len(register_screen_fieldnames)):
            if register_screen_fieldvalues[i].strip() == "":
                error_msg += ('{} is a required field.\n\n'.format(register_screen_fieldnames[i]))
        if error_msg == "": break
        register_screen_fieldvalues = easygui.multenterbox(error_msg, tittle, register_screen_fieldnames, register_screen_fieldvalues)
        return register_screen_fieldvalues
    AppenDatabase('\n')
    for i in range(len(register_screen_fieldvalues)):
        fields_val = (str(register_screen_fieldvalues[i])+"$")
        AppenDatabase(fields_val)

#Dit is het inlog scherm
def Scherm_Inloggen():
    msg = 'Enter your username and password to log in'
    logon_screen_fieldnames = ['Username', 'Password']
    logon_screen_fieldvalues = easygui.multpasswordbox(msg, title = pr, fields=logon_screen_fieldnames)
    while 1:
        for line in open('Database.txt','r').readlines():
            login_info = line.split('$')
            if logon_screen_fieldvalues[0] == login_info[0] and logon_screen_fieldvalues[1] == login_info[10]:
                Scherm_Klanten()
                return True
        print("Incorrect credentials.")
        Waarschuwing('Incorrect credentias')
        Scherm_Inloggen()
        return False

#dit is het admin  inlog scherm
def Scherm_Inloggen_Admin():
    msg = 'Enter your username and password to log in'
    logon_screen_fieldnames = ['Username', 'Password']
    logon_screen_fieldvalues = easygui.multpasswordbox(msg, title = pr, fields=logon_screen_fieldnames)
    while 1:
        for line in open('AdminDatabase.txt','r').readlines():
            login_info = line.split('$')
            if logon_screen_fieldvalues[0] == login_info[0] and logon_screen_fieldvalues[1] == login_info[10]:
                Admin_Page()
                return True
        print("Incorrect credentials.")
        Waarschuwing('Incorrect credentias')
        Scherm_Inloggen_Admin()
        return False

#-----------------------------------------------------------------------------------------------------------------------De admin tools
#hiermee kan een er gebruikerinformatie worden opgeroepen
def get_user_data(get_user_data_input):
    get_user_data_output = []
    with open("Database.txt") as all_user_data:
        for regelnummer, user_data_line in enumerate(all_user_data):
            if re.search(r'\b({})\b'.format(get_user_data_input), user_data_line) == None:
                continue
            else:
                if re.search(r'\b({})\b'.format(get_user_data_input), user_data_line):
                    list_user_data_line_temp = user_data_line.rstrip()
                    list_user_data_line = list_user_data_line_temp.split("$")
                    get_user_data_output_temp = list_user_data_line[0], list_user_data_line[1], list_user_data_line[2], list_user_data_line[3],list_user_data_line[4], list_user_data_line[5], list_user_data_line[6],list_user_data_line[7], list_user_data_line[8], list_user_data_line[9],"Gebruikersgegevens:"
                    get_user_data_output = list(get_user_data_output_temp)
    return get_user_data_output
    all_user_data.close()

#hiermee  kan een gebruiker verwijderd worden
def delete_user(delete_user_username_input):
    delete_user_username_output = ["User not found."]
    copyfile("Database.txt", "Temp.txt")
    with open("Database.txt", 'w') as all_user_data:
        all_user_data.close()
    with open("Temp.txt", 'r') as temp_user_data_:
        for regelnummer, user_data_line in enumerate(temp_user_data_):
            if re.search(r'\b({})\b'.format(delete_user_username_input), user_data_line) == None:
                with open("Database.txt", 'a') as all_user_data:
                    all_user_data.write('{}'.format(user_data_line))
            elif re.search(r'\b({})\b'.format(delete_user_username_input), user_data_line):
                delete_user_username_output = user_data_line.split()
                delete_user_username_output += ["Gebruiker succesvol verwijderd."]

    return delete_user_username_output
    all_user_data.close()
    temp_user_data_.close()
#-----------------------------------------------------------------------------------------------------------------------Producten
#hiermee worden producten toegevoegd
def Product_Add():
    msg = 'Enter your personal details'
    register_screen_fieldnames = ['Product ID', 'Product naam', 'Voorraad']
    register_screen_fieldvalues = easygui.multenterbox(msg, title=pr, fields=register_screen_fieldnames)
    while 1:
        if register_screen_fieldvalues is None: break
        error_msg = ""
        for i in range(len(register_screen_fieldnames)):
            if register_screen_fieldvalues[i].strip() == "":
                error_msg += ('{} is a required field.\n\n'.format(register_screen_fieldnames[i]))
        if error_msg == "": break
        register_screen_fieldvalues = easygui.multenterbox(error_msg, tittle, register_screen_fieldnames,
                                                           register_screen_fieldvalues)
        return register_screen_fieldvalues
    AppenDatabase_Product('\n')
    for i in range(len(register_screen_fieldvalues)):
        fields_val = (str(register_screen_fieldvalues[i]) + "$")
        AppenDatabase_Product(fields_val)

    def existsProduct(DATABASE_FILE):
        exists = set(newProductId)
        for elem in DATABASE_FILE:
            if elem in exists:
                return True
            else:
                return False

#hiermee worden producten verwijderd
def Product_Delete():
    msg = 'Verwijder een product uit de DataBase'
    title = 'Product Verwijder'
    fieldNames = ['Product ID *']
    fieldValues = easygui.multenterbox(msg, title, fields=fieldNames)

    while 1:                        # make sure that none of the fields was left blank
        if fieldValues is None: break
        error_msg = ''
        for i in range(len(fieldNames)):
            if fieldValues[i].strip() == "":
                error_msg += ('"%s" is een verplicht veld.' % fieldNames[i])
        if error_msg == '': break
        fieldValues = easygui.multenterbox(error_msg, title, fieldNames, fieldValues)
        return fieldValues
    for i in range(len(fieldValues)):
        fields_val = (str(fieldValues[i]) + "$")
        with open('ProductDatabase.txt', 'r+') as f:
            d = f.readlines()
            f.seek(0)                                    # Search for the line (product) in the list that you want to delete
            for line in d:
                if str(fields_val) not in line:          # Re-write the list, minus the selected product and code.
                    f.write(line)
            f.truncate()
    while 1:
        if fieldValues is None: break
        error_msg = ""
        easygui.msgbox('{} was verwijderd.'.format(fieldValues))
        if error_msg == "": break

#hiermee worden alle producten getoont
def Product_Show():
    msg = 'Alle producten in onze assortiment: '
    title = 'Alle producten in onze assortiment'

    with open('ProductDatabase.txt', 'r') as listOfProducts:                # 'Read' the list and place all lines into a variable.
        listOfProducts = [w.replace('$', ' ') for w in listOfProducts]      # Replace the '$' sign with a space for Legibility.
        easygui.textbox(msg, title, listOfProducts)                         # Display the list

    '''         # Alternative way of achieving same function:
    with open('ProductDatabase.txt', 'r') as p:
        for elem in p:
            listOfProducts = p
            listOfProducts = [w.replace('$', ' ') for w in listOfProducts]
            easygui.textbox(msg, title, listOfProducts)
    '''

#hiermee kan een selectie gemaakt worden tussen de producten
def Product_Select():
    msg = 'Maak aub een keuze van de product(en) u wenst te huren:'
    title = 'Product(en) Keuze'
#    product_choice_fieldnames = ['Cirkelzaag', 'Accu-klopboormachine', 'Decoupeerzaag', 'Haakse Slijper']
    with open('ProductDatabase.txt', 'r') as listOfProducts:                # 'Read' the list and place all lines into a variable.
        listOfProducts = [w.replace('$', ' ') for w in listOfProducts]
        listOfProducts = [w.strip('\n') for w in listOfProducts]
        product_choice_fieldnames = listOfProducts
    product_choice_fieldvalues = easygui.multchoicebox(msg, title, choices=product_choice_fieldnames, preselect=0, callback=None, run=True)
    while 1:
        if product_choice_fieldvalues is None: break
        error_msg = ""
        easygui.msgbox('You chose: {}'.format(product_choice_fieldvalues), image=logo)
        if error_msg == "": break

    '''        # Alternative way of achieving same function:
    choices_list = list(enumerate(product_choice_fieldvalues, 1))
    easygui.msgbox('You chose: {}'.format(choices_list), image=logo)    
    '''

#-----------------------------------------------------------------------------------------------------------------------De pagina's na het inloggen
#dit is de admin main pagina
def Admin_Page():
    begin_opties = ["Gebruikersinformatie", "Gebuiker verwijderen", "Producten", "Terug"]
    begin_keuze = easygui.buttonbox("Welkom Admin", pr, begin_opties, image=logo)
    if begin_keuze == 'gebruikersinformatie':
        get_user_data_input = easygui.enterbox("Voer gebruikersnaam in voor het opvragen van gebruikersgegevens.", pr,
                                               "")
        get_user_data_output = get_user_data(get_user_data_input)
        easygui.msgbox(f"""
                De gegevens van het account van {get_user_data_output[0]} zijn als volgt. \n
                Gebruikersnaam   :   {get_user_data_output[0]}
                Voornaam         :   {get_user_data_output[1]} 
                Achternaam       :   {get_user_data_output[2]}
                Straatnaam       :   {get_user_data_output[3]}
                Straatnummer     :   {get_user_data_output[4]} 
                Stad             :   {get_user_data_output[5]}
                Provincie        :   {get_user_data_output[6]}
                Postcode         :   {get_user_data_output[7]} 
                Land             :   {get_user_data_output[8]}
                Email            :   {get_user_data_output[9]}""", pr)

    elif begin_keuze == 'Gebuiker verwijderen':
        delete_user_input = easygui.enterbox("Voer gebruikersnaam in voor het verwijderen van de gebruikersgegevens.",
                                     "Delete user", "")
        delete_user_verification = easygui.ynbox(f"Weet je zeker dat je gebruiker {delete_user_input} wilt verwijderen?",
                                         "Delete user")
        if delete_user_verification is True:
            delete_user_output = delete_user(delete_user_input)
            print(delete_user_output)
            succes_opties = ("terug","afsluiten")
            succes = easygui.buttonbox("Gebruiker succesvol verwijderd", pr,succes_opties)
            if succes == "terug":
                Admin_Page()
            elif succes == "afsluiten":
                exit()
    elif begin_keuze == 'Producten':
        Admin_Choices_Producten()
    elif begin_keuze == 'Stoppen':
        exit()

#dit is de klanten main pagina
def Scherm_Klanten():
    msg = 'Maak aub een keuze.'
    title = 'Klanten Keuzes'
    klant_choice_fieldnames = ['Producten Tonen', 'Product(en) Huren', 'Exit']
    klant_choice_fieldvalues = easygui.buttonbox(msg, title, choices=klant_choice_fieldnames, image=logo)
    if klant_choice_fieldvalues == 'Producten Tonen':
        Product_Show()
    elif klant_choice_fieldvalues == 'Product(en) Huren':
        Product_Select()
    elif klant_choice_fieldvalues == 'Exit':
        exit()

#dit is de admin producten pagina
def Admin_Choices_Producten():
    msg = 'Maak aub een keuze.'
    title = 'Admin Keuzes'
    admin_choice_fieldnames = ['Producten Tonen', 'Product Toevoegen', 'Product Verwijderen', 'Exit']
    admin_choice_fieldvalues = easygui.buttonbox(msg, title = pr, choices=admin_choice_fieldnames, image=logo)
    if admin_choice_fieldvalues == 'Producten Tonen':
        Product_Show()
    elif admin_choice_fieldvalues == 'Product Toevoegen':
        Product_Add()
    elif admin_choice_fieldvalues == 'Product Verwijderen':
        Product_Delete()
    elif admin_choice_fieldvalues == 'Terug':
        Admin_Page()