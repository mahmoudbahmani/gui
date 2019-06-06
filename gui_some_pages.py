import tkinter as tk
from tkinter import *
import datetime
from time import strftime 
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import numpy as np
import math
#from tkinter.ttk import *   # to showing graphically button has been pressed 
import speech_recognition as sr
from matplotlib.backend_bases import MouseEvent


class Page(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

    def show(self):
        self.lift()



class main_page(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       frame22 = tk.Frame(self,bg = '#f5f2f2') # make frame inside the above box
       frame22.place(relx = 0.0,rely=0.0,relwidth=1,relheight=1)# positionin the color box
       
       lbl = Label(frame22, font = ('calibri', 50, 'bold'), 
                    background = '#f5f2f2', 
                    foreground = '#a68028') 
       lbl.place(relx=0.24,rely=0.05) 


       def quit(self):
           self.root.destroy() # special function that close the tkinter in proper way

       def voice_command():
           r = sr.Recognizer()
           r1 = sr.Recognizer()

           with sr.Microphone() as source:
              print('say somthing')
              audio = r.listen(source)
           #try:
              ab = r.recognize_google (audio)
              #print ("result:" + ab)
              if ab == "hello":
                  print ("Hi :)\nwhat should i do now?")
                  audioo = r1.listen(source)
                  ac = r1.recognize_google (audioo)
                  #print ("resut2" + ac)
                  if ac == "off":
                      print ("turn off")
                  elif ac == "turn on":
                      print("the output GPIO is at on mood")


       def time(): 
            string = strftime('%H:%M:%S %p') 
            lbl.config(text = string) 
            lbl.after(1000, time) 
       time() 

       
       photo_power = PhotoImage(file = "power.png") 
       label = Label(image=photo_power)
       label.image = photo_power # keep a reference!
       #label.pack()

       exit_button = tk.Button(frame22,text="exit",bg='red',fg='red',image=photo_power,command=self.quit)
       exit_button.place(relx=0.7,rely=0.6)


       photo_voice = PhotoImage(file = "resized.png") 
       label = Label(image=photo_voice)
       label.image = photo_voice # keep a reference!
       #label.pack()
       voice_command_button = tk.Button(frame22, text="voice command" , bg='red', fg = 'gray',image=photo_voice,command = voice_command) #button # here if instead of frame writing root buttom go to top of this box (out of color one)
       #voice_command_button = tk.Button(root,image=photo,command = voice_command)
       voice_command_button.place(relx=0.4,rely=0.6)


       
       """
       temp_label = tk.Label(frame22, text="current temperature: ",font = ('calibri', 25, 'bold'), 
                    background = '#f5f2f2', 
                    foreground = 'black') 
       temp_label.place(relx=0.0,rely=0.3)
       """
       page_pointer = tk.Label(frame22,text="-----------",font = ('calibri', 15, 'bold'), 
                    background = '#f5f2f2', 
                    foreground = 'gray') 
       page_pointer.place(relx=0.405,rely=0,relwidth=0.2,relheight=0.06)
       

    

class page_history(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       #import plot6
       


       style.use('fivethirtyeight')
       fig = plt.figure()   
       ax1 = fig.add_subplot(1,1,1) # one by on - and this is plot number one
       frame = tk.Frame(self,bg = 'silver') # make frame inside the above box
       frame.place(relx = 0.0,rely=0.0,relwidth=1,relheight=1)# positionin the color box







       def animate(i): # i = interval
           graph_data = open('samples.txt','r').read()
           lines = graph_data.split('\n')
           xs = []
           ys = []

           for line in lines:
               if len(line) > 1:# it means dont read empty lines
                   x, y=line.split(',')
                   xs.append(x)
                   ys.append(y)

                   ax1.clear()
                   ax1.plot(xs , ys)




       canvas = FigureCanvasTkAgg(fig, master=frame) #this is special widget to diplay the plot inside the tk frame
       canvas_plot = canvas.get_tk_widget()
       """
       canvas_plot.grid(   row=0, 
                    column=0, 
                    rowspan=4, 
                    columnspan=3, 
                    sticky=tk.W+tk.E+tk.N+tk.S)
       """
       page_pointer = tk.Label(frame,text="----------",font = ('calibri', 15, 'bold'), 
                    background = '#f5f2f2', 
                    foreground = 'gray') 
       page_pointer.place(relx=0.83,rely=0,relwidth=0.2,relheight=0.06)

       canvas_plot.place(relx = 0.0,rely=0.0,relwidth=1,relheight=1)

       ani = animation.FuncAnimation(fig , animate , interval=1000) # delay fr update is 300 ms = 0.3
       #plt.show()
       canvas.draw()


      



class page_setpoint(Page):
   def __init__(self, *args, **kwargs):
       Page.__init__(self, *args, **kwargs)
       label = tk.Label(self, text="This is page 3")
       label.pack(side="top", fill="both", expand=True)
       


       self._figure, self._axes, self._line = None, None, None
       self._dragging_point = None
       self._points = {}
       #self._init_plot()
      
     
       self._init_plot()

   def _init_plot(self):
      
       self._figure = plt.figure("Example plot")
       axes = plt.subplot(1, 1, 1)
       axes.set_xlim(0, 24)
       axes.set_ylim(0, 40)
       axes.grid(which="both")
       self._axes = axes

       frame_history = tk.Frame(self,bg = 'silver') # make frame inside the above box
       frame_history.place(relx = 0.0,rely=0.0,relwidth=1,relheight=1)# positionin the color box
       
       canvas = FigureCanvasTkAgg(self._figure , master=frame_history) #this is special widget to diplay the plot inside the tk frame
       canvas_plot = canvas.get_tk_widget()
       canvas_plot.place(relx = 0.0,rely=0.0,relwidth=1,relheight=1)
       axes.grid(which="both")
       

       self._figure.canvas.mpl_connect('button_press_event', self._on_click)
       self._figure.canvas.mpl_connect('button_release_event', self._on_release)
       self._figure.canvas.mpl_connect('motion_notify_event', self._on_motion)
       
       page_pointer = tk.Label(self,text="----------",font = ('calibri', 15, 'bold'), 
                    background = '#f5f2f2', 
                    foreground = 'gray') 
       page_pointer.place(relx=0,rely=0,relwidth=0.15,relheight=0.06)

       #ani = animation.FuncAnimation(self._figure , animate , interval=1000) # delay fr update is 300 ms = 0.3

       canvas.draw()
       
       

   def _update_plot(self):
       
       if not self._points:
           self._line.set_data([], [])
       else:
           x, y = zip(*sorted(self._points.items()))
           # Add new plot
           if not self._line:
               self._line, = self._axes.plot(x, y, "b", marker="o", markersize=10)
           # Update current plot
           else:
               self._line.set_data(x, y)
       self._figure.canvas.draw()

   def _add_point(self, x, y=None):

       if isinstance(x, MouseEvent):
           x, y = int(x.xdata), int(x.ydata)
           file = open("setpoints.txt","a")
           file.write("Temp:"+str(y)+","+"Hour:"+str(x)+"\n")

       self._points[x] = y
       return x, y

   def _remove_point(self, x, _):
       if x in self._points:
           self._points.pop(x)

   def _find_neighbor_point(self, event):

       distance_threshold = 3.0
       nearest_point = None
       min_distance = math.sqrt(2 * (100 ** 2))
       for x, y in self._points.items():
           distance = math.hypot(event.xdata - x, event.ydata - y)
           if distance < min_distance:
               min_distance = distance
               nearest_point = (x, y)
       if min_distance < distance_threshold:
           return nearest_point
       return None

   def _on_click(self, event):
       

       # left click
       if event.button == 1 and event.inaxes in [self._axes]:
           point = self._find_neighbor_point(event)
           if point:
               self._dragging_point = point
           else:
               self._add_point(event)
           self._update_plot()
       # right click
       elif event.button == 3 and event.inaxes in [self._axes]:
           point = self._find_neighbor_point(event)
           if point:
               self._remove_point(*point)
               self._update_plot()

   def _on_release(self, event):

       if event.button == 1 and event.inaxes in [self._axes] and self._dragging_point:
           self._dragging_point = None
           self._update_plot()

   def _on_motion(self, event):
      


       if not self._dragging_point:
           return
       if event.xdata is None or event.ydata is None:
           return
       self._remove_point(*self._dragging_point)
       self._dragging_point = self._add_point(event)
       self._update_plot()

       

       #plott = DraggablePlotExample()
           

       
      



class MainView(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
       
        p2 = page_history(self)
        p3 = page_setpoint(self)
        p1 = main_page(self)

        buttonframe = tk.Frame(self,bg="#e9f0ad")
        container = tk.Frame(self,bg="#bdc25b")
        buttonframe.pack(side="top", fill=X, pady=1, expand=False)
        container.pack(side="top", fill="both", expand=True)

        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = tk.Button(buttonframe, text="   Main page ",font=('calibri', 14, 'bold') ,command=p1.lift)
        b2 = tk.Button(buttonframe, text="   History     ",font=('calibri', 14, 'bold'), command=p2.lift)
        b3 = tk.Button(buttonframe, text="     Setpoint  ",font=('calibri', 14, 'bold'), command=p3.lift)
        p1.lift()

        b1.place(relx=0.43,rely=0.0)
        b2.pack(side="right")
        b3.pack(side="left")
        

        #p1.show()
        
       # p2.show()

        

if __name__ == "__main__":
    root = tk.Tk()
    
    main = MainView(root)
    main.pack(side="top", fill="both", expand=True)
    root.wm_geometry("600x400")
    root.mainloop()

