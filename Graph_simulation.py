

def count_soldiers_alive(soldiers_A : list,soldiers_B : list,map):
    count_A = 0
    count_B = 0

    for i in range(map.get_row()):
        for j in range(map.get_col()):
            if map.battlefield[i][j]:
                if map.battlefield[i][j].army == 'A':
                    count_A += 1
                else:
                    count_B += 1
    soldiers_A.append(count_A)
    soldiers_B.append(count_B)
    return soldiers_A, soldiers_B


from matplotlib import pyplot
def plot_soldiers_alive(plot_title, iterations, soldiers_A, soldiers_B):
    pyplot.figure(figsize=(12,12))
    pyplot.title(plot_title, fontsize = 26)
    pyplot.xlabel('iterations',fontsize = 18)
    pyplot.ylabel('soldiers still alive',fontsize = 18)
    pyplot.xticks(fontsize = 15)
    pyplot.yticks(fontsize = 15)
    ax = pyplot.subplot()
    ax.plot(iterations,soldiers_A, label= 'type A soldier')
    ax.plot(iterations,soldiers_B, label= 'type B soldier')

