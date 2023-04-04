# Problem - F - Codeforces

# 題意：
# 給 N 個元素的數列 A。問有幾種不同的非空子序列，其最大公因數不為 1。輸出方案數對 1e9 + 7 取模。

# 制約：
# The first line contains one integer number n (1 ≤ n ≤ 100000).
# The second line contains n integer numbers a1, a2... an (1 ≤ ai ≤ 100000).

# 解法：
# 看起來就很排容。
# 首先計算：
# mcnt[ i ]: i 的倍數的元素數量。
# mans[ i ]: 最大公因數為 i 的倍數的非空子序列數量。
# mans[ i ] = pow( 2, mcnt[ i ] ) - 1
# ans[ i ]: 最大公因數為 i 的非空子序列數量。
# ans[ i ] = mans[ i ] - ( ans[ j ] for all j that j % i == 0 if j > i )
# 非空的部分要特別注意，一開始就要捨掉，因為它沒有因數倍數的概念。

# 時間 / 空間複雜度：
# O( MAXA lg MAXA ) / O( MAXA )

MOD = int( 1e9 ) + 7

N = int( input() )
A = list( map( int, input().split() ) )

pow2 = [ pow( 2, i, MOD ) for i in range( N + 1 ) ]

maxa = max( A )
mcnt = [ 0 for i in range( maxa + 1 ) ]
mans = [ 0 for i in range( maxa + 1 ) ]
for i in range( N ):
  mcnt[ A[ i ] ] += 1
for i in range( 1, maxa + 1 ):
  for j in range( i + i, maxa + 1, i ):
    mcnt[ i ] += mcnt[ j ]
  mans[ i ] = pow2[ mcnt[ i ] ] - 1
for i in range( maxa, 0, -1 ):
  for j in range( i + i, maxa + 1, i ):
    mans[ i ] = ( mans[ i ] - mans[ j ] ) % MOD
print( mans[ 1 ] + ( mans[ 1 ] < 0 ) * MOD )