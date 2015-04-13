import urllib.request

# url="http://ext.mdskip.taobao.com/extension/dealRecords.htm?_ksTS=1428929331464_690&callback=jsonp691&bid_page=1&page_size=15&is_start=false&item_type=b&ends=1429240563000&starts=1428635763000&item_id=41596470534&user_tag=35196962&old_quantity=2725&seller_num_id=911757567&isFromDetail=yes&totalSQ=789&sbn=dc51abb5de1231ba315806348d225292&sold_total_num=79&&isg=8BDE22B21DD16ABFD69C76648DF327D3&isg2=AUvVIh1Yy5ULVR4-MOaM8AtVyxqL18uV"
url="http://ext.mdskip.taobao.com/extension/dealRecords.htm"
headers={
'Accept':'*/*',
'Accept-Encoding':'gzip, deflate, sdch',
'Accept-Language':'zh-CN,zh;q=0.8,en;q=0.6',
'Connection':'keep-alive',
'Cookie':'thw=cn; cna=R+E0DVnAiTcCAXUOhfr1XVOO; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; v=0; _tb_token_=537e361356be8; uc3=nk2=G5VVSllVlhG7utM%3D&id2=UNQ0XS1r14En&vt3=F8dAT%2BcWJ4NO1YI%2Br4A%3D&lg2=V32FPkk%2Fw0dUvg%3D%3D; existShop=MTQyODkyOTExOQ%3D%3D; unt=xun05de%E6%83%86%E6%80%85%26center; lgc=xun05de%5Cu60C6%5Cu6005; tracknick=xun05de%5Cu60C6%5Cu6005; sg=%E6%80%858e; cookie2=1c3441b454e3ce8a0721b87f6a10db50; mt=np=&ci=2_1; cookie1=W8q7eubHow6VyRod%2BbqXN7t7UhlClzl57svfbZ%2F6%2F68%3D; unb=343971848; t=17c229fa40c754efe89e9fdc2b8fb4ee; _cc_=W5iHLLyFfA%3D%3D; tg=0; _l_g_=Ug%3D%3D; _nk_=xun05de%5Cu60C6%5Cu6005; cookie17=UNQ0XS1r14En; isg=F6569AB61978C86E8D8CC394B3FAF808; uc1=lltime=1428853992&cookie14=UoW1HJbctHkcag%3D%3D&existShop=false&cookie16=V32FPkk%2FxXMk5UvIbNtImtMfJQ%3D%3D&cookie21=U%2BGCWk%2F7pY%2FF&tag=7&cookie15=UIHiLt3xD8xYTw%3D%3D&pas=0',
'Host':'ext.mdskip.taobao.com',
'Referer':'http://detail.yao.95095.com/item.htm?spm=a220m.1000858.1000725.2.dBwf1g&id=41596470534&skuId=4611686060023858438&areaId=310100&cat_id=2&rn=c672ba0c73c12bc099c7b3a29e7c3da9&user_id=911757567&is_b=1',
'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36'
}
req=urllib.request.Request(url,None,headers)
response=urllib.request.urlopen(req)
the_page=response.read()
print(the_page)
# r=urllib.request.urlopen("http://detail.yao.95095.com/item.htm?spm=a220m.1000858.1000725.2.dBwf1g&id=41596470534&skuId=4611686060023858438&areaId=310100&cat_id=2&rn=c672ba0c73c12bc099c7b3a29e7c3da9&user_id=911757567&is_b=1")


# data=r.readall()
# print(data)

# Accept:*/*
# Accept-Encoding:gzip, deflate, sdch
# Accept-Language:zh-CN,zh;q=0.8,en;q=0.6
# Connection:keep-alive
# Cookie:thw=cn; cna=R+E0DVnAiTcCAXUOhfr1XVOO; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; v=0; _tb_token_=537e361356be8; uc3=nk2=G5VVSllVlhG7utM%3D&id2=UNQ0XS1r14En&vt3=F8dAT%2BcWJ4NO1YI%2Br4A%3D&lg2=V32FPkk%2Fw0dUvg%3D%3D; existShop=MTQyODkyOTExOQ%3D%3D; unt=xun05de%E6%83%86%E6%80%85%26center; lgc=xun05de%5Cu60C6%5Cu6005; tracknick=xun05de%5Cu60C6%5Cu6005; sg=%E6%80%858e; cookie2=1c3441b454e3ce8a0721b87f6a10db50; mt=np=&ci=2_1; cookie1=W8q7eubHow6VyRod%2BbqXN7t7UhlClzl57svfbZ%2F6%2F68%3D; unb=343971848; t=17c229fa40c754efe89e9fdc2b8fb4ee; _cc_=W5iHLLyFfA%3D%3D; tg=0; _l_g_=Ug%3D%3D; _nk_=xun05de%5Cu60C6%5Cu6005; cookie17=UNQ0XS1r14En; isg=F6569AB61978C86E8D8CC394B3FAF808; uc1=lltime=1428853992&cookie14=UoW1HJbctHkcag%3D%3D&existShop=false&cookie16=V32FPkk%2FxXMk5UvIbNtImtMfJQ%3D%3D&cookie21=U%2BGCWk%2F7pY%2FF&tag=7&cookie15=UIHiLt3xD8xYTw%3D%3D&pas=0
# Host:ext.mdskip.taobao.com
# Referer:http://detail.yao.95095.com/item.htm?spm=a220m.1000858.1000725.2.dBwf1g&id=41596470534&skuId=4611686060023858438&areaId=310100&cat_id=2&rn=c672ba0c73c12bc099c7b3a29e7c3da9&user_id=911757567&is_b=1
# User-Agent:Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36