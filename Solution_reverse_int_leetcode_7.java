package test2;

// The input is a valid int type.
// x = 123,  return 321
// x = -123, return -321

public class Solution_reverse_int_leetcode_7 {
	int reverse(int x){

		int[] bb = new int[12];
		int i = 0;
		while(x != 0){
			bb[i] = x % 10;
			i++;
			x = (int) (x / 10);
		}
		int pos = i - 1;
		int ans = 0;
		
		for (int j = 0; j <= pos; j++){
			if (((long)ans * 10 + (long)bb[j]) <= 2147483647 && ((long)ans * 10 + (long)bb[j]) >= -2147483648){
				ans = ans * 10 + bb[j];
			} else {
				return 0;
			}
		}
		return ans;
	
		/*
		int result = 0;                                        // a very clever solution

	    while (x != 0)
	    {
	        int tail = x % 10;
	        int newResult = result * 10 + tail;
	        if ((newResult - tail) / 10 != result)
	        { 
	        	System.out.println("Overflow happens!");
	        	return 0; }
	        result = newResult;
	        x = x / 10;
	    }

	    return result;
		*/
	}
}

