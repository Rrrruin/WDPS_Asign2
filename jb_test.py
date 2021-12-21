import jieba
import nltk

sen = "南京市长江大桥欢迎你"
res = jieba.lcut(sen)
seg_str = " ".join(res)

a = ['1', '2']
for i in range(len(a)):
    a[i] = int(i)
    print(a[i])
print(a)