# MapReduce lab-1

## Local launch:
```
$ python mapper.py < example.log | sort | python reducer.py
```

## Cluster launch:

```
$ sudo su hdfs
```

Скачиваем датасет:
```
$ wget 'https://s3aws.blob.core.windows.net/public-newprolab-com/advert.log.lzma' -O /tmp/advert.log.lzma
```

Разархивируем его:
```
$ lzma -d /tmp/advert.log.lzma
```

Создаём новую папку в HDFS:
```
$ hadoop fs -mkdir -p /users/advert
```

Размещаем в HDFS датасет:
```
$ hadoop fs -put /tmp/advert.log /users/advert/
```

Запускаем задачу в hadoop:
```
$ hadoop jar /opt/cloudera/parcels/CDH/lib/hadoop-mapreduce/hadoop-streaming.jar \
-D mapred.reduce.tasks=1 \
-input /users/advert \
-output /users/advert/result \
-file mapper.py \
-file reducer.py \
-mapper "python mapper.py" \
-reducer "python reducer.py"
```

Смотрим результат:
```
$ hadoop fs -cat /users/advert/result/* | sort | tail
```

Выведет, что-то такое:
```
Australia	381016.23
Austria	208346.81
Belgium	416379.79
Brazil	198675.64
Canada	90875.03
Costa Rica	567544.9
Denmark	3334.1
Finland	141985.63
France	146249.4
Iceland	289447.15
Ireland	649337.39
Israel	476574.41
Luxembourg	579780.41
Mexico	729915.23
Netherlands	30384.08
New Zealand	644804.24
Norway	7642.3
Oman	262166.11
Panama	729918.93
Sweden	54321.99
Switzerland	15666.87
United Arab Emirates	700645.25
United Kingdom	335899.92
United States	702524.8
Venezuela	499894.47
```

Очищаем:
```
$ hadoop fs -rm -r -f /users/ && hadoop fs -mkdir -p /users/advert
```