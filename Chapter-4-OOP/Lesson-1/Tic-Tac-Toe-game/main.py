import tkinter as tk

class TicTacToeGame:
    def __init__(self, master):
        self.master = master
        master.title("Tic-Tac-Toe")

        self.canvas_size = 300
        self.cell_size = self.canvas_size // 3

        self.canvas = tk.Canvas(master, width=self.canvas_size, height=self.canvas_size, bg="white")
        self.canvas.pack()

        self.turn = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]

        self.canvas.bind("<Button-1>", self.on_click)

        self.turn_label = tk.Label(master, text=f"Turn: Player {self.turn}", font=("Arial", 12))
        self.turn_label.pack()

        self.result_label = tk.Label(master, text="", font=("Arial", 12, "bold"))
        self.result_label.pack()

        self.restart_button = tk.Button(master, text="Restart Game", command=self.restart_game, bg="#f44336", fg="white", font=("Arial", 12, "bold"))
        self.restart_button.pack()

        self.draw_board()

    def draw_board(self):
        self.canvas.delete("all")

        for i in range(1, 3):
            self.canvas.create_line(i * self.cell_size, 0, i * self.cell_size, self.canvas_size, fill="black")
            self.canvas.create_line(0, i * self.cell_size, self.canvas_size, i * self.cell_size, fill="black")

        for i in range(3):
            for j in range(3):
                x1 = j * self.cell_size
                y1 = i * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="black")

                if self.board[i][j] == "X":
                    self.canvas.create_line(x1 + 10, y1 + 10, x2 - 10, y2 - 10, fill="blue", width=2)
                    self.canvas.create_line(x2 - 10, y1 + 10, x1 + 10, y2 - 10, fill="blue", width=2)
                elif self.board[i][j] == "O":
                    self.canvas.create_oval(x1 + 10, y1 + 10, x2 - 10, y2 - 10, outline="red", width=2)

    def on_click(self, event):
        if self.result_label["text"] != "":
            return

        row = event.y // self.cell_size
        col = event.x // self.cell_size

        if self.board[row][col] == "":
            self.board[row][col] = self.turn
            self.draw_board()

            if self.check_winner():
                self.result_label.config(text=f"Player {self.turn} wins!", fg="green")
            elif self.check_draw():
                self.result_label.config(text="It's a draw!", fg="black")
            else:
                self.change_turn()

    def change_turn(self):
        self.turn = "O" if self.turn == "X" else "X"
        self.turn_label.config(text=f"Turn: Player {self.turn}")

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "":
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != "":
                return True

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return True

        return False

    def check_draw(self):
        for row in self.board:
            for cell in row:
                if cell == "":
                    return False
        return True

    def restart_game(self):
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.result_label.config(text="")
        self.draw_board()
        self.turn = "X"
        self.turn_label.config(text=f"Turn: Player {self.turn}")

def main():
    root = tk.Tk()
    app = TicTacToeGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()

