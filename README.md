# PERTEMUAN10
print ("membuat data kontak")
print("="*40)
dict = {'nama1':'ari','no.telp1':'081267888',
        'nama2':'dina','no.telp2':'087677776'}
print("nama/tl nomor telpon")
print("-"*40)
print("%s/t| %s" %(dict['nama1'], dict['no.telp1']))
print("%s/t| %s" %(dict['nama2'], dict['no.telp2']))
print("="*40)

print ("menampilkan kontak ari")
print("="*40)
print(dict['no.telp1'])
print("="*40)

print("menambahkan kontak baru")
print("="*40)
dict['nama3']= 'riko'
dict['no.telp3']='087654544'
print(dict)
print("="*40)

print("mengubah kontak dina dengan nomor 088999776")
print("="*40)
dict['no.telp2']='088999776'
print("%s/t| %s" %(dict['nama2'], dict['no.telp2']))
print("="*40)

print("menampilkan semua nama")
print("="*40)
<img width="960" alt="2021-12-10" src="https://user-images.githubusercontent.com/92783916/145543342-460c4b75-015e-4acc-b07b-dc9bba646101.png">


print(dict['nama1'])
print(dict['nama2'])
print(dict['nama3'])
print("="*40)

print("menampilkan semua nomor")
print("="*40)
print(dict['no.telp1'])
print(dict['no.telp2'])
print(dict['no.telp3'])
print("="*40)

print("menampilkan daftar nama dan nomor")
print("="*40)
print("nama/t| nomor telpon")
print("="*40)
print("%s/t| %s"%(dict['nama1'],dict['no.telp1']))
print("%s/t| %s"%(dict['nama2'],dict['no.telp2']))
print("%s/t| %s"%(dict['nama3'],dict['no.telp3']))
print("="*40)

print("menghapus kontak dina")
print("="*40)
del dict['no.telp2']
print(dict)
<img width="960" alt="2021-12-10 (1)" src="https://user-images.githubusercontent.com/92783916/145543309-9d6985f0-2504-4f45-8c2d-94010eb764c8.png">


import os,sys
Oc = os.system
while True:
    print("")
    print("" )
    c = input("T)ambah Data, U)bah Data, H)apus Data, C)ari Data, L)ihat Data, K)eluar: ")
    if c.lower() == 'k':
        break
    elif c.lower() == 't':
        i = open('database.txt','a')
        print(" Tambah Data")
        while (True):
            nama = input(" Nama : ")
            nim  = int(input(" NIM  : "))
            tugas  = int(input(" TUGAS  : "))                
            uts  = int(input(" UTS  : "))
            uas  = int(input(" UAS  : "))
            break
            
        akhir = round((float(tugas) * 0.3)+(float(uts) * 0.35)+(float(uas) * 0.35),2)
        i.write('\nNama : '+nama+'|Nim : '+str(nim)+'|Tugas : '+str(tugas)+'|UTS : '+str(uts)+'|UAS : '+str(uas)+"|Akhir : "+str(akhir)+'\n')
        i.close()
        Oc("clear")

    elif c.lower() == 'l':
        print("Lihat Data")
        i = open('database.txt','r').read().splitlines()
        print(" ========================================================================")
        print(" ||============================= DAFTAR NILAI =========================||")
        print(" ||====================================================================||")
<img width="960" alt="2021-12-10 (2)" src="https://user-images.githubusercontent.com/92783916/145543315-5ef05c6e-54f3-4d99-9df4-b2d3d0157821.png">
 print(" ||     NAMA        |       NIM        | TUGAS |  UTS  |  UAS  | AKHIR ||")        
        print(" ||====================================================================||")
        for l in i:
            if l == '':
                pass
            else:
                l1 = l.replace('Nama : ','').replace('Nim : ','').replace('Tugas : ','').replace('UTS : ','').replace('UAS : ','').replace('Akhir : ','')
                nama,nim,tugas,uts,uas,akhir = (l1.strip().split('|'))
                print((' ||')+(nama[:15]).ljust(17)+('| ')+(nim).ljust(17)+('| ')+(tugas).ljust(6)+('| ')+(uts).ljust(6)+('| ')+(uas).ljust(6)+('| ')+(akhir).ljust(6)+('||'))

        print(" ||=================|==================|=======|=======|=======|=======||")
    elif c.lower() == 'c':
        print("Mencari Data")
        cari = input(' Masukan Nama: ')
        i = open('database.txt','r').read().splitlines()
        print(" ||======================================================================")
        print(" ||=========================== DAFTAR KONTAK ==========================||")
        print(" ||====================================================================||")
        print(" ||     NAMA        |       NIM        | TUGAS |  UTS  |  UAS  | AKHIR ||")        
        print(" ||====================================================================||")
        for l in i:
            if l == '':
                pass
            elif cari in l:
                l1 = l.replace('Nama : ','').replace('Nim : ','').replace('Tugas : ','').replace('UTS : ','').replace('UAS : ','').replace('Akhir : ','')
                nama,nim,tugas,uts,uas,akhir = l1.strip().split('|')
                print((' ||')+(nama).ljust(17)+('| ')+(nim).ljust(17)+('| ')+(tugas).ljust(6)+('| ')+(uts).ljust(6)+('| ')+(uas).ljust(6)+('| ')+(akhir).ljust(6)+('||'))
        print(" ||=================|==================|=======|=======|=======|=======||")
    elif c.lower() == 'h':
        print("Menghapus Data")
<img width="960" alt="2021-12-10 (3)" src="https://user-images.githubusercontent.com/92783916/145599116-918f54c4-544c-4d4b-a334-392e80376ace.png">
nt("Menghapus Data")
        u = open('database.txt','r').read().splitlines()
        hapus = input(' Masukan Nama : ')
        nm = []
        for l in u:
            if l == '':
                pass
            else:
                l1 = l.replace('Nama : ','').replace('Nim : ','').replace('Tugas : ','').replace('UTS : ','').replace('UAS : ','').replace('Akhir : ','')
                nama,nim,tugas,uts,uas,akhir = l1.strip().split('|')
                if str(nama) == str(hapus):
                    print('Menghapus %s'%(hapus))
                    pass
                else:      
                    nm.append(str(l)+'\n')
        new = open('database.txt','w')        
        new.write(str(nm))
        new.close()
        new = open('database.txt','r').read().splitlines()
        new1 = open('database.txt','w')
        new1.close()
        new2 = open('database.txt','a')
        for i in new:
            i2 = i.replace("['","").replace("\\n', '", "\n").replace("']","").replace("\\n",'')
            new2.write(i2)
        new2.close()
    elif c.lower() == 'u':
        print("Mengubah Data")
        u = open('database.txt','r').read().splitlines()
        target = input(' Masukan Nama : ')
<img width="960" alt="2021-12-10 (4)" src="https://user-images.githubusercontent.com/92783916/145599126-0784d905-008d-4230-8100-79cacfca312b.png">
  nm = []
        for l in u:
            if l == '':
                pass
            else:
                l1 = l.replace('Nama : ','').replace('Nim : ','').replace('Tugas : ','').replace('UTS : ','').replace('UAS : ','').replace('Akhir : ','')
                nama,nim,tugas,uts,uas,akhir = l1.strip().split('|')
                if nama == target:
                    print(' Mengubah Data %s'%(target))
                    while (True):
                        nama = input(" Nama : ")
                        nim  = int(input(" NIM  : "))
                        tugas  = int(input(" TUGAS  : "))
                        uts  = int(input(" UTS  : "))
                        uas  = int(input(" UAS  : "))
                        break
                    akhir = round((float(tugas) * 0.3)+(float(uts) * 0.35)+(float(uas) * 0.35),2)
                    edit  =('Nama : '+nama+'|Nim : '+str(nim)+'|Tugas : '+str(tugas)+'|UTS : '+str(uts)+'|UAS : '+str(uas)+"|Akhir : "+str(akhir)+'\n')
                    nm.append(edit+'\n')
                else:      
                    nm.append(str(l)+'\n')
        new = open('database.txt','w')        
        new.write(str(nm))
        new.close()
        new = open('database.txt','r').read().splitlines()
        new1 = open('database.txt','w')
        new1.close()
        new2 = open('database.txt','a')
        for i in new:
            i2 = i.replace("['","").replace("\\n', '", "\n").replace("']","").replace("\\n","\n")
<img width="960" alt="2021-12-10 (5)" src="https://user-images.githubusercontent.com/92783916/145599132-c37aff34-a5a8-4cba-b335-9b12a89b2b05.png">
          new2.write(i2+'\n')
        new2.close()

    else:
        print("")
<img width="960" alt="2021-12-10 (6)" src="https://user-images.githubusercontent.com/92783916/145599137-46d6d19a-355c-4764-8c83-bc47b2d3ab04.png">

