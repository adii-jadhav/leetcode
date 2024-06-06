#include <vector>
#include <map>
using namespace std;

class Solution {
public:
    bool isNStraightHand(vector<int>& hand, int groupSize) {
        int n = hand.size();
        map<int, int> hsh;

        for(auto val: hand){
            hsh[val]++;
        }

        if(n % groupSize != 0) return false;

        while(!hsh.empty()){
            int minVal = hsh.begin()->first;
            for(int i = 0; i < groupSize; i++){
                int currentVal = minVal + i;
                if(hsh.find(currentVal) == hsh.end()) return false;
                if(hsh[currentVal] == 1) hsh.erase(currentVal);
                else hsh[currentVal]--;
            }
        }
        return true;
    }
};