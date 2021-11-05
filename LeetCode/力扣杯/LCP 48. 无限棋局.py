dxy = [[0,1],[1,0],[1,1],[1,-1]]

class Solution:
    def gobang(self, pieces: List[List[int]]) -> str:
        board = {(x,y):p for x,y,p in pieces}

        def neighbor(layer, candidates):
            moves = set()
            for x,y in candidates:
                for dx, dy in dxy:
                    for flag in [-1,1]:
                        for i in range(1,layer+1):
                            xx = x + flag*i*dx  
                            yy = y + flag*i*dy  
                            if (xx,yy) not in board and (xx,yy) not in moves:
                                moves.add((xx,yy))      
            return moves

        def check(x,y,player):
            for dx, dy in dxy:
                cnt = 1
                xx, yy = x+dx, y+dy
                while (xx,yy) in board and board[xx,yy] == player:
                    xx += dx 
                    yy += dy
                    cnt += 1
                    if cnt >= 5:
                        return True
                xx, yy = x-dx, y-dy
                while (xx,yy) in board and board[xx,yy] == player:
                    xx -= dx 
                    yy -= dy
                    cnt += 1
                    if cnt >= 5:
                        return True
            return False

        moves_b1 = neighbor(1,[(x,y) for x,y,p in pieces if p == 0])
        if any(check(x,y,0) for x,y in moves_b1):
            return "Black"
        moves_w1 = neighbor(1,[(x,y) for x,y,p in pieces if p == 1])
        move_w = None
        for x, y in moves_w1:
            if check(x,y,1):
                if move_w:
                    return "White"
                move_w = (x,y)
        if move_w:
            moves_b1 = set([move_w])
        else:
            moves_b1 = neighbor(2,[(x,y) for x,y,p in pieces if p == 0])

        for x, y in moves_b1:
            board[x,y] = 0
            moves_b2 = neighbor(5,[(x,y)])
            if sum(check(xx,yy,0) for xx, yy in moves_b2) > 1:
                return "Black"
            del board[x,y]

        return "None"








































class Solution:
    def gobang(self, pieces: List[List[int]]) -> str:
        D = [(1, 0), (0, 1), (1, 1), (-1, 1)]
        board = {(x,y):c for x, y, c in pieces}

        # 枚举指定颜色棋子五子连线的所有方案（当前棋盘额外最多下两子）
        def findLines(color) :
            lines = DefaultDict(list)
            for x, y, c in pieces : # 枚举棋盘上所有指定颜色棋子的位置
                if c != color : continue
                for i, (dx, dy) in enumerate(D) : # 连线有四个方向
                    for k in range(3) : # 因为最多额外下两子，连线端点偏离已有棋子不超过2
                        nx, ny = x-dx*k, y-dy*k
                        head = (nx, ny, i)
                        if head in lines : continue # 该“端点&方向”已存在

                        for _ in range(5) : # 把该连线上剩下的落子位找到
                            c = board.get((nx, ny), -1)
                            if c != color :
                                if c >= 0 or len(lines[head]) >= 2 : # 该连线上有异色棋子，或空位过多，舍弃
                                    lines[head].clear()
                                    break
                                lines[head].append((nx, ny))
                            nx, ny = nx+dx, ny+dy

            # 按待落子数归类连线方案
            res = [[] for _ in range(3)]
            for v in lines.values() :
                if len(v) : res[len(v)].append(v)
            return res

        # 若黑棋存在一步致胜的方案，则黑胜
        black = findLines(0)
        if len(black[1]) > 0 : return "Black"

        white = findLines(1)
        positions = set(line[0] for line in white[1]) # 不同的连线可能包含相同的落子位，须去重
        # 若白棋存在多个一步制胜的落子位，则白胜
        if len(positions) > 1 : return "White"

        if len(positions) == 1 :
            # 若白棋存在一个一步制胜的落子位，则黑先手必须堵这个位置
            x, y = positions.pop()
            pieces.append([x, y, 0])
            board[(x, y)] = 0
            black = findLines(0)

            # 黑棋堵位后，黑棋存在多个一步制胜的落子位，则黑剩，否则平
            positions = set(line[0] for line in black[1])
            return "Black" if len(positions) > 1 else "None"

        # 若白棋不存在一步制胜的落子位，黑须落一子创造多于一个一步制胜的落子位才能在两步内获胜
        pairs = set((pair[0], pair[1]) for pair in black[2]) # 不同的连线可能包含相同的两个落子位，须去重
        positions = set()
        for p1, p2 in pairs :
            # 若某个落子位在之前落子对中已出现，下该位置能产生两个一步致胜的位置
            if p1 in positions or p2 in positions : return "Black"
            positions.add(p1)
            positions.add(p2)

        return "None"


作者：foxtail
链接：https://leetcode-cn.com/problems/fsa7oZ/solution/xiang-dui-qing-xi-jian-ji-yi-dian-de-xie-wwi4/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。