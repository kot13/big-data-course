# MapReduce & HBase
Загрузить данные в HBase из большого лог-файла, лежащего в Azure Blob с помощью MapReduce

## Create hbase table
```
$ hbase shell

hbase> create 'pavel.murkin', {NAME => 'data', VERSIONS => 4096}
```

## Local launch:
```
$ cat sample.txt | python mapper.py
```

## Cluster launch:
```
$ hadoop jar /opt/cloudera/parcels/CDH/lib/hadoop-mapreduce/hadoop-streaming.jar \
-D mapred.reduce.tasks=0 \
-input wasb://data-newprolab-com@s3aws.blob.core.windows.net/facetz_2015_02_19/ \
-output /user/pavel.murkin/lab-2 \
-file mapper.py 
-mapper "python mapper.py" 
```

## See results
```
$ hbase shell

hbase> scan 'pavel.murkin'
```