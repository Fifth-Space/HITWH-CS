# post 注入

1. 用 burp suite 抓包查看提交信息

   <img src="C:\Users\A2140\AppData\Roaming\Typora\typora-user-images\image-20240504155324178.png" alt="image-20240504155324178" style="zoom:67%;" />

2. 看到提交的参数分别是 uname passwd submit

3. 其实 submit 没必要提交，而且由于这个 submit 和 form 中的 submit 重名了，如果提交反而会报错失败

4. 在 hackbar 上进行 post 注入：uname=admin' or 1=1#&passwd=111

5. 如果想获取数据库相关信息，在单引号和 # 之间进行 union 注入即可