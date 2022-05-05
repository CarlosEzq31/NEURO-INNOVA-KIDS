# Importamos todo desde el archivo constants.py
import json
from constants import *

def prueba_domino():
    if sys.argv[1]:
            global id_paciente, ruta_archivo
            id_paciente = sys.argv[1]
            ruta_archivo = docs + "\\NEURO INNOVA KIDS\\PACIENTES\\"+id_paciente+f"\\{id_paciente}_{str(datetime.now().strftime('%d-%m-%y'))}.json"
            LOGFILENAME = f"{id_paciente}_domingo_{str(datetime.now().strftime('%d-%m-%y'))}"
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
    print(log)
    # 

    

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
    pantalla.draw_text(text="Prueba del domino\nObserva las figuras a la izquierda\ny selecciona la figura que se siga en la secuencia", 
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
            if boton_presionado(x,y,boton_continuar):
                break
        if boton_presionado(mouseX, mouseY,boton_continuar):
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
    
    # Mostrar la primer prueba 
    pantalla.clear()
    colocar_fondo(pantalla)
    boton_continuar = colocarBoton(pantalla, FONDODIR+"boton_verde.png", 2.5, screenwidth*0.875,screenheight*0.8, "Continuar", 1)
    pantalla.draw_image(image = FONDODIR + "\Domino\Prueba1_Domino.png",
                        scale = IMGSCALE*0.3,
                        pos = (screenwidth*0.35,screenheight*0.5))
    
    
    boton1 = colocarBoton(pantalla, FONDODIR+"\Domino\D1.png",0.3,screenwidth*0.65,screenheight*0.5)
    boton2 = colocarBoton(pantalla, FONDODIR+"\Domino\D2.png",0.3,screenwidth*0.76,screenheight*0.5)
    boton3 = colocarBoton(pantalla, FONDODIR+"\Domino\D19.png",0.3,screenwidth*0.87,screenheight*0.5)

    display.fill(pantalla)
    display.show()
        
    # Esperar click en el boton para continuar
    x , y = 0,0
    respuestas = {}
    while True:
        mousebutton, clickpos, clicktime = mouse.get_clicked(mousebuttonlist='default', timeout= 10)
        mouseX, mouseY = mouse.get_pos()
        if clickpos:
            x,y = clickpos
            if boton_presionado(x,y,boton_continuar):
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
        if boton_presionado(mouseX, mouseY,boton_continuar):
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
    
    #with open(FONDODIR+f"{sys.argv[1]}_{str(datetime.now().strftime('%d-%m-%y'))}.json","w") as archivo:
     #   json.dump(respuestas, archivo, indent = 4)
        
    
    # Mostrar la segunda prueba 
    pantalla.clear()
    colocar_fondo(pantalla)
    boton_continuar = colocarBoton(pantalla, FONDODIR+"boton_verde.png", 2.5, screenwidth*0.875,screenheight*0.8, "Continuar", 1)
    
    pantalla.draw_image(image = FONDODIR + "\Domino\Prueba2_Domino.png",
                        scale = IMGSCALE*0.3,
                        pos = (screenwidth*0.35,screenheight*0.5))
    

    boton1 = colocarBoton(pantalla, FONDODIR+"\Domino\D7.png",0.3,screenwidth*0.65,screenheight*0.5)
    boton2 = colocarBoton(pantalla, FONDODIR+"\Domino\D18.png",0.3,screenwidth*0.76,screenheight*0.5)
    boton3 = colocarBoton(pantalla, FONDODIR+"\Domino\D12.png",0.3,screenwidth*0.87,screenheight*0.5)

    display.fill(pantalla)
    display.show()
    # print("Prueba")
    
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
                respuestas["2"] = True
                break
            if boton_presionado(x,y,boton3):
                respuestas["2"] = False
                break
        if boton_presionado(mouseX, mouseY,boton_continuar):
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
        # print("Prueba")

    # Mostrar la tercer prueba 
    pantalla.clear()
    colocar_fondo(pantalla)
    boton_continuar = colocarBoton(pantalla, FONDODIR+"boton_verde.png", 2.5, screenwidth*0.875,screenheight*0.8, "Continuar", 1)
    pantalla.draw_image(image = FONDODIR + "\Domino\Prueba3_Domino.png",
                        scale = IMGSCALE*1.8,
                        pos = (screenwidth*0.35,screenheight*0.5))
    
    boton1 = colocarBoton(pantalla, FONDODIR+"\Domino\D1.png",0.3,screenwidth*0.65,screenheight*0.5)
    boton2 = colocarBoton(pantalla, FONDODIR+"\Domino\D2.png",0.3,screenwidth*0.76,screenheight*0.5)
    boton3 = colocarBoton(pantalla, FONDODIR+"\Domino\D19.png",0.3,screenwidth*0.87,screenheight*0.5)
        
    display.fill(pantalla)
    display.show()
    # print("Prueba")
    
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

        if boton_presionado(mouseX, mouseY,boton_continuar):
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
        # print("Prueba")

    # Mostrar la cuarta prueba 
    pantalla.clear()
    colocar_fondo(pantalla)
    boton_continuar = colocarBoton(pantalla, FONDODIR+"boton_verde.png", 2.5, screenwidth*0.875,screenheight*0.8, "Continuar", 1)
    pantalla.draw_image(image = FONDODIR + "\Domino\Prueba4_Domino.png",
                        scale = IMGSCALE*2.2,
                        pos = (screenwidth*0.35,screenheight*0.5))

    boton1 = colocarBoton(pantalla, FONDODIR+"\Domino\D14.png",0.3,screenwidth*0.65,screenheight*0.5)
    boton2 = colocarBoton(pantalla, FONDODIR+"\Domino\D23.png",0.3,screenwidth*0.76,screenheight*0.5)
    boton3 = colocarBoton(pantalla, FONDODIR+"\Domino\D27.png",0.3,screenwidth*0.87,screenheight*0.5)
                             
    display.fill(pantalla)
    display.show()
    # print("Prueba")
    
    # Esperar click en el boton para continuar
    x , y = 0,0
    while True:
        mousebutton, clickpos, clicktime = mouse.get_clicked(mousebuttonlist='default', timeout= 10)
        mouseX, mouseY = mouse.get_pos()
        if clickpos:
            x,y = clickpos
            if boton_presionado(x,y,boton_continuar):
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
        # print("Prueba")

    # Mostrar la quinta prueba 
    pantalla.clear()
    colocar_fondo(pantalla)
    boton_continuar = colocarBoton(pantalla, FONDODIR+"boton_verde.png", 2.5, screenwidth*0.875,screenheight*0.8, "Continuar", 1)
    pantalla.draw_image(image = FONDODIR + "\Domino\Prueba5_Domino.png",
                        scale = IMGSCALE*0.3,
                        pos = (screenwidth*0.35,screenheight*0.5))

    boton1 = colocarBoton(pantalla, FONDODIR+"\Domino\D24.png",0.3,screenwidth*0.65,screenheight*0.5)
    boton2 = colocarBoton(pantalla, FONDODIR+"\Domino\D20.png",0.3,screenwidth*0.76,screenheight*0.5)
    boton3 = colocarBoton(pantalla, FONDODIR+"\Domino\D21.png",0.3,screenwidth*0.87,screenheight*0.5)
    
    display.fill(pantalla)
    display.show()
    # print("Prueba")
    
    # Esperar click en el boton para continuar
    x , y = 0,0
    while True:
        mousebutton, clickpos, clicktime = mouse.get_clicked(mousebuttonlist='default', timeout= 10)
        mouseX, mouseY = mouse.get_pos()
        if clickpos:
            x,y = clickpos
            if boton_presionado(x,y,boton_continuar):
                break
            if boton_presionado(x,y,boton1):
                respuestas["5"] = False
                break
            if boton_presionado(x,y,boton2):
                respuestas["5"] = False
                break
            if boton_presionado(x,y,boton3):
                respuestas["5"] = True
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
        # print("Prueba")

    # Mostrar la sexta prueba 
    pantalla.clear()
    colocar_fondo(pantalla)
    boton_continuar = colocarBoton(pantalla, FONDODIR+"boton_verde.png", 2.5, screenwidth*0.875,screenheight*0.8, "Salir", 1)
    pantalla.draw_image(image = FONDODIR + "\Domino\Prueba6_Domino.png",
                        scale = IMGSCALE*0.3,
                        pos = (screenwidth*0.35,screenheight*0.5))

    boton1 = colocarBoton(pantalla, FONDODIR+"\Domino\D1.png",0.3,screenwidth*0.65,screenheight*0.5)
    boton2 = colocarBoton(pantalla, FONDODIR+"\Domino\D0.png",0.3,screenwidth*0.76,screenheight*0.5)
    boton3 = colocarBoton(pantalla, FONDODIR+"\Domino\D16.png",0.3,screenwidth*0.87,screenheight*0.5)
    
    display.fill(pantalla)
    display.show()
    # print("Prueba")
    
    # Esperar click en el boton para continuar
    x , y = 0,0
    while True:
        mousebutton, clickpos, clicktime = mouse.get_clicked(mousebuttonlist='default', timeout= 10)
        mouseX, mouseY = mouse.get_pos()
        if clickpos:
            x,y = clickpos
            if boton_presionado(x,y,boton_continuar):
                display.close()
                break
            if boton_presionado(x,y,boton1):
                respuestas["6"] = True
                display.close()
                break
            if boton_presionado(x,y,boton2):
                respuestas["6"] = False
                display.close()
                break
            if boton_presionado(x,y,boton3):
                respuestas["6"] = False
                display.close()
                break
            
        if boton_presionado(mouseX, mouseY,boton_continuar):
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
            pruebas_sql(id_paciente, "domino", ruta_archivo)
            sys.exit()

if __name__ == "__main__":
    prueba_domino()
    