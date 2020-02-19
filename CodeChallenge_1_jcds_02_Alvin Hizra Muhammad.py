matriks = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

def putar_kanan():
    input_putar_kanan = int(input('Berapa kali putar : '))
    for putar in range(input_putar_kanan):
        matriks[0][0],matriks[0][2],matriks[2][2],matriks[2][0] = matriks[2][0],matriks[0][0],matriks[0][2],matriks[2][2]
        matriks[0][1],matriks[1][2],matriks[2][1],matriks[1][0] = matriks[1][0],matriks[0][1],matriks[1][2],matriks[2][1]
    menu()

def putar_kiri():
    input_putar_kiri = int(input('Berapa kali putar : '))
    for putar in range(input_putar_kiri):
        matriks[0][0],matriks[0][2],matriks[2][2],matriks[2][0] = matriks[0][2],matriks[2][2],matriks[2][0],matriks[0][0]
        matriks[0][1],matriks[1][2],matriks[2][1],matriks[1][0] = matriks[1][2],matriks[2][1],matriks[1][0],matriks[0][1]
    menu()

def Horizontal():
    input_horizontal = int(input('Baris ke berapa? '))
    matriks[input_horizontal-1][0],matriks[input_horizontal-1][2]=matriks[input_horizontal-1][2],matriks[input_horizontal-1][0]
    menu()

def Vertikal():
    input_vertikal = int(input('Kolom ke berapa? '))
    matriks[0][input_vertikal-1],matriks[2][input_vertikal-1]=matriks[2][input_vertikal-1],matriks[0][input_vertikal-1]
    menu()

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


menu()