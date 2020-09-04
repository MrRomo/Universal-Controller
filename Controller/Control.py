import pygame
import threading
from time import sleep as delay
from functools import partial
class Button():

    def __init__(self, name, value, button_ui, ui):
        self.name = name
        self.value = value
        self.button_ui = button_ui
        self.background = self.button_ui.setStyleSheet
        self.pushing = False
        self.button_ui.clicked.connect(partial(ui.dialog.getText, self))
        
    def push(self):
        threading.Thread(target=self.color_change, daemon=True).start()
        return self.value

    def color_change(self):
        if(not (self.pushing)):
            self.pushing = True
            self.background("background-color: red")
            delay(.2)
            self.background("background-color: white")
            self.pushing = False

class Control():
    
    def __init__(self, map, ui, pub, mqtt):
        self.control_name = 'None'
        self.control_number = 1
        self.ui = ui
        self.console = pub
        self.pub_message = mqtt
        self.reload_buttons(**map)
        self.framerate = int(self.ui.frame_rate_textbox.text())
        self.ui.frame_rate_textbox.textChanged.connect(self.update_frame_rate)
        self.init_pygame()

    def update_frame_rate(self):
        try:
            self.framerate = int(self.ui.frame_rate_textbox.text())
        except:
            self.framerate = 10

    def init_buttons(self, buttons):
        for i in range(len(buttons)):
            button_name = f'button_{i}'
            button_ui = getattr(self.ui, button_name)
            button = Button(button_name,buttons[i], button_ui, self.ui)
            button_ui.clicked.connect(button.color_change)
            button.push()
            self.buttons.append(button)

    def init_axis(self, axis):
        # print(axis)
        for i in range(len(axis)):
            axis_array = []
            for g in range(len(axis[i])):
                axis_name = f'axis_{i}_{g}'
                axis_ui = getattr(self.ui, axis_name)
                button = Button(axis_name,axis[i][g], axis_ui, self.ui)
                button.push()
                axis_array.append(button)
            self.axis.append(axis_array)

    def init_hats(self, hats):
        # print(hats)
        for i in range(len(hats)):
            hats_array = []
            for g in range(len(hats[i])):
                hat_name = f'hat_{i}_{g}'
                hat_ui = getattr(self.ui, hat_name)
                button = Button(hat_name, hats[i][g], hat_ui, self.ui)
                button.push()
                hats_array.append(button)
            self.hats.append(hats_array)

    def reload_buttons(self, broker, threshold, button, hat, axis):
        self.threshold = threshold
        self.buttons = []
        self.axis = []
        self.hats = []
        threading.Thread(target=self.init_buttons, args=(button,),  daemon=True).start()
        threading.Thread(target=self.init_axis, args=(axis,),  daemon=True).start()
        threading.Thread(target=self.init_hats, args=(hat,),  daemon=True).start()

    def init_pygame(self):
        threading.Thread(target=self.pygame_listener, daemon=True).start()

   
    def pygame_listener(self):
        pygame.init()
        clock = pygame.time.Clock()
        pygame.joystick.init()
        num = pygame.joystick.get_count()
        self.console(f"Gamepads encontrados {num}\n")
        for i in  range(num):
            print(pygame.joystick.Joystick(i).get_name())
        hecho = False
        while not hecho:
              # PROCESAMIENTO DEL EVENTO
            for evento in pygame.event.get(): 
                if evento.type == pygame.QUIT: 
                    hecho = True
                
            joystick = pygame.joystick.Joystick(0)
            joystick.init()
            num_axes = joystick.get_numaxes()
            num_buttons =joystick.get_numbuttons()
            
            for i in range(num_axes):
                axis = joystick.get_axis(i)
                if(axis>self.threshold):
                    self.send_message(self.axis[i][1].push())
                if(axis<self.threshold*-1):
                    self.send_message(self.axis[i][0].push())

            for i in range(num_buttons):
                button =joystick.get_button(i)
                if(button):
                    self.send_message(self.buttons[i].push())

            hat = joystick.get_hat(0)
            for i in range(len(hat)):
                if(hat[i]>self.threshold):
                    self.send_message(self.hats[i][1].push())            
                if(hat[i]<self.threshold*-1):
                    self.send_message(self.hats[i][0].push())            
            
            clock.tick(self.framerate)
        pygame.quit()

    def send_message(self, message):
        self.console(message+'\n')
        self.pub_message(message)
    