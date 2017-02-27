package test2;

public class Solution_MyOwnUnderstanding_string_to_integer_leetcode_8 {
	public int myAtoi( String str){
		int ans = 0;
		String tstr = str.trim();
		if (tstr.length() == 0) {return ans;} else{
			int pos = 0;
			int pn = 1;
			if ( tstr.charAt(0) == 43 ) {
				pn = 1;
				pos = 1;
			} else if ( tstr.charAt(0) == 45 ) {
				pn = -1;
				pos = 1;
			} else if ( tstr.charAt(0)<48 || tstr.charAt(0)>57) {
				return 0;
			}
		
		
			for (int i = pos; i < tstr.length() ; i++){
				if ( (int)tstr.charAt(i) > 47 && (int)tstr.charAt(i) < 58){
					if ( (long) ans * 10 + (long) pn * ( (int)tstr.charAt(i) - 48 ) <= 2147483647 && (long) ans * 10 + (long) pn * ( (int)tstr.charAt(i) - 48 ) >= -2147483648 ){
						ans = ans * 10 + pn * ( (int)tstr.charAt(i) - 48 );
					} else {return 0;}
					
				} else {return 0;}
			}
		
			return ans;
		}
		/*
		try {
            ans = Integer.parseInt(str);
            return ans;
        } catch (Exception e) {
            return ans;
        }
		*/
	}
}
