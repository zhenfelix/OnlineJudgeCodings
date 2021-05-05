class Solution:
    def orchestraLayout(self, num: int, yPos: int, xPos: int) -> int:
        x = min(xPos,num-1-xPos)
        y = min(yPos,num-1-yPos)
        r = min(x,y)
        # print(x,y,r)
        cnt = 0
        cnt += 4*(num-r)*r 
        if yPos == r:
            cnt += xPos-r+1
        elif xPos+r == num-1:
            cnt += num-r*2-1
            cnt += yPos-r+1
        elif yPos+r == num-1:
            cnt += (num-r*2-1)*2
            cnt += (num-1-r-xPos+1)
        else:
            cnt += (num-r*2-1)*3
            cnt += (num-1-r-yPos+1)
        # print(cnt)
        return (cnt-1)%9 + 1




