class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::set<int> set;
        for (size_t i = 0; i < nums.size(); i++){
            if(set.contains(nums[i])){
                return true;
            }
            set.insert((nums[i]));
        }
        return false;
    }
};