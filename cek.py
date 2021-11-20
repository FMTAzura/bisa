import base64

text = input("Masukan Teks yang Akan di Enkripsi: ").encode('utf-8')

print("===========================================")
print("PROSES PENGEKRIPSIAN PESAN")
print("===========================================")

base64_encryption = base64.b64encode(text)
print("Hasil Enkripsi   : ", base64_encryption)
print("Hasil Enkripsi 2 : ", base64_encryption.decode('utf-8'))


print("===========================================")
print("PROSES PENDESKRIPSIAN PESAN")
print("===========================================")

base64_decryption = base64.decodebytes(base64_encryption)
print("Hasil Enkripsi   : ", base64_decryption)
print("Hasil Enkripsi 2 : ", base64_decryption.decode('utf-8'))

#REVISI KETIGA
