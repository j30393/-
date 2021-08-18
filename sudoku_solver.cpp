#include <bits/stdc++.h>
using namespace std;
bool safe(vector<vector<int>>& board, int col , int row,int num){
    for(int i=0;i<9;i++)
        if(i != row && board[col][i] == num) return false;
    for(int i=0;i<9;i++)
        if(i != col && board[i][row] == num) return false;
    for(int i=0;i<3;i++){
        for(int j=0;j<3;j++){
            if( ((col/3)*3+i != col || (row/3)*3+j != row) && board[(col/3)*3+i][(row/3)*3+j] == num) return false;
        }
    }
    return true;
}
bool solve(vector<vector<int>>& board , int col , int row){

    if(row == 8 && col == 9){
        //cout << col << row << endl;
        return true;
    } 
    if(col == 9){
        col = 0;
        row++;
    }
        
    if(board[col][row] > 0) return(solve(board,col+1,row));
    if(board[col][row] == 0){
        for(int i=1;i<10;i++){
            if(safe(board,col,row,i)== true){
                board[col][row] = i;
                if(solve(board,col+1,row)){
                    return true;
                }
                board[col][row] = 0;
            }
        }
    }
    return false;
}
int main(){
    vector<vector<int>> board(9,vector<int>(9,0));
    for(int i=0;i<9;i++){
        for(int j=0;j<9;j++){
            cin >> board[i][j];
        }
    }
    if(solve(board,0,0)){
        for(int i=0;i<9;i++){
            for(int j=0;j<9;j++){
                cout << board[i][j] << " ";
            }
            cout << endl;
        }
    }
}