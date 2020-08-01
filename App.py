import Game
import Resources
import Algorithm
from engine import *
from GUI import *

def position(i,j)->tuple:
    return (50+i*50,100+j*50)

class App(object):
    def __init__(self):
        self.game=Game.Game(600,700,'爬山法')
        self.timer=0
        self.n_queue=Algorithm.N_Queue()
        self.res=Resources.Res()
        #bind event handler
        self.res.ui_res['stochastic_start'].button_clicked=self.stochastic_start
        self.res.ui_res['first_choice_start'].button_clicked=self.first_choice_start
        self.res.ui_res['random_start'].button_clicked=self.random_start
        #load to pool
        self.game.static_ui_pool=[
            self.res.ui_res['stochastic_start'],
            self.res.ui_res['first_choice_start'],
            self.res.ui_res['random_start']
        ]
        self.game.static_sprite_pool = [
            self.res.sprite_res['tool_bar']
        ]
        for i in range(10):
            for j in range(10):
                if (i+j)%2==0:
                    self.game.static_sprite_pool.append(
                        Sprite('assets/bg.png',50,50,position(i,j))
                    )
                else:
                    self.game.static_sprite_pool.append(
                        Sprite('assets/bggrey.png', 50, 50, position(i, j))
                    )
        self.game.Render()
    def exec(self,tick_flip):
        self.dt=1000/tick_flip
        while True:
            self.game.clock.tick(tick_flip)
            self.game.Event_Handle()
            self.update()
    def update(self):
        self.timer+=self.dt
        if self.timer<1000:
            return
        else:
            self.timer=0
        if self.n_queue.next():
            self.res_upd()
    def res_upd(self):
        self.game.sprite_pool.clear()
        for i in range(10):
            if self.n_queue.colli_lst[i]:
                self.game.sprite_pool.append(
                    Sprite('assets/red.png',50,50,position(i,self.n_queue.pos[i]))
                )
            else:
                self.game.sprite_pool.append(
                    Sprite('assets/green.png', 50, 50, position(i, self.n_queue.pos[i]))
                )
        self.res.ui_res['NQueue_info'].set_content('当前估价（冲突对数）={0}'.format(self.n_queue.f))
        if self.n_queue.rst:
            self.res.ui_res['Count_info'].set_content('重启'.format(self.n_queue.cnt))
            self.res.ui_res['Count_info'].set_pos((300,60))
        else:
            self.res.ui_res['Count_info'].set_content('迭代次数={0}'.format(self.n_queue.cnt))
            self.res.ui_res['Count_info'].set_pos((250, 60))
        self.game.ui_pool=[
            self.res.ui_res['NQueue_info'],
            self.res.ui_res['Count_info']
        ]
        self.game.Render()

    def stochastic_start(self):
        self.n_queue.restart(0)
        self.res_upd()
        self.timer=0
    def first_choice_start(self):
        self.n_queue.restart(1)
        self.res_upd()
        self.timer=0
    def random_start(self):
        self.n_queue.restart(2)
        self.res_upd()
        self.timer=0