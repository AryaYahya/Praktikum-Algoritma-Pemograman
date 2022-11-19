# Tugas Akhir Praktikum Algoritma
# creat by Arya Yahya

""""
Top Up Dana

program ini berfungsi untuk melakukan pencetakan bon transaksi Top Up Dana. program akan meminta masukan
identitas customer. kemudian menanyakan jumlah nominal yang ingin di Top Up. lalu di serahkan hasilnya.

"""

import datetime

identitas = ["Nama Pengguna","Nomor Handphone","jumlah nominal"]
data = []
biayaLayanan = 0
tanggal = datetime.datetime.now()

print(30*"="+"""
      Nama\t: Arya Yahya Prihandana
      NIM\t: 2070231070
      program\t: Top Up Dana
      """+30*"="+"\n")

for x in range(len(identitas)):
    val = input("masukan "+ identitas[x]+":")
    data.append(val)
    
    serviceCheck = str(data[4]).upper()
    
    if(serviceCheck == "REGULER"):
        biayaLayanan = 50000*int(data[3])
    elif(serviceCheck == "PREMIUM"):
        biayaLayanan = 100000*int(data[3])
    else:
        print("Harap masukan layanan service")
        
        print("\n"+8*"="+"transaksi Top Up"+8*"="+"\n")
        
        print("Tanggal :"+ tanggal.strftime("%d-%m-%Y%X"))
        
for x in range(4):
    print(identitas[x]+":"+data[x])
    
    if(biayaLayanan%50000 == 0):
        print("Service : 50000")
    else:
        print("Service : 100000")
        print("Total biaya:+str(biayaLayanan")
