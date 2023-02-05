from userInterface import Interface
from ps_settings import S_POS, S_SIZE, bg
from Display import Simulation1, Simulation2, Simulation3, Simulation4, Pendulum1, Pendulum2, Learn

class PhysicsSimulator():
    def __init__(self, surface):
        self.surface = surface

        self.interface = Interface(self.surface)
        self.simulations = []

        learnSize = S_SIZE
        learnPos = S_POS
        self.learn = Learn(self.surface, learnPos, learnSize, self.interface.currentChapter, self.interface.currentPage)

        Simulation1Gravity = 9.81
        self.simulation1 = Simulation1(self.surface, S_POS, S_SIZE, Simulation1Gravity)
        self.simulations.append(self.simulation1)

        Simulation2Gravity = 9.81
        self.simulation2 = Simulation2(self.surface, S_POS, S_SIZE, Simulation2Gravity)
        self.simulations.append(self.simulation2)

        Simulation3Gravity = 9.81
        self.simulation3 = Simulation3(self.surface, S_POS, S_SIZE, Simulation3Gravity)
        self.simulations.append(self.simulation3)

        Simulation4Gravity = 9.81
        self.simulation4 = Simulation4(self.surface, S_POS, S_SIZE, Simulation4Gravity)
        self.simulations.append(self.simulation4)

        pendulum1Gravity = 9.81
        self.Pendulum1 = Pendulum1(self.surface, S_POS, S_SIZE, pendulum1Gravity)
        self.simulations.append(self.Pendulum1)

        pendulum2Gravity = 9.81
        self.Pendulum2 = Pendulum2(self.surface, S_POS, S_SIZE, pendulum2Gravity)
        self.simulations.append(self.Pendulum2)

        self.inputs = [self.interface.learnClicked, self.interface.simulation]

    def update(self):

        counter = 0
        for input in self.inputs:
            if input != self.interface.simulation:
                if not input:
                    counter += 1
                else:
                    break
            else:
                for simulation in self.interface.simulation:
                    if not simulation[0]:
                        counter += 1
                    else:
                        break

        if counter == len(self.inputs) - 1 + len(self.interface.simulation):
            self.surface.blit(bg, S_POS)

        self.learn.update(self.interface.currentChapter, self.interface.currentPage)
        self.learn.show(self.interface.learnClicked)

        for index, simulation in enumerate(self.simulations):
            simulation.run(self.interface.simulation[index][0], self.interface.simulation[index][1], self.interface.simulation[index][2], self.interface.simulation[index][3])
            if self.interface.simulation[index][2]:
                self.interface.simulation[index][2] = False
        
        self.interface.update()
        self.interface.draw()
