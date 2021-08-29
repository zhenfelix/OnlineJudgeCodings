class Complex{
public:
    int real, image;
    Complex() = default;
    Complex(string num)
        : real(0), image(0)
    {
        int idx = 0;
        while (num[idx] != '+')
            idx++;
        int flag = 1;
        for (int i = 0; i < idx; i++){
            if (num[i] == '-'){
                flag *= (-1);
                continue;
            }
            real = real*10 + (num[i]-'0');
        }
        real *= flag;
        flag = 1;
        for (int i = idx+1; i < num.size()-1; i++){
            if (num[i] == '-'){
                flag *= (-1);
                continue;
            }
            image = image*10 + (num[i]-'0');
        }
        image *= flag;
        // cout << real << ' ' << image << endl;
    }
    Complex operator * (Complex other){
        Complex c;
        c.real = real*other.real - image*other.image;
        c.image = real*other.image+image*other.real;
        return c;
    }
    string output(){
        string res;
        // if (real < 0)
        //     res.push_back('-');
        res += to_string(real);
        res.push_back('+');
        // if (image < 0)
        //     res.push_back('-');
        res += to_string(image);
        res.push_back('i');
        return res;
    }
};

class Solution {
public:
    string complexNumberMultiply(string num1, string num2) {
        Complex a(num1), b(num2);
        Complex c = a*b;
        return c.output();
        
    }
};




class Solution {
public:
    string complexNumberMultiply(string a, string b) {
        int ra, ia, rb, ib;
        char buff;
        stringstream aa(a), bb(b), ans;
        aa >> ra >> buff >> ia >> buff;
        bb >> rb >> buff >> ib >> buff;
        ans << ra*rb - ia*ib << "+" << ra*ib + rb*ia << "i";
        return ans.str();
    }
};