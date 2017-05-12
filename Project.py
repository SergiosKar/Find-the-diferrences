import wx
import os

class App(wx.App):
    def OnInit(self):
        frame=FindTheDifferences(None,-1,'FindTheDifferences')
        frame.Show(True)
        self.SetTopWindow(frame)
        return True

score=0;counter=0;timerr=121;isPaused=False;isStarted=True

class FindTheDifferences(wx.Frame):
    
    def __init__(self,parent,id,title):
        
        wx.Frame.__init__(self,parent,id,title,size=(900,700),style=wx.DEFAULT_FRAME_STYLE^(wx.MAXIMIZE_BOX|wx.CLOSE_BOX|wx.RESIZE_BORDER))
        self.Center()

        bmp = wx.Bitmap('splash_img.png', wx.BITMAP_TYPE_PNG)
        self.splash = ProgressSplashScreen(bmp,
                                           wx.SPLASH_CENTRE_ON_SCREEN|\
                                           wx.SPLASH_NO_TIMEOUT, -1, self)
        self.splash.Show()
        self.panel = wx.Panel(self)
        

        # Simulate long startup time
        for x in range(1, 11):
            self.splash.SetProgress(x * 10)
            wx.Sleep(1)
        self.splash.Destroy()

        

        self.startmenu=wx.Panel(self.panel)
        self.helpPanel=wx.Panel(self.panel)
        
        self.newgamePanel=wx.Panel(self.panel)
        
        
        self.timer=wx.Timer(self,id=-1)
        
       
        soundfilename =os.path.abspath("./music.wav")
        self.sound = wx.Sound(soundfilename)
        

        self.mainmenu()
        self.helpmenu()

        self.newgamemenu()
        
        wx.FutureCall(1000,self.aas)

    def aas(self):
        askaboutsound=wx.MessageDialog(None,'Do you want music?','Music',wx.YES_NO)
        answer=askaboutsound.ShowModal()
        if answer == wx.ID_YES:
            self.sound.Play(wx.SOUND_ASYNC|wx.SOUND_LOOP)

        askaboutsound.Destroy()
        
        
    def mainmenu(self):
        sizer = wx.GridBagSizer(7,3)
    
        self.newgame=wx.Button(self.startmenu,label='New Game',size=(300,75))
        self.newgame.Bind(wx.EVT_BUTTON,self.newgameme)
        self.newgame.SetBackgroundColour(wx.Colour(20, 46, 122))
        self.newgame.SetForegroundColour(wx.Colour(255, 0, 0))
        self.newgame.SetFont(wx.Font(14, wx.MODERN, wx.ITALIC, wx.BOLD, 0, "Bookman Old Style"))
        sizer.Add(self.newgame,pos=(1,1),flag=wx.LEFT|wx.RIGHT,border=250)
        


        helpm=wx.Button(self.startmenu,label='Help',size=(300,75))
        helpm.Bind(wx.EVT_BUTTON,self.helpme)
        helpm.SetBackgroundColour(wx.Colour(20, 46, 122))
        helpm.SetForegroundColour(wx.Colour(255, 0, 0))
        helpm.SetFont(wx.Font(14, wx.MODERN, wx.ITALIC, wx.BOLD, 0, "Bookman Old Style"))
        sizer.Add(helpm,pos=(3,1),flag=wx.LEFT|wx.RIGHT,border=250)
        

        
        self.loadgame=wx.Button(self.startmenu,label='Load game',size=(300,75))
        self.loadgame.Bind(wx.EVT_BUTTON,self.Loadgame)
        self.loadgame.SetBackgroundColour(wx.Colour(20, 46, 122))
        self.loadgame.SetForegroundColour(wx.Colour(255, 0, 0))
        self.loadgame.SetFont(wx.Font(14, wx.MODERN, wx.ITALIC, wx.BOLD, 0, "Bookman Old Style"))
        self.loadgame.Disable()
        sizer.Add(self.loadgame,pos=(5,1),flag=wx.LEFT|wx.RIGHT,border=250)

        exitgame=wx.Button(self.startmenu,label='Exit Game',size=(300,75))
        exitgame.Bind(wx.EVT_BUTTON,self.exitgamemenu)
        exitgame.SetBackgroundColour(wx.Colour(20, 46, 122))
        exitgame.SetForegroundColour(wx.Colour(255, 0, 0))
        exitgame.SetFont(wx.Font(14, wx.MODERN, wx.ITALIC, wx.BOLD, 0, "Bookman Old Style"))
        sizer.Add(exitgame,pos=(7,1),flag=wx.LEFT|wx.RIGHT,border=250)

        

        self.startmenu.SetSizerAndFit(sizer)


       
        
    def newgamemenu(self):
        
        
        
        #Image1
        img_path1=os.path.abspath("1/1.png")
        bitmap1=wx.Bitmap(img_path1,type=wx.BITMAP_TYPE_PNG)
        self.bitmap1=wx.StaticBitmap(self.newgamePanel,pos=(100,80),bitmap=bitmap1)    
        #Image2
        img_path2=os.path.abspath("2/2.png")
        bitmap2=wx.Bitmap(img_path2,type=wx.BITMAP_TYPE_PNG)
        self.bitmap2=wx.StaticBitmap(self.newgamePanel,pos=(100,80),bitmap=bitmap2)
        self.bitmap2.Hide()
        #Image3
        img_path3=os.path.abspath("3/3.png")
        bitmap3=wx.Bitmap(img_path3,type=wx.BITMAP_TYPE_PNG)
        self.bitmap3=wx.StaticBitmap(self.newgamePanel,pos=(100,80),bitmap=bitmap3)
        self.bitmap3.Hide()
        #Image4
        img_path4=os.path.abspath("4/4.png")
        bitmap4=wx.Bitmap(img_path4,type=wx.BITMAP_TYPE_PNG)
        self.bitmap4=wx.StaticBitmap(self.newgamePanel,pos=(100,80),bitmap=bitmap4)
        self.bitmap4.Hide()

        self.Images=[self.bitmap1,self.bitmap2,self.bitmap3,self.bitmap4]
        self.DifferencesList=[4,4,5,6]
        #Bitmaps Image1
        imageFile11="1/Bitmap1.png"
        image11=wx.Image(imageFile11,wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        self.button11=wx.BitmapButton(self.bitmap1,id=-1,bitmap=image11,pos=(403,247),size=(image11.GetWidth(),image11.GetHeight()))
        self.button11.Bind(wx.EVT_BUTTON,self.button_click)
        
        imageFile12="1/Bitmap2.png"
        image12=wx.Image(imageFile12,wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        self.button12=wx.BitmapButton(self.bitmap1,id=-1,bitmap=image12,pos=(548,57),size=(image12.GetWidth(),image12.GetHeight()))
        self.button12.Bind(wx.EVT_BUTTON,self.button_click)
         
        imageFile13="1/Bitmap3.png"
        image13=wx.Image(imageFile13,wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        self.button13=wx.BitmapButton(self.bitmap1,id=-1,bitmap=image13,pos=(549, 5),size=(image13.GetWidth(),image13.GetHeight()))
        self.button13.Bind(wx.EVT_BUTTON,self.button_click)
        
        imageFile14="1/Bitmap4.png"
        image14=wx.Image(imageFile14,wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        self.button14=wx.BitmapButton(self.bitmap1,id=-1,bitmap=image14,pos=(615,98),size=(image14.GetWidth(),image14.GetHeight()))
        self.button14.Bind(wx.EVT_BUTTON,self.button_click)

        #Bitmaps Image2
        imageFile21="2/Bitmap1.png"
        image21=wx.Image(imageFile21,wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        self.button21=wx.BitmapButton(self.bitmap2,id=-1,bitmap=image21,pos=(349,235),size=(image21.GetWidth(),image21.GetHeight()))
        self.button21.Bind(wx.EVT_BUTTON,self.button_click)
        
        imageFile22="2/Bitmap2.png"
        image22=wx.Image(imageFile22,wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        self.button22=wx.BitmapButton(self.bitmap2,id=-1,bitmap=image22,pos=(513,62),size=(image22.GetWidth(),image22.GetHeight()))
        self.button22.Bind(wx.EVT_BUTTON,self.button_click)
         
        imageFile23="2/Bitmap3.png"
        image23=wx.Image(imageFile23,wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        self.button23=wx.BitmapButton(self.bitmap2,id=-1,bitmap=image23,pos=(558,371),size=(image23.GetWidth(),image23.GetHeight()))
        self.button23.Bind(wx.EVT_BUTTON,self.button_click)
        
        imageFile24="2/Bitmap4.png"
        image24=wx.Image(imageFile24,wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        self.button24=wx.BitmapButton(self.bitmap2,id=-1,bitmap=image24,pos=(580,17),size=(image24.GetWidth(),image24.GetHeight()))
        self.button24.Bind(wx.EVT_BUTTON,self.button_click)

        #Bitmaps Image3
        imageFile31="3/Bitmap1.png"
        image31=wx.Image(imageFile31,wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        self.button31=wx.BitmapButton(self.bitmap3,id=-1,bitmap=image31,pos=(429,90),size=(image31.GetWidth(),image31.GetHeight()))
        self.button31.Bind(wx.EVT_BUTTON,self.button_click)
        
        imageFile32="3/Bitmap2.png"
        image32=wx.Image(imageFile32,wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        self.button32=wx.BitmapButton(self.bitmap3,id=-1,bitmap=image32,pos=(534,3),size=(image32.GetWidth(),image32.GetHeight()))
        self.button32.Bind(wx.EVT_BUTTON,self.button_click)
         
        imageFile33="3/Bitmap3.png"
        image33=wx.Image(imageFile33,wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        self.button33=wx.BitmapButton(self.bitmap3,id=-1,bitmap=image33,pos=(522,393),size=(image33.GetWidth(),image33.GetHeight()))
        self.button33.Bind(wx.EVT_BUTTON,self.button_click)
        
        imageFile34="3/Bitmap4.png"
        image34=wx.Image(imageFile34,wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        self.button34=wx.BitmapButton(self.bitmap3,id=-1,bitmap=image34,pos=(601,224),size=(image34.GetWidth(),image34.GetHeight()))
        self.button34.Bind(wx.EVT_BUTTON,self.button_click)

        imageFile35="3/Bitmap5.png"
        image35=wx.Image(imageFile35,wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        self.button35=wx.BitmapButton(self.bitmap3,id=-1,bitmap=image35,pos=(643,360),size=(image35.GetWidth(),image35.GetHeight()))
        self.button35.Bind(wx.EVT_BUTTON,self.button_click)

        #Bitmaps Image4
        imageFile41="4/Bitmap1.png"
        image41=wx.Image(imageFile41,wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        self.button41=wx.BitmapButton(self.bitmap4,id=-1,bitmap=image41,pos=(355,225),size=(image41.GetWidth(),image41.GetHeight()))
        self.button41.Bind(wx.EVT_BUTTON,self.button_click)
        
        imageFile42="4/Bitmap2.png"
        image42=wx.Image(imageFile42,wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        self.button42=wx.BitmapButton(self.bitmap4,id=-1,bitmap=image42,pos=(442,212),size=(image42.GetWidth(),image42.GetHeight()))
        self.button42.Bind(wx.EVT_BUTTON,self.button_click)
         
        imageFile43="4/Bitmap3.png"
        image43=wx.Image(imageFile43,wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        self.button43=wx.BitmapButton(self.bitmap4,id=-1,bitmap=image43,pos=(468,324),size=(image43.GetWidth(),image43.GetHeight()))
        self.button43.Bind(wx.EVT_BUTTON,self.button_click)
        
        imageFile44="4/Bitmap4.png"
        image44=wx.Image(imageFile44,wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        self.button44=wx.BitmapButton(self.bitmap4,id=-1,bitmap=image44,pos=(501,180),size=(image44.GetWidth(),image44.GetHeight()))
        self.button44.Bind(wx.EVT_BUTTON,self.button_click)

        imageFile45="4/Bitmap5.png"
        image45=wx.Image(imageFile45,wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        self.button45=wx.BitmapButton(self.bitmap4,id=-1,bitmap=image45,pos=(556,140),size=(image45.GetWidth(),image45.GetHeight()))
        self.button45.Bind(wx.EVT_BUTTON,self.button_click)

        imageFile46="4/Bitmap6.png"
        image46=wx.Image(imageFile46,wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        self.button46=wx.BitmapButton(self.bitmap4,id=-1,bitmap=image46,pos=(593,249),size=(image46.GetWidth(),image46.GetHeight()))
        self.button46.Bind(wx.EVT_BUTTON,self.button_click)


        self.Bind(wx.EVT_TIMER,self.clock)
       
        self.timetext=wx.StaticText(self.newgamePanel,id=-1,label='Remaining Time: ')
        self.timetext.SetFont(wx.Font(10, wx.MODERN, wx.ITALIC, wx.BOLD, 0, "Bookman Old Style"))
        self.clock_text=wx.StaticText(self.newgamePanel,id=-1,pos=(200,0),label='')
        self.clock_text.SetFont(wx.Font(10, wx.MODERN, wx.ITALIC, wx.BOLD, 0, "Bookman Old Style"))
        self.Scoretext=wx.StaticText(self.newgamePanel,id=-1,pos=(400,0),label='Score: ')
        self.Scoretext.SetFont(wx.Font(10, wx.MODERN, wx.ITALIC, wx.BOLD, 0, "Bookman Old Style"))
        self.score_text=wx.StaticText(self.newgamePanel,id=-1,pos=(500,0),label='')
        self.score_text.SetFont(wx.Font(10, wx.MODERN, wx.ITALIC, wx.BOLD, 0, "Bookman Old Style"))
        pausebutton=wx.Button(self.newgamePanel,label="Pause",pos=(750,0),size=(60,30))
        pausebutton.Bind(wx.EVT_BUTTON,self.pause)
        

        self.newgamePanel.Hide()


   
    
            
        
    def button_click(self,event):
        global score,counter,timerr,Images,DifferencesList
        score+=50;counter+=1;
        self.score_text.SetLabel(str(score))
        
        
        self.button_click_dis=event.GetEventObject()
        pos=self.button_click_dis.GetPosition()
        self.DrawLine(pos.x,pos.y)
        self.button_click_dis.Disable()
                
        if counter==self.DifferencesList[0] :
            timmer=0
            self.timer.Stop()
            counter=0
            timerr=121
            self.timer.Start(1000)
            self.DifferencesList.pop(0)
           
            self.Images[0].Destroy()
            self.Images.pop(0)
            if self.Images!=[]:
                self.Images[0].Show()
            else:
                self.timer.Stop()
                if score>200:self.final=wx.StaticText(self.newgamePanel,id=-1,label='\n\n\n\n\nCongratulations!!  ',pos=(350,150))
                elif score>0:self.final=wx.StaticText(self.newgamePanel,id=-1,label='\n\n\n\n\nGood Job!!  ',pos=(400,150))
                else:self.final=wx.StaticText(self.newgamePanel,id=-1,label='\n\n\n\n\nToo Bad!!  ',pos=(400,150))
                self.final.SetFont(wx.Font(14, wx.MODERN, wx.ITALIC, wx.BOLD, 0, "Bookman Old Style"))

                exitgamef=wx.Button(self.newgamePanel,label='Exit Game',size=(300,50),pos=(300,400))
                exitgamef.Bind(wx.EVT_BUTTON,self.exitgamemenu)
                exitgamef.SetBackgroundColour(wx.Colour(20, 46, 122))
                exitgamef.SetForegroundColour(wx.Colour(255, 0, 0))
                 
            
                
    def clock(self,event):
        global timerr,counter,Images,score,DifferencesList
        
        timerr-=1
        self.clock_text.SetLabel(str(timerr))
        
        if timerr==0 :

            self.timer.Stop()
            score-=200
            counter=0
            timerr=121
            self.timer.Start(1000)
            self.score_text.SetLabel(str(score))
            self.DifferencesList.pop(0)
           
            self.Images[0].Destroy()
            self.Images.pop(0)
            if self.Images!=[]:
                self.Images[0].Show()
            else:
                self.timer.Stop()
                if score>200:self.final=wx.StaticText(self.newgamePanel,id=-1,label='\n\n\n\n\nCongratulations!!  ',pos=(350,150))
                elif score>0:self.final=wx.StaticText(self.newgamePanel,id=-1,label='\n\n\n\n\nGood Job!!  ',pos=(400,150))
                else:self.final=wx.StaticText(self.newgamePanel,id=-1,label='\n\n\n\n\nToo Bad!!  ',pos=(400,150))
                self.final.SetFont(wx.Font(14, wx.MODERN, wx.ITALIC, wx.BOLD, 0, "Bookman Old Style"))
                
                exitgamef=wx.Button(self.newgamePanel,label='Exit Game',size=(300,50),pos=(300,400))
                exitgamef.Bind(wx.EVT_BUTTON,self.exitgamemenu)
                exitgamef.SetBackgroundColour(wx.Colour(20, 46, 122))
                exitgamef.SetForegroundColour(wx.Colour(255, 0, 0))
                
         
    def DrawLine(self,x,y):
        global counter
        dc =wx.ClientDC(self.Images[0])
        dc.SetTextForeground((255,0,0))
        dc.DrawText(str(counter),x-10, y-10)
        
    
        

    def pause(self,event):
        global isStarted,isPaused
        
            
        self.timer.Stop()
        self.clock_text.SetLabel('paused')
        isPaused=True
        isStarted=False
        self.remenufromnewgame(-1)
        self.newgame.Disable()
        self.loadgame.Enable()
            
    
    def Loadgame(self,event):
        global isStarted,IsPaused
        self.timer.Start(1000)
        self.clock_text.SetLabel(str(timerr))
        isStarted=True
        ispaused=False
        self.newgameme(-1)
           

        
            
    def helpmenu(self):    
        helptxt="     \n\nFind the differences \n\nbetween the two pictures.\n\nClick them to confirm \n\n on the right picture \n\nbefore the time runs out."
        self.helpPanel=wx.Panel(self.panel)
        sizer1=wx.GridBagSizer(10,3)
        close=wx.Button(self.helpPanel,label='Return to main menu',size=(300,60))
        close.SetBackgroundColour(wx.Colour(20, 46, 122))
        close.SetForegroundColour(wx.Colour(255, 0, 0))
        close.SetFont(wx.Font(14, wx.MODERN, wx.ITALIC, wx.BOLD, 0, "Bookman Old Style"))
        close.Bind(wx.EVT_BUTTON,self.remenufromhelp)
        texthelp=wx.StaticText(self.helpPanel,label=helptxt,style=wx.ALIGN_CENTER)
        texthelp.SetForegroundColour(wx.Colour(255, 0, 0))
        texthelp.SetFont(wx.Font(14, wx.MODERN, wx.ITALIC, wx.BOLD, 0, "Bookman Old Style"))
        sizer1.Add(close,pos=(8,1),flag=wx.LEFT|wx.RIGHT,border=250)
        sizer1.Add(texthelp,pos=(2,1),flag=wx.LEFT|wx.RIGHT,border=250)
        self.helpPanel.SetSizer(sizer1)
        self.helpPanel.Hide()
        self.Bind(wx.EVT_SIZE, self._onSize)
        self.remenufromhelp(-1)

        
       
      
       
       
    def helpme(self,event):
        self.helpPanel.Show()
        self.startmenu.Hide()
        self.newgamePanel.Hide()
        


    def newgameme(self,event):
        self.newgamePanel.Show()
        self.startmenu.Hide()
        self.helpPanel.Hide()
        self.timer.Start(1000)

    


    def exitgamemenu(self,event):
        self.sound.Stop()
        self.Close(True)
        
    def remenufromhelp(self,event):
        self.helpPanel.Hide()
        self.startmenu.Show()
        


    def remenufromnewgame(self,event):
        self.newgamePanel.Hide()
        self.startmenu.Show()
        self.helpPanel.Hide()
        
    

    def _onSize(self,event):
        event.Skip()
        self.helpPanel.SetSize(self.GetClientSizeTuple())
        self.newgamePanel.SetSize(self.GetClientSizeTuple())

   
class ProgressSplashScreen(wx.SplashScreen):
    def __init__(self, *args, **kwargs):
        super(ProgressSplashScreen, self).__init__(*args,
                                                   **kwargs)

        
        self.gauge = wx.Gauge(self, size=(-1, 16))

        
        rect = self.GetClientRect()
        new_size = (rect.width, 16)
        self.gauge.SetSize(new_size)
        self.SetSize((rect.width, rect.height + 16))
        self.gauge.SetPosition((0, rect.height))

    def SetProgress(self, percent):
        """Set the indicator gauges progress"""
        self.gauge.SetValue(percent)

    def GetProgress(self):
        """Get the current progress of the gauge"""
        return self.gauge.GetValue()




if __name__ == "__main__":
    App(0).MainLoop()

   
