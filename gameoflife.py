from tkinter import*
from tkinter import messagebox
from tkinter import ttk
from random import randint

#Pencerenin boyutları
screenWidth  = 1000
screenHeigth = 750

#Matrisin botyutları
row = 17
col = 22
#Akıştaki hızı belirleyen değişken
time= 1000

class GameofLine:
    def __init__(self, master):
        self.master = master
        self.play = True
        
        label = Label( master, text = "Game of Life")
        label.grid(column = 0, row = 0 )
        label.config(width=15, height=1)

        self.btnStart = Button(master, text = "Başla", command = self.start)
        self.btnStart.grid(column = 0 , row = 1)
        self.btnStart.config(width=15, height=1, bg= "white")

        self.btnStop = Button(master, text = "Dur", command = self.stop)
        self.btnStop.grid(column = 0 , row = 2)
        self.btnStop.config(width=15, height=1, bg= "white")
        
        btnRandom = Button(master, text = "Rastgele", command = self.rand)
        btnRandom.grid(column = 0 , row = 3)
        btnRandom.config(width=15, height=1, bg= "white")

        btnClean = Button(master, text = "Temizle", command = self.clean)
        btnClean.grid(column = 0 , row = 4)
        btnClean.config(width=15, height=1, bg= "white")

        btnInfo = Button(master, text = "Nasıl Oynanır", command = self.info)
        btnInfo.grid(column = 0 , row = 5)
        btnInfo.config(width=15, height=1, bg= "white")

        label1 = Label( master, text = "HIZ")
        label1.grid(column = 0, row = 6 )
        label1.config(width=15, height=2, bg= "white")

        self.speed = Scale(master, from_=1, to=100, orient=HORIZONTAL, width = 15)
        self.speed.grid(column = 0, row = 7)

        self.patterns = ttk.Combobox(master, 
                            values=[
                                    "Desenler",
                                    "Glider", 
                                    "Tumbler",
                                    "Exploder",
                                    "Small Exploder",
                                    "Ligthweigth Spaceship",
                                    "10 Cell Row"])
        self.patterns.grid(column=0, row=8)
        self.patterns.current(0)
        self.patterns.bind("<<ComboboxSelected>>", self.comboListen)

        #Map'in oluşturuluyor
        self.btn=  [[0 for x in range(col)] for x in range(row)]
        for i in range(row):
            for j in range(col):
                self.btn[i][j] = Button(master,command= lambda name="" + str(i) + "+"  + str(j) + "":self.click(name))
                self.btn[i][j].grid(row=i, column=j + 1)
                self.btn[i][j].config(width=4, height=2)
                self.btn[i][j].config(bg = "black")
        
        self.master.update()
        self.play = False
    
    #Rastgele oluşturulmasını sağlayan method
    def rand(self):
        for i in range(row):
            for j in range(col):
                self.matrix[i][j] = randint(0, 1)
            self.matrixEdit()

    #ComboBox'tan seçilecek olan Pattern'in oluşturuluduğu method
    def comboListen(self,event):
        self.clean()
        if self.patterns.get() == "Desenler":
            self.clean()
        elif self.patterns.get() == "Glider":
            self.matrixPatterns(
                [[0, 1, 0, 0], 
                 [0, 0, 1, 0], 
                 [1, 1, 1, 0]]
            )
        elif self.patterns.get() == "Tumbler":
            self.matrixPatterns(
                [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0],
                 [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0],
                 [0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
            )
        elif self.patterns.get() == "Exploder":
            self.matrixPatterns(
                [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
            )
        elif self.patterns.get() == "Small Exploder":
            self.matrixPatterns(
                [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
            )
        elif self.patterns.get() == "Ligthweigth Spaceship":
            self.matrixPatterns(
                [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
            )
        elif self.patterns.get() == "10 Cell Row":
            self.matrixPatterns(
                [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
            )
    
    #Seçilen Pattern'i ana matrise aktarmayı sağlayan method
    def matrixPatterns(self, matrix):
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.matrix[i][j] = matrix[i][j]
        self.matrixEdit()

    #Ana matrisi oluşturulduğu method
    def matrixCreate(self):
        self.matrix = [[0 for x in range(col)] for x in range(row)]
        self.matrixCheck()

    #Başla butonuna bastığında çalışacak olan method
    def start(self):
        self.play = True
        self.btnStart.config(bg = "green")
        self.btnStop.config(bg = "white")

    #Stop butonuna basıldığında çalışacak olan method
    def stop(self):
        self.play = False
        self.btnStop.config(bg = "red")
        self.btnStart.config(bg = "white")

    #Temizle butonuna çalışcak olan method
    def clean(self):
        self.btnStop.config(bg = "white")
        self.btnStart.config(bg = "white")
        self.play = False
        self.matrixReset()
        self.matrixCheck()
        self.master.update()

    #Nasıl Oynanır butonuna basıldığında çalışcak olan method
    def info(self):
        messagebox.showinfo("Nasıl Oynanır","Kural - 1 ) Bir canlı hücrenin, iki'den daha az " +
                                            "canlı komşusu varsa yalnızlık nedeniyle ölür.\n" + 
                                            "Kural - 2 ) Bir canlı hücrenin, üç'ten daha fazla " + 
                                            "canlı komşusu varsa kalabalıklaşma nedeniyle ölür.\n" +
                                            "Kural - 3 ) Bir canlı hücrenin, iki ya da üç canlı " + 
                                            "komşusu varsa değişmeden bir sonraki nesile kalır.\n" + 
                                            "Kural - 4 ) Bir ölü hücrenin tam olarak üç canlı komşusu varsa canlanır.")

    #Temizle butonuna bastığında çalışaca kolan method
    def matrixReset(self):
        for i in range(row):
            for j in range(col):
                self.matrix[i][j] = 0
                self.btn[i][j].config(bg = "black")

    #Herhangi bir hücreye bastığında çalışacak olan method
    def click(self,name):
        pos = name.split('+')
        i = int(pos[0])
        j = int(pos[1])
        if self.matrix[i][j] == 0:  # Basılan hücre ölü ise canlandır
            self.matrix[i][j] = 1
            self.btn[i][j].config(bg = "white")
        else:                       # Basılan hücre canlı ise öldür
            self.matrix[i][j] = 0
            self.btn[i][j].config(bg = "black")
        
    #Hücrelerin tümünü kontrol eden method
    def matrixCheck(self):
        if self.play == True:
            for i in range(row):
                for j in range(col):
                    self.matrixChange(i , j , self.neighborCheck(i,j)) #Hücrenin komşularını say
            self.matrixEdit()
            self.master.after(int(time / self.speed.get()))
        self.master.update()

    #Kontrol edilen hücrelerin düzenlendiği method method
    def matrixEdit(self):
        for i in range(row):
            for j in range(col):
                if self.matrix[i][j] == 1 or self.matrix[i][j] == 2:
                    self.matrix[i][j] = 1
                    self.btn[i][j].config(bg = "white")
                elif self.matrix[i][j] == 0 or self.matrix[i][j] == -1:
                    self.matrix[i][j] = 0
                    self.btn[i][j].config(bg = "black")

    #Kontrol edilen hücrelerin gerekli işlemlerinin yapıldığı method
    def matrixChange(self, i , j , sum):
        if self.matrix[i][j]  == 0:
            if sum == 3: # Ölü hücre canlandı
                self.matrix[i][j] = 2
        elif self.matrix[i][j]  == 1:
            if sum < 2: # Yalnızlık nedeniyle öldü
                self.matrix[i][j] = -1
            elif sum > 3: # Kalabalıklaşma nedeniyle öldü"
                self.matrix[i][j] = -1
            elif sum == 2 or sum == 3: # Bir sonraki nesle kaldı
                self.matrix[i][j] = 1

    # Hürenin komşuluklarını kontrol eden method
    def neighborCheck(self,x,y):
        counter = 0
        for i in [-1,0,1]:
            for j in [-1,0,1]:
                if i == 0 and j == 0 or (x + i) < 0 or (y + j) < 0 or (x + i) == row or (y + j) == col:
                    continue
                if self.matrix [(x + i)][(y + j)] == 1 or self.matrix [(x + i)][(y + j)] == -1:
                    counter = counter + 1
        return counter

if __name__ == "__main__":
    root=Tk()
    root.title("SKYZ TECH")

    master = GameofLine(root)
    master.matrixCreate()

    root.geometry(str(screenWidth) + "x" + str(screenHeigth))
    root.resizable(False, False)
    
    while 1:
        master.matrixCheck()
    root.mainloop()


    