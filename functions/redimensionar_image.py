from PIL import Image as PImage, ImageTk as ImageTk, ImageGrab

# obtener resolucion de pantalla
resolution = ImageGrab.grab()
screenwidth, screenheight = resolution.size
del resolution


# función para redimensionar las imagenes
def get_image_resized(path: str, ratio: float = 1, es_fondo: bool = None) -> PImage:
    imagen = PImage.open(path)
    imagen = imagen.convert('RGBA')
    if es_fondo:
        imagen = imagen.resize((screenwidth, screenheight), PImage.ANTIALIAS)
    else:
        imagen_ancho, imagen_alto = imagen.size
        imagen = imagen.resize((int(imagen_ancho*screenwidth*ratio), int(imagen_alto*screenwidth*ratio)), PImage.ANTIALIAS)
    return ImageTk.PhotoImage(imagen)