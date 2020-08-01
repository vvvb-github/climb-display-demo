from engine import *
from GUI import *

class Res(object):
    def __init__(self):
        self.sprite_res={
            'bg':Sprite('assets/bg.png',500,500,(50,100),-1),
            'tool_bar':Sprite('assets/default/button.png',500,80,(50,10))
        }
        self.ui_res={
            'stochastic_start':Button(100,50,(80,620),0,'随机爬山',20),
            'first_choice_start':Button(100,50,(250,620),0,'首选爬山',20),
            'random_start':Button(100,50,(420,620),0,'随机重启',20),
            'NQueue_info':Font('当前估价（冲突对数）=0',(180,20),20),
            'Count_info':Font('迭代次数=0',(250,60),20)
        }