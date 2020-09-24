print("""************************

kullanıcı girişi

*******************""")


userName1 = "ousman"
parola1 = "123456"

userName = input("Kullanıcı adı giriniz: ")
parola = (input("Şifrenizi giriniz: "))

if(userName == userName1 and parola != parola1):
    print("Parola hatalı!")


elif(userName != userName1 and parola == parola1):
    print("Kullanıcı adı hatalı!")

elif(userName != userName1 and parola != parola1):
    print("Kullanıcı adı ve Parola hatalı!")

else:
    print("Sisteme başarıyla giriş yaptınız.")
