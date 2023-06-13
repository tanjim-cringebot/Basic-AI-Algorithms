import random

def get_student_id():
    return input("Enter your student id: ")

def get_value_range():
    return map(int, input("Minimum and Maximum value for the range of negative HP: ").split(' '))

def create_game_table(turn, branch):
    num_rows = (turn*2)+1
    table = [[]]

    for i in range(num_rows):
        for j in range(branch**i):
            table[i].append(0)

        if i < num_rows-1:
            table.append([])

    return table

def fill_last_row_with_random_numbers(table, rand_start, rand_end):
    last_row_index = len(table) - 1
    last_row_length = len(table[last_row_index])

    for i in range(last_row_length):
        table[last_row_index][i] = random.sample(range(rand_start, rand_end+1), 1)[0]

    return table

def apply_min_max_algorithm(table, turn, branch):
    curr_row_index = len(table) - 1
    for i in range(turn*2):
        start_index = 0

        if (i+1) % 2 != 0:
            for j in range(int((branch**curr_row_index)/branch)):
                end_index = start_index+branch-1
                sublist = table[curr_row_index][start_index:end_index+1]
                table[curr_row_index-1][j] = min(sublist)
                start_index = end_index+1
        else:
            for j in range(int((branch**curr_row_index)/branch)):
                end_index = start_index+branch-1
                sublist = table[curr_row_index][start_index:end_index+1]
                table[curr_row_index-1][j] = max(sublist)
                start_index = end_index+1
        curr_row_index = curr_row_index - 1

    return table

def count_leaf_node_comparisons(table, branch):
    leaf_nodes = table[-1]
    alpha = min(leaf_nodes[:branch])
    comparisons = branch
    index = branch

    for i in range(int((len(leaf_nodes)/branch)-1)):
        iterator = 0
        while iterator < branch:
            if alpha > leaf_nodes[index]:
                comparisons = comparisons + 1
                index = index+branch-iterator
                break
            else:
                comparisons = comparisons + 1
            index = index+1
            iterator = iterator+1
        if iterator == branch:
            start_index = (i+1)*branch
            alpha = min(leaf_nodes[start_index:index])

    return comparisons

def calculate_leftover_life(table, HP):
    return HP - table[0][0]

def run_game():
    student_id = get_student_id()
    rand_start, rand_end = get_value_range()

    num_turns = int(student_id[0])
    num_branches = int(student_id[2])
    HP = int(student_id[7] + student_id[6])

    game_table = create_game_table(num_turns, num_branches)
    game_table = fill_last_row_with_random_numbers(game_table, rand_start, rand_end)
    game_table = apply_min_max_algorithm(game_table, num_turns, num_branches)

    depth = num_turns*2
    leftover_life = calculate_leftover_life(game_table, HP)
    num_comparisons = count_leaf_node_comparisons(game_table, num_branches)

    print("1. Depth and Branches ratio is", depth, ":", num_branches)
    print("2. Terminal States(Leaf Nodes) are", game_table[-1])
    print("3. Left life(HP) of the defender after maximum damage caused by the attacker is ", calculate_leftover_life(game_table, HP))
    print("4. After Alpha-Beta Pruning Leaf Comparisons", num_comparisons)
  

run_game()
