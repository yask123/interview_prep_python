class Solution {
private:
    int expandBothWays(string s, int st, int en) {
    	int len = s.length();
    	while(st>=0 && en<len && s[st]==s[en]) {
    		st--;
    		en++;
    	}
    	st++;
    	en--;
    	return en-st;
    }
public:
    string longestPalindrome(string s) {
        int len = s.length();
    	int res, start = 0, end = 0;
    	for(int i=0;i<len;i++) {
    		res = expandBothWays(s,i,i);
    		if(res>end-start) {
    			start = i - (res/2);
    			end = i + (res/2);
    		}
    		res = expandBothWays(s,i,i+1);
    		if(res>end-start) {
    			start = i - (res/2);
    			end = i+1+(res/2);
    		}
    	}
    	//cout << start << " " << end << endl;
    	return s.substr(start, end-start+1);
    }
};
