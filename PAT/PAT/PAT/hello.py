import collections
class candidate:
	def __init__(self,nums,score,level,site,date):
		self.nums = nums
		self.score = score
		self.level = level
		self.site = site
		self.date = date

	def __lt__(self,others):
		if self.score == others.score:
			return self.nums <= others.nums
		return self.score > others.score

n,m = list(map(int,input().split()))
candidates = []
for _ in range(n):
	nums, score = input().split()
	score = int(score)
	level = nums[0]
	site = nums[1:4]
	date = nums[4:10]
	candidates.append(candidate(nums,score,level,site,date))

candidates.sort()

for case in range(m):
	types, terms = input().split()
	print("Case {}: {} {}".format(str(case+1),types,terms))
	if types == "1":
		res = [x for x in candidates if x.level == terms]
		if len(res) == 0:
			print("NA")
			continue
		# res.sort()
		for x in res:
			print("{} {}".format(x.nums,x.score))
	elif types == "2":
		res = [x for x in candidates if x.site == terms]
		if len(res) == 0:
			print("NA")
			continue
		sums = sum(x.score for x in res)
		print("{} {}".format(len(res),sums))
	else:
		res = [x.site for x in candidates if x.date == terms]
		if len(res) == 0:
			print("NA")
			continue
		cc = collections.Counter(res)
		res = [(int(v),k) for k,v in cc.items()]
		res.sort(key = lambda x: (-x[0],x[1]))
		for v, k in res:
			print("{} {}".format(k,str(v)))






