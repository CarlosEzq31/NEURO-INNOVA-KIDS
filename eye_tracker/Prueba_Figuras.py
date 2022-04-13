# Importamos todo desde el archivo constants.py
from constants import *

def main():
    # Creamos los objetos para el eyetracker y la pantalla
    display = Display()
    pantalla = Screen()

    # Creamos los objetos para el mouse, el seguidor ocular y el teclado
    teclado = Keyboard()
    mouse = Mouse()
    eyetracker = EyeTracker(display)

    # Archivos de salida
    # log = Logfile()
    # log.write(["trialnr", "image", "imgtime"])

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
    pantalla.draw_text(text="Prueba de las figuras\nsuperpuestas\nObserva las figuras a la izquierda\ny selecciona la figura que se repita", 
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
            if boton_presionado(x,y, (boton_continuar.get("x"),boton_continuar.get("y")), (boton_continuar.get("ancho"),boton_continuar.get("alto")) ):
                break
        if boton_presionado(mouseX, mouseY, (boton_continuar.get("x"),boton_continuar.get("y")), (boton_continuar.get("ancho"),boton_continuar.get("alto")) ):
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
    botonSalir = colocarBoton(pantalla, FONDODIR+"boton_verde.png", 2.5, screenwidth*0.875,screenheight*0.8, "Continuar", 1)
    pantalla.draw_image(image = FONDODIR + "\Figuras_Superpuestas\Prueba_1\prueba_1.jpg",
                        scale = IMGSCALE*2,
                        pos = (screenwidth*0.35,screenheight*0.5))
    pantalla.draw_image(image = FONDODIR + f"\Figuras_Superpuestas\Prueba_1\\1.jpg",
                        scale = IMGSCALE*0.7,
                        pos = (screenwidth*0.65,screenheight*0.5))
    pantalla.draw_image(image = FONDODIR + f"\Figuras_Superpuestas\Prueba_1\\9.jpg",
                        scale = IMGSCALE*0.7,
                        pos = (screenwidth*0.75,screenheight*0.5))
    pantalla.draw_image(image = FONDODIR + f"\Figuras_Superpuestas\Prueba_1\\10.jpg",
                        scale = IMGSCALE*0.7,
                        pos = (screenwidth*0.85,screenheight*0.5))
    display.fill(pantalla)
    display.show()

    # Esperar click en el boton para continuar
    x , y = 0,0
    while True:
        mousebutton, clickpos, clicktime = mouse.get_clicked(mousebuttonlist='default', timeout= 10)
        mouseX, mouseY = mouse.get_pos()
        if clickpos:
            x,y = clickpos
            if boton_presionado(x,y, (botonSalir.get("x"),botonSalir.get("y")), (botonSalir.get("ancho"),botonSalir.get("alto")) ):
                break
        if boton_presionado(mouseX, mouseY, (botonSalir.get("x"),botonSalir.get("y")), (botonSalir.get("ancho"),botonSalir.get("alto")) ):
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
    botonSalir = colocarBoton(pantalla, FONDODIR+"boton_verde.png", 2.5, screenwidth*0.875,screenheight*0.8, "Salir", 1)
    pantalla.draw_image(image = FONDODIR + "\Figuras_Superpuestas\Prueba_2\prueba_2.jpg",
                        scale = IMGSCALE*2,
                        pos = (screenwidth*0.35,screenheight*0.5))
    imagen1 = colocarBoton( pantalla,
                            imagen = FONDODIR + f"\Figuras_Superpuestas\Prueba_2\\1.jpg",
                            ratio = IMGSCALE*4,
                            x = screenwidth*0.65,
                            y = screenheight*0.5)
    imagen2 = colocarBoton( pantalla,
                            imagen = FONDODIR + f"\Figuras_Superpuestas\Prueba_2\\6.jpg",
                            ratio = IMGSCALE*4,
                            x = screenwidth*0.76,
                            y = screenheight*0.5)
    imagen3 = colocarBoton( pantalla,
                            imagen = FONDODIR + f"\Figuras_Superpuestas\Prueba_2\\10.jpg",
                            ratio = IMGSCALE*4,
                            x = screenwidth*0.87,
                            y = screenheight*0.5)
    display.fill(pantalla)
    display.show()

    # Esperar click en el boton para continuar
    x , y = 0,0
    while True:
        mousebutton, clickpos, clicktime = mouse.get_clicked(mousebuttonlist='default', timeout= 10)
        mouseX, mouseY = mouse.get_pos()
        if clickpos:
            x,y = clickpos
            if boton_presionado(x,y, (botonSalir.get("x"),botonSalir.get("y")), (botonSalir.get("ancho"),botonSalir.get("alto")) ):
                display.close()
                break
            if click_imagen(x,y, imagen1):
                print("PRESIONADO")
        if boton_presionado(mouseX, mouseY, (botonSalir.get("x"),botonSalir.get("y")), (botonSalir.get("ancho"),botonSalir.get("alto")) ):
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



    
if __name__ == "__main__":
    main()