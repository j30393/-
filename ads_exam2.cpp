#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

vector<int> people;
vector<int> combination;

void pretty_print(const vector<int>& v) {
  static int count = 0;
  cout << "combination no " << (++count) << ": [ ";
  for (int i = 0; i < v.size(); ++i) { cout << v[i] << " "; }
  cout << "] ";
  int sum = 0;
  for (int i = 0; i < v.size(); ++i){
      sum += pow(v[i],2); 
  }
  cout << " the sum is " << sum << endl; 
  for(int i=5 ; i< 20 ; i++){
      if(sum == pow(i,2)){
        cout << "find it " << endl;
      }
  }
}

void go(int offset, int k) {
  if (k == 0) {
    pretty_print(combination);
    return;
  }
  for (int i = offset; i <= people.size() - k; ++i) {
    combination.push_back(people[i]);
    go(i+1, k-1);
    combination.pop_back();
  }
}

int main() {
  int n = 9, k = 5;

  for (int i = 0; i < n; ++i) { people.push_back(i+1); }
  go(0, k);

  return 0;
}
