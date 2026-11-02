class Solution {
public:
    int rob(vector<int>& nums) {
        if(nums.size() == 1){
            return nums[0];
        }
        map<tuple<int,bool>, int> memo;
        return max(dfs(0, memo, nums, true), dfs(1,memo,nums,false));
        
    }
    int dfs(int i, map<tuple<int, bool>, int> &memo, vector<int> &nums, bool first){
        if (i >= nums.size() || first && i == nums.size() - 1){
            return 0;
        }
        tuple<int,bool> state{i,first};
        if(memo.contains(state)){
            return memo[state];
        }
        int skip = dfs(i+1, memo, nums, first);
        int take = nums[i] + dfs(i+2, memo, nums, first);
        

        memo[state] = max(take,skip);
        
        return max(take,skip);
    }
};
