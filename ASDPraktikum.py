import random

def Merge_Sort(List_Kosong):
    if len(List_Kosong) > 1:
        mid        = len(List_Kosong) // 2
        left_data  = List_Kosong[:mid]
        right_data = List_Kosong[mid:]

        Merge_Sort(left_data)
        Merge_Sort(right_data)

        b = i = j = 0

        while b < len(left_data) and i < len(right_data):
            if left_data[b] < right_data[i]:
                List_Kosong[j] = left_data[b]
                b += 1
            else:
                List_Kosong[j] = right_data[i]
                i += 1
            j += 1
        while b < len(left_data):
            List_Kosong[j] = left_data[b]
            b += 1
            j += 1
        while i < len(right_data):
            List_Kosong[j] = right_data[i]
            i += 1
            j += 1

def Shell_Sort(List_Kosong):
    n = len (List_Kosong)
    gap = n // 2

    while gap > 0:
        for i in range (gap, n):
            temp = List_Kosong[i]
            j=i
            while j >= gap and List_Kosong [j-gap] > temp:
                List_Kosong[j] = List_Kosong[j-gap]
                j -= gap

            List_Kosong [j] = temp
        gap //= 2

    return List_Kosong


List_Kosong = []
for i in range(10):
   List_Kosong.append(random.randint(1, 100))

while True:
    print("|---------------------------------------------|")
    print("|Mengurutkan Angka, Dengan Angka Acak (Random)|")
    print("|---------------------------------------------|")
    print()
    print("Pengurutan Angka (Sort) Yang Tersedia")
    print("            1. Shell Short           ")
    print("            2. Merge Sort            ")
    print("            3. Keluar                ")
    menu = int(input("Masukkan pilihan Sort yang ingin dilakukan: "))
    if menu == 1:
        print("Pengurutan Dengan Shell Sort Short")
        print("Angka sebelum di sort :",List_Kosong)
        Merge_Sort(List_Kosong)
        print("Angka Setelah di sort :",List_Kosong)
        print("")
        List_Kosong.clear()
        for i in range(10):
            List_Kosong.append(random.randint(1, 100))
    elif menu == 2:
        print("Pengurutan Dengan Merge Sort")
        print(f"Angka sebelum di sort : {List_Kosong}")
        result = Shell_Sort(List_Kosong)
        print(f"Angka Setelah di sort : {result}")
        print("")
        List_Kosong.clear()
        for i in range(10):
            List_Kosong.append(random.randint(1, 100))
    elif menu == 3:
        print("Terima Kasih")
        break
    else:
        print("Masukkan Pilihan Yang Tersedia antara 1/2")