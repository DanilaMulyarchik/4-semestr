def parser():
    f = open('data')
    lines = f.readlines()
    f.close()
    for i in range(len(lines)):
        lines[i] = lines[i][0:len(lines[i])-1:1]
    rez = []

    for i in range(len(lines)):
        line = list(lines[i].split(','))
        rez.append(tuple(line))
    return rez


def write(row_data: list):

    f = open('data', 'w')
    s = ''
    for i in range(len(row_data)):
        for j in range(len(row_data[i])):
            s += row_data[i][j] + ','
        s = s[0:len(s)-1:1] + '\n'
        f.write(s)
        s = ''
    f.close()
    return parser()
