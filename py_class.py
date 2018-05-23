
# coding: utf-8

# In[7]:


class Dog:
    def __init__(self,newColor):
        self.color = newColor
    def bark(self):
        print("---旺旺叫----")
    def printColor(self):
        print("颜色为：%s"%self.color)
    def __str__(self):
        return "color = "+self.color
        
def test(aaa):
    aaa.printColor()
    
wangcai = Dog("白色")

xiaoqiang =Dog("黑色")

test(wangcai)

print(wangcai)
print(xiaoqiang)


print(id(wangcai))
print(id(xiaoqiang))

