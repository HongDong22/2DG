from pico2d import *

def handle_events():
    global running,dx,x,y
    evts = get_events()
    for e in evts:
        if e.type ==SDL_QUIT:
            running = False
        elif e.type == SDL_KEYDOWN:
            if e.key == SDLK_ESCAPE:
                running = FALSE
            elif e.key ==SDLK_LEFT:
                dx -= 1
            elif e.key ==SDLK_RIGHT:
                dx += 1
        elif e.type ==SDL_KEYUP:
            if e.key == SDLK_LEFT:
                dx += 1
            elif e.key == SDLK_RIGHT:
                dx -= 1
        elif e.type == SDL_MOUSEMOTION:
            x,y =e.x,get_canvas_height()-e.y -1
   

open_canvas()
gra = load_image('../res/grass.png')
cha = load_image('../res/run_animation.png')

running = True
x= get_canvas_width()
y=get_canvas_width()
dx = 0
frame = 0
while running:

    clear_canvas()
    
    gra.draw(400, 30)
    cha.clip_draw(frame * 100, 0, 100, 100, x, y)
    
    update_canvas()

    x += dx*5
    frame = (frame + 1) % 8

    handle_events()
   
    delay(0.05)
    
close_canvas()
