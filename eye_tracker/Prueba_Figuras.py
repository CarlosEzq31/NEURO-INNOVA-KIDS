# Importamos todo desde el archivo constants.py
from constants import *

def Figuras_superpuestas():
    
    if sys.argv[1]:
            global id_paciente, ruta_archivo
            id_paciente = sys.argv[1]
            ruta_archivo = docs + "\\NEURO INNOVA KIDS\\PACIENTES\\"+id_paciente+f"\\{id_paciente}_{str(datetime.now().strftime('%d-%m-%y'))}.json"
            LOGFILENAME = f"{id_paciente}_figuras_{str(datetime.now().strftime('%d-%m-%y'))}"
    
    # Creamos los objetos para el eyetracker y la pantalla
    display = Display()
    pantalla = Screen()

    # Creamos los objetos para el mouse, el seguidor ocular y el teclado
    teclado = Keyboard()
    mouse = Mouse()
    eyetracker = EyeTracker(display, eyedatafile = LOGFILENAME, logfile = LOGFILENAME)
    eyetracker.calibrate()

    # Archivos de salida
    LOGFILE = os.path.join(DATADIR, LOGFILENAME)
    log = Logfile(filename = LOGFILE)
    log.write(["trialnr", "image", "imgtime"])

    # Configuramos la entrada del mouse
    mouse.set_visible(visible = True)

    # Leemos todos los nombres de la imagenes
    # images = os.listdir(IMGDIR)

    # Coloreamos la pantalla
    pantalla.set_background_colour((250, 235, 255))
    display.fill(pantalla)
    display.show()


    # Colocamos la imagen de fondo y las instrucciones en Pantalla 
    pantalla.clear()
    colocar_fondo(pantalla)
    boton_continuar = colocarBoton(pantalla, FONDODIR+"boton_verde.png", 2.5, screenwidth*0.875,screenheight*0.8, "Continuar", 1)
    pantalla.draw_text(text="Prueba de las figuras\nsuperpuestas\nObserva las figuras a la izquierda\ny selecciona la figura que NO se encuentre", 
                fontsize=TEXTSIZE, 
                font='Mukta Malar ExtraLight',
                pos = (screenwidth*0.35,screenheight*0.5),
                colour =(0,0,0))
    display.fill(pantalla)
    display.show()

    # Esperar click en el boton para continuar
    x , y = 0,0
    while True:
        mousebutton, clickpos, clicktime = mouse.get_clicked(mousebuttonlist='default', timeout= 10)
        mouseX, mouseY = mouse.get_pos()
        if clickpos:
            x,y = clickpos
            if boton_presionado(x,y, boton_continuar):
                break
        if boton_presionado(mouseX, mouseY, boton_continuar):
            colocarBoton(pantalla, 
                         FONDODIR+"verde_hover.png", 
                         2.5, 
                         screenwidth*0.875,
                         screenheight*0.8, 
                         "Continuar", 
                         1, 
                         color = (255,255,255))
        else: 
            colocarBoton(pantalla, FONDODIR+"boton_verde.png", 2.5, screenwidth*0.875,screenheight*0.8, "Continuar", 1)
        display.fill(pantalla)
        display.show()

    # Calibrar eyetracker
    # eyetracker.calibrate()
    
    # Mostrar la primer prueba 
    pantalla.clear()
    colocar_fondo(pantalla)
    boton_continuar = colocarBoton(pantalla, FONDODIR+"boton_verde.png", 2.5, screenwidth*0.875,screenheight*0.8, "Continuar", 1)
   
    pantalla.draw_image(image = FONDODIR + "\Figuras_Superpuestas\\prueba_1.jpg",
                        scale = IMGSCALE*2,
                        pos = (screenwidth*0.25,screenheight*0.5))

                           
    boton1 = colocarBoton(pantalla, FONDODIR+"\Figuras_Superpuestas\\16.png",0.6,screenwidth*0.50,screenheight*0.5)
    boton2 = colocarBoton(pantalla, FONDODIR+"\Figuras_Superpuestas\\17.png",0.6,screenwidth*0.62,screenheight*0.5)
    boton3 = colocarBoton(pantalla, FONDODIR+"\Figuras_Superpuestas\\10.jpg",0.6,screenwidth*0.75,screenheight*0.5)
    boton4 = colocarBoton(pantalla, FONDODIR+"\Figuras_Superpuestas\\8.jpg",0.6,screenwidth*0.88,screenheight*0.5)

    display.fill(pantalla)
    display.show()

    # Esperar click en el boton para continuar
    x , y = 0,0
    respuestas = {'prueba': 'figuras'}
    while True:
        mousebutton, clickpos, clicktime = mouse.get_clicked(mousebuttonlist='default', timeout= 10)
        mouseX, mouseY = mouse.get_pos()
        if clickpos:
            x,y = clickpos
            if boton_presionado(x,y, boton_continuar):
                break
            if boton_presionado(x,y,boton1):
                respuestas["1"] = False
                break
            if boton_presionado(x,y,boton2):
                respuestas["1"] = False
                break
            if boton_presionado(x,y,boton3):
                respuestas["1"] = True
                break
            if boton_presionado(x,y,boton4):
                respuestas["1"] = False
                break
        if boton_presionado(mouseX, mouseY, boton_continuar):
            colocarBoton(pantalla, 
                         FONDODIR+"verde_hover.png", 
                         2.5, 
                         screenwidth*0.875,
                         screenheight*0.8, 
                         "Continuar", 
                         1, 
                         color = (255,255,255))
        else: 
            colocarBoton(pantalla, FONDODIR+"boton_verde.png", 2.5, screenwidth*0.875,screenheight*0.8, "Continuar", 1)
        display.fill(pantalla)
        display.show()
        
    # Mostrar la segunda prueba 
    pantalla.clear()
    colocar_fondo(pantalla)
    boton_continuar = colocarBoton(pantalla, FONDODIR+"boton_verde.png", 2.5, screenwidth*0.875,screenheight*0.8, "Continuar", 1)
   
    pantalla.draw_image(image = FONDODIR + "\Figuras_Superpuestas\\prueba_2.jpg",
                        scale = IMGSCALE*2,
                        pos = (screenwidth*0.25,screenheight*0.5))

                           
    boton1 = colocarBoton(pantalla, FONDODIR+"\Figuras_Superpuestas\\1.jpg",0.6,screenwidth*0.50,screenheight*0.5)
    boton2 = colocarBoton(pantalla, FONDODIR+"\Figuras_Superpuestas\\10.jpg",0.6,screenwidth*0.62,screenheight*0.5)
    boton3 = colocarBoton(pantalla, FONDODIR+"\Figuras_Superpuestas\\16.png",0.6,screenwidth*0.75,screenheight*0.5)
    boton4 = colocarBoton(pantalla, FONDODIR+"\Figuras_Superpuestas\\8.jpg",0.6,screenwidth*0.88,screenheight*0.5)

    display.fill(pantalla)
    display.show()

    # Esperar click en el boton para continuar
    x , y = 0,0
    while True:
        mousebutton, clickpos, clicktime = mouse.get_clicked(mousebuttonlist='default', timeout= 10)
        mouseX, mouseY = mouse.get_pos()
        if clickpos:
            x,y = clickpos
            if boton_presionado(x,y, boton_continuar):
                break
            if boton_presionado(x,y,boton1):
                respuestas["2"] = True
                break
            if boton_presionado(x,y,boton2):
                respuestas["2"] = False
                break
            if boton_presionado(x,y,boton3):
                respuestas["2"] = False
                break
            if boton_presionado(x,y,boton4):
                respuestas["2"] = False
                break
        if boton_presionado(mouseX, mouseY, boton_continuar):
            colocarBoton(pantalla, 
                         FONDODIR+"verde_hover.png", 
                         2.5, 
                         screenwidth*0.875,
                         screenheight*0.8, 
                         "Continuar", 
                         1, 
                         color = (255,255,255))
        else: 
            colocarBoton(pantalla, FONDODIR+"boton_verde.png", 2.5, screenwidth*0.875,screenheight*0.8, "Continuar", 1)
        display.fill(pantalla)
        display.show()

    # Mostrar la tercer prueba 
    pantalla.clear()
    colocar_fondo(pantalla)
    boton_continuar = colocarBoton(pantalla, FONDODIR+"boton_verde.png", 2.5, screenwidth*0.875,screenheight*0.8, "Continuar", 1)
   
    pantalla.draw_image(image = FONDODIR + "\Figuras_Superpuestas\\prueba_3.jpg",
                        scale = IMGSCALE*2,
                        pos = (screenwidth*0.25,screenheight*0.5))

                           
    boton1 = colocarBoton(pantalla, FONDODIR+"\Figuras_Superpuestas\\10.jpg",0.6,screenwidth*0.50,screenheight*0.5)
    boton2 = colocarBoton(pantalla, FONDODIR+"\Figuras_Superpuestas\\1.jpg",0.6,screenwidth*0.62,screenheight*0.5)
    boton3 = colocarBoton(pantalla, FONDODIR+"\Figuras_Superpuestas\\9.jpg",0.6,screenwidth*0.75,screenheight*0.5)
    boton4 = colocarBoton(pantalla, FONDODIR+"\Figuras_Superpuestas\\4.jpg",0.6,screenwidth*0.88,screenheight*0.5)

    display.fill(pantalla)
    display.show()

    # Esperar click en el boton para continuar
    x , y = 0,0
    while True:
        mousebutton, clickpos, clicktime = mouse.get_clicked(mousebuttonlist='default', timeout= 10)
        mouseX, mouseY = mouse.get_pos()
        if clickpos:
            x,y = clickpos
            if boton_presionado(x,y, boton_continuar):
                break
            if boton_presionado(x,y,boton1):
                respuestas["3"] = False
                break
            if boton_presionado(x,y,boton2):
                respuestas["3"] = False
                break
            if boton_presionado(x,y,boton3):
                respuestas["3"] = False
                break
            if boton_presionado(x,y,boton4):
                respuestas["3"] = True
                break
        if boton_presionado(mouseX, mouseY, boton_continuar):
            colocarBoton(pantalla, 
                         FONDODIR+"verde_hover.png", 
                         2.5, 
                         screenwidth*0.875,
                         screenheight*0.8, 
                         "Continuar", 
                         1, 
                         color = (255,255,255))
        else: 
            colocarBoton(pantalla, FONDODIR+"boton_verde.png", 2.5, screenwidth*0.875,screenheight*0.8, "Continuar", 1)
        display.fill(pantalla)
        display.show()        
    
    # Mostrar la cuarta prueba 
    pantalla.clear()
    colocar_fondo(pantalla)
    boton_continuar = colocarBoton(pantalla, FONDODIR+"boton_verde.png", 2.5, screenwidth*0.875,screenheight*0.8, "Continuar", 1)
   
    pantalla.draw_image(image = FONDODIR + "\Figuras_Superpuestas\\prueba_4.jpg",
                        scale = IMGSCALE*2,
                        pos = (screenwidth*0.25,screenheight*0.5))

                           
    boton1 = colocarBoton(pantalla, FONDODIR+"\Figuras_Superpuestas\\16.png",0.6,screenwidth*0.50,screenheight*0.5)
    boton2 = colocarBoton(pantalla, FONDODIR+"\Figuras_Superpuestas\\1.jpg",0.6,screenwidth*0.62,screenheight*0.5)
    boton3 = colocarBoton(pantalla, FONDODIR+"\Figuras_Superpuestas\\10.jpg",0.6,screenwidth*0.75,screenheight*0.5)
    boton4 = colocarBoton(pantalla, FONDODIR+"\Figuras_Superpuestas\\4.jpg",0.6,screenwidth*0.88,screenheight*0.5)

    display.fill(pantalla)
    display.show()

    # Esperar click en el boton para continuar
    x , y = 0,0
    while True:
        mousebutton, clickpos, clicktime = mouse.get_clicked(mousebuttonlist='default', timeout= 10)
        mouseX, mouseY = mouse.get_pos()
        if clickpos:
            x,y = clickpos
            if boton_presionado(x,y, boton_continuar):
                break
            if boton_presionado(x,y,boton1):
                respuestas["4"] = False
                break
            if boton_presionado(x,y,boton2):
                respuestas["4"] = False
                break
            if boton_presionado(x,y,boton3):
                respuestas["4"] = False
                break
            if boton_presionado(x,y,boton4):
                respuestas["4"] = True
                break
        if boton_presionado(mouseX, mouseY, boton_continuar):
            colocarBoton(pantalla, 
                         FONDODIR+"verde_hover.png", 
                         2.5, 
                         screenwidth*0.875,
                         screenheight*0.8, 
                         "Continuar", 
                         1, 
                         color = (255,255,255))
        else: 
            colocarBoton(pantalla, FONDODIR+"boton_verde.png", 2.5, screenwidth*0.875,screenheight*0.8, "Continuar", 1)
        display.fill(pantalla)
        display.show()

    # Mostrar la quinta prueba 
    pantalla.clear()
    colocar_fondo(pantalla)
    boton_continuar = colocarBoton(pantalla, FONDODIR+"boton_verde.png", 2.5, screenwidth*0.875,screenheight*0.8, "Continuar", 1)
   
    pantalla.draw_image(image = FONDODIR + "\Figuras_Superpuestas\\prueba_5.jpg",
                        scale = IMGSCALE*2,
                        pos = (screenwidth*0.25,screenheight*0.5))

                           
    boton1 = colocarBoton(pantalla, FONDODIR+"\Figuras_Superpuestas\\5.jpg",0.6,screenwidth*0.50,screenheight*0.5)
    boton2 = colocarBoton(pantalla, FONDODIR+"\Figuras_Superpuestas\\1.jpg",0.6,screenwidth*0.62,screenheight*0.5)
    boton3 = colocarBoton(pantalla, FONDODIR+"\Figuras_Superpuestas\\10.jpg",0.6,screenwidth*0.75,screenheight*0.5)
    boton4 = colocarBoton(pantalla, FONDODIR+"\Figuras_Superpuestas\\4.jpg",0.6,screenwidth*0.88,screenheight*0.5)

    display.fill(pantalla)
    display.show()

    # Esperar click en el boton para continuar
    x , y = 0,0
    while True:
        mousebutton, clickpos, clicktime = mouse.get_clicked(mousebuttonlist='default', timeout= 10)
        mouseX, mouseY = mouse.get_pos()
        if clickpos:
            x,y = clickpos
            if boton_presionado(x,y, boton_continuar):
                break
            if boton_presionado(x,y,boton1):
                respuestas["5"] = True
                break
            if boton_presionado(x,y,boton2):
                respuestas["5"] = False
                break
            if boton_presionado(x,y,boton3):
                respuestas["5"] = False
                break
            if boton_presionado(x,y,boton4):
                respuestas["5"] = False
                break
        if boton_presionado(mouseX, mouseY, boton_continuar):
            colocarBoton(pantalla, 
                         FONDODIR+"verde_hover.png", 
                         2.5, 
                         screenwidth*0.875,
                         screenheight*0.8, 
                         "Continuar", 
                         1, 
                         color = (255,255,255))
        else: 
            colocarBoton(pantalla, FONDODIR+"boton_verde.png", 2.5, screenwidth*0.875,screenheight*0.8, "Continuar", 1)
        display.fill(pantalla)
        display.show()

    # Mostrar la sexta prueba 
    pantalla.clear()
    colocar_fondo(pantalla)
    boton_continuar = colocarBoton(pantalla, FONDODIR+"boton_verde.png", 2.5, screenwidth*0.875,screenheight*0.8, "Continuar", 1)
   
    pantalla.draw_image(image = FONDODIR + "\Figuras_Superpuestas\\prueba_6.jpg",
                        scale = IMGSCALE*2,
                        pos = (screenwidth*0.25,screenheight*0.5))

                           
    boton1 = colocarBoton(pantalla, FONDODIR+"\Figuras_Superpuestas\\6.jpg",0.6,screenwidth*0.50,screenheight*0.5)
    boton2 = colocarBoton(pantalla, FONDODIR+"\Figuras_Superpuestas\\16.png",0.6,screenwidth*0.62,screenheight*0.5)
    boton3 = colocarBoton(pantalla, FONDODIR+"\Figuras_Superpuestas\\10.jpg",0.6,screenwidth*0.75,screenheight*0.5)
    boton4 = colocarBoton(pantalla, FONDODIR+"\Figuras_Superpuestas\\1.jpg",0.6,screenwidth*0.88,screenheight*0.5)

    display.fill(pantalla)
    display.show()

    # Esperar click en el boton para continuar
    x , y = 0,0
    while True:
        mousebutton, clickpos, clicktime = mouse.get_clicked(mousebuttonlist='default', timeout= 10)
        mouseX, mouseY = mouse.get_pos()
        if clickpos:
            x,y = clickpos
            if boton_presionado(x,y, boton_continuar):
                break
            if boton_presionado(x,y,boton1):
                respuestas["6"] = False
                break
            if boton_presionado(x,y,boton2):
                respuestas["6"] = True
                break
            if boton_presionado(x,y,boton3):
                respuestas["6"] = False
                break
            if boton_presionado(x,y,boton4):
                respuestas["6"] = False
                break
        if boton_presionado(mouseX, mouseY, boton_continuar):
            colocarBoton(pantalla, 
                         FONDODIR+"verde_hover.png", 
                         2.5, 
                         screenwidth*0.875,
                         screenheight*0.8, 
                         "Continuar", 
                         1, 
                         color = (255,255,255))
        else: 
            colocarBoton(pantalla, FONDODIR+"boton_verde.png", 2.5, screenwidth*0.875,screenheight*0.8, "Continuar", 1)
        display.fill(pantalla)
        display.show()

    # Mostrar la séptima prueba 
    pantalla.clear()
    colocar_fondo(pantalla)
    boton_continuar = colocarBoton(pantalla, FONDODIR+"boton_verde.png", 2.5, screenwidth*0.875,screenheight*0.8, "Continuar", 1)
   
    pantalla.draw_image(image = FONDODIR + "\Figuras_Superpuestas\\prueba_7.jpg",
                        scale = IMGSCALE*2,
                        pos = (screenwidth*0.25,screenheight*0.5))

                           
    boton1 = colocarBoton(pantalla, FONDODIR+"\Figuras_Superpuestas\\9.jpg",0.6,screenwidth*0.50,screenheight*0.5)
    boton2 = colocarBoton(pantalla, FONDODIR+"\Figuras_Superpuestas\\1.jpg",0.6,screenwidth*0.62,screenheight*0.5)
    boton3 = colocarBoton(pantalla, FONDODIR+"\Figuras_Superpuestas\\10.jpg",0.6,screenwidth*0.75,screenheight*0.5)
    boton4 = colocarBoton(pantalla, FONDODIR+"\Figuras_Superpuestas\\5.jpg",0.6,screenwidth*0.88,screenheight*0.5)

    display.fill(pantalla)
    display.show()

    # Esperar click en el boton para continuar
    x , y = 0,0
    while True:
        mousebutton, clickpos, clicktime = mouse.get_clicked(mousebuttonlist='default', timeout= 10)
        mouseX, mouseY = mouse.get_pos()
        if clickpos:
            x,y = clickpos
            if boton_presionado(x,y, boton_continuar):
                break
            if boton_presionado(x,y,boton1):
                respuestas["7"] = True
                break
            if boton_presionado(x,y,boton2):
                respuestas["7"] = False
                break
            if boton_presionado(x,y,boton3):
                respuestas["7"] = False
                break
            if boton_presionado(x,y,boton4):
                respuestas["7"] = False
                break
        if boton_presionado(mouseX, mouseY, boton_continuar):
            colocarBoton(pantalla, 
                         FONDODIR+"verde_hover.png", 
                         2.5, 
                         screenwidth*0.875,
                         screenheight*0.8, 
                         "Continuar", 
                         1, 
                         color = (255,255,255))
        else: 
            colocarBoton(pantalla, FONDODIR+"boton_verde.png", 2.5, screenwidth*0.875,screenheight*0.8, "Continuar", 1)
        display.fill(pantalla)
        display.show()

    # Mostrar la octava prueba 
    pantalla.clear()
    colocar_fondo(pantalla)
    boton_continuar = colocarBoton(pantalla, FONDODIR+"boton_verde.png", 2.5, screenwidth*0.875,screenheight*0.8, "Continuar", 1)
   
    pantalla.draw_image(image = FONDODIR + "\Figuras_Superpuestas\\prueba_8.jpg",
                        scale = IMGSCALE*2,
                        pos = (screenwidth*0.25,screenheight*0.5))

                           
    boton1 = colocarBoton(pantalla, FONDODIR+"\Figuras_Superpuestas\\6.jpg",0.6,screenwidth*0.50,screenheight*0.5)
    boton2 = colocarBoton(pantalla, FONDODIR+"\Figuras_Superpuestas\\8.jpg",0.6,screenwidth*0.62,screenheight*0.5)
    boton3 = colocarBoton(pantalla, FONDODIR+"\Figuras_Superpuestas\\10.jpg",0.6,screenwidth*0.75,screenheight*0.5)
    boton4 = colocarBoton(pantalla, FONDODIR+"\Figuras_Superpuestas\\1.jpg",0.6,screenwidth*0.88,screenheight*0.5)

    display.fill(pantalla)
    display.show()

    # Esperar click en el boton para continuar
    x , y = 0,0
    while True:
        mousebutton, clickpos, clicktime = mouse.get_clicked(mousebuttonlist='default', timeout= 10)
        mouseX, mouseY = mouse.get_pos()
        if clickpos:
            x,y = clickpos
            if boton_presionado(x,y, boton_continuar):
                break
            if boton_presionado(x,y,boton1):
                respuestas["8"] = True
                break
            if boton_presionado(x,y,boton2):
                respuestas["8"] = False
                break
            if boton_presionado(x,y,boton3):
                respuestas["8"] = False
                break
            if boton_presionado(x,y,boton4):
                respuestas["8"] = False
                break
        if boton_presionado(mouseX, mouseY, boton_continuar):
            colocarBoton(pantalla, 
                         FONDODIR+"verde_hover.png", 
                         2.5, 
                         screenwidth*0.875,
                         screenheight*0.8, 
                         "Salir", 
                         1, 
                         color = (255,255,255))
        else: 
            colocarBoton(pantalla, FONDODIR+"boton_verde.png", 2.5, screenwidth*0.875,screenheight*0.8, "Salir", 1)
        display.fill(pantalla)
        display.show()
        
        if sys.argv[1]:
            with open(ruta_archivo, "w") as archivo:
                json.dump(respuestas, archivo, indent = 4)
            pruebas_sql(id_paciente, "figuras", ruta_archivo)
            sys.exit()
    
if __name__ == "__main__":
    Figuras_superpuestas()