#!/usr/bin/env python
# coding: utf-8

# In[3]:


for num in range(1, 101):
    string = ''

    # ここから記述
    if num % 3 == 0:　#3で割ったとき0になればstringに文字列Fizzを追加
        string += 'Fizz'
    if num % 5 == 0:　#5で割ったとき0になればstringに文字列Buzzを追加
        string += 'Buzz'
    if not string:
        string = num
    # ここまで記述

    print(string)


# In[ ]:




