class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        
        for(int i=0;i<9;i++){
            vector<bool> row(10,false),col(10,false),block(10,false);
            for(int j=0;j<9;j++){
                int tmp;
                tmp=board[i][j]-'0';
                if(tmp>=1&&tmp<=9){
                    if(row[tmp])return false;
                    else row[tmp]=true;
                }
                tmp=board[j][i]-'0';
                if(tmp>=1&&tmp<=9){
                    if(col[tmp])return false;
                    else col[tmp]=true;
                }
                tmp=board[(i/3)*3+j/3][(i%3)*3+j%3]-'0';
                if(tmp>=1&&tmp<=9){
                    if(block[tmp])return false;
                    else block[tmp]=true;
                }
            }
        }
        return true;
    }
};