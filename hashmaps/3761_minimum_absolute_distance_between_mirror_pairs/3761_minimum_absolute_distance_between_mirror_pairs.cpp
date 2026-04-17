// u/algo-xero
using hashmap = unordered_map<int, int>;
class Solution {
public:
    int minMirrorPairDistance(vector<int>& nums) {
        int dist = INT_MAX;
        hashmap indices;
        for (int i = 0; i < nums.size(); ++i) {
            int key = nums[i];
            if (indices.count(key)) {
                dist = min(dist, abs(indices[key] - i));
            }
            indices[reverse(key)] = i;
        }
        return (dist == INT_MAX) ? -1 : dist;
    }
private:
    int reverse(int x) {
        int sum = 0, r = 0;
        while (x) {
            r = x % 10;
            sum = (sum * 10) + r;
            x /= 10;
        }
        return sum;
    }
};
