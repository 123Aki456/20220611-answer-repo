#!/usr/bin/env python
# coding: utf-8

# In[18]:


def main():
    # 昇順にソートされた配列
    sorted_array = [1, 2, 3, 5, 12, 7890, 12345]
    # 探索対象の番号
    target_number = 7890
    # 探索実行
    target_index = serch_index(sorted_array, target_number)
    # 結果出力
    print(target_index)
    
def serch_index(sorted_array, target_number):

    # ここから記述
    left, right = 0, len(sorted_array) - 1 #leftに0、rightにsorted_arrayのリスト内の要素数-1を格納
    while left <= right: #leftがrihgtが以下になるまで処理を実行
        mid = (left + right) // 2 #リスト内の要素数の中間の値をmidとして定義
        if sorted_array[mid] == target_number: #sorted_arrayの中間(mid)がtarget_numberと同じ場合、midを返す
            return mid
        elif sorted_array[mid] < target_number: #sorted_arrayの中間(mid)がtarget_numberより小さい場合
            left = mid + 1 #leftにmid+1した値を格納
        else:
            right = mid - 1 #rightにmid+1した値を格納
     
    # ここまで記述

    # 探索対象が存在しない場合、-1を返却
    return -1

if __name__ == '__main__':
    main()
    
    

