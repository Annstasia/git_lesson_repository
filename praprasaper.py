import pygame, random
pygame.init()
screen = pygame.display.set_mode((600, 600))


class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[-1] * width for _ in range(height)]
        self.left = 10
        self.top = 10
        self.cell_size = 30

    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self):
        for i in range(self.height):
            for j in range(self.width):
                if self.board[i][j] == 10:
                    color = pygame.Color('red')
                else:
                    color = pygame.Color('white')
                pygame.draw.rect(screen, (255, 255, 255),
                                 (self.left + j * self.cell_size, self.top + i * self.cell_size,
                                  self.cell_size, self.cell_size), 1)
                '''pygame.draw.circle(screen, color, (self.left + int((j + 0.5) * self.cell_size),
                                                                self.top + int((i + 0.5) * self.cell_size)),
                                    self.cell_size // 2 - 2)'''
                screen.fill(color, (self.left + int(j) * self.cell_size + 1,
                                    self.top + int(i) * self.cell_size + 1, self.cell_size - 1,
                                    self.cell_size - 1))

    def get_click(self, mouse_pos):
        cell = self.get_cell(mouse_pos)
        self.on_click(cell)

    def get_cell(self, mouse_pos):
        for i in range(self.height):
            for j in range(self.width):
                if self.left + j * self.cell_size < mouse_pos[0] < self.left + (j + 1) * self.cell_size and \
                        self.top + i * self.cell_size < mouse_pos[1] < self.top + (i + 1) * self.cell_size:
                    return self.left + j * self.cell_size, self.top + i * self.cell_size

    def on_click(self, coords):
        if coords != None:
            rowPressed = (coords[1] - self.top) // self.cell_size
            colPressed = (coords[0] - self.left) // self.cell_size
            self.board[rowPressed][colPressed] = (self.board[rowPressed][colPressed] + 1) % 2


class Minesweeper(Board):
    def __init__(self, width, height, number):
        super().__init__(width, height)
        for i in range(number):
            row, col = random.randint(len(self.board) - 1), random.randint(len(self.board[0]) - 1)
            while self.board[row][col] == 10:
                row, col = random.randint(len(self.board) - 1), random.randint(len(self.board[0]) - 1)
            self.board[row][col] = 10

    def open_cell(self):
        pass


saper = Minesweeper(300, 450, 10)
running = True
while running:
    for event in pygame.event.get():
        