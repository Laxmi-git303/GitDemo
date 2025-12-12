# # # # #print(len("guydwsiydiwyd k"))
# # # # from collections import Counter

# # # # s=[1,1,1,12,3,3,3]
# # # # count=Counter(s)
# # # # print(count.most_common(2))
# # # # names = ["a", "b", "c", "b"]
# # # # names.remove("b")
# # # # print(names)
# # # # # ["a", "c", "b"]

# # # nums=[10,20,30]
# # # nums.insert(2,40)
# # # print(nums)

# # nums=[1,2,3,3,4,44,5,5,5,8]
# # print(nums.count(5))

# nums=[45,89,12,34]
# nums.sort()
# print(nums)

# nums=[3,1,2]
# sorted(nums)
# print(nums)

# d={"a":1,"b":2}
# val=d.get("c","Not Found")
# print(val)
# print(d["a"])
# d1 = {"a":1}
# d2 = {"b":2, "a":10}
# #d1.update(d2)
# print(d2.popitem())
# print(d2)
# # {"a":10, "b":2}

d = {"a":1}
d.setdefault("a", 10)
print(d)
# {"a":1, "b":10}

