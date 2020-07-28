#include <vector>
using namespace std;

vector<int> twoNumberSum(vector<int> array, int targetSum) {
  vector<int> answer;
	unordered_map<int, bool> hash;
	int n = array.size();
	for(int i=0;i<n;i++) {
		int x = array[i];
		int y = targetSum - x;
		if(hash.find(y) != hash.end()) {
			answer.push_back(x);
			answer.push_back(y);
		}
		else 
			hash[x] = true;
	}
  return answer;
}
