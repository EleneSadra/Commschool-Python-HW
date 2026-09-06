# დავალება #10 — ამოცანა 1: ლაბირინთი

# S -> საწყისი წერტილი
# E -> საბოლოო წერტილი
# # -> კედელი
# . -> გზა

# სწორი სვლა -> ვაგრძელებთ
# არასწორი სვლა -> თამაში თავიდან იწყება
# E-მდე მისვლა -> "შენ გაიარე ლაბირინთი"

# ვალიდაცია არაა საჭირო — ვვარაუდობთ, რომ მომხმარებელი სწორად წერს სიტყვებს.

maze = [
    ["S", ".", "#", ".", "."],
    ["#", ".", "#", ".", "#"],
    [".", ".", ".", ".", "."],
    ["#", "#", "#", ".", "#"],
    [".", ".", ".", ".", "E"],
]

# მიმართულება -> (რიგის ცვლილება, სვეტის ცვლილება)
DIRECTIONS = {
    "მაღლა":   (-1, 0),
    "დაბლა":   (1, 0),
    "მარცხნივ": (0, -1),
    "მარჯვნივ": (0, 1),
}


def show_maze(maze, row, col):
    # ბეჭდავს ლაბირინთს, მოთამაშის პოზიცია მონიშნულია.
    for r, line in enumerate(maze):
        display = []
        for c, cell in enumerate(line):
            display.append("@" if (r, c) == (row, col) else cell)
        print("   " + " ".join(display))


def find_start(maze):
    for r, line in enumerate(maze):
        for c, cell in enumerate(line):
            if cell == "S":
                return r, c
    raise ValueError("S ვერ მოიძებნა")


def play():
    while True:                       # გარე ციკლი — თამაშის თავიდან დაწყება
        row, col = find_start(maze)
        print("\n" + "=" * 40)
        print("ლაბირინთი იწყება!")
        print("=" * 40)

        while True:                   # შიდა ციკლი — ერთი მცდელობა
            show_maze(maze, row, col)
            move = input("\nრომელ მხარეს გინდა წასვლა? "
                         "(მაღლა / დაბლა / მარცხნივ / მარჯვნივ): ").strip()

            d_row, d_col = DIRECTIONS[move]
            new_row, new_col = row + d_row, col + d_col

            # საზღვრებს გარეთ გასვლა
            if not (0 <= new_row < len(maze) and 0 <= new_col < len(maze[0])):
                print("\n❌ ლაბირინთის გარეთ გახვედი! თამაში თავიდან.\n")
                break

            cell = maze[new_row][new_col]

            if cell == "#":
                print("\n❌ კედელს წააწყდი! თამაში თავიდან.\n")
                break

            row, col = new_row, new_col

            if cell == "E":
                show_maze(maze, row, col)
                print("\n🎉 შენ გაიარე ლაბირინთი!")
                return

            print("✅ სწორად მიდიხარ.")


if __name__ == "__main__":
    play()