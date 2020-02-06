'''
print("hello world")
print(22222)
print(2.2222)
print(True)
print(None)
print(())
print([])
print({})

print("刘洋有点傻",28,170.0,"he is single dog")

num = 20200202
print(num)


input("请输入：")


a = int(input("请输入第一个数："))
b = int (input("请输入第二个数："))
print  ("两个数的和是：",a+b)
c = "2222.0"
print(len(c))


a = ("lala","啊哈哈哈",1234,"zxcv","lala","lala","lala","lala")
print(a[2])

print(a.count("lala"))

print(len(a))


b = ((1,"刘敏","大长腿"),(2,"刘洋","小短腿"))
print(b[0][1:],b[1][1:])





a = [1,2,3,"whahah","gaga",[22,33,2233]]
print(a[-1][-1])


a.append("我要去买菜了")
print(a)

a.insert(2,"今天晚上吃冒菜")
print(a)
b = [1,2,2,2,5]
b.extend("啊哈哈或或")
print(b)


del b [-1]
print (b)
del b[4]
print(b)

name = input("请输入你的名字:")
age = input("请输入你的年龄:")
tedian = input("请输入你的特点:")

print("hi,大家好！我叫{}，今年{}，我没什么特点，非要说特点的话我想我应该是{}".format(name,age,tedian))

print("hi,大家好！我叫{name}，今年{age}，我没什么特点，非要说特点的话我想我应该是.\
{tedian},{tedian},{tedian},{tedian}".format(name=name,age=age,tedian=tedian))



a = {"name":"yangyang","like":"玩王者荣耀"}

a["name"]="刘洋"#修改
a['age']="28"#新增
a.update(like = "打麻将")#修改
del a["age"]#删除

print(a.get("name"))
print(a["name"])

age = int(input("请输入你的年龄："))
if age > 25:
    print('好好工作')
elif age > 18:
    print('好好学习')
elif age > 12:
    print('好好看书')
else:
    print('好好玩')

a = ['lalala','ahahah','heheheh','xixixi','huhuhuhu']
for i in a :
    bb = "我想"
    bb = bb + i 
    print(bb)
print(bb)

for i in range(1,10):
    for j in range(1,i+1):
        print("{}×{}={}".format(i,j,i*j),end = " ")
    print()

a = [11,564,4156,211,5633,5444,1,33,55,44,456,789895,34561,44,99,87,77,253,245,45,454,5648,235,475,5668,48245,55,5,6,31]
b = []
c = []
for i in a:
    if i > 200:
        b.append(i)              
    else:
        c.append(i)      
print(b,c)



i = 10
while i < 20:
    i = i + 1 
    if i == 17:
        break 
    print("好像没太明白！", i)

i = 0 
while i < 30:
    i = i + 1



sl = {"红灯":30,"黄灯":3,"绿灯":30}
while True:
    for i in sl:
        j = 0 
        while j < sl[i]:
            j = j + 1 
            print("{}{}".format(i,sl[i]-j))

year = int(input("请输入年份："))
month = int(input("请输入月份："))
day = int(input("请输入日期："))
monthlist = [31,28,31,30,31,30,31,31,30,31,30,31]
if (year % 400 == 0 ) or ((year % 4 == 0 ) and (yaer % 100 != 0 )):
    monthlist[1] = 29 
    m = 0 
 '''  

 

 












    