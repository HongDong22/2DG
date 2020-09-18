from pico2d import *

open_canvas()

gra = load_image('../res/grass.png')
cha = load_image('../res/run_animation.png')


frame = 0
for x in range(0,800,2):
    clear_canvas()
    
    gra.draw(400, 30)
    cha.clip_draw(frame * 100, 0, 100, 100, x, 80)
    
    update_canvas()
    
    frame = (frame + 1) % 8
    delay(0.05)
    get_events()
    
close_canvas()
