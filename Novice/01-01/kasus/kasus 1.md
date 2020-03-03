1. Bubble Sort

Bubble sort mungkin metode sorting paling populer yang digunakan dan sederhana. Proses pengurutan dilakukan dengan membandingkan masing-masing nilai dalam suatu list secara berpasangan, kemudian tukar nilai jika diperlukan, dan mengulanginya sampai akhir list secara berurutan, sehingga tidak ada lagi nilai yang dapat ditukar.

Langkahnya seperti di bawah ini :

    Bandingkan nilai pada data ke-1 dengan data ke-2.

    Jika nilai data ke-1 lebih besar dari data ke-2 maka tukar posisinya.

    Kemudian data yang lebih besar tersebut dibandingkan lagi dengan data ke-3.

    Jika data ke-3 lebih kecil dari data ke-2 maka tukar posisinya, dan begitu seterusnya sampai semua data yang ada jadi terurut.

Contoh script dengan Python :
Python
#!/usr/bin/python 

def BubbleSort(val):
    for passnum in range(len(val)-1,0,-1):
        for i in range(passnum):
            if val[i]>val[i+1]:
                temp = val[i]
                val[i] = val[i+1]
                val[i+1] = temp

DaftarAngka = [23,7,32,99,4,15,11,20]
BubbleSort(DaftarAngka)
print(DaftarAngka)
1
2
3
4
5
6
7
8
9
10
11
12
13
	
#!/usr/bin/python 
 
def BubbleSort(val):
    for passnum in range(len(val)-1,0,-1):
        for i in range(passnum):
            if val[i]>val[i+1]:
                temp = val[i]
                val[i] = val[i+1]
                val[i+1] = temp
 
DaftarAngka = [23,7,32,99,4,15,11,20]
BubbleSort(DaftarAngka)
print(DaftarAngka)

2. Selection Sort

Prinsip dari algoritma selection sort adalah memilih elemen dengan nilai paling rendah dan menukar elemen tersebut dengan elemen ke-i. Nilai dari i dimulai dari 1 ke n, dimana n adalah jumlah total elemen dikurangi 1.

Langkahnya seperti di bawah ini :

    Pengecekan dimulai dari data ke-1 sampai dengan data ke n.

    Tentukan bilangan dengan index terkecil dari data bilangan tersebut.

    Tukar bilangan dengan index terkecil tersebut dengan bilangan pertama (i=1) dari data bilangan tersebut.

    Lakukan langkah 2 dan 3 untuk bilangan berikutnya (i=i+1) sampai di dapatkan data yang sesuai.

Contoh script dengan Python :
#!/usr/bin/python 

def SelectionSort(val):
   for isi in range(len(val)-1,0,-1):
       Max=0
       for lokasi in range(1,isi+1):
           if val[lokasi]>val[Max]:
               Max = lokasi

       temp = val[isi]
       val[isi] = val[Max]
       val[Max] = temp

DaftarAngka = [23,7,32,99,4,15,11,20]
SelectionSort(DaftarAngka)
print(DaftarAngka)
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
	
#!/usr/bin/python 
 
def SelectionSort(val):
   for isi in range(len(val)-1,0,-1):
       Max=0
       for lokasi in range(1,isi+1):
           if val[lokasi]>val[Max]:
               Max = lokasi
 
       temp = val[isi]
       val[isi] = val[Max]
       val[Max] = temp
 
DaftarAngka = [23,7,32,99,4,15,11,20]
SelectionSort(DaftarAngka)
print(DaftarAngka)

 

3. Insertion Sort

Prinsip algoritma insertion sort pada dasarnya membagi data yang akan diurutkan menjadi dua bagian, satu bagian yang belum diurutkan dan yang satunya lagi sudah diurutkan. Elemen pertama diambil dari bagian list yang belum diurutkan dan kemudian diletakkan sesuai posisinya pada bagian lain dari list yang telah diurutkan. Langkah ini dilakukan secara berulang hingga tidak ada lagi elemen yang tersisa pada bagian list yang belum diurutkan.

Langkahnya seperti di bawah ini :

    Bandingkan data ke-2 dengan data ke-1, jika data ke-2 lebih kecil maka tukar posisinya, jika tidak biarkan aja.

    Data ke-3 dibandingkan dengan data ke-1 dan ke-2, jika data ke-3 lebih kecil kemudian tukar lagi posisinya.

    Data ke-4 dibandingkan dengan data ke-3, ke-2, dan ke-1, jika data ke-4 lebih kecil dari ketiganya maka letakkan data ke-4 ke posisi paling depan. Begitu seterusnya sampai tidak ada lagi data yang bisa dipindahkan.

Contoh script dalam Python :
Python
#!/usr/bin/python 

def InsertionSort(val):
   for index in range(1,len(val)):

     valueaktif = val[index]
     posisi = index

     while posisi>0 and val[posisi-1]>valueaktif:
         val[posisi]=val[posisi-1]
         posisi = posisi-1

     val[posisi]=valueaktif

DaftarAngka = [23,7,32,99,4,15,11,20]
InsertionSort(DaftarAngka)
print(DaftarAngka)
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
	
#!/usr/bin/python 
 
def InsertionSort(val):
   for index in range(1,len(val)):
 
     valueaktif = val[index]
     posisi = index
 
     while posisi>0 and val[posisi-1]>valueaktif:
         val[posisi]=val[posisi-1]
         posisi = posisi-1
 
     val[posisi]=valueaktif
 
DaftarAngka = [23,7,32,99,4,15,11,20]
InsertionSort(DaftarAngka)
print(DaftarAngka)
