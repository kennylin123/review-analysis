data = []
count = 0
with open('reviews.txt', 'r') as f:
    for X in f:
        data.append(X)
        count +=1
        if count %1000 == 0:
           print(len(data))
print('檔案讀取完了 總共有:', len(data), '筆資料')

sum_len = 0
for d in data:
    sum_len += len(d)
print('平均每行有:', sum_len / len(data), '個字')
