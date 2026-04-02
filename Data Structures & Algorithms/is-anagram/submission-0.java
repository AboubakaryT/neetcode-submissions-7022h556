class Solution {
    public boolean isAnagram(String s, String t) {

    char [] myArray = s.toCharArray();
    char [] mySecondArray = t.toCharArray();

    Arrays.sort(myArray);
    Arrays.sort(mySecondArray);

    if(Arrays.equals(myArray, mySecondArray)){
        return true;
    }
    return false;
    }
    }

