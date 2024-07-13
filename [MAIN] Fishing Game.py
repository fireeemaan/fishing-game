import tkinter as tk
from tkinter import ttk, messagebox
import pygame
import pyautogui
from operator import itemgetter
from PIL import Image, ImageTk
from decimal import Decimal as dec
from datetime import date, datetime
import pandas as pd
import random as rd
import os

os.system("cls")
# os.chdir('D:\Python Learn\Semester 2\[PROJECT] Fishing Game')
pygame.init()

#==== Peta Keseluruhan

petaDunia = [
    [1, 1, 1, 1, 1, 24, 1, 1, 1, 1, 1],
    [1, 22, 1, 6, 1, 23, 1, 1, 1, 0, 1],
    [1, 0, 1, 12, 10, 15, 10, 10, 10, 5, 1],
    [1, 1, 1, 24, 1, 11, 1, 1, 22, 1, 1],
    [1, 1, 1, 23, 21, 11, 1, 1, 1, 1, 1],
    [1, 24, 1, 0, 24, 16, 10, 10, 10, 13, 1],
    [0, 23, 1, 1, 23, 11, 1, 22, 1, 4, 1],
    [1, 1, 14, 10, 10, 17, 0, 1, 24, 1, 1],
    [1, 1, 11, 21, 24, 11, 1, 1, 23, 21, 1],
    [1, 1, 3, 0, 23, 12, 10, 10, 10, 2, 1],
    [1, 0, 1, 1, 1, 0, 1, 21, 1, 1, 1],
]

walkablePath = list(range(2,10)) + list(range(10,18))
unlockedArea = [2]
lockedArea = [3, 4, 5, 6]

requirementLvl = {
    2: 3, #Area 2 terbuka di Level 3
    3: 5, #Area 3 terbuka di Level 5
    4: 7, #Area 4 terbuka di Level 7
    5: 9  #Area 5 terbuka di Level 9
}



#==== Ukuran Tiles
tileSize = 60

#==== Ukuran Window
w = len(petaDunia[0]) * tileSize
h = len(petaDunia) * tileSize + 60


todayDate = date.today().strftime("%d-%m-%Y")

# print(h)
#==== Setup
window = tk.Tk()
window.configure(borderwidth=0)
window.resizable(False, False)
window.title("[A05] Fishing Game!")

#==== Center the Window
xWin = (window.winfo_screenwidth() // 2) - (w // 2)
yWin = (window.winfo_screenheight() // 2) - (h // 2)
window.geometry(f"{w}x{h}+{xWin}+{yWin}")

#==== Assets
tileImgPath = {
    0 : ImageTk.PhotoImage(Image.open("image//tile//WallMushroom.png")), # Path
    1 : ImageTk.PhotoImage(Image.open("image//tile//Wall.png")), # Wall
    2 : ImageTk.PhotoImage(Image.open("image//tile//Dest.png")), # Tujuan 1
    3 : ImageTk.PhotoImage(Image.open("image//tile//Dest.png")), # Tujuan 2
    4 : ImageTk.PhotoImage(Image.open("image//tile//Dest.png")), # Tujuan 3
    5 : ImageTk.PhotoImage(Image.open("image//tile//Dest.png")), # Tujuan 4
    6 : ImageTk.PhotoImage(Image.open("image//tile//Dest.png")), # Tujuan 5
    9 : ImageTk.PhotoImage(Image.open("image//tile//Locked.png")), # Terkunci
    10 : ImageTk.PhotoImage(Image.open("image//tile//Horizontal.png")),
    11 : ImageTk.PhotoImage(Image.open("image//tile//Vertical.png")),
    12 : ImageTk.PhotoImage(Image.open("image//tile//CornerRU.png")),
    13 : ImageTk.PhotoImage(Image.open("image//tile//CornerLD.png")),
    14 : ImageTk.PhotoImage(Image.open("image//tile//CornerRD.png")),
    15 : ImageTk.PhotoImage(Image.open("image//tile//TDown.png")),
    16 : ImageTk.PhotoImage(Image.open("image//tile//TRight.png")),
    17 : ImageTk.PhotoImage(Image.open("image//tile//TLeft.png")),
    21 : ImageTk.PhotoImage(Image.open("image//tile//WallRock.png")),
    22 : ImageTk.PhotoImage(Image.open("image//tile//WallTrunk.png")),
    23 : ImageTk.PhotoImage(Image.open("image//tile//TreeB.png")),
    24 : ImageTk.PhotoImage(Image.open("image//tile//TreeU.png"))   
}

uiPath = {
    0 : ImageTk.PhotoImage(Image.open("image//ui//start_menu.png")),
    1 : ImageTk.PhotoImage(Image.open("image//ui//start_button.png")),
    2 : ImageTk.PhotoImage(Image.open("image//ui//leaderboard_button.png")),
    3 : ImageTk.PhotoImage(Image.open("image//ui//quit_button.png")),
    4 : ImageTk.PhotoImage(Image.open("image//ui//button_label.png")),
    5 : ImageTk.PhotoImage(Image.open("image//ui//enter_button.png")),
    6 : ImageTk.PhotoImage(Image.open("image//ui//back_button.png")),
    7 : ImageTk.PhotoImage(Image.open("image//ui//optimize_button.png")),
    8 : ImageTk.PhotoImage(Image.open("image//ui//level_bar.png")),
    9 : ImageTk.PhotoImage(Image.open("image//ui//back_to_menu.png")),
    10 : ImageTk.PhotoImage(Image.open("image//ui//name_input_bg.png")),
    11 : ImageTk.PhotoImage(Image.open("image//ui//name_input.png")),
    12 : ImageTk.PhotoImage(Image.open("image//ui//submit_button.png")),
    13 : ImageTk.PhotoImage(Image.open("image//ui//knapsack_ui.png")),
    14 : ImageTk.PhotoImage(Image.open("image//ui//click_area.png")),
    15 : ImageTk.PhotoImage(Image.open("image//ui//cast_button.png")),
    16 : ImageTk.PhotoImage(Image.open("image//ui//reel_button.png")),
    17 : ImageTk.PhotoImage(Image.open("image//ui//asc_button.png")),
    18 : ImageTk.PhotoImage(Image.open("image//ui//desc_button.png")),
    19 : ImageTk.PhotoImage(Image.open("image//ui//leaderboard_ui.png")),
    20 : ImageTk.PhotoImage(Image.open("image//ui//strike.png")),
    21 : ImageTk.PhotoImage(Image.open("image//ui//help_button.png")),
    22 : ImageTk.PhotoImage(Image.open("image//ui//info_button.png")),
    23 : ImageTk.PhotoImage(Image.open("image//ui//help_screen.png")),
    24 : ImageTk.PhotoImage(Image.open("image//ui//info_screen.png"))
}

sfxPath = {
    "menu" : pygame.mixer.Sound("music//menu_bgm.wav"),
    "game" : pygame.mixer.Sound("music//game_bgm.wav"),
    "click" : pygame.mixer.Sound("music//click.mp3"),
    "cast" : pygame.mixer.Sound("music//cast.wav"),
    "success" : pygame.mixer.Sound("music//catch_success.wav"),
    "fail" : pygame.mixer.Sound("music//catch_fail.wav"),
    "fstep" : pygame.mixer.Sound("music//footstep.wav"),
    "reel" : pygame.mixer.Sound("music//reel.wav"),
    "strike" : pygame.mixer.Sound("music//strike.wav"),
    "lvlup" :pygame.mixer.Sound("music//levelup.wav")
    # "cast" : pygame.mixer.Sound("music//click.mp3"),
}

fishingAreaPath = {
    1 : ImageTk.PhotoImage(Image.open("image//fishingarea//fa1.png")),
    2 : ImageTk.PhotoImage(Image.open("image//fishingarea//fa2.png")),
    3 : ImageTk.PhotoImage(Image.open("image//fishingarea//fa3.png")),
    4 : ImageTk.PhotoImage(Image.open("image//fishingarea//fa4.png")),
    5 : ImageTk.PhotoImage(Image.open("image//fishingarea//fa5.png"))
}

playerPath = ImageTk.PhotoImage(Image.open("image//char//Character.png"))



#==== Database Path
fishListPath = "database//fishList.csv"
playerRank = "database//playerRank.csv"

#==== Play Music
sfxPath["menu"].play(-1)
sfxPath["menu"].set_volume(0.2)

#==== Limit Karakter

def limitChar(text):
    if len(text) <= 11:
        return True
    else:
        return False



#===== untuk limit karakter pada nama
limitCharacter = window.register(limitChar)

#===== Untuk skor agar ikan dapat tertangkap
goalScore = 0

#===== Mode sorting
sortingMode = "asc"



#===== Fungsi untuk keluar dari game
def exitGame():
    window.destroy()

#===== Fungsi untuk memulai dari game
def startGame():
    global playerPos
    print(f"Halo {playerName}")
    
    sfxPath["menu"].stop()
    sfxPath["game"].play(-1)
    sfxPath["game"].set_volume(0.17)
    
    mainButton.config(image=uiPath[5], command=enterArea, state="disabled")
    nameCanvas.place_forget()
    startFrame.pack_forget()
    playerPos = (5, 9)
    gameFrame.place(relx=0, rely=0, anchor="nw")
    buttonCanvas.place(relx = 0, rely = 1, anchor="sw")
    homeButton.place(relx = 0.98, rely= 0.5, anchor="e")
    mainButton.place(relx = 0.5, rely=0.5, anchor="center")

    window.bind("<Key>", movePlayer)
    createMaze()
    createPlayer()
    
#===== Fungsi untuk memuat help screen
def helpScreen():
    global helpCanvas
    
    sfxPath["click"].play()
    sfxPath["click"].set_volume(0.3)
    
    helpList = ["Halo Player!, berikut beberapa pertanyaan yang mungkin bisa membantu kamu!", " ",
    "Bagaimana cara menaikkan exp?",
    "Untuk menaikan jumlah exp, player harus menyelesaikan permainan pada level tersebut dengan menangkap ikan yang memiliki bobot besar. Dengan begitu, exp akan bertambah dengan nilai yang optimal.",
    "",
    "Bagaimana cara berpindah tempat pada peta?",
    "Untuk berpindah tempat pada peta, player harus menyelesaikan level yang telah terbuka terlebih dahulu. Setelah menyelesaikan, tempat baru akan otomatis terbuka. Player hanya perlu bergerak ke atas, bawah, kanan, maupun kiri menggunakan WASD atau tombol panah hingga sampai di tempat yang baru.",
    "",
    "Bagaimana Cara Membuka Area?",
    "Untuk melanjutkan permainan ke level selanjutnya, player harus memenuhi minimum exp. Jika exp tidak memenuhi, player harus mengulang permainan lada level tersebut atau level-level sebelumnya hingga exp memenuhi.",
    "",
    "Mengapa saya tidak bisa menambahkan ikan lagi?",
    "Tas memiliki kapasitas. Tidak semua ikan yang tertangkap dapat dimasukkan ke dalam tas. Jika kapasitas tas masih tersisa, dan tidak ada ikan yang beratnya kurang dari sama dengan sisa kapasitas tas, maka player tidak bisa memasukkan ikan ke dalam tas lagi. Kemudian sisa ikan yang tidak masuk tas, akan dikembalikan ke dalam air."
  ]
    heading = [2, 5, 8, 11]

    startFrame.pack_forget()
    helpCanvas = tk.Canvas(gameFrame, width=w, height=h, background="gray", borderwidth=0)
    helpCanvas.create_image(0, 0, image=uiPath[23], anchor="nw")
    #874F45
    helpText = tk.Text(helpCanvas, width=46, height=13, background="#874F45", foreground="lightgray", borderwidth=0, wrap="word")
    helpText.tag_config("normal", justify="center", font=("Retro Pixel Cute Prop", 12))
    helpText.tag_config("heading", justify="center", font=("Retro Pixel Thick", 14))
    
    for idx, item in enumerate(helpList):
        if idx in heading:
            helpText.insert(tk.END, item + "\n", "heading")
        else:
            helpText.insert(tk.END, item + "\n", "normal")
    
    
    gameFrame.place(relx=0, rely=0, anchor="nw")
    helpCanvas.place(relx=0, rely=0, anchor="nw")
    
    buttonCanvas.place(relx = 0, rely = 1, anchor="sw")
    mainButton.config(image=uiPath[6], command=backToMenu)
    mainButton.place(relx = 0.5, rely = 0.5, anchor="center")
    mainButton["state"] = "normal"
    
    helpText.place(relx = 0.5, y=337, anchor="n")
    helpText["state"] = "disabled"

#===== Fungsi untuk memuat info screen
def infoScreen():
    global infoCanvas
    
    sfxPath["click"].play()
    sfxPath["click"].set_volume(0.3)
    
    startFrame.pack_forget()
    infoCanvas = tk.Canvas(gameFrame, width=w, height=h, background="gray", borderwidth=0)
    infoCanvas.create_image(0,0, image=uiPath[24], anchor="nw")
    
    gameFrame.place(relx=0, rely=0, anchor="nw")
    infoCanvas.place(relx=0, rely=0, anchor="nw")
    
    buttonCanvas.place(relx = 0, rely = 1, anchor="sw")
    mainButton.config(image=uiPath[6], command=backToMenu)
    mainButton.place(relx = 0.5, rely = 0.5, anchor="center")
    mainButton["state"] = "normal"
    
#===== Fungsi untuk mengubah mode sorting (asc/desc)
def sortMode():
    global sortingMode
    
    sfxPath["click"].play()
    sfxPath["click"].set_volume(0.3)
    
    if sortingMode == "asc":
        sortButton["image"] = uiPath[18]
        sortingMode = "desc"
    else:
        sortingMode = "asc"
        sortButton["image"] = uiPath[17]

#===== Fungsi untuk implementasi algoritma sorting (Selection Sort)
def selectionSort(column, colType="char", start=0):
    
    # set(itemID, column) adalah untuk mengambil value dari lboardTable dengan `ItemID` pada kolom `column`
    playerData = [(lboardTable.set(itemID, column), itemID) for itemID in lboardTable.get_children()]
    
    if colType == "char":
        if start >= len(playerData) + 20:
            return
        
        for i in range(0, len(playerData) - 1):
            minIDX = i
            for j in range(i + 1, len(playerData)):
                if playerData[j][0].isnumeric():
                    if sortingMode == "asc":
                        if int(playerData[j][0]) < int(playerData[minIDX][0]):
                            minIDX = j
                    else:
                        if int(playerData[j][0]) > int(playerData[minIDX][0]):
                            minIDX = j
                else:
                    if sortingMode == "asc":
                        if playerData[j][0] < playerData[minIDX][0]:
                            minIDX = j
                    else:
                        if playerData[j][0] > playerData[minIDX][0]:
                            minIDX = j
            if i != minIDX:
                lboardTable.move(playerData[minIDX][1], '', i)
            
        selectionSort(column, colType="char", start = start + 1)
    
    elif colType == "date":
        if start >= len(playerData) + 20:
            return
        
        for i in range(0, len(playerData) - 1):
            minIDX = i
            for j in range(i + 1, len(playerData)):
                # Untuk convert ke tipe datetime agar bisa di sort
                d1 = datetime.strptime(playerData[minIDX][0], "%d-%m-%Y")
                d2 = datetime.strptime(playerData[j][0], "%d-%m-%Y")
                
                if sortingMode == "asc":
                    if d1 > d2:
                        minIDX = j
                else:
                    if d1 < d2:
                        minIDX = j
                    
            if i != minIDX:
                lboardTable.move(playerData[minIDX][1], '', i)
            
        selectionSort(column, colType="date", start = start + 1)

#===== Fungsi untuk implementasi algoritma searching (Linear Search)
def search(event):
    typed = searchField.get()
    
    
    #Delete semua yang ada di Treeview/Tabel
    lboardTable.delete(*lboardTable.get_children())
    
    result = []
    for item in playerList:
        if typed.lower() in item[0][:len(typed)].lower():
            result.append(item)
    
    for i in result:

        lboardTable.insert('', 'end', value=(i[0], i[1], i[2]))
            
#===== Fungsi untuk menampilkan leaderboard
def leaderboard():
    global leaderboardCanvas, lboardTable, scrollbar, searchField, playerList
    
    sfxPath["click"].play()
    sfxPath["click"].set_volume(0.3)
    
    startFrame.pack_forget()
    gameFrame.place(relx=0, rely=0, anchor="nw")
    leaderboardCanvas = tk.Canvas(gameFrame, width=w, height=h, bg="gray")
    leaderboardCanvas.create_image(0, 0, image=uiPath[19], anchor="nw")
    leaderboardCanvas.place(relx=0, rely=0, anchor="nw")

    
    # Untuk konfigurasi dari treeview itu sendiri
    treeviewStyle.configure("Custom.Treeview", background="#D9A066", fieldbackground="#D9A066", font=("Retro Pixel Cute Prop", 11))
    treeviewStyle.configure("Treeview.Heading", background="#D9A066", fieldbackground="#D9A066", font=("Retro Pixel Thick", 13), padding=(2,5))
    treeviewStyle.configure("Custom.Vertical.TScrollbar", background="#D36C55", troughcolor="#D9A066")
    
    lboardTable = ttk.Treeview(leaderboardCanvas, height=23, columns = ("name", "level", "date"), show="headings", style="Custom.Treeview")
    
    scrollbar = ttk.Scrollbar(gameFrame, orient="vertical", command=lboardTable.yview, style="Custom.Vertical.TScrollbar")
    scrollbar.place(relx=0.9, rely=0.53, anchor="center", height=494)
    
    
    
    df = pd.read_csv(playerRank)
    
    playerList = df.values.tolist()

    lboardTable.configure(yscrollcommand=scrollbar.set)
    
    searchField = tk.Entry(leaderboardCanvas, width=20, font=("Perfect DOS VGA 437", 9), bg="#D9A066", justify="center")
    searchField.place(relx = 0.5, rely = 0.18, anchor="s")
    searchField.bind('<KeyRelease>', search)
    
    
    buttonCanvas.place(relx = 0, rely = 1, anchor="sw")
    mainButton.config(image=uiPath[6], command=backToMenu)
    mainButton.place(relx = 0.5, rely = 0.5, anchor="center")
    sortButton.place(relx = 0.97, rely = 0.5, anchor="e")
    mainButton["state"] = "normal"
    

    
    # Menghubungkan heading treeview, agar ketika di klik akan menjalankan command tertentu
    lboardTable.heading("name", text = "Player Name", command=lambda: selectionSort("name"))
    lboardTable.heading("level", text = "Highest Level", command=lambda: selectionSort("level"))
    lboardTable.heading("date", text = "Date Played", command=lambda: selectionSort("date","date"))
    
    lboardTable.column("name", width=172, anchor="center")
    lboardTable.column("level", width=172, anchor="center")
    lboardTable.column("date", width=172, anchor="center")
    
    lboardTable.place(relx = 0.5, rely = 0.18, anchor = "n")
    
    
    for i in range(len(playerList)):
        lboardTable.insert(parent='', index = len(playerList), values = playerList[i], iid=f"{i}")
    
#===== Fungsi untuk submit nama player
def submitName():
    global playerName
    playerName = nameInput.get()
    
    
    if not playerName:
        messagebox.showerror("Invalid Name", "Player name cannot be empty.")
    elif len(playerName) < 3:
        messagebox.showerror("Invalid Name", "Name must be more than two letters.")
    else:
        sfxPath["click"].play()
        sfxPath["click"].set_volume(0.3)
        
        nameInput.delete(0, tk.END)
        nameInput["state"] = 'readonly'
        nameInput.place_forget()
        nameCanvas.delete('all')
        startGame()

#===== Fungsi untuk membuat input nama player
def inputName():
    global playerName
    
    sfxPath["click"].play()
    sfxPath["click"].set_volume(0.3)
    
    nameCanvas.create_image(w//2, h//2, anchor="center", image=uiPath[10])
    nameCanvas.create_image(w//2, h//2, anchor="center", image=uiPath[11])
    
    nameCanvas.place(relx=0.5, rely=0.5, anchor="center")
    submitButton.place(x = 440, y = 391 ,anchor="e")
    nameInput.place(x = 410 , y = 391, anchor="e")

#===== Fungsi untuk me-reset data player
def resetPlayer():
    global playerLevel, maxExp, currExp
    playerLevel = 1
    maxExp = 250
    currExp = 0
    
    # Untuk mengubah value dari `value`, `maximum`, dan `text`
    levelBar["value"], levelBar["maximum"] = currExp, maxExp
    expLabel["text"], levelLabel["text"] = f"{currExp}/{maxExp}", playerLevel

#===== Fungsi untuk kembali ke menu
def backToMenu():
    
    df = pd.read_csv(playerRank)
    
    sfxPath["click"].play()
    sfxPath["click"].set_volume(0.3)
    
    if playerLevel != 1 and currExp != 0:
        if messagebox.askokcancel("Back To Menu", "Are you sure you want to return to the menu? All progress will be reset and your score will be saved on the leaderboard."):
            playerData = [playerName, playerLevel, todayDate]
            df.loc[len(df)] = playerData
            df.to_csv(playerRank, index=False)
            window.unbind("<Key>")
            homeButton.place_forget()
            buttonCanvas.place_forget()
            gameFrame.place_forget()
            startFrame.pack()
            nameInput["state"] = 'normal'
            
            resetPlayer()
            
    else:
        try:
            sortButton.place_forget()
            scrollbar.place_forget()
            leaderboardCanvas.place_forget()
            helpCanvas.place_forget()
            
        except:
            pass
        try:
            helpCanvas.place_forget()
        except:
            pass
        try:
            infoCanvas.place_forget()
        except:
            pass
        

        window.unbind("<Key>")
        homeButton.place_forget()
        buttonCanvas.place_forget()
        gameFrame.place_forget()
        startFrame.pack()
        nameInput["state"] = 'normal'
    
#==== Draw Maze
def createMaze():
    canvas.delete("all")
    for col in range(len(petaDunia)):
        for row in range(len(petaDunia[0])):
            tileType = tileImgPath[petaDunia[col][row]]
            x0 = row * tileSize
            y0 = col * tileSize
            if petaDunia[col][row] in lockedArea:
                canvas.create_image(x0, y0, anchor="nw", image=tileImgPath[9])
            else:
                canvas.create_image(x0, y0, anchor="nw", image=tileType)
    canvas.create_image(380, 10, image=uiPath[8], anchor="nw")
    
#==== Fungsi untuk membuat player
def createPlayer():
    x = playerPos[0] * tileSize
    y = playerPos[1] * tileSize
    canvas.create_image(x, y, anchor="nw", image=playerPath)

#==== Fungsi agar player dapat bergerak
def movePlayer(event):
    global playerPos
    playerRow, playerCol = playerPos
    sfxPath["fstep"].set_volume(0.3)
    if (event.keysym == "w" or event.keysym == "Up") and petaDunia[playerCol - 1][playerRow] in walkablePath:
        playerCol -= 1
        sfxPath["fstep"].play()
    elif (event.keysym == "s" or event.keysym == "Down") and petaDunia[playerCol + 1][playerRow] in walkablePath:
        playerCol += 1
        sfxPath["fstep"].play()
    elif (event.keysym == "a" or event.keysym == "Left") and petaDunia[playerCol][playerRow - 1] in walkablePath:
        playerRow -= 1
        sfxPath["fstep"].play()
    elif (event.keysym == "d" or event.keysym == "Right") and petaDunia[playerCol][playerRow + 1] in walkablePath:
        playerRow += 1
        sfxPath["fstep"].play()
    playerPos = (playerRow, playerCol)
    if petaDunia[playerCol][playerRow] in range(2,10):
        mainButton["state"] = "active"
    else:
        mainButton["state"] = "disabled"
    
    

    createMaze()
    createPlayer()

#==== Fungsi untuk implementasi algoritma knapsack (Greedy 0/1)
def knapsackGreedy():
    global playerInventory, fishBarrel
    
    
    fishBarrel.sort(key=itemgetter(3), reverse=True)

    sfxPath["click"].play()
    sfxPath["click"].set_volume(0.3)

    capacity = dec(f"{inventoryCapacity}")
    fishBarrelTemp = []
    for i in fishBarrel:
        fishBarrelTemp.append(i)

    rowDelete = []
    
    for i in range(len(fishBarrel)):
        # dec() adalah untuk menghitung desimal secara tepat.
        if dec(f"{fishBarrel[i][1]}") <= capacity:
            
            capacity -= dec(f'{fishBarrel[i][1]}')

            playerInventory.append(fishBarrel[i])
            rowDelete.append(f"{i}")

    for i in rowDelete:

        fishBarrelTable.delete(i)
        
        
    capacityDisplay["text"] = f"{inventoryCapacity - capacity} / {float(inventoryCapacity)} kg"
    # capacityDisplay.update()
    
    updateTable()
    fishBarrel.clear()

    mainButton.config(image=uiPath[6], command=fishToExp)

#==== Fungsi untuk meng-update tabel
def updateTable():
    for i in range(len(playerInventory)):
        pInventoryTable.insert(parent='', index = i, values = playerInventory[i], iid={i})
 
#==== Fungsi untuk menampilkan inventory player
def inventory():
    global pInventoryTable, fishBarrelTable, fishBarrel, capacityDisplay

    knapsackCanvas.place(relx = 0, rely = 0, anchor="nw")
    knapsackCanvas.create_image(0,0, anchor="nw", image=uiPath[13])
    fishBarrelDisplay.place(relx = 0.75, rely = 0.5, anchor="center")
    inventoryDisplay.place(relx = 0.25, rely = 0.11, anchor="n")
    mainButton.config(image=uiPath[7], command=knapsackGreedy)
    
    
    capacityDisplay.place(relx = 0.25, rely = 0.88, anchor = "s")
    
    
    treeviewStyle.configure("Custom.Treeview", background="#D9A066", fieldbackground="#D9A066", font=("Retro Pixel Cute Prop", 9))
    treeviewStyle.configure("Treeview.Heading", background="#D9A066", fieldbackground="#D9A066", font=("Retro Pixel Thick", 9))
    
    #==== Tabel Fish Barrel
    fishBarrelTable = ttk.Treeview(fishBarrelDisplay, height=560, columns = ("fish", "weight", "exp", "value"), show="headings", style="Custom.Treeview")

    fishBarrelTable.column("fish", width=70, anchor="center")
    fishBarrelTable.column("weight", width=80, anchor="center")
    fishBarrelTable.column("exp", width=70, anchor="center")
    fishBarrelTable.column("value", width=73, anchor="center")
    
    fishBarrelTable.heading("fish", text = "Fish")
    fishBarrelTable.heading("weight", text = "Weight(kg)")
    fishBarrelTable.heading("exp", text = "Exp")
    fishBarrelTable.heading("value", text = "Value")
    fishBarrelTable.place(relx = 0, rely = 0, anchor="nw")
    
    
    fishBarrel.sort(key=itemgetter(3), reverse=True)
    for i in range(len(fishBarrel)):
        fishBarrelTable.insert(parent='', index = len(fishBarrel), values = fishBarrel[i], iid=f"{i}")
        
    #==== Tabel Inventory player
    pInventoryTable = ttk.Treeview(inventoryDisplay, height=560, columns = ("fish", "weight", "exp", "value"), show="headings", style="Custom.Treeview")

    pInventoryTable.column("fish", width=70, anchor="center")
    pInventoryTable.column("weight", width=80, anchor="center")
    pInventoryTable.column("exp", width=70, anchor="center")
    pInventoryTable.column("value", width=73, anchor="center")
    
    pInventoryTable.heading("fish", text = "Fish")
    pInventoryTable.heading("weight", text = "Weight(kg)")
    pInventoryTable.heading("exp", text = "Exp")
    pInventoryTable.heading("value", text = "Value")
    pInventoryTable.place(relx = 0, rely = 0, anchor="nw")
    
#==== Fungsi untuk player dapat kembali ke map/peta
def backToMap():
    try:
        fishingCanvas.place_forget()
        knapsackCanvas.delete("all")
        knapsackCanvas.place_forget()
        if randomButton.winfo_ismapped():
            randomButton.place_forget()
    except (tk.TclError, NameError):
        pass
    sfxPath["click"].play()
    sfxPath["click"].set_volume(0.3)
    if len(fishBarrel) > 0:
        inventory()
    else:
        mainButton.config(image=uiPath[5], command=enterArea)
        homeButton.place(relx = 0.98, rely= 0.5, anchor="e")
        canvas.pack()

        window.bind("<Key>", movePlayer)

#==== Fungsi untuk menampilkan area memancing sesuai dengan area
def fishingArea(area):
    global fishingCanvas, clickArea, score
    homeButton.place_forget()
    mainButton.config(image=uiPath[6], command=backToMap)
    
    score = 0
    window.unbind("<Key>")
    canvas.pack_forget()
    
    areaType = area

    spriteType = fishingAreaPath[area-1]
    fishingSprite.create_image(0, 0, anchor="nw", image=spriteType)
    fishingSprite.place(relx=0, rely=0, anchor="nw")
    fishingCanvas.place(relx=1.0, rely=0, anchor="ne")
    

    fishingProgress.place(relx=0.9, rely=0.5, anchor="center")
    
    
    clickArea.place(relx=0.47, rely=0.5, anchor="center")

#==== Fungsi untuk membuka area memancing
def unlockArea(area):
    if area in lockedArea:
        lockedArea.remove(area)
        unlockedArea.append(area)

#==== Fungsi untuk konversi ikan ke EXP
def fishToExp():
    global currExp, playerLevel, maxExp, inventoryCapacity
    try:
        fishingCanvas.place_forget()
        fishingSprite.place_forget()
        knapsackCanvas.delete("all")
        knapsackCanvas.place_forget()
        capacityDisplay.place_forget()
        print("yuhu")
        if randomButton.winfo_ismapped():
            randomButton.place_forget()
    # except (tk.TclError, NameError):
    except:
        pass
    
    sfxPath["click"].play()
    sfxPath["click"].set_volume(0.3)
    sfxPath["lvlup"].set_volume(0.5)
    
    canvas.pack()
    
    for i in playerInventory:
        print(i[-2])
        currExp += int(i[-2])
        
        # Dibawah ini adalah kondisi untuk levelup player.
        if currExp >= maxExp:
            # Jadi, ketika exp player lebih dari maksimum exp saat ini.
            if currExp > maxExp:
                # Kita bikin while loop, untuk mengantisipasi player naik level 2x atau lebih.
                while currExp > maxExp:
                    playerLevel += 1
                    inventoryCapacity += 1
                    currExp = currExp - maxExp
                    maxExp += int(maxExp * 0.20)
                    sfxPath["lvlup"].play()
                    # canvas.pack()
                    pyautogui.alert(f"You've leveled up to level {playerLevel}", "Level Up!")
                    # pyautogui.alert("")
            elif currExp == maxExp:
                playerLevel += 1
                inventoryCapacity += 1
                currExp = 0
                maxExp += int(maxExp * 0.20)
                sfxPath["lvlup"].play()
                pyautogui.alert(f"You've leveled up to level {playerLevel}", "Level Up!")
            
            # Perkondisian dibawah ini adalah untuk membuka area
            # Jadi, ketika lockedArea itu true (masih ada area yang terkunci)
            if lockedArea:
                # Kita bakal lakukan perulangan for pada requirementLvl.items()
                # .items() disini adalah untuk mendapatkan key dan value sekaligus pada dictionary dalam bentuk tuple/list.
                for area, level in requirementLvl.items():
                    # Kita bakal melakukan perulangan lagi untuk mengecek level player apakah sudah bisa unlock area berikutnya.
                    for i in range(1, playerLevel+1):
                        # Jika bisa, maka area akan terbuka dan area dihilangkan dari `lockedArea`
                        if i == level and area + 1 in lockedArea:
                            unlockArea(area+1)
                            sfxPath["lvlup"].play()
                            pyautogui.alert(f"You Unlocked Area {area+1}", "Area Unlocked")
                            # messagebox.showinfo("Area Unlocked", f"You Unlocked Area {area+1}")
            
  

    #==== Update Value
    levelBar["value"], levelBar["maximum"] = currExp, maxExp
    expLabel["text"], levelLabel["text"] = f"{currExp}/{maxExp}", playerLevel
    capacityDisplay["text"] = f"0.0 / {float(inventoryCapacity)} kg"

    playerInventory.clear()
    homeButton.place(relx = 0.98, rely= 0.5, anchor="e")
    mainButton.config(image=uiPath[5], command=enterArea)
    createMaze()
    createPlayer()
    canvas.pack()
    window.bind("<Key>", movePlayer)
            
#==== Fungsi untuk time out saat memancing ikan
def timeOut():
    global goalScore
    
    sfxPath["fail"].play()
    sfxPath["fail"].set_volume(0.3)
    
    randomButton.destroy()
    fishingProgress["value"] = 0
    goalScore = 0
    castButton.place(relx=0.5, rely=0.5, anchor="center")

#==== Fungsi untuk ketika ikan menyambar kail
def strike(interval):
    strikeLabel.place(relx = 0.5, rely= 0.5, anchor="center")
    clickArea.after(700, lambda: strikeLabel.place_forget())
    sfxPath["strike"].play()
    sfxPath["strike"].set_volume(0.2)

#==== Fungsi untuk melempar kail / memulai memancing
def castHook():
    global score, tempFish, goalScore, strikeLabel
    castButton.place_forget()
    gameIP = True
    df = pd.read_csv(fishListPath)
    currArea = petaDunia[playerPos[1]][playerPos[0]]-1

    sfxPath["cast"].play()
    sfxPath["cast"].set_volume(0.3)
    
    if goalScore == 0:
        
        # Jadi, line dibawah ini adalah untuk mendapatkan ikan dengan area tertentu.
        # Seperti di sistem basis data, ini persis seperti penggunaan `WHERE`
        areaFish = df[df["area"] == currArea].values.tolist()
        randomFish = rd.randint(0, len(areaFish)-1)
        tempFish = areaFish[randomFish][1:]
        goalScore = tempFish[-1]
    
    if gameIP:
        try:
            fishText.place_forget()
            youGot.place_forget()
        except:
            pass
        random = rd.randint(1000, 2500)
        # random = 50
        
        strikeLabel = tk.Label(clickArea, image=uiPath[20], background="#D9A066")
        
        # .after() itu untuk melakukan suatu perintah dalam interval sekian detik
        clickArea.after(random, lambda: strike(random))
       

        
       
        # strikeLabel.place_forget()
        score = 0
        fishingProgress["value"] = 0
        clickArea.after(random + 1000, randButtons)

#==== Fungsi untuk membuat tombol acak
def randButtons():
    global score, randomButton, clickArea, timeOutID
    wRandButtons = 50
    hRandButtons = 50
    wArea = clickArea.winfo_width()
    hArea = clickArea.winfo_height()
    
    xRand = rd.randint(0, wArea - wRandButtons)
    yRand = rd.randint(0, hArea - hRandButtons)
    
    randomButton = tk.Button(clickArea, command=addProgress, image=uiPath[16], background="#D9A066", borderwidth=0, activebackground="#D9A066")
    randomButton.place(x=xRand, y=yRand, width=wRandButtons, height=hRandButtons)
    
    timeOutID = clickArea.after(1500, timeOut)
    
#==== Fungsi untuk menambahkan progress pada bar memancing
def addProgress():
    global score, gameIP, clickArea, goalScore, fishBarrel, fishText, youGot
    clickArea.after_cancel(timeOutID)
    randomButton.destroy()

    sfxPath["reel"].play()
    sfxPath["reel"].set_volume(0.3)
    
    
    score += 1
    fishingProgress["value"] = score * (100 / goalScore)
    
    if score == goalScore:
        sfxPath["success"].play()
        sfxPath["success"].set_volume(0.3)
        youGot = tk.Label(fishingCanvas, text=f"Kamu dapat", font=("Perfect DOS VGA 437", 13), foreground="#E4D295", background="#874F45")
        fishText = tk.Label(fishingCanvas, text=f"{tempFish[0]}!", font=("Perfect DOS VGA 437", 13), foreground="white", background="#874F45")
        youGot.place(relx = 0.48, rely=0.759, anchor = "center")
        fishText.place(relx = 0.48, rely=0.789, anchor = "center")
        
        goalScore = 0
        fishBarrel.append(tempFish[0:4])
        print(fishBarrel)
        fishingProgress["value"] = 0
        castButton.place(relx=0.5, rely=0.5, anchor="center")
        gameIP = False
        
        
    else:
        randButtons()
        
#==== Fungsi untuk membuat player dapat memasuki area
def enterArea():
    try:
        fishText.place_forget()
        youGot.place_forget()
    except:
        pass
    sfxPath["click"].play()
    sfxPath["click"].set_volume(0.3)
    
    if petaDunia[playerPos[1]][playerPos[0]] in unlockedArea:
        castButton.place(relx=0.5, rely=0.5, anchor="center")
        fishingArea(petaDunia[playerPos[1]][playerPos[0]])
    elif petaDunia[playerPos[1]][playerPos[0]] in lockedArea:
        messagebox.showwarning("Area Terkunci", "Level Kamu Belum Cukup!")


#==== Style
style = ttk.Style()
style.theme_use("winnative")

treeviewStyle = ttk.Style()
treeviewStyle.theme_use("default")


#==== Frame untuk menu start
startFrame = tk.Frame(window)
startFrame.pack()


#==== Input Nama Player
nameCanvas = tk.Canvas(window, width=w, height=h, bg="black", highlightthickness=0)
nameInput = tk.Entry(nameCanvas, width=12, font=("VCR OSD Mono", 16), justify="center", bg="#874F45", foreground="white", relief="flat", validate="key", validatecommand=(limitCharacter, "%P"))
submitButton = tk.Button(nameCanvas, image=uiPath[12], borderwidth=0, background="#874F45", activebackground="#874F45", command=submitName)

#==== Frame untuk Game
gameFrame = tk.Frame(window, bg="#4D9262", borderwidth=0)

#==== Frame untuk button di dalam game
buttonCanvas = tk.Canvas(window, width=w, height=60, bg="gray")

#==== Object dalam menu start
startLabel = ttk.Label(startFrame, image=uiPath[0])
startLabel.pack()

startButton = tk.Button(startFrame, image=uiPath[1], command=inputName,width=385, height=82, background="#2ED6FC", borderwidth=0, activebackground="#2ED6FC")
startButton.place(relx=0.5, rely=0.625, anchor="center")

leaderboardButton = tk.Button(startFrame, image=uiPath[2], width=385, height=82, background="#2FBDFF", borderwidth=0, activebackground="#2FBDFF", command=leaderboard)
leaderboardButton.place(relx=0.5, rely=0.763, anchor="center")

quitButton = tk.Button(startFrame, image=uiPath[3], width=181, height=59, background="#2FBDFF", borderwidth=0, activebackground="#2FBDFF", command=exitGame)
quitButton.place(relx=0.5, rely=0.877, anchor="center")

helpButton = tk.Button(startFrame, image=uiPath[21], background="#2FBDFF", borderwidth=0, activebackground="#2FBDFF", command=helpScreen)
helpButton.place(relx=0.7, rely=0.877, anchor="center")

infoButton = tk.Button(startFrame, image=uiPath[22], background="#2FBDFF", borderwidth=0, activebackground="#2FBDFF", command=infoScreen)
infoButton.place(relx=0.3, rely=0.877, anchor="center")

buttonLabel = tk.Label(buttonCanvas, image=uiPath[4])
buttonLabel.place(relx=0, rely=0, anchor="nw")


#==== Fish Barrel
fishBarrel = []

#==== Player Score
score = 0

#==== Game In Progress
gameIP = False

#==== Fishing Game
wHalfCanvas = w//2
hHalfCanvas = h

fishingSprite = tk.Canvas(gameFrame, width=wHalfCanvas, height=hHalfCanvas, bg="black")

fishingCanvas = tk.Canvas(gameFrame, width=wHalfCanvas, height=hHalfCanvas, bg="gray")
fishingCanvas.create_image(0,0, image=uiPath[14], anchor="nw")
clickArea = tk.Canvas(fishingCanvas, width=250, height=250, bg="#D9A066", highlightbackground="#D9A066")

style.configure("fish.Vertical.TProgressbar", background="#84FF89", troughcolor="#C7935D")
fishingProgress = ttk.Progressbar(fishingCanvas, orient="vertical", length=250, mode="determinate", style="fish.Vertical.TProgressbar")


#==== Posisi Player
playerPos = (5, 9)

#==== Inventory Player
inventoryCapacity = 2
playerInventory = []

#==== Player Level
playerLevel = 1
maxExp = 250
currExp = 0

#===== Canvas untuk Implementasi Knapsack
knapsackCanvas = tk.Canvas(gameFrame, width=w, height=h)
fishBarrelCanvas = tk.Canvas(knapsackCanvas, width=wHalfCanvas, height=hHalfCanvas)
fishBarrelDisplay = tk.Canvas(knapsackCanvas, width=wHalfCanvas-40, height=hHalfCanvas-160)
inventoryCanvas = tk.Canvas(knapsackCanvas, width=wHalfCanvas, height=hHalfCanvas)
inventoryDisplay = tk.Canvas(knapsackCanvas, width=wHalfCanvas-40, height=hHalfCanvas-215)
capacityDisplay = tk.Label(knapsackCanvas, text=f"0 / {float(inventoryCapacity)} kg", font=("Perfect DOS VGA 437", 17), background="#D9A066")


#==== Membuat Canvas
canvas = tk.Canvas(gameFrame, width=w, height=h)
canvas.pack()

#==== Level UI
levelLabel = tk.Label(canvas, text=f"{playerLevel}", font=("VCR OSD Mono", 18), foreground="white", bg="#BB563E", padx=0, pady=0, justify="center")
levelLabel.place(relx=0.933, rely=0.055, anchor="center")

expLabel = tk.Label(canvas, text=f"{currExp}/{maxExp}", bg="#994941", foreground="white", font=("VCR OSD Mono", 11))
expLabel.place(relx=0.8, rely=0.105, anchor="center")


#==== Konfigurasi Progress Bar untuk Level
style.configure("level.Horizontal.TProgressbar", background="#84FF89", troughcolor="#C7935D", direction="reverse", thickness=25)
levelBar = ttk.Progressbar(canvas, orient="horizontal", length=195, mode="determinate", style="level.Horizontal.TProgressbar", maximum=maxExp, value=currExp)
levelBar.place(relx = 0.885, rely = 0.057, anchor="e")

#==== Home Button
homeButton = tk.Button(buttonCanvas, image=uiPath[9], command=backToMenu, background="#D9A066", activebackground="#D9A066", borderwidth=0)

#==== Main Button
mainButton = tk.Button(buttonCanvas, state="disabled", image=uiPath[5], command=enterArea, background="#D9A066", borderwidth=0, activebackground="#D9A066")

#==== Sort Mode Button
sortButton = tk.Button(buttonCanvas, image=uiPath[17], command=sortMode, background="#D9A066", borderwidth=0, activebackground="#D9A066")


#==== Cast Button
castButton = tk.Button(clickArea, command=castHook, image=uiPath[15], background="#D9A066", borderwidth=0, activebackground="#D9A066")


createMaze()
createPlayer()


window.mainloop()