class Solution {
public:
    int climbStairs(int n) {
        if(n == 1){
            return 1;
        }

        int one = 1;
        int two = 2;

        for(int i = 0; i < n - 2; i++){
            int temp = one;
            one = two;
            two = one + temp;
            
        }

        return two;
    }
};
