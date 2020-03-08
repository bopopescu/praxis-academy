user_id = 0
loop = "n"
user =  [
            {   
                "id":"1",
                "no_rekening":"111111",
                "username":"Budi",
                "pin":"1111",
                "saldo":5000000
            },
            {   
                "id":"2",
                "no_rekening":"222222",
                "username":"Agoy",
                "pin":"2222",
                "saldo":25000000
            },
            {   
                "id":"3",
                "no_rekening":"333333",
                "username":"Dana",
                "pin":"3333",
                "saldo":20000000
            }
        ]
status_login = False
pakai_atm = "y"
 
def cek_login(p):
    for us in user:
        if us['pin'] == p:
            return us
    return False       
     
def cek_user(id):
    for i in range(len(user)):
        if user[i]['id'] == str(id):
            return int(i)
    # return -1
 
# def cek_rekening(no):
#    for i in range(len(user)):
#        if str(user[i]['no_rekening']) == str(no):
#            return int(i)
#   return -1
 
def tranfer_uang(uang):
    index1 = cek_user(user_id)
    
    if index1 >= 0:
        if user[index1]['saldo'] >= int(uang):
            user[index1]['saldo'] =user[index1]['saldo'] + int(uang)
            print("Anda berhasil mentransfer uang Rp."+str(uang)+" ke rekening ")
            print("sisa saldo anda adalah Rp.",user[index1]['saldo'])
      
             
def ambil_uang(uang):
    index1 = cek_user(user_id)

    if index1 >= 0:
        if user[index1]['saldo'] >= int(uang):
            user[index1]['saldo'] =user[index1]['saldo'] - int(uang) 
            print("Anda berhasil menarik uang Rp."+str(uang))
            print("sisa saldo anda Rp.",user[index1]['saldo'])
        else:
            print("maaf saldo anda tidak cukup")
 
 
while pakai_atm == "y":
    while status_login == False:
        print("=========================================")
        print("\tSELAMAT DATANG DI ATM BANK")
        print("=========================================")
        print("")
        pin = input("Masukan PIN : ")
     
        cl = cek_login(pin)
        if cl != False:
            print("Hallo "+cl['username'])
            user_id = cl['id']
            status_login = True
            loop = "y"
        else:
            print("")
            print("PIN anda salah")
            print("")
            print("")
     
    while loop == "y" and status_login == True:
        u = user[cek_user(user_id)]
        print("PILIH MENU ATM")
        print("1.Cek Saldo")
        print("2.Transfer Uang")
        print("3.Ambil Uang")
        print("4.Keluar ATM")
        a = int(input("pilih menu : "))
        if a == 1:
            print("")
            print("Saldo anda adalah Rp.",u['saldo'])
            print("")
            print("")
            loop = "n"

        elif a == 2:
            nominal = input("Nominal Yang Akan Di Transfer : ")
            tranfer_uang(nominal)
            print("")
            loop = "n"
           
                 
        elif a == 3:
            nominal = input("Nominal Yang Akan Di Tarik : ")
            ambil_uang(nominal)
            print("")
            loop = "n"

        # elif a == 4:
        #    status_login = False 
             
        elif a == 4:
            status_login = False
            loop = "n"
            pakai_atm = "n"
        else:
            print("pilihan tidak tersedia")
        if status_login == True:
             
            input("kembali Ke menu ")
            print("")
            loop = "y"