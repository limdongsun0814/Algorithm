def solution(m, n, board):
    answer = 0
    boardList=[]
    for j in range(n):
        flag = []
        for i in range(m):
            flag.append(board[i][j])
        boardList.append(flag)
    while True:
        cnt=check(boardList,m,n)
        if cnt == 0:
            break
        else:
            answer+=cnt
    return answer


def check(board,m,n):
    checkBoard = [[False for i in range(m)]for j in range(n)]
    result=0
    for i in range(n-1):
        for j in range(m-1):
            # print(i,j,board[i][j]==board[i+1][j]==board[i][j+1]==board[i+1][j+1])
            if board[i][j]==board[i+1][j]==board[i][j+1]==board[i+1][j+1]!="X":
                checkBoard[i][j]=True
                checkBoard[i+1][j]=True
                checkBoard[i][j+1]=True
                checkBoard[i+1][j+1]=True
    # print(checkBoard)
    for i in range(n):
        flag = []
        cnt=0
        for j in range(m):
            if checkBoard[i][j]:
                result+=1
                cnt+=1
            else:
                flag.append(board[i][j])
        board[i]=["X"]*cnt+flag
        
    # for i in board:
    #     print(i)
    # print()
    return result
                