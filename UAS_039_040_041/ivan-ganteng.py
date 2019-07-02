#Yoga Satria W (l200170039)
#Ivan Amar F (L200170040)
#Elvy Rahmatillah I (L200170041)

#PROGRAM RAK BUKU

# Class stack
def swap(A, p, q):
    temp=A[p]
    A[p]=A[q]
    A[q]=temp
def bubbleSort(data):
    n=len(data)
    for i in range(n-1):
        for j in range(n-i-1):
            if data[j] > data[j+1]:
                swap(data, j, j+1)

class Stack:
    def __init__(self):
        self.items = []
       
    # Memeriksa apakah stack kosong
    def isEmpty(self):
        return self.items == []
    
    # Menambah objek/data ke dalam stack
    def push(self, item):
        self.items.append(item)
        
    # Mengeluarkan data dari stack
    def pop(self):
        return self.items.pop()
    
    # Menampilkan objek terakhir dari stack
    def peek(self):
        return self.items[len(self.items)-1]
    
    # Mehitung panjang stack
    def size(self):
        return len(self.items)

    # Mencari Data
    def cariData(self, key):
        index=0
        for k in self.items:
            if k == key:
                print(str(key)+" Ditemukan, Pada indexing ke "+str(index))
            index+=1

    def Urutkan(self):
        data_sebelum=self.items
        print("Data Berhasil Di urutkan\n")
        print("Sebelum diurutkan :")
        print(data_sebelum)
        bubbleSort(self.items)
        print("\n")
        print("Setelah diurutkan :")
        print(self.items)
        print("\n")
   
    # Menu dari aplikasi
    def mainmenu(self):
        pilih = "y"
        while (pilih == "y"):
            print("=========================")
            print("|  Aplikasi Rak Buku  |")
            print("=========================")
            print("1. Menambah buku")
            print("2. Mengambil Buku yang paling atas ")
            print("3. Mengecek Rak Buku")
            print("4. Menampilkan Buku Teratas")
            print("5. Menampilkan Jumlah Buku")
            print("6. Apakah raknya kosong ? ")
            print("7. Pencarian Buku ")
            print("8. Urutkan Buku ")
            print("n. Keluar ? ")
            print("=========================")
            pilihan=str(input(("Silakan masukan pilihan anda: ")))
            if(pilihan=="1"):
                obj = str(input("Masukan judul buku yang ingin anda tambahkan: "))
                self.push(obj)
                print("Buku "+obj+" telah ditambahkan")
                print("\n")
            elif(pilihan=="2"):
                if self.isEmpty() != True :
                    print("Buku "+self.pop()+" dihapus")
                    print("\n")
                else :
                    print("raknya udah kosong, tidak bisa diambil lagi")
                    print("\n")
            elif(pilihan=="3"):
                print(self.items)
                print("\n")
            elif(pilihan=="4"):
                print("Buku terakhir: "+self.peek())
                print("\n")
            elif(pilihan=="5"):
                print("Jumlah buku di rak adalah: "+str(self.size()))
                print("\n")
            elif(pilihan =="6"):
                print(self.isEmpty())
                print("\n")
            elif(pilihan =="7"):
                obj = str(input("Masukan judul buku yang ingin anda cari: "))
                self.cariData(obj)
                print("\n")
            elif(pilihan=="8"):
                self.Urutkan()
            elif pilihan=="n":
                break
            else:
                print("\n") 
 
if __name__ == "__main__":
    s=Stack()
    s.mainmenu()
