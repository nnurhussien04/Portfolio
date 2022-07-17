from tkinter import *
import time
root = Tk()
root.title('Oyster Top up')
Oyster_Screen = Entry(root,width=40,font=('Arial',15))
Oyster_Screen.grid(row=0,column=1,columnspan=3,padx=10,pady=10)
TPcount = 0
def Topup():
    current = Oyster_Screen.get()
    Oyster_Screen.insert(0,'Top_up')
    global Top_up
    global Calculate
    global TPcount
    Top_up = 5
    Calculate = Top_up
    TPcount = TPcount + 1
Weekly1Count = 0
def Weekly_1():
    Oyster_Screen.insert(0,'Weekly 1')
    global Weekly_1
    global Calculate
    global Weekly1Count
    Weekly_1 = 30
    Calculate = Weekly_1
    Weekly1Count = Weekly1Count + 1
Weekly2Count = 0
def Weekly_2():
    Oyster_Screen.insert(0,'Weekly_2')
    global Weekly_2
    global Calculate
    global Weekly2Count
    Weekly_2 = 40
    Calculate = Weekly_2
    Weekly2Count = Weekly2Count + 1
STCounter1 = 0
def Single_Ticket_1():
    Oyster_Screen.insert(0,'Single_Ticket_1')
    global Single_Ticket_1
    global Calculate
    global STCounter1
    Single_Ticket_1 = 1.90
    Calculate = Single_Ticket_1
    STCounter1 = STCounter1 + 1
STCounter2 = 0
def Single_Ticket_2():
    Oyster_Screen.insert(0,'Single_Ticket_2')
    global Single_Ticket_2
    global Calculate
    global STCounter2
    Single_Ticket_2 = 2.40
    Calculate = Single_Ticket_2
    STCounter2 = STCounter2 + 1
ECCounter = 0
def Empty_Card():
    Oyster_Screen.insert(0,'EmptyCard')
    global Empty_Card
    global Calculate
    global ECCounter
    Empty_Card = 3.00
    Calculate = Empty_Card
    ECCounter = ECCounter + 1
def Clear():
    Oyster_Screen.delete(0,END)
    global TPcount
    global Weekly1Count
    global Weekly2Count
    global STCounter1
    global STCounter2
    global ECCounter
    global Cash10Counter
    global Cash20Counter
    global Cash50Counter
    global Cash100Counter
    global Cash200Counter
##    global Button11
##    global Button12
##    global ButtonDelete
##    global Button13
##    global Button10p
##    global Button14
##    global Button15
##    global Button16
##    global Button17
    global Total
    global TotalLabel
    global Card
    TPcount = 0
    Weekly1Count = 0
    Weekly2Count = 0
    STCounter1 = 0
    STCounter2 = 0
    ECCounter = 0
    Cash10Counter = 0
    Cash20Counter = 0
    Cash50Counter = 0
    Cash100Counter = 0
    Cash200Counter = 0
##    Button11['state'] = DISABLED
##    Button12['state'] = DISABLED
##    ButtonDelete['state'] = DISABLED
##    Button13['state'] = DISABLED
##    Button10p['state'] = DISABLED
##    Button14['state'] = DISABLED
##    Button15['state'] = DISABLED
##    Button16['state'] = DISABLED
##    Button17['state'] = DISABLED
    Total=0
    TotalLabel = Label(root,text = str(Total))
    TotalLabel.grid_forget()
    Card = Label(root,text='Enter PIN',padx=10,pady=10)
    Card.grid(row=0,column=0)
    Card.grid_forget()
def Calculate():
    Top_up = 5
    if Calculate == Top_up:
        Oyster_Screen.delete(0,END)
        global Top_up2
        Top_up2 = 0
        Top_up2 = TPcount * Top_up
        Oyster_Screen.insert(0,str(Top_up))
        Oyster_Screen.insert(0,'You owe')
    #Empty_Card = 3
    if Calculate == Empty_Card:
        Oyster_Screen.delete(0,END)
        global Empty_Card2
        Empty_Card2 = 0
        Empty_Card2 = ECCounter * Empty_Card
        Oyster_Screen.insert(0,str(Empty_Card2))
        Oyster_Screen.insert(0,'You owe')
    #Weekly_1 = 30
    if Calculate == Weekly_1:
        Oyster_Screen.delete(0,END)
        global Weekly1_V2
        Weekly1_V2 = 0
        Weekly1_V2 = Weekly1Count * Weekly_1
        Oyster_Screen.insert(0,str(Weekly1_V2))
        Oyster_Screen.insert(0,'You owe')
    #Weekly_2 = 40
    if Calculate == Weekly_2:
        Oyster_Screen.delete(0,END)
        global Weekly2_V2
        Weekly2_V2 = 0
        Weekly2_V2 = Weekly2Count * Weekly_2
        Oyster_Screen.insert(0,str(Weekly2_V2))
        Oyster_Screen.insert(0,'You owe')
    #Single_Ticket_1 = 1.90
    if Calculate == Single_Ticket_1:
        Oyster_Screen.delete(0,END)
        global ST1_V2
        ST1_V2 = 0
        ST1_V2 = round(STCounter1 * Single_Ticket_1,2) 
        Oyster_Screen.insert(0,str(ST1_V2))
        Oyster_Screen.insert(0,'You owe')
    #Single_Ticket_2 = 2.40
    if Calculate == Single_Ticket_2:
        Oyster_Screen.delete(0,END)
        global ST2_V2
        ST2_V2 = 0
        ST2_V2 = round(STCounter2 * Single_Ticket_2,2)
        Oyster_Screen.insert(0,str(ST2_V2))
        Oyster_Screen.insert(0,'You owe')

def Payment():
    global Top_up
    global Top_up2
    global Empty_Card
    global Empty_Card2
    global Weekly1
    global Weekly1_V2
    global Weekly2
    global Weekly2_V2
    global Single_Ticket_1
    global ST1_V2
    global ST2_V2
    global Total
    global TotalLabel
    ##global Button11
    ##global Button12
    ##global ButtonDelete
    ##global Button13
    ##global Button10p
    ##global Button14
    ##global Button15
    ##global Button16
    ##global Button17 
    #NNEntry.delete(0,END)
    Top_up = 5
    Top_up2 = TPcount * Top_up
    Empty_Card = 3
    Empty_Card2 = ECCounter * Empty_Card
    Weekly_1 = 30
    Weekly1_V2 = Weekly1Count * Weekly_1
    Weekly_2 = 40
    Weekly2_V2 = Weekly2Count * Weekly_2
    Single_Ticket_1 = 1.90
    ST1_V2 = round(STCounter1 * Single_Ticket_1,2)
    Single_Ticket_2 = 2.40
    ST2_V2 = round(STCounter2 * Single_Ticket_2,2)
    Total = round(Top_up2 + Empty_Card2 + Weekly1_V2 + Weekly2_V2 + ST1_V2 + ST2_V2,2)
    print(Total)
    #NNEntry.insert(0,str(Total))
    #NNEntry.insert(0,'In Total you owe')
    TotalLabel = Label(root,text = str(Total))
    TotalLabel.grid(row=0,column=0)
    ##Button11['state'] = NORMAL
    ##Button12['state'] = NORMAL
    ##ButtonDelete['state'] = NORMAL
    ##Button13['state'] = NORMAL
    ##Button10p['state'] = NORMAL
    ##Button14['state'] = NORMAL
    ##Button15['state'] = NORMAL
    ##Button16['state'] = NORMAL
    ##Button17['state'] = NORMAL



def New_Window():
    global NN
    global NNEntry
    global Top_up
    global Top_up2
    global Empty_Card
    global Empty_Card2
    global Weekly1
    global Weekly1_V2
    global Weekly2
    global Weekly2_V2
    global Single_Ticket_1
    global ST1_V2
    global ST2_V2
    global Total
    NN = Tk()
    NN.title('Nebil Program')
    NNEntry = Entry(NN,width=40,font=('Arial',15))
    NNEntry.grid(row=0,column=0)
    Top_up = 5
    Top_up2 = TPcount * Top_up
    Empty_Card = 3
    Empty_Card2 = ECCounter * Empty_Card
    Weekly_1 = 30
    Weekly1_V2 = Weekly1Count * Weekly_1
    Weekly_2 = 40
    Weekly2_V2 = Weekly2Count * Weekly_2
    Single_Ticket_1 = 1.90
    ST1_V2 = round(STCounter1 * Single_Ticket_1,2)
    Single_Ticket_2 = 2.40
    ST2_V2 = round(STCounter2 * Single_Ticket_2,2)
    Total = round(Top_up2 + Empty_Card2 + Weekly1_V2 + Weekly2_V2 + ST1_V2 + ST2_V2,2)
    NNEntry.insert(0,str(Total))
    NNEntry.insert(0,'You owe')
##    NNEntry.insert(0,str(Total))
##    NNEntry.insert(0,'In Total you owe')
##    Card = Label(NN,text='Enter PIN',padx=10,pady=10)
##    Card.grid(row=0,column=1)
##    UserPIN = NNEntry.get()
##    ValidPIN = re.match('[0-9]{4}',UserPIN)
##    if ValidPIN:
##        SuccessLabel = Label(NN,text='Payment Complete',padx=10,pady=10)
##        SuccessLabel.grid(row=0,column=1)
##    else:
##        SuccessLabel = Label(NN,text='Card has been denied please try again',padx=10,pady=20)
##        SuccessLabel.grid(row=0,column=1)
    CompleteCounter = 0
    def Card():
        global Card
        NNEntry.delete(0,END)
        Card = Label(NN,text='Enter PIN',padx=10,pady=10)
        Card.grid(row=0,column=1)
        CompleteCounter = 0
    def Complete():
        global Card
        Card = Label(NN,text='Enter PIN',padx=10,pady=10)
        Card.grid(row=0,column=1)
        Card.grid_forget()
        UserPIN = NNEntry.get()
        if UserPIN.isdigit() == True and len(UserPIN) == 4:
            NNEntry.delete(0,END)
            NNEntry.insert(0,'Payment Complete')
            #SuccessLabel = Label(NN,text='Payment Complete',padx=10,pady=10)
            #SuccessLabel.grid(row=0,column=0)
            Button11 = Button(NN,text='Card',padx=20,pady=20,command = Card)
            Button11.grid(column=1,row=1)
            Button12 = Button(NN,text='Complete',padx=20,pady=20,command=Complete)
            Button12.grid(column=2,row=1)
            ButtonDelete= Button(NN,text='Cancel',padx=20,pady=20,command=Delete)
            ButtonDelete.grid(column=3,row=1)
            Button10p = Button(NN,text='10p',padx=20,pady=20 ,command = CashTen)
            Button10p.grid(column=1,row=2)
            Button13 = Button(NN,text ='20p',padx=20,pady=20,command = CashTwenty)
            Button13.grid(column=2,row=2)
            Button14 = Button(NN,text='50p',padx=20,pady=20 ,command = CashFifty)
            Button14.grid(column=3,row=2)
            Button15 = Button(NN,text='£1',padx=20,pady=20,command = CashHundred)
            Button15.grid(column=1,row=3)
            Button16 = Button(NN,text='£2',padx=20,pady=20 ,command = CashTwohundred)
            Button16.grid(column=2,row=3)
            Button17 = Button(NN,text='Done',padx=20,pady=20 ,command = Done)
            Button17.grid(column=3,row=3)
            Button11['state'] = DISABLED
            Button12['state'] = DISABLED
            ButtonDelete['state'] = DISABLED
            Button13['state'] = DISABLED
            Button10p['state'] = DISABLED
            Button14['state'] = DISABLED
            Button15['state'] = DISABLED
            Button16['state'] = DISABLED
            Button17['state'] = DISABLED
        else:
            NNEntry.delete(0,END)
            NNEntry.insert(0,'Card has been denied, try again')
            #SuccessLabel = Label(NN,text='Card has been denied please try again',padx=10,pady=20)
            #SuccessLabel.grid(row=0,column=0)
            #Oyster_Screen.delete(0,END)
        CompleteCounter = 0
#print(Oyster_Screen.get())    
    global Cash10Counter    
    Cash10Counter = 0
    def CashTen():
        NNEntry.delete(0,END)
        NNEntry.insert(0,'10p')
        global Cash10
        global Cash10Counter
        global Total10
        Cash10 = 0.10
        Cash10Counter = Cash10Counter+1
        Total10 = Cash10 * Cash10Counter
    global Cash20Counter 
    Cash20Counter = 0
    def CashTwenty():
        NNEntry.delete(0,END)
        NNEntry.insert(0,'20p')
        global Cash20
        global Cash20Counter
        global Total20
        Cash20 = 0.20
        Cash20Counter = Cash20Counter +1
        Total20 = Cash20 * Cash20Counter
    global Cash50Counter
    Cash50Counter = 0
    def CashFifty():
        NNEntry.delete(0,END)
        NNEntry.insert(0,'50p')
        global Cash50
        global Cash50Counter
        global Total50
        Cash50 = 0.50
        Cash50Counter = Cash50Counter + 1
        Total50 = Cash50 * Cash50Counter
    global Cash100Counter
    Cash100Counter = 0
    def CashHundred():
        NNEntry.delete(0,END)
        NNEntry.insert(0,'£1')
        global Cash100
        global Cash100Counter
        global Total100
        Cash100 = 1.00
        Cash100Counter = Cash100Counter + 1
        Total100 = Cash100 * Cash100Counter
    global Cash200Counter
    Cash200Counter = 0
    def CashTwohundred():
        NNEntry.delete(0,END)
        NNEntry.insert(0,'£2')
        global Cash200
        global Cash200Counter
        global Total200
        Cash200 = 2.00
        Cash200Counter = Cash200Counter + 1
        Total200 = Cash200 * Cash200Counter
    def Done():
        NNEntry.delete(0,END)
        global Cash10Counter
        global Cash20Counter
        global Cash50Counter
        global Cash100Counter
        global Cash200Counter
        global Total10
        global Total20
        global Total50
        global Total100
        global Total200
        global CashTotal
        global Total
        Cash10 = 0.10
        Total10 = Cash10 * Cash10Counter
        Cash20 = 0.20
        Total20 = Cash20 * Cash20Counter
        Cash50 = 0.50
        Total50 = Cash50 * Cash50Counter
        Cash100 = 1.00
        Total100 = Cash100 * Cash100Counter
        Cash200 = 2.00
        Total200 = Cash200 * Cash200Counter
        CashTotal = Total10 + Total20 + Total50 + Total100 + Total200
        if CashTotal == Total:
##            global TPcount
##            global Weekly1Count
##            global Weekly2Count
##            global STCounter1
##            global STCounter2
##            global ECCounter
##            global Cash10Counter
##            global Cash20Counter
##            global Cash50Counter
##            global Cash100Counter
##            global Cash200Counter
##            global Total
            NNEntry.insert(0,'Payment Complete')
            TPcount = 0
            Weekly1Count = 0
            Weekly2Count = 0
            STCounter1 = 0
            STCounter2 = 0
            ECCounter = 0
            Cash10Counter = 0
            Cash20Counter = 0
            Cash50Counter = 0
            Cash100Counter = 0
            Cash200Counter = 0
            Total = 0
            Button11 = Button(NN,text='Card',padx=20,pady=20,command = Card)
            Button11.grid(column=1,row=1)
            Button12 = Button(NN,text='Complete',padx=20,pady=20,command=Complete)
            Button12.grid(column=2,row=1)
            ButtonDelete= Button(NN,text='Cancel',padx=20,pady=20,command=Delete)
            ButtonDelete.grid(column=3,row=1)
            Button10p = Button(NN,text='10p',padx=20,pady=20 ,command = CashTen)
            Button10p.grid(column=1,row=2)
            Button13 = Button(NN,text ='20p',padx=20,pady=20,command = CashTwenty)
            Button13.grid(column=2,row=2)
            Button14 = Button(NN,text='50p',padx=20,pady=20 ,command = CashFifty)
            Button14.grid(column=3,row=2)
            Button15 = Button(NN,text='£1',padx=20,pady=20,command = CashHundred)
            Button15.grid(column=1,row=3)
            Button16 = Button(NN,text='£2',padx=20,pady=20 ,command = CashTwohundred)
            Button16.grid(column=2,row=3)
            Button17 = Button(NN,text='Done',padx=20,pady=20 ,command = Done)
            Button17.grid(column=3,row=3)
            Button11['state'] = DISABLED
            Button12['state'] = DISABLED
            ButtonDelete['state'] = DISABLED
            Button13['state'] = DISABLED
            Button10p['state'] = DISABLED
            Button14['state'] = DISABLED
            Button15['state'] = DISABLED
            Button16['state'] = DISABLED
            Button17['state'] = DISABLED
            
        elif CashTotal > Total:
            Change = round(CashTotal - Total,2)
            text = 'Your Change:' + str(Change)
            NNEntry.insert(0,text)
##            global TPcount
##            global Weekly1Count
##            global Weekly2Count
##            global STCounter1
##            global STCounter2
##            global ECCounter
##            global Cash10Counter
##            global Cash20Counter
##            global Cash50Counter
##            global Cash100Counter
##            global Cash200Counter
##            global Total
            TPcount = 0
            Weekly1Count = 0
            Weekly2Count = 0
            STCounter1 = 0
            STCounter2 = 0
            ECCounter = 0
            Cash10Counter = 0
            Cash20Counter = 0
            Cash50Counter = 0
            Cash100Counter = 0
            Cash200Counter = 0
            Total = 0
            Button11 = Button(NN,text='Card',padx=20,pady=20,command = Card)
            Button11.grid(column=1,row=1)
            Button12 = Button(NN,text='Complete',padx=20,pady=20,command=Complete)
            Button12.grid(column=2,row=1)
            ButtonDelete= Button(NN,text='Cancel',padx=20,pady=20,command=Delete)
            ButtonDelete.grid(column=3,row=1)
            Button10p = Button(NN,text='10p',padx=20,pady=20 ,command = CashTen)
            Button10p.grid(column=1,row=2)
            Button13 = Button(NN,text ='20p',padx=20,pady=20,command = CashTwenty)
            Button13.grid(column=2,row=2)
            Button14 = Button(NN,text='50p',padx=20,pady=20 ,command = CashFifty)
            Button14.grid(column=3,row=2)
            Button15 = Button(NN,text='£1',padx=20,pady=20,command = CashHundred)
            Button15.grid(column=1,row=3)
            Button16 = Button(NN,text='£2',padx=20,pady=20 ,command = CashTwohundred)
            Button16.grid(column=2,row=3)
            Button17 = Button(NN,text='Done',padx=20,pady=20 ,command = Done)
            Button17.grid(column=3,row=3)
            Button11['state'] = DISABLED
            Button12['state'] = DISABLED
            ButtonDelete['state'] = DISABLED
            Button13['state'] = DISABLED
            Button10p['state'] = DISABLED
            Button14['state'] = DISABLED
            Button15['state'] = DISABLED
            Button16['state'] = DISABLED
            Button17['state'] = DISABLED
        else:
            text = 'Not enough, you only added' + str(CashTotal) + '' + 'add more'
            NNEntry.insert(0,text)


    def Delete():
        NNEntry.delete(0,END)
        global CashTotal
        global Total10
        global Total20
        global Total50
        global Total100
        global Total200
        text = 'You are being returned your money'
        NNEntry.insert(0,text)
        CashTotal = 0
        Total10 = 0
        Total20 = 0
        Total50 = 0
        Total100 = 0
        Total200 = 0
    Button11 = Button(NN,text='Card',padx=20,pady=20,command = Card)
    Button11.grid(column=1,row=1)
    Button12 = Button(NN,text='Complete',padx=20,pady=20,command=Complete)
    Button12.grid(column=2,row=1)
    ButtonDelete= Button(NN,text='Cancel',padx=20,pady=20,command=Delete)
    ButtonDelete.grid(column=3,row=1)
    Button10p = Button(NN,text='10p',padx=20,pady=20 ,command = CashTen)
    Button10p.grid(column=1,row=2)
    Button13 = Button(NN,text ='20p',padx=20,pady=20,command = CashTwenty)
    Button13.grid(column=2,row=2)
    Button14 = Button(NN,text='50p',padx=20,pady=20 ,command = CashFifty)
    Button14.grid(column=3,row=2)
    Button15 = Button(NN,text='£1',padx=20,pady=20,command = CashHundred)
    Button15.grid(column=1,row=3)
    Button16 = Button(NN,text='£2',padx=20,pady=20 ,command = CashTwohundred)
    Button16.grid(column=2,row=3)
    Button17 = Button(NN,text='Done',padx=20,pady=20 ,command = Done)
    Button17.grid(column=3,row=3)
    ##Button18 = Button(root,text = 'Window', padx=10,pady=10, command = New_Window).grid(row = 9,column=9)
##    Button11['state'] = DISABLED
##    Button12['state'] = DISABLED
##    ButtonDelete['state'] = DISABLED
##    Button10p['state'] = DISABLED
##    Button13['state'] = DISABLED
##    Button14['state'] = DISABLED
##    Button15['state'] = DISABLED
##    Button16['state'] = DISABLED
##    Button17['state'] = DISABLED

##def New_Window():
##    NN = Tk()
##    NN.title('Nebil Program')
##    NNEntry = Entry(NN,width=40,font=('Arial',20))
##    NNEntry.grid(row=0,column=0)
##    Card = Label(NN,text='Enter PIN',padx=10,pady=10)
##    Card.grid(row=0,column=1)
##    UserPIN = NNEntry.get()
##    ValidPIN = re.match('[0-9]{4}',UserPIN)
##    if ValidPIN:
##        SuccessLabel = Label(NN,text='Payment Complete',padx=10,pady=10)
##        SuccessLabel.grid(row=0,column=1)
##    else:
##        SuccessLabel = Label(NN,text='Card has been denied please try again',padx=10,pady=20)
##        SuccessLabel.grid(row=0,column=1)
    




##global Button11
##global Button12
##global ButtonDelete
##global Button10p
##global Button13
##global Button14
##global Button15
##global Button16
##global Button17
Button1 = Button(root,text='Top up',padx=20,pady=20, command = Topup)
Button1.grid(column=0, row=2,)
Button2 = Button(root,text='Weekly_1',padx=20,pady=20, command =Weekly_1)
Button2.grid(column=0, row=3)
Button3 = Button(root,text='Weekly_2',padx=20,pady=20, command = Weekly_2)
Button3.grid(column=0, row=4)
Button4 = Button(root,text='Single_Ticket_1',padx=20,pady=20, command = Single_Ticket_1)
Button4.grid(column=1, row=2)
Button5 = Button(root,text='Single_Ticket_2',padx=20,pady=20, command = Single_Ticket_2)
Button5.grid(column=1, row=3)
Button6 = Button(root,text='Empty Card',padx=20,pady=20, command = Empty_Card)
Button6.grid(column=1, row=4)
Button8 = Button(root,text='Clear',padx=20,pady=20, command = Clear)
Button8.grid(column=2, row=2)
Button9 = Button(root,text='Finish',padx=20,pady=20, command = Calculate)
Button9.grid(column=2, row=3)
Button10 = Button(root,text='Pay',padx=20,pady=20, command = New_Window)
Button10.grid(column=2, row=4)
##Button11 = Button(NN,text='Card',padx=20,pady=20 ,command = Card)
##Button11.grid(column=3,row=2)
##Button12 = Button(NN,text='Complete',padx=20,pady=20,command=Complete)
##Button12.grid(column=3,row=3)
##ButtonDelete= Button(NN,text='Cancel',padx=20,pady=20,command=Delete)
##ButtonDelete.grid(column=3,row=4)
##Button10p = Button(NN,text='10p',padx=20,pady=20 ,command = CashTen)
##Button10p.grid(column=4,row=2)
##Button13 = Button(NN,text ='20p',padx=20,pady=20,command = CashTwenty)
##Button13.grid(column=4,row=3)
##Button14 = Button(NN,text='50p',padx=20,pady=20 ,command = CashFifty)
##Button14.grid(column=4,row=4)
##Button15 = Button(NN,text='£1',padx=20,pady=20,command = CashHundred)
##Button15.grid(column=5,row=2)
##Button16 = Button(NN,text='£2',padx=20,pady=20 ,command = CashTwohundred)
##Button16.grid(column=5,row=3)
##Button17 = Button(NN,text='Done',padx=20,pady=20 ,command = Done)
##Button17.grid(column=5,row=4)
####Button18 = Button(root,text = 'Window', padx=10,pady=10, command = New_Window).grid(row = 9,column=9)
##Button11['state'] = DISABLED
##Button12['state'] = DISABLED
##ButtonDelete['state'] = DISABLED
##Button10p['state'] = DISABLED
##Button13['state'] = DISABLED
##Button14['state'] = DISABLED
##Button15['state'] = DISABLED
##Button16['state'] = DISABLED
##Button17['state'] = DISABLED


root.mainloop()
