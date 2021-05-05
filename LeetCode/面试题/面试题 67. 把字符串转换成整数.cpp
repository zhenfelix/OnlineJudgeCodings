class Solution {
public:
    int strToInt(string str) {
    	enum State
    	{
    		READY,
    		SYMBOL,
    		DIGIT
    	};
    	long long res = 0;
    	State s = READY;
    	bool positive = true;
    	for(char ch : str)
    	{
    		if (isdigit(ch))
    		{
    			res *= 10;
    			res += ch-'0';
    			if (positive && res > INT_MAX)
    				return INT_MAX;
    			if (!positive && -res < INT_MIN)
    				return INT_MIN;
    			s = DIGIT;
    		}
    		else
    		{
    			if (s == DIGIT)
    				break;
    			if (ch == '-' || ch == '+')
    			{
    				if (s == SYMBOL)
    					return 0;
    				if (ch == '-')
    					positive = false;
    				s = SYMBOL;
    			}
    			else if (ch == ' ')
    			{
    				if (s == SYMBOL)
    					return 0;
    			}
    			else
    				return 0;

    		}
    	}
    	if (!positive)
    		res = -res;
    	
    	return res;
    }
};