def findD(board):
    result = [0,0]
    boardArr = []
    for i in range(len(board)):
        flog = []
        for j in range(len(board[i])):
            flog.append(board[i][j])
            if board[i][j]=="R":
                result = [i,j]
        boardArr.append(flog)
    return [result,boardArr]
def bfs(board,start):
    maxX=len(board)
    maxY=len(board[0])
    stack = [[start[0],start[1],0]]
    movement = [[1,0],[-1,0],[0,1],[0,-1]]
    visit = [[True for i in range(maxY)] for j in range(maxX)]

    while len(stack) > 0:
        value=stack.pop(0)
        if board[value[0]][value[1]]=='G':
            return value[2]
        for move in movement:
            nextPos = [value[0],value[1]]
            while True:
                nextPos[0]+=move[0]
                nextPos[1]+=move[1]
                if (nextPos[0]<0 or nextPos[1]<0 or nextPos[0]>=maxX or nextPos[1]>=maxY) or board[nextPos[0]][nextPos[1]]=='D':
                    nextPos[0] -= move[0]
                    nextPos[1] -= move[1]
                    if visit[nextPos[0]][nextPos[1]]:
                        visit[nextPos[0]][nextPos[1]] = False
                        stack.append([nextPos[0],nextPos[1],value[2]+1])
                    break
    return -1
def solution(board):
    start=findD(board)
    answer = bfs(start[1],start[0])
    return answer
