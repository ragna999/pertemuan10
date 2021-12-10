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