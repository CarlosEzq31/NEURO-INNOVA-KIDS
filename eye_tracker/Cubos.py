# Importamos todo desde el archivo constants.py
from pickle import TRUE
from constants import *

def cubos_khos():
    
    if sys.argv[1]:
            global id_paciente, ruta_archivo
            id_paciente = sys.argv[1]
            ruta_archivo = docs + "\\NEURO INNOVA KIDS\\PACIENTES\\"+id_paciente+f"\\{id_paciente}_{str(datetime.now().strftime('%d-%m-%y'))}.json"
            LOGFILENAME = f"{id_paciente}_cubos_{str(datetime.now().strftime('%d-%m-%y'))}"
    
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
    pantalla.draw_text(text="Prueba de cubos de Khos\nObserva el cubo desplegado a la izquierda\ny selecciona el cubo que corresponde ", 
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
    
    # Mostrar la prueba 1
    pantalla.clear()
    colocar_fondo(pantalla)
    boton_continuar = colocarBoton(pantalla, FONDODIR+"boton_verde.png", 2.5, screenwidth*0.875,screenheight*0.8, "Continuar", 1)
    pantalla.draw_image(image = FONDODIR + "\Cubos\cubos_desplegados\p1.png",
                        scale = IMGSCALE*2.5,
                        pos = (screenwidth*0.25,screenheight*0.5))
    boton1 = colocarBoton(pantalla, FONDODIR+"\Cubos\\cubos\\c32.png",1.5,screenwidth*0.55,screenheight*0.5)
    boton2 = colocarBoton(pantalla, FONDODIR+"\Cubos\\cubos\\c1.png",1.5,screenwidth*0.66,screenheight*0.5)
    boton3 = colocarBoton(pantalla, FONDODIR+"\Cubos\\cubos\\c51.png",1.5,screenwidth*0.77,screenheight*0.5)
    boton4 = colocarBoton(pantalla, FONDODIR+"\Cubos\\cubos\\c56.png",1.5,screenwidth*0.87,screenheight*0.5)
    
    display.fill(pantalla)
    display.show()
    # print("PRUEBA")
    
    # Esperar click en el boton para continuar
    x , y = 0,0
    respuestas = {}
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
        
    # Mostrar la prueba 2
    pantalla.clear()
    colocar_fondo(pantalla)
    boton_continuar = colocarBoton(pantalla, FONDODIR+"boton_verde.png", 2.5, screenwidth*0.875,screenheight*0.8, "Continuar", 1)
    pantalla.draw_image(image = FONDODIR + "\Cubos\cubos_desplegados\p2.png",
                        scale = IMGSCALE*2.5,
                        pos = (screenwidth*0.25,screenheight*0.5))
    boton1 = colocarBoton(pantalla, FONDODIR+"\Cubos\\cubos\\c67.png",1.5,screenwidth*0.55,screenheight*0.5)
    boton2 = colocarBoton(pantalla, FONDODIR+"\Cubos\\cubos\\c15.png",1.5,screenwidth*0.66,screenheight*0.5)
    boton3 = colocarBoton(pantalla, FONDODIR+"\Cubos\\cubos\\c72.png",1.5,screenwidth*0.77,screenheight*0.5)
    boton4 = colocarBoton(pantalla, FONDODIR+"\Cubos\\cubos\\c48.png",1.5,screenwidth*0.87,screenheight*0.5)
    
    display.fill(pantalla)
    display.show()
    # print("PRUEBA")
    
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
                respuestas["2"] = False
                break
            if boton_presionado(x,y,boton2):
                respuestas["2"] = False
                break
            if boton_presionado(x,y,boton3):
                respuestas["2"] = True
                break
            if boton_presionado(x,y,boton4):
                respuestas["2"] = True
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

    # Mostrar la prueba 3
    pantalla.clear()
    colocar_fondo(pantalla)
    boton_continuar = colocarBoton(pantalla, FONDODIR+"boton_verde.png", 2.5, screenwidth*0.875,screenheight*0.8, "Continuar", 1)
    pantalla.draw_image(image = FONDODIR + "\Cubos\cubos_desplegados\p3.png",
                        scale = IMGSCALE*2.5,
                        pos = (screenwidth*0.25,screenheight*0.5))
    boton1 = colocarBoton(pantalla, FONDODIR+"\Cubos\\cubos\\c3.png",1.5,screenwidth*0.55,screenheight*0.5)
    boton2 = colocarBoton(pantalla, FONDODIR+"\Cubos\\cubos\\c12.png",1.5,screenwidth*0.66,screenheight*0.5)
    boton3 = colocarBoton(pantalla, FONDODIR+"\Cubos\\cubos\\c75.png",1.5,screenwidth*0.77,screenheight*0.5)
    boton4 = colocarBoton(pantalla, FONDODIR+"\Cubos\\cubos\\c50.png",1.5,screenwidth*0.87,screenheight*0.5)
    
    display.fill(pantalla)
    display.show()
    # print("PRUEBA")
    
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
                respuestas["3"] = True
                break
            if boton_presionado(x,y,boton2):
                respuestas["3"] = False
                break
            if boton_presionado(x,y,boton3):
                respuestas["3"] = False
                break
            if boton_presionado(x,y,boton4):
                respuestas["3"] = False
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

    # Mostrar la prueba 4
    pantalla.clear()
    colocar_fondo(pantalla)
    boton_continuar = colocarBoton(pantalla, FONDODIR+"boton_verde.png", 2.5, screenwidth*0.875,screenheight*0.8, "Continuar", 1)
    pantalla.draw_image(image = FONDODIR + "\Cubos\cubos_desplegados\p4.png",
                        scale = IMGSCALE*2.5,
                        pos = (screenwidth*0.25,screenheight*0.5))
    boton1 = colocarBoton(pantalla, FONDODIR+"\Cubos\\cubos\\c38.png",1.5,screenwidth*0.55,screenheight*0.5)
    boton2 = colocarBoton(pantalla, FONDODIR+"\Cubos\\cubos\\c60.png",1.5,screenwidth*0.66,screenheight*0.5)
    boton3 = colocarBoton(pantalla, FONDODIR+"\Cubos\\cubos\\c75.png",1.5,screenwidth*0.77,screenheight*0.5)
    boton4 = colocarBoton(pantalla, FONDODIR+"\Cubos\\cubos\\c53.png",1.5,screenwidth*0.87,screenheight*0.5)
    
    display.fill(pantalla)
    display.show()
    # print("PRUEBA")
    
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
                respuestas["4"] = True
                break
            if boton_presionado(x,y,boton3):
                respuestas["4"] = False
                break
            if boton_presionado(x,y,boton4):
                respuestas["4"] = False
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

    # Mostrar la prueba 5
    pantalla.clear()
    colocar_fondo(pantalla)
    boton_continuar = colocarBoton(pantalla, FONDODIR+"boton_verde.png", 2.5, screenwidth*0.875,screenheight*0.8, "Continuar", 1)
    pantalla.draw_image(image = FONDODIR + "\Cubos\cubos_desplegados\p5.png",
                        scale = IMGSCALE*2.5,
                        pos = (screenwidth*0.25,screenheight*0.5))
    boton1 = colocarBoton(pantalla, FONDODIR+"\Cubos\\cubos\\c43.png",1.5,screenwidth*0.55,screenheight*0.5)
    boton2 = colocarBoton(pantalla, FONDODIR+"\Cubos\\cubos\\c55.png",1.5,screenwidth*0.66,screenheight*0.5)
    boton3 = colocarBoton(pantalla, FONDODIR+"\Cubos\\cubos\\c5.png",1.5,screenwidth*0.77,screenheight*0.5)
    boton4 = colocarBoton(pantalla, FONDODIR+"\Cubos\\cubos\\c29.png",1.5,screenwidth*0.87,screenheight*0.5)
    
    display.fill(pantalla)
    display.show()
    # print("PRUEBA")
    
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
                respuestas["5"] = False
                break
            if boton_presionado(x,y,boton2):
                respuestas["5"] = True
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

    # Mostrar la prueba 6
    pantalla.clear()
    colocar_fondo(pantalla)
    boton_continuar = colocarBoton(pantalla, FONDODIR+"boton_verde.png", 2.5, screenwidth*0.875,screenheight*0.8, "Continuar", 1)
    pantalla.draw_image(image = FONDODIR + "\Cubos\cubos_desplegados\p6.png",
                        scale = IMGSCALE*2.5,
                        pos = (screenwidth*0.25,screenheight*0.5))
    boton1 = colocarBoton(pantalla, FONDODIR+"\Cubos\\cubos\\c2.png",1.5,screenwidth*0.55,screenheight*0.5)
    boton2 = colocarBoton(pantalla, FONDODIR+"\Cubos\\cubos\\c1.png",1.5,screenwidth*0.66,screenheight*0.5)
    boton3 = colocarBoton(pantalla, FONDODIR+"\Cubos\\cubos\\c75.png",1.5,screenwidth*0.77,screenheight*0.5)
    boton4 = colocarBoton(pantalla, FONDODIR+"\Cubos\\cubos\\c15.png",1.5,screenwidth*0.87,screenheight*0.5)
    
    display.fill(pantalla)
    display.show()
    # print("PRUEBA")
    
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
                respuestas["6"] = False
                break
            if boton_presionado(x,y,boton3):
                respuestas["6"] = True
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

    # Mostrar la prueba 7
    pantalla.clear()
    colocar_fondo(pantalla)
    boton_continuar = colocarBoton(pantalla, FONDODIR+"boton_verde.png", 2.5, screenwidth*0.875,screenheight*0.8, "Continuar", 1)
    pantalla.draw_image(image = FONDODIR + "\Cubos\cubos_desplegados\p7.png",
                        scale = IMGSCALE*2.5,
                        pos = (screenwidth*0.25,screenheight*0.5))
    boton1 = colocarBoton(pantalla, FONDODIR+"\Cubos\\cubos\\c72.png",1.5,screenwidth*0.55,screenheight*0.5)
    boton2 = colocarBoton(pantalla, FONDODIR+"\Cubos\\cubos\\c13.png",1.5,screenwidth*0.66,screenheight*0.5)
    boton3 = colocarBoton(pantalla, FONDODIR+"\Cubos\\cubos\\c45.png",1.5,screenwidth*0.77,screenheight*0.5)
    boton4 = colocarBoton(pantalla, FONDODIR+"\Cubos\\cubos\\c44.png",1.5,screenwidth*0.87,screenheight*0.5)
    
    display.fill(pantalla)
    display.show()
    # print("PRUEBA")
    
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

    # Mostrar la prueba 8
    pantalla.clear()
    colocar_fondo(pantalla)
    boton_continuar = colocarBoton(pantalla, FONDODIR+"boton_verde.png", 2.5, screenwidth*0.875,screenheight*0.8, "Continuar", 1)
    pantalla.draw_image(image = FONDODIR + "\Cubos\cubos_desplegados\p8.png",
                        scale = IMGSCALE*2.5,
                        pos = (screenwidth*0.25,screenheight*0.5))
    boton1 = colocarBoton(pantalla, FONDODIR+"\Cubos\\cubos\\c22.png",1.5,screenwidth*0.55,screenheight*0.5)
    boton2 = colocarBoton(pantalla, FONDODIR+"\Cubos\\cubos\\c67.png",1.5,screenwidth*0.66,screenheight*0.5)
    boton3 = colocarBoton(pantalla, FONDODIR+"\Cubos\\cubos\\c77.png",1.5,screenwidth*0.77,screenheight*0.5)
    boton4 = colocarBoton(pantalla, FONDODIR+"\Cubos\\cubos\\c30.png",1.5,screenwidth*0.87,screenheight*0.5)
    
    display.fill(pantalla)
    display.show()
    # print("PRUEBA")
    
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
                respuestas["8"] = False
                break
            if boton_presionado(x,y,boton2):
                respuestas["8"] = True
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
                         "Continuar", 
                         1, 
                         color = (255,255,255))
        else: 
            colocarBoton(pantalla, FONDODIR+"boton_verde.png", 2.5, screenwidth*0.875,screenheight*0.8, "Continuar", 1)
        display.fill(pantalla)
        display.show()              

    # Mostrar la prueba 9
    pantalla.clear()
    colocar_fondo(pantalla)
    boton_continuar = colocarBoton(pantalla, FONDODIR+"boton_verde.png", 2.5, screenwidth*0.875,screenheight*0.8, "Continuar", 1)
    pantalla.draw_image(image = FONDODIR + "\Cubos\cubos_desplegados\p9.png",
                        scale = IMGSCALE*2.5,
                        pos = (screenwidth*0.25,screenheight*0.5))
    boton1 = colocarBoton(pantalla, FONDODIR+"\Cubos\\cubos\\c46.png",1.5,screenwidth*0.55,screenheight*0.5)
    boton2 = colocarBoton(pantalla, FONDODIR+"\Cubos\\cubos\\c59.png",1.5,screenwidth*0.66,screenheight*0.5)
    boton3 = colocarBoton(pantalla, FONDODIR+"\Cubos\\cubos\\c69.png",1.5,screenwidth*0.77,screenheight*0.5)
    boton4 = colocarBoton(pantalla, FONDODIR+"\Cubos\\cubos\\c63.png",1.5,screenwidth*0.87,screenheight*0.5)
    
    display.fill(pantalla)
    display.show()
    # print("PRUEBA")
    
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
                respuestas["9"] = False
                break
            if boton_presionado(x,y,boton2):
                respuestas["9"] = False
                break
            if boton_presionado(x,y,boton3):
                respuestas["9"] = False
                break
            if boton_presionado(x,y,boton4):
                respuestas["9"] = True
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

    # Mostrar la prueba 10
    pantalla.clear()
    colocar_fondo(pantalla)
    boton_continuar = colocarBoton(pantalla, FONDODIR+"boton_verde.png", 2.5, screenwidth*0.875,screenheight*0.8, "Continuar", 1)
    pantalla.draw_image(image = FONDODIR + "\Cubos\cubos_desplegados\p10.png",
                        scale = IMGSCALE*2.5,
                        pos = (screenwidth*0.25,screenheight*0.5))
    boton1 = colocarBoton(pantalla, FONDODIR+"\Cubos\\cubos\\c1.png",1.5,screenwidth*0.55,screenheight*0.5)
    boton2 = colocarBoton(pantalla, FONDODIR+"\Cubos\\cubos\\c25.png",1.5,screenwidth*0.66,screenheight*0.5)
    boton3 = colocarBoton(pantalla, FONDODIR+"\Cubos\\cubos\\c11.png",1.5,screenwidth*0.77,screenheight*0.5)
    boton4 = colocarBoton(pantalla, FONDODIR+"\Cubos\\cubos\\c9.png",1.5,screenwidth*0.87,screenheight*0.5)
    
    display.fill(pantalla)
    display.show()
    # print("PRUEBA")
    
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
                respuestas["10"] = False
                break
            if boton_presionado(x,y,boton2):
                respuestas["10"] = False
                break
            if boton_presionado(x,y,boton3):
                respuestas["10"] = True
                break
            if boton_presionado(x,y,boton4):
                respuestas["10"] = False
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

    # Mostrar la prueba 11
    pantalla.clear()
    colocar_fondo(pantalla)
    boton_continuar = colocarBoton(pantalla, FONDODIR+"boton_verde.png", 2.5, screenwidth*0.875,screenheight*0.8, "Continuar", 1)
    pantalla.draw_image(image = FONDODIR + "\Cubos\cubos_desplegados\p11.png",
                        scale = IMGSCALE*2.5,
                        pos = (screenwidth*0.25,screenheight*0.5))
    boton1 = colocarBoton(pantalla, FONDODIR+"\Cubos\\cubos\\c20.png",1.5,screenwidth*0.55,screenheight*0.5)
    boton2 = colocarBoton(pantalla, FONDODIR+"\Cubos\\cubos\\c7.png",1.5,screenwidth*0.66,screenheight*0.5)
    boton3 = colocarBoton(pantalla, FONDODIR+"\Cubos\\cubos\\c26.png",1.5,screenwidth*0.77,screenheight*0.5)
    boton4 = colocarBoton(pantalla, FONDODIR+"\Cubos\\cubos\\c24.png",1.5,screenwidth*0.87,screenheight*0.5)
    
    display.fill(pantalla)
    display.show()
    # print("PRUEBA")
    
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
                respuestas["11"] = False
                break
            if boton_presionado(x,y,boton2):
                respuestas["11"] = True
                break
            if boton_presionado(x,y,boton3):
                respuestas["11"] = False
                break
            if boton_presionado(x,y,boton4):
                respuestas["11"] = False
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

    # Mostrar la prueba 12
    pantalla.clear()
    colocar_fondo(pantalla)
    boton_continuar = colocarBoton(pantalla, FONDODIR+"boton_verde.png", 2.5, screenwidth*0.875,screenheight*0.8, "Continuar", 1)
    pantalla.draw_image(image = FONDODIR + "\Cubos\cubos_desplegados\p12.png",
                        scale = IMGSCALE*2.5,
                        pos = (screenwidth*0.25,screenheight*0.5))
    boton1 = colocarBoton(pantalla, FONDODIR+"\Cubos\\cubos\\c19.png",1.5,screenwidth*0.55,screenheight*0.5)
    boton2 = colocarBoton(pantalla, FONDODIR+"\Cubos\\cubos\\c2.png",1.5,screenwidth*0.66,screenheight*0.5)
    boton3 = colocarBoton(pantalla, FONDODIR+"\Cubos\\cubos\\c61.png",1.5,screenwidth*0.77,screenheight*0.5)
    boton4 = colocarBoton(pantalla, FONDODIR+"\Cubos\\cubos\\c66.png",1.5,screenwidth*0.87,screenheight*0.5)
    
    display.fill(pantalla)
    display.show()
    # print("PRUEBA")
    
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
                respuestas["12"] = True
                break
            if boton_presionado(x,y,boton2):
                respuestas["12"] = False
                break
            if boton_presionado(x,y,boton3):
                respuestas["12"] = False
                break
            if boton_presionado(x,y,boton4):
                respuestas["12"] = False
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

    # Mostrar la prueba 13
    pantalla.clear()
    colocar_fondo(pantalla)
    boton_continuar = colocarBoton(pantalla, FONDODIR+"boton_verde.png", 2.5, screenwidth*0.875,screenheight*0.8, "Continuar", 1)
    pantalla.draw_image(image = FONDODIR + "\Cubos\cubos_desplegados\p13.png",
                        scale = IMGSCALE*2.5,
                        pos = (screenwidth*0.25,screenheight*0.5))
    boton1 = colocarBoton(pantalla, FONDODIR+"\Cubos\\cubos\\c29.png",1.5,screenwidth*0.55,screenheight*0.5)
    boton2 = colocarBoton(pantalla, FONDODIR+"\Cubos\\cubos\\c64.png",1.5,screenwidth*0.66,screenheight*0.5)
    boton3 = colocarBoton(pantalla, FONDODIR+"\Cubos\\cubos\\c71.png",1.5,screenwidth*0.77,screenheight*0.5)
    boton4 = colocarBoton(pantalla, FONDODIR+"\Cubos\\cubos\\c15.png",1.5,screenwidth*0.87,screenheight*0.5)
    
    display.fill(pantalla)
    display.show()
    # print("PRUEBA")
    
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
                respuestas["13"] = False
                break
            if boton_presionado(x,y,boton2):
                respuestas["13"] = False
                break
            if boton_presionado(x,y,boton3):
                respuestas["13"] = False
                break
            if boton_presionado(x,y,boton4):
                respuestas["13"] = True
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

    # Mostrar la prueba 14
    pantalla.clear()
    colocar_fondo(pantalla)
    boton_continuar = colocarBoton(pantalla, FONDODIR+"boton_verde.png", 2.5, screenwidth*0.875,screenheight*0.8, "Continuar", 1)
    pantalla.draw_image(image = FONDODIR + "\Cubos\cubos_desplegados\p14.png",
                        scale = IMGSCALE*2.5,
                        pos = (screenwidth*0.25,screenheight*0.5))
    boton1 = colocarBoton(pantalla, FONDODIR+"\Cubos\\cubos\\c38.png",1.5,screenwidth*0.55,screenheight*0.5)
    boton2 = colocarBoton(pantalla, FONDODIR+"\Cubos\\cubos\\c26.png",1.5,screenwidth*0.66,screenheight*0.5)
    boton3 = colocarBoton(pantalla, FONDODIR+"\Cubos\\cubos\\c8.png",1.5,screenwidth*0.77,screenheight*0.5)
    boton4 = colocarBoton(pantalla, FONDODIR+"\Cubos\\cubos\\c6.png",1.5,screenwidth*0.87,screenheight*0.5)
    
    display.fill(pantalla)
    display.show()
    # print("PRUEBA")
    
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
                respuestas["14"] = False
                break
            if boton_presionado(x,y,boton2):
                respuestas["14"] = True
                break
            if boton_presionado(x,y,boton3):
                respuestas["14"] = False
                break
            if boton_presionado(x,y,boton4):
                respuestas["14"] = False
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

    # Mostrar la prueba 15
    pantalla.clear()
    colocar_fondo(pantalla)
    boton_continuar = colocarBoton(pantalla, FONDODIR+"boton_verde.png", 2.5, screenwidth*0.875,screenheight*0.8, "Continuar", 1)
    pantalla.draw_image(image = FONDODIR + "\Cubos\cubos_desplegados\p15.png",
                        scale = IMGSCALE*2.5,
                        pos = (screenwidth*0.25,screenheight*0.5))
    boton1 = colocarBoton(pantalla, FONDODIR+"\Cubos\\cubos\\c13.png",1.5,screenwidth*0.55,screenheight*0.5)
    boton2 = colocarBoton(pantalla, FONDODIR+"\Cubos\\cubos\\c12.png",1.5,screenwidth*0.66,screenheight*0.5)
    boton3 = colocarBoton(pantalla, FONDODIR+"\Cubos\\cubos\\c4.png",1.5,screenwidth*0.77,screenheight*0.5)
    boton4 = colocarBoton(pantalla, FONDODIR+"\Cubos\\cubos\\c23.png",1.5,screenwidth*0.87,screenheight*0.5)
    
    display.fill(pantalla)
    display.show()
    # print("PRUEBA")
    
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
                respuestas["15"] = False
                break
            if boton_presionado(x,y,boton2):
                respuestas["15"] = False
                break
            if boton_presionado(x,y,boton3):
                respuestas["15"] = False
                break
            if boton_presionado(x,y,boton4):
                respuestas["15"] = True
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

    # Mostrar la prueba 16
    pantalla.clear()
    colocar_fondo(pantalla)
    boton_continuar = colocarBoton(pantalla, FONDODIR+"boton_verde.png", 2.5, screenwidth*0.875,screenheight*0.8, "Continuar", 1)
    pantalla.draw_image(image = FONDODIR + "\Cubos\cubos_desplegados\p16.png",
                        scale = IMGSCALE*2.5,
                        pos = (screenwidth*0.25,screenheight*0.5))
    boton1 = colocarBoton(pantalla, FONDODIR+"\Cubos\\cubos\\c50.png",1.5,screenwidth*0.55,screenheight*0.5)
    boton2 = colocarBoton(pantalla, FONDODIR+"\Cubos\\cubos\\c63.png",1.5,screenwidth*0.66,screenheight*0.5)
    boton3 = colocarBoton(pantalla, FONDODIR+"\Cubos\\cubos\\c40.png",1.5,screenwidth*0.77,screenheight*0.5)
    boton4 = colocarBoton(pantalla, FONDODIR+"\Cubos\\cubos\\c34.png",1.5,screenwidth*0.87,screenheight*0.5)
    
    display.fill(pantalla)
    display.show()
    # print("PRUEBA")
    
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
                respuestas["16"] = False
                break
            if boton_presionado(x,y,boton2):
                respuestas["16"] = False
                break
            if boton_presionado(x,y,boton3):
                respuestas["16"] = False
                break
            if boton_presionado(x,y,boton4):
                respuestas["16"] = True
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

    # Mostrar la prueba 17
    pantalla.clear()
    colocar_fondo(pantalla)
    boton_continuar = colocarBoton(pantalla, FONDODIR+"boton_verde.png", 2.5, screenwidth*0.875,screenheight*0.8, "Continuar", 1)
    pantalla.draw_image(image = FONDODIR + "\Cubos\cubos_desplegados\p17.png",
                        scale = IMGSCALE*2.5,
                        pos = (screenwidth*0.25,screenheight*0.5))
    boton1 = colocarBoton(pantalla, FONDODIR+"\Cubos\\cubos\\c40.png",1.5,screenwidth*0.55,screenheight*0.5)
    boton2 = colocarBoton(pantalla, FONDODIR+"\Cubos\\cubos\\c37.png",1.5,screenwidth*0.66,screenheight*0.5)
    boton3 = colocarBoton(pantalla, FONDODIR+"\Cubos\\cubos\\c26.png",1.5,screenwidth*0.77,screenheight*0.5)
    boton4 = colocarBoton(pantalla, FONDODIR+"\Cubos\\cubos\\c33.png",1.5,screenwidth*0.87,screenheight*0.5)
    
    display.fill(pantalla)
    display.show()
    # print("PRUEBA")
    
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
                respuestas["17"] = True
                break
            if boton_presionado(x,y,boton2):
                respuestas["17"] = False
                break
            if boton_presionado(x,y,boton3):
                respuestas["17"] = False
                break
            if boton_presionado(x,y,boton4):
                respuestas["17"] = False
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

    # Mostrar la prueba 18
    pantalla.clear()
    colocar_fondo(pantalla)
    boton_continuar = colocarBoton(pantalla, FONDODIR+"boton_verde.png", 2.5, screenwidth*0.875,screenheight*0.8, "Continuar", 1)
    pantalla.draw_image(image = FONDODIR + "\Cubos\cubos_desplegados\p18.png",
                        scale = IMGSCALE*2.5,
                        pos = (screenwidth*0.25,screenheight*0.5))
    boton1 = colocarBoton(pantalla, FONDODIR+"\Cubos\\cubos\\c55.png",1.5,screenwidth*0.55,screenheight*0.5)
    boton2 = colocarBoton(pantalla, FONDODIR+"\Cubos\\cubos\\c53.png",1.5,screenwidth*0.66,screenheight*0.5)
    boton3 = colocarBoton(pantalla, FONDODIR+"\Cubos\\cubos\\c3.png",1.5,screenwidth*0.77,screenheight*0.5)
    boton4 = colocarBoton(pantalla, FONDODIR+"\Cubos\\cubos\\c15.png",1.5,screenwidth*0.87,screenheight*0.5)
    
    display.fill(pantalla)
    display.show()
    # print("PRUEBA")
    
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
                respuestas["18"] = False
                break
            if boton_presionado(x,y,boton2):
                respuestas["18"] = False
                break
            if boton_presionado(x,y,boton3):
                respuestas["18"] = True
                break
            if boton_presionado(x,y,boton4):
                respuestas["18"] = False
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

    # Mostrar la prueba 19
    pantalla.clear()
    colocar_fondo(pantalla)
    boton_continuar = colocarBoton(pantalla, FONDODIR+"boton_verde.png", 2.5, screenwidth*0.875,screenheight*0.8, "Continuar", 1)
    pantalla.draw_image(image = FONDODIR + "\Cubos\cubos_desplegados\p19.png",
                        scale = IMGSCALE*2.5,
                        pos = (screenwidth*0.25,screenheight*0.5))
    boton1 = colocarBoton(pantalla, FONDODIR+"\Cubos\\cubos\\c42.png",1.5,screenwidth*0.55,screenheight*0.5)
    boton2 = colocarBoton(pantalla, FONDODIR+"\Cubos\\cubos\\c30.png",1.5,screenwidth*0.66,screenheight*0.5)
    boton3 = colocarBoton(pantalla, FONDODIR+"\Cubos\\cubos\\c71.png",1.5,screenwidth*0.77,screenheight*0.5)
    boton4 = colocarBoton(pantalla, FONDODIR+"\Cubos\\cubos\\c68.png",1.5,screenwidth*0.87,screenheight*0.5)
    
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
                respuestas["19"] = False
                break
            if boton_presionado(x,y,boton2):
                respuestas["19"] = True
                break
            if boton_presionado(x,y,boton3):
                respuestas["19"] = False
                break
            if boton_presionado(x,y,boton4):
                respuestas["19"] = False
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
            pruebas_sql(id_paciente, "cubos", ruta_archivo)
            sys.exit()
        
if __name__ == "__main__":
    cubos_khos()
    