import pymunk, pygame
from userInterface import Label
from ps_settings import FPS, WIDTH, HEIGHT, S_POS, S_SIZE, COLORS, TITLEFONT, SUBTITLEFONT, FONT, labelHeight, imageSize, getImage
from Ball import Ball
from Obstacle import Square, Triangle, Circle, String

class Display():
    def __init__(self, surface, position, size, gravity):

        self.surface = surface
        self.position = position
        self.size = size

        self.objects = []
        self.bodies = []

        self.space = pymunk.Space()
        gravity = gravity * 100
        self.space.gravity = (0, gravity)

        self.initialization()

    def clear(self):
        for object in self.objects:
            if object.doesCollide:
                pymunk.Space.remove(self.space, object.shape)
                pymunk.Space.remove(self.space, object.body)
        self.objects.clear()

    def initialization(self):
        pass   

    def update(self):
        self.space.step(1/FPS)

    def run(self):
        self.update()

class Simulation1(Display):
    def __init__(self, surface, position, size, gravity):
        super().__init__(surface, position, size, gravity)

    def initialization(self):
        super().initialization()
        ballElasticity = 0.5
        ballRadius = 0.015 * HEIGHT
        ballPos = [WIDTH/2, ballRadius]
        ballVel = [5,-10]
        ballMass = 0.5
        ballColor = COLORS['BUTTONPRESSED']
        self.ball = Ball(self.surface, self.space, ballPos, ballVel, ballMass, ballRadius, ballColor, ballElasticity)

        squareElasticity = 0
        squareTopLeft = [0, 4*HEIGHT/5]
        squareSize = [WIDTH, HEIGHT/5]
        squareColor = COLORS['WHITESMOKE']
        self.square = Square(self.surface, self.space, squareTopLeft, squareSize, squareColor, squareElasticity)

        triangleElasticity = 0.5
        trianglePoints = [(0, HEIGHT/3), (0, 4*HEIGHT/5), (WIDTH, 4*HEIGHT/5)]
        triangleColor = COLORS['WHITESMOKE']
        self.triangle = Triangle(self.surface, self.space, trianglePoints, triangleColor, triangleElasticity)
    
    def run(self, display = False, start = False, reset = False, paused = False):
        if display:
            self.square.draw()
            self.triangle.draw()
            self.ball.draw()
            if start:
                if not paused:
                    super().run()
            if reset:
                self.clear()
                self.initialization()

class Simulation2(Display):
    def __init__(self, surface, position, size, gravity):
        super().__init__(surface, position, size, gravity)

    def initialization(self):
        super().initialization()

        groundPos = (S_POS[0], 4*HEIGHT/5)
        groundSize = (WIDTH - S_POS[0], HEIGHT/5)
        groundColor = COLORS['WHITE']
        groundE = 0.5
        self.square = Square(self.surface, self.space, groundPos, groundSize, groundColor, groundE, 1)
        self.objects.append(self.square)

        groundElevationPoints = [(S_POS[0], 4*HEIGHT/5), (S_POS[0], 3*HEIGHT/5), (S_POS[0] + 200, 4*HEIGHT/5)]
        groundElevationColor = COLORS['WHITE']
        groundElevationE = 0.8
        self.elevation = Triangle(self.surface, self.space, groundElevationPoints, groundElevationColor, groundElevationE, 10)
        self.objects.append(self.elevation)

        objectRadius = 30
        objectVel = [0,0]
        objectMass = 0.1
        objectPos = (S_POS[0] + objectRadius, 3*HEIGHT/5 - objectRadius)
        objectColor = COLORS['BUTTONPRESSED2']
        objectE = 0.2
        self.object = Ball(self.surface, self.space, objectPos, objectVel, objectMass, objectRadius, objectColor, objectE)
        self.objects.append(self.object)

    def run(self, display = False, start = False, reset = False, paused = False):
        if display:
            for object in self.objects:
                object.draw()
            if start:
                if not paused:
                    super().run()
            if reset:
                self.clear()
                self.initialization()

class Simulation3(Display):
    def __init__(self, surface, position, size, gravity):
        super().__init__(surface, position, size, gravity)

    def initialization(self):
        super().initialization()

        self.ballsCaracteristics = [[0.999, 0.03 * self.size[1], [self.position[0] + 0.03 * self.size[1], 0.03 * self.size[1]], [0,0], 1, COLORS['BUTTONPRESSED']], 
                                    [0.999, 0.05 * self.size[1], [self.position[0] + self.size[0] - 0.03 * self.size[1], 0.03 * self.size[1]], [0,0], 20, COLORS['BUTTONPRESSED']]]

        for b in self.ballsCaracteristics:
            ballElasticity = b[0]
            ballRadius = b[1]
            ballPos = b[2]
            ballVel = b[3]
            ballMass = b[4]
            ballColor = b[5]
            
            ball = Ball(self.surface, self.space, ballPos, ballVel, ballMass, ballRadius, ballColor, ballElasticity)
            self.objects.append(ball)

        groundPos = (S_POS[0], 4*HEIGHT/5)
        groundSize = (WIDTH - S_POS[0], HEIGHT/5)
        groundColor = COLORS['WHITE']
        groundE = 0.999
        self.square = Square(self.surface, self.space, groundPos, groundSize, groundColor, groundE, 1)
        self.objects.append(self.square)

        elevation1Pos = [(S_POS[0], 2*HEIGHT/5), (S_POS[0], 4*HEIGHT/5), (S_POS[0] + S_SIZE[0]/2, 4*HEIGHT/5)]
        elevation2Pos = [(WIDTH, 2*HEIGHT/5), (WIDTH, 4*HEIGHT/5), (S_POS[0] + S_SIZE[0]/2, 4*HEIGHT/5)]
        elevationColor = COLORS['WHITE']
        elevationE = 0
        self.elevation1 = Triangle(self.surface, self.space, elevation1Pos, elevationColor, elevationE)
        self.elevation2 = Triangle(self.surface, self.space, elevation2Pos, elevationColor, elevationE)
        self.objects.append(self.elevation1)
        self.objects.append(self.elevation2)

    def run(self, display = False, start = False, reset = False, paused = False):
        if display:
            for object in self.objects:
                object.draw()
            if start:
                if not paused:
                    super().run()
            if reset:
                self.clear()
                self.initialization()

class Simulation4(Display):
    def __init__(self, surface, position, size, gravity):
        super().__init__(surface, position, size, gravity)

    def initialization(self):
        super().initialization()

        self.ballsCaracteristics = [[0.999, 0.03 * self.size[1], [self.position[0] + int(self.size[0]/3), 0.03 * self.size[1]], [0,0], 1, COLORS['WHITESMOKE']], 
                                    [0.999, 0.05 * self.size[1], [self.position[0] + int(2*self.size[0]/3), 0.05 * self.size[1]], [0,0], 20, COLORS['WHITESMOKE']]]

        for b in self.ballsCaracteristics:
            ballElasticity = b[0]
            ballRadius = b[1]
            ballPos = b[2]
            ballVel = b[3]
            ballMass = b[4]
            ballColor = b[5]
            
            ball = Ball(self.surface, self.space, ballPos, ballVel, ballMass, ballRadius, ballColor, ballElasticity)
            self.objects.append(ball)

    def run(self, display = False, start = False, reset = False, paused = False):
        if display:
            for object in self.objects:
                object.draw()
            if start:
                if not paused:
                    super().run()
            if reset:
                self.clear()
                self.initialization()

class Pendulum1(Display):
    def __init__(self, surface, position, size, gravity):
        super().__init__(surface, position, size, gravity)

    def initialization(self):
        super().initialization()

        groundPos = (S_POS[0], 4*HEIGHT/5)
        groundSize = (WIDTH - S_POS[0], HEIGHT/5)
        groundColor = COLORS['WHITE']
        groundE = 0.9
        self.square = Square(self.surface, self.space, groundPos, groundSize, groundColor, groundE, 1)
        self.objects.append(self.square)

        baseSize = (int(groundSize[0]*0.2), int(groundSize[1]*0.15))
        basePos = [groundPos[0] + groundSize[0]/2 - baseSize[0]/2, groundPos[1] - baseSize[1]]
        baseColor = COLORS['DARKCIAN']
        baseE = 0.9
        self.base = Square(self.surface, self.space, basePos, baseSize, baseColor, baseE, 1)
        self.objects.append(self.base)

        columnSize = (int(groundSize[0]*0.01), int(HEIGHT*0.6))
        columnPos = [groundPos[0] + groundSize[0]/2 - columnSize[0]/2, groundPos[1] - baseSize[1] - columnSize[1]]
        columnColor = COLORS['WHITESMOKE']
        columnE = 0.9
        self.column = Square(self.surface, self.space, columnPos, columnSize, columnColor, columnE, 1)
        self.objects.append(self.column)

        jointPos = [columnPos[0] + columnSize[0]/2, columnPos[1]]
        jointRadius = (columnSize[0])*1.5
        jointColor = COLORS['GREEN']
        jointE = 0.5
        self.joint = Circle(self.surface, self.space, jointPos, jointRadius, jointColor, jointE, 1)

        ballPos = [columnPos[0] - int(columnSize[1]*0.75), columnPos[1]]
        ballRadius = columnSize[0]*3
        ballVel = [0,0]
        ballMass = 10
        ballColor = COLORS['GREEN']
        ballE = 0.999
        self.ball = Ball(self.surface, self.space, ballPos, ballVel, ballMass, ballRadius, ballColor, ballE)

        stringColor = COLORS['BUTTONPRESSED2']
        self.string = String(self.surface, self.space, stringColor, self.ball.body, jointPos, identifier='position')

        self.objects.append(self.string)
        self.objects.append(self.joint)       
        self.objects.append(self.ball)

    def run(self, display = False, start = False, reset = False, paused = False):
        if display:
            for object in self.objects:
                object.draw()
            if start:
                if not paused:
                    super().run()
            if reset:
                self.clear()
                self.initialization()

class Pendulum2(Display):
    def __init__(self, surface, position, size, gravity):
        super().__init__(surface, position, size, gravity)

    def initialization(self):
        super().initialization()

        groundPos = (S_POS[0], 4*HEIGHT/5)
        groundSize = (WIDTH - S_POS[0], HEIGHT/5)
        groundColor = COLORS['WHITE']
        groundE = 0.9
        self.square = Square(self.surface, self.space, groundPos, groundSize, groundColor, groundE, 1)
        self.objects.append(self.square)

        baseSize = (int(groundSize[0]*0.2), int(groundSize[1]*0.15))
        basePos = [groundPos[0] + groundSize[0]/2 - baseSize[0]/2, groundPos[1] - baseSize[1]]
        baseColor = COLORS['DARKCIAN']
        baseE = 0.9
        self.base = Square(self.surface, self.space, basePos, baseSize, baseColor, baseE, 1)
        self.objects.append(self.base)

        columnSize = (int(groundSize[0]*0.01), int(HEIGHT*0.6))
        columnPos = [groundPos[0] + groundSize[0]/2 - columnSize[0]/2, groundPos[1] - baseSize[1] - columnSize[1]]
        columnColor = COLORS['WHITESMOKE']
        columnE = 0.9
        self.column = Square(self.surface, self.space, columnPos, columnSize, columnColor, columnE, 1, doesCollide=False)
        self.objects.append(self.column)

        jointPos = [columnPos[0] + columnSize[0]/2, columnPos[1]]
        jointRadius = (columnSize[0])*1.5
        jointColor = COLORS['RED']
        jointE = 0.5
        self.joint = Circle(self.surface, self.space, jointPos, jointRadius, jointColor, jointE, 1)

        ballPos = [columnPos[0] - int(columnSize[1]*0.75), columnPos[1]]
        ballRadius = columnSize[0]*3
        ballVel = [0,0]
        ballMass = 10
        ballColor = COLORS['RED']
        ballE = 0.999
        self.ball = Ball(self.surface, self.space, ballPos, ballVel, ballMass, ballRadius, ballColor, ballE)

        stringColor = COLORS['BUTTONPRESSED2']
        self.string = String(self.surface, self.space, stringColor, self.ball.body, jointPos, identifier='position')

        self.objects.append(self.string)
        self.objects.append(self.joint)       
        self.objects.append(self.ball)

    def run(self, display = False, start = False, reset = False, paused = False):
        if display:
            for object in self.objects:
                object.draw()
            if start:
                if not paused:
                    super().run()
            if reset:
                self.clear()
                self.initialization()

class Learn(Display):
    def __init__(self, surface, position, size, currentChapter, currentPage):
        super().__init__(surface, position, size, 0)

        self.bg = COLORS['BACKGROUND']
        self.fg = COLORS['WHITESMOKE']

        self.boardRect = pygame.Rect(int(self.position[0] + self.size[0]*0.01), int(self.position[1] + self.size[0]*0.01), self.size[0]*0.98, self.size[1]*0.97)

        self.textBoxPos = (self.position[0] + self.size[0]*0.03, self.position[1] + self.size[1]*0.225)
        self.textBoxSize = (int(self.size[0] * 0.65), int(self.size[1]*0.8))
        self.labelSize = (self.textBoxSize[0], labelHeight)
        self.labelSpacing = 2.5
        self.imageBoxPos = (self.position[0] + self.size[0]*0.7, self.position[1] + self.size[1]*0.5)

        self.currentChapter = currentChapter
        self.currentPage = currentPage

        self.chapters = []
        self.pages1 = []
        self.pages2 = []
        self.textLabels = []

        self.title = 'Movimentos de Corpos Sujeitos a Ligações'
        self.titleSize = (int(self.textBoxSize[0] * 0.6), int(self.textBoxSize[1] * 0.05))
        self.subtitleSize = (int(self.titleSize[0]*0.5), int(self.titleSize[1]*0.5))

        # Chapter 1 - Movimentos de Corpos Sujeitos a Ligações
        self.subtitle1 = 'Forças Aplicadas e Forças de Ligação'
        self.forcesText = ['Forças Aplicadas - Estas forças atuam num corpo independentemente das ligações ou vínculos a que o corpo está sujeito.',
                           'Estas podem atuar à distância ou por contacto no corpo. São exemplos de forcas aplicadas as forças gravíticas, magnéticas,',
                            'elétricas, elásticas, etc.', '//', '//', '//', '//', '//', '//', '//', '//', '//', '//', '//', '//', '//',
                           'Forças de Ligação - Estas forças exercem-se pelo facto de um corpo estar sujeito a ligações ou vínculos e que restringem a trajetória do corpo.',
                           'A sua intensidade depende das forças aplicadas e, em situação de movimento, das características do movimento. São exemplos de forças de ligação',
                           'a tensão exercida por um fio sobre um corpo ao qual se encontra ligado, as reações normais de superfícies em contacto com um corpo e as forças de atrito.']
        self.images1 = [[getImage('peso.png'), (self.textBoxPos[0], self.textBoxPos[1] + (self.labelSize[1] + self.labelSpacing) * 3)], 
        [getImage('iman.jpg'), (self.textBoxPos[0] + imageSize[0] + 20, self.textBoxPos[1] + (self.labelSize[1] + self.labelSpacing) * 3)], 
        [getImage('normal.jpg'), (self.textBoxPos[0], self.textBoxPos[1] + (self.labelSize[1] + self.labelSpacing) * 19)],
        [getImage('fa.jpg'), (self.textBoxPos[0] + imageSize[0] + 20, self.textBoxPos[1] + (self.labelSize[1] + self.labelSpacing) * 19)]]

        self.pages1.append([self.subtitle1, self.forcesText, self.images1])

        self.subtitle2 = 'Força de Atrito entre Sólidos'
        self.FaText = [
        '- Se ao aplicarmos uma força horizontal, F, o bloco não se mover, é porque sobre o bloco atua uma força de atrito com a mesma direção e intensidade de F,',
        'mas de sentido contrário. Essa força é a força de atrito estático, Fae.', '//', 
        '- Se aumentarmos a intensidade da força aplicada, F, a força de atrito aumenta até que para uma determinada intensidade de F, o bloco começa a escorregar.',
        'Nesse instante, a força de atrito estático atingiu o seu valor máximo, designando-se por força máxima de atrito estático, FaeMax.', '//', 
        '- Quando o bloco começa a mover-se, a força de atrito diminui, passando a designar-se por força de atrito cinético, Fac.', '///', 'Fac < FaeMax', '//']

        self.graph1 = [getImage('graph1.png', (int(WIDTH * 750/1980), int(HEIGHT * 550/1080))), (self.textBoxPos[0] + self.textBoxSize[0]/2 - int(WIDTH * 750/1980)/2, self.textBoxPos[1] + (self.labelSize[1] + self.labelSpacing) * 9)]

        self.pages1.append([self.subtitle2, self.FaText, self.graph1])

        self.subtitle3 = 'Leis Empíricas para as Forças de Atrito Estático e Cinético'
        self.LawsText = ['Primeira Lei:', '//',
        '- A Força de atrito não depende da ÁREA APARENTE de contacto das superfícies. O atrito resulta das múltiplas interações a nível microscópico.', '//', '///',
        'Área Real ≠ Área Aparente', '//',
        'Segunda Lei:', '//',
        '- Quando duas superfícies em contacto estão em repouso relativo, a intensidade máxima de força de atrito estático é diretamente proporcional ao módulo da reação normal, N.',
        'A constante de proporcionalidade, μe, chama-se coeficiente de atrito estático.', '//', '///',
        'FaeMax = μe * N', '//', 
        '- Quando duas superfícies em contacto estão em movimento relativo, a intensidade da força de atrito cinético é diretamente porporcional ao módulo da reação normal, N.', '//',
        'A constante de proporcionalidade, μc, chama-se coeficiente de atrito cinético.', '//', '///',
        'Fac = μc * N', '//',
        'Os coeficientes, μe e μc, dependem da natureza dos materiais em contacto e do polimento das superfícies, sendo característico de cada par de materiais.', '//', '///',
        'μc < μe', '//', '//', '//', 'Força de Reação, R:', '//', 'R = N + Fa (Componente Vertical - Reação Normal (N), Componente Horizontal - Força de Atrito (Fa))']

        self.pages1.append([self.subtitle3, self.LawsText])

        self.subtitle4 = 'Movimento Circular num Plano Vertical - o Looping'
        self.graph2 = [getImage('looping.jpg', (int(WIDTH * 600/1980), int(HEIGHT * 350/1080))), ((self.imageBoxPos[0] - int(WIDTH * 600/1980)/4, self.imageBoxPos[1] - int(HEIGHT * 350/1080) - 50))]
        self.loopingText = ['- Em D:', 'FR (Força Resultante) está dirigida para o centro da trajetória circular, sendo:', '//',
        'FR = P + N, com FR = Fc e Ft = 0 (P, Peso; N, Reação Normal; Fc, Força Centrífuga; Ft, Força tangencial à trajetória)', '//',
        'Como P e N têm, em D, a mesma direção e sentido, podemos escrever:', '//',
        'Fc = P + N <=> m * (v2 / r) = m * g + N <=> N = m * ((v2 / r) - g)',
        '(v - módulo da velocidade do corpo em D; r - raio da curvatura do looping; g - acelaração gravítica; m - massa do corpo)', '//',
        'Como a pista nunca atrai o corpo, o valor da acelaração normal, N (em D), não pode ser menor que zero.',
        'Quando N = 0, o carro perde o contacto com a pista. Portanto:', '//',
        'N > 0 <=> m * ( (v2 / r) - g) > 0 <=> v2 / r > g <=> v > √(rg)', '(v - módulo da velocidade do corpo em D; r - raio da curvatura do looping; g - acelaração gravítica; m - massa do corpo)', '//',
        'Por isto, o carrinho tem de passar em D com uma velocidade mínima para não cair, velocidade essa que depende do raio da curvatura do looping.', '//', '//',
        '- Em B (posição mais baixa em que o carrinho se pode encontrar no looping):', 'FR tem de estar também dirigida para o centro da trajetória circular.', '//',
        'Fc = N - P <=> m * (v2 / r) = N - m * g <=> N = m * ((v2 / r) + g)', '(N - Reação Normal em B; v - módulo da velocidade do corpo em B: r - raio da curvatura do looping)', '//', '//', '//',
        'Velocidade Mínima em B para ultrapassar D', '//',
        'EmB = EmD <=> 0.5*m*vB2 = 0.5*m*vD2 + m*g*(2*r) <=> vB2 = vD2 + 4gr', '//',
        'Sendo vD2 > rg, então: vB2 > 5rg => vB > √(5rg)']

        self.pages1.append([self.subtitle4, self.graph2, self.loopingText])

        self.subtitle5 = 'Movimento Circular em Plano Horizontal'
        self.ConicPendulum = ['- Pêndulo Cónico: corpo suspenso por um fio inextensível e de massa desprezável, face à massa do corpo,',
        'que descreve um movimento circular uniforme num plano horizontal.', '//',
        'Como o movimento se faz num plano horizontal: az (acelaração no eixo z) = 0 e:', '//',
        'Tz - P = 0 <=> Tcosθ = mg <=> T = mg / cosθ', '//',
        'A tensão exercida pelo fio depende do ângulo θ:', '//',
        'Tn = m*an <=> Tsinθ = m(v2 / r) <=> T = (m*v2) / (r*sinθ)', '//',
        'Será que a tensão exercida pelo fio varia com a velocidade angular?', '//', 'Num movimento uniforme: v = ω*r.', 'Como r = l*sinθ:', '//',
        'T = (m*ω2*r2)/(r*sinθ) = (m*ω2*r)/sinθ = (m*ω2*l*sinθ)/sinθ = m*ω2*l <=> T = m*ω2*l']
        self.graph3 = [getImage('conicPendulum.jpg', (int(WIDTH * 450/1980), int(HEIGHT * 450/1080))), ((self.imageBoxPos[0] - int(WIDTH * 450/1980)/4, self.textBoxPos[1]))]

        self.pages1.append([self.subtitle5, self.ConicPendulum, self.graph3])

        self.subtitle6 = 'Curvas nas Estradas e Revelé'
        self.graph4 = [getImage('s_releve.jpg'), (self.imageBoxPos[0], self.textBoxPos[1] - int(self.textBoxSize[1]*0.1 + self.subtitleSize[1] + self.titleSize[1]))]
        self.graph5 = [getImage('releve.png'), (self.imageBoxPos[0], self.textBoxPos[1] - int(self.textBoxSize[1]*0.1 + self.subtitleSize[1] + self.titleSize[1]) + imageSize[1] + 50)]
        self.Revele = ['As curvas das estradas, normalmente, não são planas, têm relevé, isto é: uma certa inclinação. Porquê?', '//',
        'Consideremos, por exemplo, um automóvel a descrever uma curva circular plana, de raio R, com velocidade de módulo constante',
        '(consideramos a acelaração centrípeta do automóvel, ac, não nula e a tangencial, at, nula).', '//',
        'FR = Fc <=> Fc = P + N + Fa; Sendo P = - N, Fa = Fc.', '//',
        'FaMax = FcMax <=> μe * N = m(v2Max / r) <=> μe * mg = m(v2Max / r) <=> vMax = √(μe*r*g)', '//',
        'Esta é a velocidade máxima permitida ao automóvel para descrever a curva sem derrapar.',
        'Assim, esta depende do coeficiente de atrito estático e do raio da curva.', '//',
        'Desta vez consideremos a mesma curva, mas com revelé. Nesta situação, mesmo que o atrito fosse desprezável,',
        'o carro conseguiria descrever a curva, porque a reação normal tem uma componente centrípeta, Nx.', '//',
        'Nx = Fc <=> Nsinθ = m(v2 / r)',
        'Ny = P <=> Ncosθ = mg', '//',
        'Se dividirmos membro a membro as equações acima:', '//',
        '(sinθ / cosθ) = (v2 / r) / g <=> tanθ = (v2 / r*g) <=> v = √(r*g*tanθ)', '//',
        'Podemos concluir, assim, que existe uma relação entre a inclinação da curva, o seu raio de curvatura e a velocidade que deve ser considerada quando a estrada é projetada,',
        'de modo a acautelar situações em que não haja atrito significativo. A segurança do condutor é, desta forma, maior em curvas com revelé.']

        self.pages1.append([self.subtitle6, self.graph4, self.graph5, self.Revele])

        self.chapters.append([self.title,self.pages1])

        self.title1 = 'Centro de Massa e Momento Linear de Sistemas de Partículas'

        # Chapter 2 - Centro de Massa e Momento Linear de Sistemas de Partículas
        self.subtitle7 = 'Sistemas de Partículas e Corpo Rígido'
        self.sistemasText = ['Corpo Rígido - sistema de partículas que mantêm as suas posições relativas.', '//',
        'Centro de massa de um sistema de partículas', '- ponto onde se considera estar toda a massa do sistema e aplicada a resultante das forças que atuam no sistema.', '//', 
        'Placa Triangular', '   - CM: Ponto de interseção das 3 medianas;', '//', 'Placa Retangular', '   - CM: Ponto de interseção das duas diagonais;',
        '//', 'Esfera', '   - CM: Centro da esfera;', '//', 'Pirâmide e Cone', '   - CM: Ponto do eixo vertical que une o vértice com o centro da base a 1/4 da altura em relação à base;',
        '//', 'Anel Circular', '   - CM: Centro geométrico do anel;', '//', 'O centro de massa de um corpo com elevada simetria encontra-se no centro geométrico do corpo.']

        self.pages2.append([self.subtitle7, self.sistemasText])

        self.subtitle8 = 'Vetor posição, velocidade e acelaração do centro de massa; rCM, vCM, aCM'
        self.positionVectorText = [
        '- O vetor posição do centro de massa, rCM, de um sistema de N partículas é igual à média, ponderada pelas massas, dos vetores posição das partículas do sistema.',
        '//','//','//','//','//','//','//','//','//','//','//','//','//','//','//','//','//','//','//',
        '- O vetor velocidade do centro de massa, vCM, de um sistema de N partículas é igual à média, ponderada pelas massas, das velocidades das partículas do sistema.',
        '- O vetor acelação do centro de massa, aCM, de um sistema de N partículas é igual à média, ponderada pelas massas, das acelarações das partículas do sistema.']
        self.positionVector = [getImage('positionVector.png', (int(WIDTH * 550/1980), int(HEIGHT * 375/1080))), (self.textBoxPos[0] + self.textBoxSize[0]/2 - int(WIDTH * 500/1980)/2, self.textBoxPos[1] + (self.labelSize[1] + self.labelSpacing) * 2)]
        self.velAcVectors = [getImage('velAcVectors.png', (int(WIDTH * 300/1980), int(HEIGHT * 200/1080))), (self.textBoxPos[0] + self.textBoxSize[0]/2 - int(WIDTH * 300/1980)/2, self.textBoxPos[1] + (self.labelSize[1] + self.labelSpacing) * 8 + int(HEIGHT * 375/1080))]

        self.pages2.append([self.subtitle8, self.positionVectorText, self.positionVector, self.velAcVectors])

        self.subtitle9 = 'Momento Linear'
        self.momentumtext = [
        'Momento Linear de Partícula, p - grandeza física vetorial igual ao produto da massa pela velocidade da partícula.', '//', '//', '//', '//', '//', '//', '//', '//', '//', '//', 
        'Momento Linear de um Sistema de N Partículas, pSis - soma dos momentos lineares das partículas constituintes do sistema.',
        'É também igual ao produto da massa do sistema, M, pela velocidade do centro de massa, vCM, ou seja, é igual ao momento linear do centro de massa do sistema.']
        self.pic1 = [getImage('1 (1).jpg', (int(WIDTH * 250/1980), int(HEIGHT * 180/1080))), 
        (self.textBoxPos[0] + self.textBoxSize[0]/2 - int(WIDTH * 250/1980)/2, self.textBoxPos[1] + (self.labelSize[1] + self.labelSpacing) * 2)]
        self.pic2 = [getImage('1 (2).jpg', (int(WIDTH * 250/1980), int(HEIGHT * 180/1080))), 
        (self.textBoxPos[0] + self.textBoxSize[0]/2 - int(WIDTH * 250/1980)*1.5, self.textBoxPos[1] + (self.labelSize[1] + self.labelSpacing) * 14)]
        self.pic3 = [getImage('1 (10).jpg', (int(WIDTH * 500/1980), int(HEIGHT * 180/1080))), 
        (self.textBoxPos[0] + self.textBoxSize[0]/2 + int(WIDTH * 250/1980)/2, self.textBoxPos[1] + (self.labelSize[1] + self.labelSpacing) * 14)]

        self.pages2.append([self.subtitle9, self.momentumtext, self.pic1, self.pic2, self.pic3])

        self.subtitle10 = 'Segunda Lei de Newton Aplicada a um Sistema de Partículas'
        self.newtonSecLawText = [
        '- A resultante das forças exteriores que atuam sobre um sistema de partículas é igual ao produto da massa total do sistema pela acelaração do seu centro de massa.',
        '//', '//', '//', '//', '//', 'ou', 
        '- A resultante das forças exteriores que atuam sobre um sistema de partículas é igual à taxa de variação temporal do momento linear do sistema.',
        '//', '//', '//', '//', '//', '//', '//',
        'Lei da Conservação do Momento Linear - se a resultante das forças exteriores que atuam num sistema for nula, o momento linear do sistema permanece constante.',
        '//', '//', '//', '//', '//', '//', '//',
        'Numa colisão, em que a resultante das forças exteriores seja desprezável, há conservação do momento linear.']
        self.pic4 = [getImage('1 (8).jpg', (int(WIDTH * 150/1980), int(HEIGHT * 100/1080))), 
        (self.textBoxPos[0] + self.textBoxSize[0]/2 - int(WIDTH * 150/1980)/2, self.textBoxPos[1] + (self.labelSize[1] + self.labelSpacing) * 1.5)]
        self.pic5 = [getImage('1 (9).jpg', (int(WIDTH * 150/1980), int(HEIGHT * 120/1080))), 
        (self.textBoxPos[0] + self.textBoxSize[0]/2 - int(WIDTH * 150/1980)/2, self.textBoxPos[1] + (self.labelSize[1] + self.labelSpacing) * 8.5)]
        self.pic6 = [getImage('1 (11).jpg', (int(WIDTH * 350/1980), int(HEIGHT * 80/1080))), 
        (self.textBoxPos[0] + self.textBoxSize[0]/2 - int(WIDTH * 350/1980)/2, self.textBoxPos[1] + (self.labelSize[1] + self.labelSpacing) * 16.5)]
        self.pic7 = [getImage('1 (7).jpg', (int(WIDTH * 250/1980), int(HEIGHT * 120/1080))), 
        (self.textBoxPos[0] + self.textBoxSize[0]/2 - int(WIDTH * 250/1980)/2, self.textBoxPos[1] + (self.labelSize[1] + self.labelSpacing) * 24.5)]

        self.pages2.append([self.subtitle10, self.newtonSecLawText, self.pic4, self.pic5, self.pic6, self.pic7])

        self.subtitle11 = 'Colisões elásticas, inelásticas e perfeitamente inelásticas'
        self.collisionsText = [
        'Forças de Colisão - forças interiores ao sistema e, em geral, de intensidade muito superior à das forças exteriores. Daí estas últimas podem ser desprezadas.',
        'As colisões podem ser:',
        '- colisões elásticas ou perfeitamente elásticas - com conservação do momento linear e da energia cinética do sistema.', '//', '//', '//', '//', '//',
        '- colisões inelásticas - apenas com conservação do momento linear do sistema.', '//', '//', '//', '//', '//',
        'Quando numa colisão inelástica a energia cinética diminui o máximo possível, a colisão diz-se perfeitamente inelástica.',
        'Numa colisão perfeitamente inelástica, as partículas adquirem a mesma velocidade, isto é, as partículas seguem juntas.', '//', '//', '//', '//', '//', '//',
        'Coeficiente de Restituição, e - razão entre a velocidadede afastamento e a velocidade de aproximação. Mede, de certa forma, a elestecidade de uma colisão. Para uma colisão frontal é:',
        '//', '//', '//', '//', '//', '//', '//', '//',
        'Numa colisão elástica é e = 1, numa colisão inelástica é 0 < e < 1 e numa colisão perfeitamente inelástica é e = 0.'
        ]
        self.pic8 = [getImage('1 (6).jpg', (int(WIDTH * 350/1980), int(HEIGHT * 85/1080))), 
        (self.textBoxPos[0] + self.textBoxSize[0]/2 - int(WIDTH * 350/1980)/2, self.textBoxPos[1] + (self.labelSize[1] + self.labelSpacing) * 3.5)]
        self.pic9 = [getImage('1 (5).jpg', (int(WIDTH * 350/1980), int(HEIGHT * 95/1080))), 
        (self.textBoxPos[0] + self.textBoxSize[0]/2 - int(WIDTH * 350/1980)/2, self.textBoxPos[1] + (self.labelSize[1] + self.labelSpacing) * 9)]
        self.pic10 = [getImage('1 (4).jpg', (int(WIDTH * 350/1980), int(HEIGHT * 80/1080))), 
        (self.textBoxPos[0] + self.textBoxSize[0]/2 - int(WIDTH * 350/1980)/2, self.textBoxPos[1] + (self.labelSize[1] + self.labelSpacing) * 17)]
        self.pic11 = [getImage('1 (3).jpg', (int(WIDTH * 250/1980), int(HEIGHT * 150/1080))), 
        (self.textBoxPos[0] + self.textBoxSize[0]/2 - int(WIDTH * 250/1980)/2, self.textBoxPos[1] + (self.labelSize[1] + self.labelSpacing) * 23.5)]

        self.pages2.append([self.subtitle11, self.collisionsText, self.pic8, self.pic9, self.pic10, self.pic11])

        self.chapters.append([self.title1, self.pages2])

        self.graphs = [self.graph1, self.graph2, self.graph3, self.graph4, self.graph5,
                       self.images1, self.positionVector, self.velAcVectors, self.pic1, self.pic2, self.pic3, self.pic4, self.pic5, self.pic6, self.pic7,
                       self.pic8, self.pic9, self.pic10, self.pic11]

    def board(self):
        pygame.draw.rect(self.surface, self.bg, self.boardRect)
        pygame.draw.rect(self.surface, self.fg, self.boardRect, 2)

    def update(self, chapter, page):
        self.currentChapter = chapter
        self.currentPage = page

    def show(self, draw = False):
        if draw:

            self.board()

            for index, chapter in enumerate(self.chapters):

                if self.currentChapter == index:
                    Label(self.surface, chapter[0], background=self.bg, foreground=COLORS['BUTTONPRESSED2'], font=TITLEFONT).place(x=self.textBoxPos[0], y=self.textBoxPos[1] - int(self.textBoxSize[1]*0.1 + self.subtitleSize[1] + self.titleSize[1]))
                    pages = chapter[1]

                    for i, page in enumerate(pages):

                        if self.currentPage == i:
                            
                            center = False
                            for n, argument in enumerate(page):
                                if n == 0:
                                    Label(self.surface, argument, background=self.bg, foreground=COLORS['BUTTONPRESSED'], font=SUBTITLEFONT).place(x=self.textBoxPos[0], y=self.textBoxPos[1] - int(self.textBoxSize[1]*0.075 + self.subtitleSize[1]/2))
                                
                                elif not argument in self.graphs:
                                    for t, text in enumerate(argument):
                                        if not text == '//':
                                            if not text == '///':

                                                if center:
                                                    justify = 'center'
                                                    x = self.textBoxPos[0] + self.textBoxSize[0]/2
                                                    center = False
                                                else:
                                                    justify = 'left'
                                                    x = self.textBoxPos[0]

                                                y = self.textBoxPos[1] + (self.labelSize[1] + self.labelSpacing) * t

                                                Label(self.surface, text, background=self.bg, foreground=self.fg, font=FONT, justify=justify).place(x, y)

                                            else:
                                                center = True

                                else:
                                    if argument != self.images1:
                                        self.surface.blit(argument[0], argument[1])
                                        rect = argument[0].get_rect(topleft=argument[1])
                                        pygame.draw.rect(self.surface, COLORS['DARKCIAN'], rect, 3)
                                    else:
                                        for image in argument:
                                            self.surface.blit(image[0], image[1])
                                            rect = image[0].get_rect(topleft=image[1])
                                            pygame.draw.rect(self.surface, COLORS['DARKCIAN'], rect, 3)