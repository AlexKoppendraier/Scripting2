import easygui
import Encrypter
pr = "PowerRent"

def ReadDatabase():
    ReadDatabase = open("Database.txt", "r")
    print(ReadDatabase.read())
    ReadDatabase.close()

def WriteDatabase(S):
    WriteDatabase = open("Database.txt", "w")
    WriteDatabase.write(S)
    WriteDatabase.close()

def AppenDatabase(S):
    AppenDatabase = open("Database.txt", "a")
    AppenDatabase.writelines(S)
    AppenDatabase.close()

def ReadDatabase_admin():
    ReadDatabase = open("AdminDatabase.txt", "r")
    print(ReadDatabase.read())
    ReadDatabase.close()

def WriteDatabase_admin(S):
    WriteDatabase = open("AdminDatabase.txt", "w")
    WriteDatabase.write(S)
    WriteDatabase.close()

def AppenDatabase_admin(S):
    AppenDatabase = open("AdminDatabase.txt", "a")
    AppenDatabase.writelines(S)
    AppenDatabase.close()
#-----------------------------------------------------------------------------------------------------------------------

def Waarschuwing(S):
    msg = S
    tittle = pr
    easygui.msgbox(msg,tittle)

def hasher(S):
    S = hash(S)

#-----------------------------------------------------------------------------------------------------------------------

def Scherm_Registreer():
    msg = 'Enter your personal details'
    tittle = 'Personal details'
    register_screen_fieldnames = ['Username *','Name *', 'last name *', 'Street','Number', 'City', 'State', 'ZipCode', 'Country','E-mail *','Password *']
    register_screen_fieldvalues = easygui.multpasswordbox(msg, tittle, fields=register_screen_fieldnames)
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

def Scherm_Inloggen():
    msg = 'Enter your username and password to log in'
    tittle = 'Log on screen'
    logon_screen_fieldnames = ['Username', 'Password']
    logon_screen_fieldvalues = easygui.multpasswordbox(msg, tittle, fields=logon_screen_fieldnames)
    while 1:
        for line in open('Database.txt','r').readlines():
            login_info = line.split('$')
            if logon_screen_fieldvalues[0] == login_info[0] and logon_screen_fieldvalues[1] == login_info[10]:
                print("Correct credentials!")
                Waarschuwing('Correct credentials')
                return True
        print("Incorrect credentials.")
        Waarschuwing('Incorrect credentias')
        Scherm_Inloggen()
        return False

def Scherm_Inloggen_Admin():
    msg = 'Enter your username and password to log in'
    tittle = 'Log on screen'
    logon_screen_fieldnames = ['Username', 'Password']
    logon_screen_fieldvalues = easygui.multpasswordbox(msg, tittle, fields=logon_screen_fieldnames)
    while 1:
        for line in open('AdminDatabase.txt','r').readlines():
            login_info = line.split('$')
            if logon_screen_fieldvalues[0] == login_info[0] and logon_screen_fieldvalues[1] == login_info[10]:
                print("Correct credentials!")
                Waarschuwing('Correct credentials')
                return True
        print("Incorrect credentials.")
        Waarschuwing('Incorrect credentias')
        Scherm_Inloggen()
        return False