#include <bits/stdc++.h>

using namespace std;
ofstream flog("log_solution");
const int inf = 0x3f3f3f3f;

struct BigNum
{
    string num;
    BigNum() = default;
    BigNum(string x)
        : num(x)
        {}
    BigNum(const BigNum& other)
        : num(other.num)
        {}

    bool operator== (BigNum& other){
        return num == other.num;
    }
};

istream& operator>> (istream& input, BigNum& x){
    input >> x.num;
    return input;
}

ostream& operator<< (ostream& out, const BigNum& x){
    out << x.num;
    return out;
}

BigNum operator+ (BigNum& a, BigNum& b){
    int na = a.num.size(), nb = b.num.size();
    int n = max(na, nb);
    string res(n,'0');
    string sa = a.num, sb = b.num;
    reverse(sa.begin(), sa.end());
    reverse(sb.begin(), sb.end());
    int carry = 0;
    for (int i = 0; i < n; i++){
        int cur = sa[i]-'0'+sb[i]-'0'+carry;
        carry = cur/10;
        cur %= 10;
        res[i] = '0'+cur;
    }
    if (carry){
        res.push_back('0'+carry);
    }
    reverse(res.begin(), res.end());
    BigNum y(res);
    return y;

}

BigNum palindromic(BigNum x){
    string tmp = x.num;
    reverse(tmp.begin(), tmp.end());
    BigNum y(tmp);
    return y;
}


int main()
{
    ios::sync_with_stdio(false);
    // freopen(input, "r", stdin);
    // freopen(output, "w", stdout);
//     freopen("input", "r", stdin);
    int cnt = 0;
    BigNum x;
    cin >> x;
    for (; cnt < 10; cnt++){
        BigNum y = palindromic(x);
        if (x == y)
            break;
        cout << x << " + " << y << " = " << x+y << endl;
        x = x + y;
    }
    if (cnt < 10){
        cout << x << " is a palindromic number.\n";
    }
    else{
        cout << "Not found in 10 iterations.\n";
    }
    
    
    return 0;
}
