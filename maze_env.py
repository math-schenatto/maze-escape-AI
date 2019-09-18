import numpy as np
import time
import sys

if sys.version_info.major == 2:
    import Tkinter as tk
else:
    import tkinter as tk


UNIT = 40   # pixels
MAZE_H = 10  # grid height
MAZE_W = 10  # grid width


class Maze(tk.Tk, object):

    def __init__(self, controller):
        super(Maze, self).__init__()
        self.action_space = ['u', 'd', 'l', 'r']
        self.n_actions = len(self.action_space)
        self.title('Algoritmo Genético')
        self.geometry('{0}x{1}'.format(MAZE_H * 80, MAZE_H * 40))
        self.control = controller
        self._build_maze()


    def _build_maze(self):
        self.canvas = tk.Canvas(self, bg='blue',
                           height=MAZE_H * UNIT * 2,
                           width=MAZE_W * UNIT * 2)

        #Caixa de Texto
        ##################################################################
        self.tex = tk.Text(master=self.canvas, height=10, width=40)
        self.tex.place(x=430, y=200)

        # Botões e labels
        ##########################################################3
        self.title_app = tk.Label(self.canvas, text='Parâmetros', width=16, height=1)
        self.title_app.place(x=430,y=5)
        self.title_app.config(font=("Courier", 12))

        #População
        ########################################################################
        self.title_pop = tk.Label(self.canvas, text='Tam População:', width=12)
        self.title_pop.place(x=430, y=50)

        self.input_pop = tk.Entry(self.canvas, width=10)
        self.input_pop.place(x=530, y=50)
        self.input_pop.insert(tk.END, '2000')
        ###########################################################################

        #CrossOver
        ########################################################################
        self.title_cross = tk.Label(self.canvas, text='Crossover (%):', width=12)
        self.title_cross.place(x=430, y=73)

        self.input_cross = tk.Entry(self.canvas, width=10)
        self.input_cross.place(x=530, y=73)
        self.input_cross.insert(tk.END, '0.7')
        ###########################################################################

        #Mutação
        ########################################################################
        self.title_mut = tk.Label(self.canvas, text='Mutação (%):', width=12)
        self.title_mut.place(x=430, y=96)

        self.input_mut = tk.Entry(self.canvas, width=10)
        self.input_mut.place(x=530, y=96)
        self.input_mut.insert(tk.END, '0.2')
        ###########################################################################

        #Max generations
        ########################################################################
        self.title_max_generation = tk.Label(self.canvas, text='Max Geração:', width=12)
        self.title_max_generation.place(x=430, y=120)

        self.input_max_generation = tk.Entry(self.canvas, width=10)
        self.input_max_generation.place(x=530, y=120)
        self.input_max_generation.insert(tk.END, '500')
        ###########################################################################

        # Elitismo
        ########################################################################
        self.title_elitismo = tk.Label(self.canvas, text='Elitismo(0,1)', width=12)
        self.title_elitismo.place(x=430, y=143)

        self.input_elitismo = tk.Entry(self.canvas, width=10)
        self.input_elitismo.place(x=530, y=143)
        self.input_elitismo.insert(tk.END, '1')
        ###########################################################################

        #Botao iniciar
        ##################################################################
        self.btn_ini = tk.Button(self.canvas,
                                     text='Iniciar',
                                     width=10,
                                     command=(lambda
                                         text='teste':
                                         self.control.main_show_maze(
                                                                    self.input_pop.get(),
                                                                    self.input_cross.get(),
                                                                    self.input_mut.get(),
                                                                    self.input_max_generation.get(),
                                                                    self.input_elitismo.get()
                                        )
                                     )
                                 )
        self.btn_ini.place(x=430, y=170)
        ############################################################

        # Coins
        ##################################################################
        self.img = tk.PhotoImage(file="coin.gif").subsample(5)
        self.image = self.canvas.create_image(0, 80, anchor=tk.NW, image=self.img)
        self.image = self.canvas.create_image(200, 80, anchor=tk.NW, image=self.img)
        self.image = self.canvas.create_image(360, 0, anchor=tk.NW, image=self.img)
        self.image = self.canvas.create_image(80, 120, anchor=tk.NW, image=self.img)
        self.image = self.canvas.create_image(120, 160, anchor=tk.NW, image=self.img)
        self.image = self.canvas.create_image(0, 280, anchor=tk.NW, image=self.img)
        ##################################################################

        # create grids
        for c in range(0, MAZE_W * UNIT, UNIT):
            x0, y0, x1, y1 = c, 0, c, MAZE_W * UNIT
            self.canvas.create_line(x0, y0, x1, y1)
        for r in range(0, MAZE_H * UNIT, UNIT):
            x0, y0, x1, y1 = 0, r, MAZE_W * UNIT, r
            self.canvas.create_line(x0, y0, x1, y1)

        #Linhas externas
        self.line1 = self.canvas.create_line(3,396,396,396, width=5)
        self.line2 = self.canvas.create_line(3, 3, 396, 3, width=5)
        self.line3 = self.canvas.create_line(3, 3, 3, 360, width=5)
        self.line3 = self.canvas.create_line(398, 40, 398, 398, width=5)


        #Linhas horizontais
        self.line4 = self.canvas.create_line(40, 320, 40, 398, width=5)
        self.line5 = self.canvas.create_line(3, 240, 80, 240, width=5)
        self.line6 = self.canvas.create_line(3, 160, 120, 160, width=5)

        self.line7 = self.canvas.create_line(40, 40, 160, 40, width=5)
        self.line8 = self.canvas.create_line(40, 80, 200, 80, width=5)
        self.line9 = self.canvas.create_line(40, 120, 200, 120, width=5)

        self.line10 = self.canvas.create_line(40, 280, 120, 280, width=5)
        self.line11 = self.canvas.create_line(80, 320, 160, 320, width=5)
        self.line14 = self.canvas.create_line(80, 360, 160, 360, width=5)

        self.line12 = self.canvas.create_line(40, 200, 80, 200, width=5)
        self.line13 = self.canvas.create_line(160, 240, 360, 240, width=5)
        self.line15 = self.canvas.create_line(160, 280, 200, 280, width=5)

        self.line16 = self.canvas.create_line(240, 360, 360, 360, width=5)
        self.line17 = self.canvas.create_line(280, 320, 360, 320, width=5)
        self.line18 = self.canvas.create_line(320, 280, 400, 280, width=5)

        self.line19 = self.canvas.create_line(200, 200, 400, 200, width=5)
        self.line20 = self.canvas.create_line(160, 160, 320, 160, width=5)
        self.line21 = self.canvas.create_line(320, 120, 360, 120, width=5)

        self.line22 = self.canvas.create_line(320, 80, 400, 80, width=5)
        self.line23 = self.canvas.create_line(240, 40, 320, 40, width=5)
        self.line24 = self.canvas.create_line(240, 120, 280, 120, width=5)

        #Linhas verticais
        self.line25 = self.canvas.create_line(80, 320, 80, 360, width=5)
        self.line26 = self.canvas.create_line(160, 320, 160, 360, width=5)
        self.line27 = self.canvas.create_line(200, 320, 200, 400, width=5)

        self.line28 = self.canvas.create_line(240, 280, 240, 360, width=5)
        self.line29 = self.canvas.create_line(280, 240, 280, 320, width=5)
        self.line30 = self.canvas.create_line(160, 120, 160, 200, width=5)

        self.line31 = self.canvas.create_line(160, 240, 160, 280, width=5)
        self.line32 = self.canvas.create_line(120, 200, 120, 280, width=5)
        self.line33 = self.canvas.create_line(80, 160, 80, 200, width=5)

        self.line34 = self.canvas.create_line(40, 40, 40, 80, width=5)
        self.line35 = self.canvas.create_line(200, 3, 200, 80, width=5)
        self.line36 = self.canvas.create_line(240, 40, 240, 120, width=5)

        self.line37 = self.canvas.create_line(280, 80, 280, 120, width=5)
        self.line38 = self.canvas.create_line(320, 40, 320, 80, width=5)
        self.line39 = self.canvas.create_line(360, 0, 360, 40, width=5)

        self.line40 = self.canvas.create_line(360, 120, 360, 200, width=5)
        self.line41 = self.canvas.create_line(320, 120, 320, 160, width=5)

        # create origin
        origin = np.array([20, 380])


        # create red rect
        # self.rect = self.canvas.create_rectangle(
        #     origin[0] - 10, origin[1] - 10,
        #     origin[0] + 10, origin[1] + 10,
        #     fill='red')
        self.mario = tk.PhotoImage(file="mario.gif").subsample(2)
        self.rect = self.canvas.create_image(0,0,anchor=tk.NW, image=self.mario)
        self.canvas.move(self.rect, 10, 365)

        # pack all
        self.canvas.pack()

    def delete(self):
        self.tex.delete('1.0', tk.END)
    def escreve(self, conteudo):
        self.tex.insert(tk.END, conteudo)

    def reset(self):
        self.update()
        time.sleep(0.30)
        self.canvas.delete(self.rect)
        # origin = np.array([20, 380])
        # self.rect = self.canvas.create_rectangle(
        #     origin[0] - 10, origin[1] - 10,
        #     origin[0] + 10, origin[1] + 10,
        #     fill='red')
        # return observation
        self.rect = self.canvas.create_image(0,0,anchor=tk.NW, image=self.mario)
        self.canvas.move(self.rect, 10, 365)
        return self.canvas.coords(self.rect)

    def step(self, action):
        s = self.canvas.coords(self.rect)
        base_action = np.array([0, 0])
        if action == 2:   # up
            if s[1] > UNIT:
                base_action[1] -= UNIT
        elif action == 1:   # down
            if s[1] < (MAZE_H - 1) * UNIT:
                base_action[1] += UNIT
        elif action == 3:   # right
            if s[0] < (MAZE_W - 1) * UNIT:
                base_action[0] += UNIT
        elif action == 4:   # left
            if s[0] > UNIT:
                base_action[0] -= UNIT

        self.canvas.move(self.rect, base_action[0], base_action[1])  # move agent


    def render(self):
        time.sleep(0.1)
        self.update()


def update():
    for t in range(10):
        s = env.reset()
        while True:
            env.render()
            a = 1
            env.step(a)


if __name__ == '__main__':
    env = Maze()
    env.after(100, update)
    env.mainloop()
