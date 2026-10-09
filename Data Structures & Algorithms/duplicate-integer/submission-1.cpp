class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_set<int> store;
        for (int& num : nums) {
            if (!store.count(num)) {
                store.insert(num);
            }
            else {
                return true;
            }
        }
        return false;
    }
};