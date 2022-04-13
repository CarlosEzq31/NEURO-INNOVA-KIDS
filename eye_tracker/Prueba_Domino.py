# Importamos todo desde el archivo constants.py
from constants import *

def prueba_domino():
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
    
    # Mostrar la primer prueba 
    pantalla.clear()
    colocar_fondo(pantalla)
    botonSalir = colocarBoton(pantalla, FONDODIR+"boton_verde.png", 2.5, screenwidth*0.875,screenheight*0.8, "Continuar", 1)
    pantalla.draw_image(image = FONDODIR + "\Domino\Prueba1_Domino.png",
                        scale = IMGSCALE*0.3,
                        pos = (screenwidth*0.35,screenheight*0.5))
    pantalla.draw_image(image = FONDODIR + f"\Domino\D1.png",
                        scale = IMGSCALE*0.3,
                        pos = (screenwidth*0.65,screenheight*0.5))
    pantalla.draw_image(image = FONDODIR + f"\Domino\D2.png",
                        scale = IMGSCALE*0.3,
                        pos = (screenwidth*0.76,screenheight*0.5))
    pantalla.draw_image(image = FONDODIR + f"\Domino\D3.png",
                        scale = IMGSCALE*0.3,
                        pos = (screenwidth*0.87,screenheight*0.5))
    display.fill(pantalla)
    display.show()
    print("PRUEBA")
    
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
    
if __name__ == "__main__":
    prueba_domino()