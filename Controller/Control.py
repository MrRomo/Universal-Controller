import pygame
import threading


class Button():

    def __init__(self, name = "N/A", value = "N/A"):
        self.name = name
        self.value = value

    def push(self):
        return self.value


class Control():
    
    def __init__(self, map):
        self.control_name = 'None'
        self.control_number = 1
        self.reload_buttons(**map)
        self.framerate = 20
        self.init_pygame()

    def init_buttons(self, buttons):
        # print(buttons)
        for i in range(len(buttons)):
            button_name = f'button_{i}'
            self.buttons.append(
                Button(button_name,buttons[i])
            )

    def init_axis(self, axis):
        # print(axis)
        for i in range(len(axis)):
            axis_array = []
            for g in range(len(axis[i])):
                axis_name = f'axis_{i}_{g}'
                axis_array.append(
                    Button(axis_name,axis[i][g])
                )
            self.axis.append(axis_array)

    def init_hats(self, hats):
        # print(hats)
        for i in range(len(hats)):
            hats_array = []
            for g in range(len(hats[i])):
                hat_name = f'hat_{i}_{g}'
                hats_array.append(
                    Button(hat_name,hats[i][g])
                )
            self.hats.append(hats_array)

    def reload_buttons(self, threshold, buttons, hats, axis):
        self.threshold = threshold
        self.buttons = []
        self.axis = []
        self.hats = []
        self.init_buttons(buttons)
        self.init_axis(axis)
        self.init_hats(hats)


    def init_pygame(self):
        threading.Thread(target=self.pygame_listener, daemon=True).start()

   
    def pygame_listener(self):
        pygame.init()
        clock = pygame.time.Clock()
        pygame.joystick.init()
        num = pygame.joystick.get_count()
        print(f"Gamepads encontrados {num}")
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
                    self.send_message(self.axis[i][0].push())
                if(axis<self.threshold*-1):
                    self.send_message(self.axis[i][1].push())

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
            
            clock.tick(90)
        pygame.quit()

    def send_message(self, message):
        print(message)
    