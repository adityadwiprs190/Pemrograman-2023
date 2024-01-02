def tambah(angka1, angka2):
    return angka1 + angka2
def kurang(angka1, angka2):
    return angka1 - angka2
def bagi(angka1, angka2):
    return angka1 / angka2
def kali(angka1, angka2):
    return angka1 * angka2
def pangkat(angka1, angka2):
    return angka1 ** angka2
angka1 = float(input("masukkan angka1 :"))
angka2 = float(input("Masukkan angka2 : "))
operator = input("Pilih operator : ")
if operator == '+':
    hasil = tambah(angka1, angka2)
    operator_keterangan = "Tambah"
elif operator == '-':
    hasil = kurang(angka1, angka2)
    operator_keterangan = "Kurang"
elif operator == '/':
    hasil = bagi(angka1, angka2)
    operator_keterangan = "Bagi"
elif operator == '*':
    hasil = kali(angka1, angka2)
    operator_keterangan = "Kali"
elif operator == '**':  
    hasil = pangkat(angka1, angka2)
    operator_keterangan = "Pangkat"
else:
    print("Operator tidak valid")
    exit()    
print(f"angka kesatu: {angka1}")    
print(f"Angka kedua: {angka2}")
print(f"Pilihan Operator: {operator_keterangan}")
print(f"Hasil operator {angka1} {operator} {angka2} = {hasil}")
    

