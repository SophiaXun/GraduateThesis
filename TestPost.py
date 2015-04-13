import urllib.request
r=urllib.request.urlopen("http://detail.yao.95095.com/item.htm?spm=a220m.1000858.1000725.2.dBwf1g&id=41596470534&skuId=4611686060023858438&areaId=310100&cat_id=2&rn=c672ba0c73c12bc099c7b3a29e7c3da9&user_id=911757567&is_b=1")
data=r.readall()
print(data)