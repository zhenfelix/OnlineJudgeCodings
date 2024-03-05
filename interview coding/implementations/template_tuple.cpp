// https://zhuanlan.zhihu.com/p/596673583
#include <string>
#include <vector>
#include <iostream>

using namespace std;

template<typename ...Ty>struct Tuple;
template<>struct Tuple<> {
    template <class... Ty>
    bool equal(const Tuple<>& rhs)const {
        return true;
    }
};
template<typename Ty1, typename ...Ty2>
struct Tuple<Ty1, Ty2...> : Tuple<Ty2...> {
    Ty1 val;
    using Base = Tuple<Ty2...>;
    Tuple() {}
    Tuple(Ty1 v, Ty2... args) : val(v), Base(args...) {}
    Base& getBase() {
        return *this;
    }
    const Base& getBase() const {
        return *this;
    }
    template <class... Ty>
    bool equal(const Tuple<Ty...>& rhs)const {
        return this->val == rhs.val && Base::equal(rhs.getBase());
    }
};

template<int idx, typename _Tuple>
struct Tuple_element {
    using Type = typename Tuple_element<idx - 1, typename _Tuple::Base>::Type;
};
template<typename _Tuple >
struct Tuple_element<0, _Tuple> {
    using Type = _Tuple;
};

template<int idx, typename _Tuple>
constexpr auto& Get(_Tuple& t) {
    using Type = typename Tuple_element < idx, _Tuple>::Type;
    return static_cast<Type&>(t).val;
}

template<typename ...Ty1, typename ...Ty2>
bool operator == (const Tuple<Ty1...>& L, const Tuple<Ty2...>& R) {
    return L.equal(R);
}

int main()
{
    Tuple<int, string> t(21, "ygg");
    cout << t.val << endl;
    cout << t.getBase().val << endl;
    cout << &t << endl;
    cout << &(t.getBase()) << endl;
    auto tmp = (Tuple<int,string>&) t;
    cout << tmp.val << endl;
    auto tmp2 = (Tuple<string>&) t;
    cout << tmp2.val << endl;
    // cout << t.getBase().getBase().val << endl;
    vector<Tuple<int, int, double>>vec;
    for (int i = 1; i <= 10; i++) {
        vec.push_back({ i, i, 1.0 / i });
    }
    for (auto& x : vec) {
        cout << Get<0>(x) << " " << Get<1>(x) << " " << Get<2>(x) << endl;
    }
}
