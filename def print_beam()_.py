Chapter 3
def print_beam():
    print('+ - - - - ' * 2 + '+')

def print_post():
    print('|         ' * 2 + '|')

def print_row():
    print_beam()
    print_post()
    print_post()
    print_post()
    print_post()

def print_grid_2x2():
    print("--- Lưới 2x2 ---")
    print_row()
    print_row()
    print_beam() 
print_grid_2x2()
print("\n")


def print_beam_4():
    print('+ - - - - ' * 4 + '+')

def print_post_4():
    print('|         ' * 4 + '|')

def print_row_4():
    print_beam_4()
    print_post_4()
    print_post_4()
    print_post_4()
    print_post_4()

def print_grid_4x4():
    print("--- Lưới 4x4 ---")
    print_row_4()
    print_row_4()
    print_row_4()
    print_row_4()
    print_beam_4()

print_grid_4x4()
