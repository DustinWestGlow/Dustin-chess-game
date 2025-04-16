replay_index = 0
replay_sequence = []
with open('records/temp.txt', 'r') as file:
    replay_sequence
    replay_sequence.append("BEGINNING")
    for line in file:
        line = line.rstrip()
        non_numbered = line.split('/')[1]
        move_pair = non_numbered.split('.')
        print(move_pair)
        white = move_pair[0]
        replay_sequence.append(white)
        if move_pair[1] == '':
            break
        black = move_pair[1]
        replay_sequence.append(black)
    replay_sequence.append('END')
print(replay_sequence)

# TODO: "implement"
def make_move(code):
    print(code)

def replay_next():
    global replay_index
    if replay_index == (len(replay_sequence) - 1):
        return
    replay_index += 1
    m = replay_sequence[replay_index]
    if m == "END":
        return
    make_move(m)

def replay_prev():
    global replay_index
    if replay_index == 0:
        return
    replay_index -= 1
    m = replay_sequence[replay_index]
    if m == "BEGINNING":
        return
    make_move(m)