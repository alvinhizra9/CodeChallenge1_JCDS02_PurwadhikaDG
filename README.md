# Code Challenge 1 Data Science Purwadhika
Jawaban dan pembahasan code challenge 1 Program Job Connector Data Science Batch 2 Purwadhika Kampus Bandung.

### Problem
Diberikan Matriks sebagai berikut:
```
1 2 3
4 5 6
7 8 9
```
Buatlah program untuk:
- Memutar matriks ke kanan
- Memutar matriks ke kiri
- Membalikkan baris pilihan secara horizontal
- Membalikkan kolom pilihan secara vertikal

### Solution
###### Buat fungsi untuk putar kanan
```
def putar_kanan():
    input_putar_kanan = int(input('Berapa kali putar : '))
    for putar in range(input_putar_kanan):
        matriks[0][0],matriks[0][2],matriks[2][2],matriks[2][0] = matriks[2][0],matriks[0][0],matriks[0][2],matriks[2][2]
        matriks[0][1],matriks[1][2],matriks[2][1],matriks[1][0] = matriks[1][0],matriks[0][1],matriks[1][2],matriks[2][1]
    menu()
```
###### Buat fungsi untuk putar kiri
```
def putar_kiri():
    input_putar_kiri = int(input('Berapa kali putar : '))
    for putar in range(input_putar_kiri):
        matriks[0][0],matriks[0][2],matriks[2][2],matriks[2][0] = matriks[0][2],matriks[2][2],matriks[2][0],matriks[0][0]
        matriks[0][1],matriks[1][2],matriks[2][1],matriks[1][0] = matriks[1][2],matriks[2][1],matriks[1][0],matriks[0][1]
    menu()
```

###### Buat fungsi untuk bailk horizontal
```
def Horizontal():
    input_horizontal = int(input('Baris ke berapa? '))
    matriks[input_horizontal-1][0],matriks[input_horizontal-1][2]=matriks[input_horizontal-1][2],matriks[input_horizontal-1][0]
    menu()
```
###### Buat fungsi untuk bailk vertikal
```
def Vertikal():
    input_vertikal = int(input('Kolom ke berapa? '))
    matriks[0][input_vertikal-1],matriks[2][input_vertikal-1]=matriks[2][input_vertikal-1],matriks[0][input_vertikal-1]
    menu()
```
###### Buat fungsi menu utama
```
def menu():
    print('Matriks:')
    for item in matriks:
        for element in item:
            print(element,end=' ')
        print('')
    print('----------------')
    print('1. Putar kanan' + '\n' + '2. Putar Kiri' + '\n' + '3. Horizontal' + '\n' + '4. Vertikal' + '\n' + '5. Exit')
    nomor_menu = int(input('Pilihan menu : '))
    list_menu = [putar_kanan,putar_kiri,Horizontal,Vertikal,exit]
    list_menu[nomor_menu-1]()
```
### Let's Try
```
# Panggil fungsi menu
menu()
```
###### maka, akan muncul:
```
Matriks:
1 2 3
4 5 6
7 8 9
----------------
1. Putar kanan
2. Putar Kiri
3. Horizontal
4. Vertikal
5. Exit
Pilihan menu :
```
###### isikan 1 untuk memilih fitur putar kanan.
###### Setelah itu, akan muncul:
```
Berapa kali putar :
```
###### isikan 1 untuk memutar matriks ke kanan 1 kali.
###### Setelah itu, akan muncul output dan menu utama:
```
Matriks:
7 4 1
8 5 2
9 6 3
----------------
1. Putar kanan
2. Putar Kiri
3. Horizontal
4. Vertikal
5. Exit
Pilihan menu :
```
###### isikan 2 untuk memilih fitur putar kiri.
###### Setelah itu, akan muncul:
```
Berapa kali putar :
```
###### isikan 1 untuk memutar matriks ke kiri 1 kali.
###### Setelah itu, akan muncul output dan menu utama:
```
Matriks:
1 2 3
4 5 6
7 8 9
----------------
1. Putar kanan
2. Putar Kiri
3. Horizontal
4. Vertikal
5. Exit
Pilihan menu :
```
###### isikan 3 untuk memilih fitur balik horizontal.
###### Setelah itu, akan muncul:
```
Baris ke berapa?
```
###### isikan 1 untuk memutar isi baris ke 1 secara horizontal.
###### Setelah itu, akan muncul output dan menu utama:
```
Matriks:
3 2 1
4 5 6
7 8 9
----------------
1. Putar kanan
2. Putar Kiri
3. Horizontal
4. Vertikal
5. Exit
Pilihan menu :
```
###### isikan 4 untuk memilih fitur balik vertikal.
###### Setelah itu, akan muncul:
```
Baris ke berapa?
```
###### isikan 3 untuk memutar isi kolom ke 3 secara vertikal.
###### Setelah itu, akan muncul output dan menu utama:
```
Matriks:
3 2 9
4 5 6
7 8 1
----------------
1. Putar kanan
2. Putar Kiri
3. Horizontal
4. Vertikal
5. Exit
Pilihan menu :
```
###### isikan 5 untuk keluar dari program.

### Thank you For Reading 😊  Pull it. Try it. Evaluate it.  🔥  🔥  🔥 
