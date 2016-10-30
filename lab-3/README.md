# MapReduce
Классифицировать интернет-пользователей на группы по логу посещения сайтов

## Local launch:
```
$ cat sample.txt | python mapper.py | sort | python reducer.py | sort -n -k1,1
```

## Cluster launch:
```
$ hadoop jar /opt/cloudera/parcels/CDH/lib/hadoop-mapreduce/hadoop-streaming.jar \
-D mapred.reduce.tasks=1 \
-input wasb://data-newprolab-com@s3aws.blob.core.windows.net/lab03data/ \
-output /user/pavel.murkin/lab-3 \
-file mapper.py \
-file reducer.py \
-mapper "python mapper.py" \
-reducer "python reducer.py" 
```

Сохраним для проверки:
```
$ hadoop fs -cat /user/pavel.murkin/lab-3/part-00000 | sort -n -k1,1 > ~/lab03_users.txt
```