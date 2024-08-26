class Character:
    def __init__(self, name, player, x, y):
        self.name = name
        self.player = player
        self.x = x
        self.y = y

    def move(self, direction, grid):
        pass

    def in_bounds(self, x, y):
        return 0 <= x < 5 and 0 <= y < 5

    def get_position(self):
        return self.x, self.y

    def set_position(self, x, y):
        self.x = x
        self.y = y

class Pawn(Character):
    def move(self, direction, grid):
        move_map = {'L': (0, -1), 'R': (0, 1), 'F': (-1, 0), 'B': (1, 0)}
        if direction in move_map:
            dx, dy = move_map[direction]
            new_x, new_y = self.x + dx, self.y + dy
            if self.in_bounds(new_x, new_y):
                return self.update_position(new_x, new_y, grid)
        return False

    def update_position(self, new_x, new_y, grid):
        if grid[new_x][new_y] is None or grid[new_x][new_y].player != self.player:
            grid[self.x][self.y] = None
            self.x, self.y = new_x, new_y
            grid[new_x][new_y] = self
            return True
        return False

class Hero1(Character):
    def move(self, direction, grid):
        move_map = {'L': (0, -2), 'R': (0, 2), 'F': (-2, 0), 'B': (2, 0)}
        if direction in move_map:
            dx, dy = move_map[direction]
            new_x, new_y = self.x + dx, self.y + dy
            if self.in_bounds(new_x, new_y):
                return self.update_position(new_x, new_y, grid)
        return False

    def update_position(self, new_x, new_y, grid):
        mid_x, mid_y = (self.x + new_x) // 2, (self.y + new_y) // 2
        if grid[mid_x][mid_y] is not None and grid[mid_x][mid_y].player != self.player:
            grid[mid_x][mid_y] = None  # Remove opponent's character in the path
        if grid[new_x][new_y] is None or grid[new_x][new_y].player != self.player:
            grid[self.x][self.y] = None
            self.x, self.y = new_x, new_y
            grid[new_x][new_y] = self
            return True
        return False

class Hero2(Character):
    def move(self, direction, grid):
        move_map = {'FL': (-2, -2), 'FR': (-2, 2), 'BL': (2, -2), 'BR': (2, 2)}
        if direction in move_map:
            dx, dy = move_map[direction]
            new_x, new_y = self.x + dx, self.y + dy
            if self.in_bounds(new_x, new_y):
                return self.update_position(new_x, new_y, grid)
        return False

    def update_position(self, new_x, new_y, grid):
        mid_x, mid_y = (self.x + new_x) // 2, (self.y + new_y) // 2
        if grid[mid_x][mid_y] is not None and grid[mid_x][mid_y].player != self.player:
            grid[mid_x][mid_y] = None  # Remove opponent's character in the path
        if grid[new_x][new_y] is None or grid[new_x][new_y].player != self.player:
            grid[self.x][self.y] = None
            self.x, self.y = new_x, new_y
            grid[new_x][new_y] = self
            return True
        return False

class Game:
    def __init__(self):
        self.grid = [[None for _ in range(5)] for _ in range(5)]
        self.players = {'A': [], 'B': []}
        self.current_player = 'A'

    def setup(self):
        print("Player A setup:")
        self.setup_player('A')
        print("Player B setup:")
        self.setup_player('B')

    def setup_player(self, player):
        positions = input(f"Enter the positions of {player}'s characters (e.g., P1 H1 H2 P2 P3): ").split()
        row = 0 if player == 'A' else 4
        for i, char in enumerate(positions):
            x, y = row, i
            if char[0] == 'P':
                self.players[player].append(Pawn(char, player, x, y))
            elif char[0:2] == 'H1':
                self.players[player].append(Hero1(char, player, x, y))
            elif char[0:2] == 'H2':
                self.players[player].append(Hero2(char, player, x, y))
            self.grid[x][y] = self.players[player][-1]

    def display_grid(self):
        for row in self.grid:
            print(' '.join(['.' if cell is None else cell.player + '-' + cell.name for cell in row]))
        print()

    def play(self):
        while True:
            self.display_grid()
            move = input(f"Player {self.current_player}, enter your move: ")
            if not self.process_move(move):
                print("Invalid move, try again.")
                continue
            if self.check_win():
                self.display_grid()
                print(f"Player {self.current_player} wins!")
                break
            self.current_player = 'B' if self.current_player == 'A' else 'A'

    def process_move(self, move):
        try:
            char_name, direction = move.split(':')
            for char in self.players[self.current_player]:
                if char.name == char_name:
                    return char.move(direction, self.grid)
        except:
            pass
        return False

    def check_win(self):
        opponent = 'B' if self.current_player == 'A' else 'A'
        return all(self.grid[char.x][char.y] is None for char in self.players[opponent])

if __name__ == "__main__":
    game = Game()
    game.setup()
    game.play()
