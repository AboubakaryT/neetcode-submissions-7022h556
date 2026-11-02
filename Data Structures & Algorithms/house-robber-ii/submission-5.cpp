class Solution {
public:
    int rob(vector<int>& nums) {
        if(nums.size() == 1){
            return nums[0];
        }
        map<tuple<int,int,bool>, int> memo;
        return max(dfs(0,0, memo, nums, true), dfs(1,0,memo,nums,false));
        
    }
    int dfs(int i, int amount, map<tuple<int,int,bool>, int> &memo, vector<int> &nums, bool first){
        if (i >= nums.size() || first && i == nums.size() - 1){
            return amount;
        }
        tuple<int,int,bool> state{i, amount,first};
        if(memo.contains(state)){
            return memo[state];
        }
        int take = dfs(i+1, amount, memo, nums,first);
        int skip = dfs(i+2, amount+nums[i], memo, nums, first);
        

        memo[state] = max(take,skip);
        
        return max(take,skip);
    }
};
