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



<img width="960" alt="2021-12-10 (2)" src="https://user-images.githubusercontent.com/92783916/145543315-5ef05c6e-54f3-4d99-9df4-b2d3d0157821.png">
