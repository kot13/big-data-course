# MapReduce
Классифицировать интернет-пользователей на группы по логу посещения сайтов

## Local launch:
```
$ cat sample.txt | python mapper.py | sort | python reducer.py | sort -rn -k2,2
```

## Cluster launch:
```
$ hadoop jar /opt/cloudera/parcels/CDH/lib/hadoop-mapreduce/hadoop-streaming.jar \
-D mapred.reduce.tasks=1 \
-input wasb://data-newprolab-com@s3aws.blob.core.windows.net/facetz_2015_02_12/ \
-output /user/pavel.murkin/lab-3 \
-file mapper.py \
-file reducer.py \
-mapper "python mapper.py" \
-reducer "python reducer.py" 
```
