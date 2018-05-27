from algorithm import get_prufer

def main():
    R = [1, 2, 3]
    D = [[0, 2, 3], [2, 0, 3], [3, 3, 0]]
    print(get_prufer(R, D))

if __name__ == '__main__':
    main()