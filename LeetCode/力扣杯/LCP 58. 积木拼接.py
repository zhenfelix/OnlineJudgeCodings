class Solution:
    def composeCube(self, shapes: List[List[str]]) -> bool:
        # print(shapes)
        cube_base = [(0,0,1),(0,1,1),(1,1,1),(1,0,1),(1,0,1),(0,0,0)]
        cube_dr = [(0,0,-1),(0,0,-1),(0,0,-1),(0,0,-1),(-1,0,0),(1,0,0)]
        cube_dc = [(0,1,0),(1,0,0),(0,-1,0),(-1,0,0),(0,1,0),(0,1,0)]

        rotation_base = [(0,0),(0,1),(1,1),(1,0)]
        rotation_drc = [(1,1),(1,-1),(-1,-1),(-1,1)]

        n = len(shapes[0])
        states = [[[0]*n for _ in range(n)] for _ in range(n)]
        used = [False]*6

        edges = []
        for a in range(n):
            for b in range(n):
                if a in [0,n-1] or b in [0,n-1]:
                    edges.append((a,b))

        def doit(idx, s, r, flip, setting, debug = False):
            if debug:
                print('configuration parameters: ', idx, s, r, flip, setting)
            for a, b in edges:
                i = cube_base[idx][0]*(n-1) + cube_dr[idx][0]*a + cube_dc[idx][0]*b 
                j = cube_base[idx][1]*(n-1) + cube_dr[idx][1]*a + cube_dc[idx][1]*b
                k = cube_base[idx][2]*(n-1) + cube_dr[idx][2]*a + cube_dc[idx][2]*b
                
                sa = rotation_base[r][0]*(n-1) + rotation_drc[r][0]*(b if flip else a)
                sb = rotation_base[r][1]*(n-1) + rotation_drc[r][1]*(a if flip else b)
                if debug:
                    # print('cube detail: ',a,b,i,j,k)
                    print('rotation detail: ',a,b,sa,sb)
                
                if shapes[s][sa][sb] == '0':
                    continue
                if setting == 1:
                    states[i][j][k] = 1
                elif setting == -1:
                    states[i][j][k] = 0
                elif states[i][j][k] == 1:
                    return False
            return True

        def test_cube(s):
            print('testing cube')
            print(shapes[s])
            for idx in range(6):
                doit(idx,s,0,0,1,True)
                print(idx,states)
                print("setting done!\n")
                doit(idx,s,0,0,-1,True)
                print(idx,states)
                print("unsetting done!\n")
            print('testing cube done\n')
            return

        def test_rotation(s):
            print('testing rotation')
            print(shapes[s])
            for r in range(4):
                for flip in range(2):
                    doit(0,s,r,flip,1,True)
                    print(r,flip,states)
                    print("setting done!\n")
                    doit(0,s,r,flip,-1,True)
                    print(r,flip,states)
                    print("unsetting done!\n")
            print('testing rotation done\n')
            return

        def dfs(idx):
            if idx == 6:
                return True
            for s in range(6):
                if used[s]:
                    continue
                used[s] = True
                for r in range(4):
                    for flip in range(2):
                        if doit(idx, s, r, flip, 0):
                            doit(idx, s, r, flip, 1)
                            if dfs(idx+1):
                                return True
                            doit(idx, s, r, flip, -1)
                used[s] = False
            return False


        # test_cube(0)
        # test_rotation(0)

        if n**3-(n-2)**3 != sum(1 if ch == '1' else 0 for s in shapes for row in s for ch in row):
            return False

        used[0] = True
        for f in range(2):
            doit(0,0,0,f,1)
            if dfs(1):
                return True
            doit(0,0,0,f,-1)
        return False
            

