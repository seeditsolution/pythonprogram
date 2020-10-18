class Solution(object):
    def isValidSudoku(self, board):
        for i in range(9):
            valid=[True]*10
            for j in range(9):
                if board[i][j]==0:
                    continue
                if valid[board[i][j]]:
                    valid[board[i][j]]=False
                else:
                    return False
            valid=[True]*10
            for j in range(9):
                if board[j][i]==0:
                    continue
                if valid[board[j][i]]:
                    valid[board[j][i]]=False
                else:
                    return False
        for i in range(3):
            for j in range(3):
                valid=[True]*10
                for k in range(i*3,(i+1)*3):
                    for l in range(j*3,(j+1)*3):
                        if board[k][l]==0:
                            continue
                        if valid[board[k][l]]:
                            valid[board[k][l]]=False
                        else:
                            return False
        return True

    def solve(self, board0):
        board=[]
        for i in range(9):
            board.append([])
            for j in range(9):
                board[i].append(board0[i][j])
        while True:
            tot=0
            valid=[]
            for i in range(9):
                valid.append([])
                for j in range(9):
                    if board[i][j]>0:
                        valid[i].append([])
                        tot+=1
                    else:
                        valid[i].append([k for k in range(1,10)])
            if tot==81:
                return board
            for i in range(9):
                for j in range(9):
                    if board[i][j]>0:
                        for k in range(9):
                            if board[i][j] in valid[i][k]:
                                del valid[i][k][valid[i][k].index(board[i][j])]
                            if board[i][j] in valid[k][j]:
                                del valid[k][j][valid[k][j].index(board[i][j])]
                        row=i/3
                        column=j/3
                        for k in range(row*3,(row+1)*3):
                            for l in range(column*3,(column+1)*3):
                                if board[i][j] in valid[k][l]:
                                    del valid[k][l][valid[k][l].index(board[i][j])]
            count=[]
            tot2=0
            x=0
            y=0
            flag=10
            for i in range(9):
                count.append([])
                for j in range(9):
                    count[i].append(len(valid[i][j]))
                    tot2+=len(valid[i][j])
                    if len(valid[i][j])<flag and len(valid[i][j])!=0:
                        x=i
                        y=j
                        flag=len(valid[i][j])
                    if len(valid[i][j])==1:
                        board[i][j]=valid[i][j][0]
            if tot2==0:
                return None
            if not self.isValidSudoku(board):
                return None
            if flag>1:
                board2=[]
                for i in range(9):
                    board2.append([])
                    for j in range(9):
                        board2[i].append(board[i][j])
                for i in range(flag):
                    board2[x][y]=valid[x][y][i]
                    board3=self.solve(board2)
                    if board3!=None:
                        return board3
                return None

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        board2=[]
        for i in range(9):
            board2.append([])
            for j in range(9):
                if board[i][j]=='.':
                    board2[i].append(0)
                else:
                    board2[i].append(int(board[i][j]))
        board2=self.solve(board2)
        for i in range(9):
            for j in range(9):
                board[i][j]=str(board2[i][j])
