from constants import *

class TOVA:
    def __init__(self, debug=False):
        """
        TOVA class constructor

        Parameters
        ----------

        * debug: bool
            If True, the program will run without the eye tracker
        """
        self.screen = Screen()
        self.display = Display()
        self.tracker = EyeTracker(self.display, eyedatafile = LOGFILENAME, logfile = LOGFILE)
        self.keyboard = Keyboard()
        self.mouse = Mouse()
        self.test_id = 0
        self.debug = debug
        if not self.debug:
            self.log = Logfile(filename=LOGFILE)
        else: 
            self.log = None

    
    def setup(self):
        """
        Setup the experiment
        """
        if not self.debug:
            self.tracker.calibrate()
            self.log.write(['type', 'show_time', 'press_time', 'hide_time'])
        self.mouse.set_visible(visible=True)

    
    def run(self):
        """
        Run the experiment
        """
        self.screen.set_background_colour((0, 0, 0))
        self.display.fill()
        self.show_instructions()
        self.mix_test()
        for i in self.random_array:
            if i:
                self.target_test()
            else:
                self.non_target_test()
        if not self.debug:
            self.tracker.close()
            self.log.close()
        self.exit()

    def show_instructions(self):
        self.screen.clear()
        colocar_fondo(self.screen)
        self.screen.draw_text(text="TOVA\n\nObserva las imágenes y presional alguna tecla si es el objetivo y ninguna si no lo es.\n\nHaz click para continuar",
                              fontsize=TEXTSIZE, 
                              font = font,
                              pos = (screenwidth*0.35,screenheight*0.5),
                              colour =(0,0,0))
        self.display.fill(self.screen)
        self.display.show()
        self.wait_for_click()

    def exit(self):
        self.screen.clear()
        colocar_fondo(self.screen)
        self.screen.draw_text(text="Gracias por participar, presiona cualquier tecla para salir",
                              fontsize=TEXTSIZE, 
                              font = font,
                              pos = (screenwidth*0.35,screenheight*0.5),
                              colour =(0,0,0))
        self.display.fill(self.screen)
        self.display.show()
        self.wait_for_key()


    def wait_for_click(self, timeout=None):
        while True:
            mousebutton, _, _ = self.mouse.get_clicked()
            if mousebutton == 1:
                return True

    def wait_for_key(self, timeout=None):
        while True:
            if timeout is not None:
                key = self.keyboard.get_key(timeout=timeout)
                if key:
                    return (True if key[0] != None else False, key[1])
            if self.keyboard.get_key():
                return

    def target_test(self):
        if not self.debug:
            self.tracker.start_recording()
            self.tracker.wait_recording_ready()
            self.tracker.log("TRIALSTART %d" % self.test_id)
        self.screen.clear()
        self.screen.draw_rect(colour=(255, 255, 255), w=screenwidth*0.7, h=screenheight*0.9, fill=True)
        self.screen.draw_rect(colour=(0, 0, 0), y=screenheight*0.2, w=screenwidth*0.2, h=screenheight*0.2, fill=True)
        self.display.fill(self.screen)
        self.display.show()
        start_time = time.time()
        key_press = self.wait_for_key(timeout=3700)
        end_time = time.time()
        self.screen.clear()
        self.screen.draw_rect(colour=(0, 255, 0), w=screenwidth*0.7, h=screenheight*0.9, fill=True)
        self.display.fill(self.screen)
        self.display.show()
        if self.debug:
            print(['target', start_time, key_press[0], end_time])
            print("Reaction time %s ms" % ((end_time - start_time) * 1000))
        else:
            self.log.write(['target', start_time, key_press[0], end_time])
            self.tracker.log("TRIALEND %d" % self.test_id)
            self.tracker.stop_recording()
        time.sleep(0.2)
        self.test_id += 1

    def non_target_test(self):
        if not self.debug:
            self.tracker.start_recording()
            self.tracker.wait_recording_ready()
            self.tracker.log("TRIALSTART %d" % self.test_id)
        self.screen.clear()
        self.screen.draw_rect(colour=(255, 255, 255), w=screenwidth*0.7, h=screenheight*0.9, fill=True)
        self.screen.draw_rect(colour=(0, 0, 0), y=screenheight*0.7, w=screenwidth*0.2, h=screenheight*0.2, fill=True)
        self.display.fill(self.screen)
        self.display.show()
        start_time = time.time()
        key_press = self.wait_for_key(timeout=3700)
        end_time = time.time()
        self.screen.clear()
        self.screen.draw_rect(colour=(0, 255, 0), w=screenwidth*0.7, h=screenheight*0.9, fill=True)
        self.display.fill(self.screen)
        self.display.show()
        if self.debug:
            print(['target', start_time, key_press[0], end_time])
            print("Reaction time %s ms" % ((end_time - start_time) * 1000))
        else:
            self.log.write(['target', start_time, key_press[0], end_time])
            self.tracker.log("TRIALEND %d" % self.test_id)
            self.tracker.stop_recording()
        time.sleep(0.2)
        self.test_id += 1

    def mix_test(self):
        num_targets = 2
        num_non_targets = 5
        self.random_array = np.array([True] * num_targets + [False] * num_non_targets)
        np.random.shuffle(self.random_array)

    
tova = TOVA(debug=True)
tova.setup()
tova.run()