# coding: utf-8


if __name__ == '__main__':
    N = int(input())
    d = []
    for _ in range(N):
        cmd = input().strip()
        if cmd != 'print':
            cmd = cmd.split()
            if len(cmd) > 1:
                for i, var in enumerate(cmd[1:], 1):
                    cmd[i] = int(var)
            getattr(d, cmd[0])(*cmd[1:])
        elif cmd == 'print':
            print(d)
