import pyglet

source = pyglet.media.load(".\\Video 3.1.mp4")
fmt = source.video_format

player = pyglet.media.Player()
player.queue(source)
player.play()

window = pyglet.window.Window(width=fmt.width, height=fmt.height)

@window.event
def on_draw():
    player.get_texture().blit(0, 0)

pyglet.app.run()