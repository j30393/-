#include <bits/stdc++.h>
using namespace std;

vector<vector<int>> avaible_space(9,vector<int>(9,10));
int cycle_count = 0;
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

void count_avaible_space(vector<vector<int>>& board){
    for(int i=0;i<9;i++){
        for(int j=0;j<9;j++){
            if(board[i][j] != 0){
                avaible_space[i][j] = 0;
            }
            else{
                vector<int> total_posiblilty(11,1);
                for(int k=0;k<9;k++){
                    if(board[i][k] != 0){
                        total_posiblilty[board[i][k]] = 0;
                    }
                    if(board[k][j] != 0){
                        total_posiblilty[board[i][k]] = 0;
                    }
                }
                for(int k=0;k<3;k++){
                    for(int z=0;z<3;z++){
                        if( board[(i/3)*3+k][(j/3)*3+z] != 0){
                            total_posiblilty[board[(i/3)*3+k][(j/3)*3+z]] = 0;
                        }
                    }
                }
                int cnt = 0;
                for(int k=1;k<10;k++) cnt += total_posiblilty[k];
                avaible_space[i][j] = cnt;
            }
        }
    }
}

bool solve(vector<vector<int>>& board){
    int avaible = 0;  
    for(int i=0;i<9;i++){
        for(int j=0;j<9;j++){
            avaible += avaible_space[i][j];
        }
    }
    count_avaible_space(board);
    if(avaible == 0) return true;
    cycle_count += 1;
    pair<int,int> mini;
    int min = 10;
    for(int i=0;i<9;i++){
        for(int j=0;j<9;j++){
            if(avaible_space[i][j] < min && avaible_space[i][j] != 0){
                min = avaible_space[i][j];
                mini = std::make_pair(i,j);
            }
        }
    }

    for(int i=1;i<10;i++){
        if(safe(board,mini.first,mini.second,i)){
            /*ofstream myfile;
            myfile.open("example.txt",std::ios::app);
            myfile << mini.first << mini.second << " " <<  i <<endl;
            for(int j=0;j<9;j++){
                for(int k=0;k<9;k++){
                    myfile << board[j][k] << " ";
                }
                myfile << endl;
            }
            for(int j=0;j<9;j++){
                for(int k=0;k<9;k++){
                    myfile << avaible_space[j][k] << " ";
                }
                myfile << endl;
            }
            myfile.close();*/
            board[mini.first][mini.second] = i;
            if(solve(board)){
                return true;
            }
            board[mini.first][mini.second] = 0;
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
    cout << "\n\n" ;
    if(solve(board)){
        for(int i=0;i<9;i++){
            for(int j=0;j<9;j++){
                cout << board[i][j] << " ";
            }
            cout << endl;
        }
    }
    cout << "\n\n" << "cycle count = " << cycle_count ;
}