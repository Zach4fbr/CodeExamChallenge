import matplotlib.pyplot as plt

def Queulorior(inst):
    L = [0]*len(inst)
    L[0] = [0,0]
    for i in range(1,len(inst)):
        if inst[i] == 'N':
            L[i] = [L[i-1][0],L[i-1][1]+1]
        if inst[i] == 'E':
            L[i] = [L[i-1][0]+1,L[i-1][1]]
        if inst[i] == 'O':
            L[i] = [L[i-1][0]-1,L[i-1][1]]
        if inst[i] == 'S':
            L[i] = [L[i-1][0],L[i-1][1]-1]
    X = [L[i][0] for i in range(len(inst))]
    Y = [L[i][1] for i in range(len(inst))]
    plt.plot(X,Y)
    plt.show()

Queulorior("NNEESOOESEENNEEOOSEOSEEENNESENSSENNEESSOOEEENNEEOOSEOSEEENEENOOEESOOSEEEEEEENONSESENNSSENNEESSOOEEENNSSEENNSSEEENOONEEOOSEESEEEENNEESSOOEEENNEESOOEESENNESENSSEEENOONEEOOSEESEEEENNSSEEENNEESOOEESEEEENNEEOOSEOSEEENNEESSOOEEENNEESOOESEENNEEOOSEOSEEEENNOEEOSSEEEEENNEESOOEESOOEEENNEESOOESEENNSSEENNSSENNESNESSENNEEOOSEOSEEENNSSEENNSSEEENOONEEOOSEESENNEEOOSEOSEEEEEENNEESSOOEEENNEEOOSEOSEEENNESNESSENNEESOOEESENNSSENNESENSS")

