def hanoi(n, start='A', temp='B', goal='C'):
    if n == 1:
        print(f'shift disk {1} from {start} to {goal}.')
        return
    hanoi(n-1, start, goal, temp)
    print(f'shift disk {n} from {start} to {goal}.')
    hanoi(n-1, temp, start, goal)

hanoi(int(input('n = ')), 'A', 'B', 'C')