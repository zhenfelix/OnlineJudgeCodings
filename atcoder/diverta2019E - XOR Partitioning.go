package main
import("bufio";."fmt";"os")

const mod = 1_000_000_007

func main() {
    in := bufio.NewReader(os.Stdin)
    var n, v, xor int
    // f[xor] 相当于只看前缀异或和中的 0 和 xor，求 DP
    f := [1 << 20]struct{ s0, s1, pre0 int }{}
    for i := range f {
        f[i].s0 = 1
    }
    cnt0 := 1 // 前缀异或和的第一个数是 0
    for Fscan(in, &n); n > 0; n-- {
        Fscan(in, &v)
        xor ^= v
        if xor == 0 {
            cnt0++
        } else {
            t := &f[xor]
            // f[i][0] = 一堆 f[j][1] 的和 = s1，这里直接把 f[i][0] 加到 s0 中
            t.s0 = (t.s0 + t.s1*(cnt0-t.pre0)) % mod
            // f[i][1] = 一堆 f[j][0] 的和 = s0，这里直接把 f[i][1] 加到 s1 中
            t.s1 = (t.s1 + t.s0) % mod
            t.pre0 = cnt0
        }
    }
    if xor > 0 {
        // 答案 = f[n][1] = 一堆 f[j][0] 的和 = s0
        // 注意不能写 f[xor].s1，因为前缀异或和的末尾如果有多个 xor，我们只能选一个
        Print(f[xor].s0)
    } else {
        ans := pow(2, cnt0-2) // 只选 0 的方案数
        for _, t := range f {
            // 答案 = f[n][0] = 一堆 f[j][1] 的和 = s1
            // 注意不能写 t.s0，因为前缀异或和的末尾如果有多个 0，我们只能选一个
            ans += t.s1
        }
        Print(ans % mod)
    }
}

func pow(x, n int) (res int) {
    res = 1
    for ; n > 0; n /= 2 {
        if n%2 > 0 {
            res = res * x % mod
        }
        x = x * x % mod
    }
    return
}

