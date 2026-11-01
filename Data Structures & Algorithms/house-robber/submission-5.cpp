class Solution {
public:
    int rob(vector<int>& nums) {
        map<tuple<int, int> ,int> memo;
        return dfs(0,0,nums,memo);
    }

    int dfs(int i, int amount, vector<int> &nums, map<tuple<int,int>, int> &memo){
        if (i >= nums.size()){
            return amount;
        }
        
        tuple<int,int> state{i, amount};

        if (memo.contains(state)){
            return memo[state];
    }   
        int res1 = dfs(i+1, amount, nums, memo);
        int res2 = dfs(i+2, amount+nums[i], nums, memo);
        memo[state] = max(res1,res2);
        return max(res1,res2);

        }
};
