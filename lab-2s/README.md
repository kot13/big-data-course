# MapReduce
Построить TOP350 самых популярных адресов (URL) из большого лог-файла, лежащего в Azure Blob Storage с помощью MapReduce

## Local launch:
```
$ cat sample.txt | python mapper.py | sort | python reducer.py | sort -rn -k2,2
```

## Cluster launch:
```
$ hadoop jar /opt/cloudera/parcels/CDH/lib/hadoop-mapreduce/hadoop-streaming.jar \
-D mapred.reduce.tasks=1 \
-input wasb://data-newprolab-com@s3aws.blob.core.windows.net/facetz_2015_02_12/ \
-output /user/pavel.murkin/lab-2s \
-file mapper.py \
-file reducer.py \
-mapper "python mapper.py" \
-reducer "python reducer.py" 
```

Запустим сортировку и сохранение в файл top350
```
$ hadoop fs -cat /user/pavel.murkin/lab-2s/part-00000 | sort -rn -k2,2 -T /tmp/pm | head -350 > /data/home/pavel.murkin/top350.txt
```