# MapReduce
Определить по логу сайты, релевантные для определенной группы пользователей

## Local launch:

### Считаем домены:
```
$ cat sample.txt | python mapper.py | sort | python reducer.py > domains.txt
```

### Вычисляем необходимые константы:
```
$ cat domains.txt | awk '{x+=$2} END {print x}' # всего доменов
$ cat domains.txt | awk '{x+=$3} END {print x}' # доменов посещённых автомобилистами
```

### Вычисляем релевантность:
```
$ cat domains.txt | python relevant.py | sort -k2,2rn -k1,1 | head -n 200 > top200.txt
```

## Cluster launch:

### Запустим job:
```
$ hadoop jar /opt/cloudera/parcels/CDH/lib/hadoop-mapreduce/hadoop-streaming.jar \
-D mapred.reduce.tasks=1 \
-input wasb://data-newprolab-com@s3aws.blob.core.windows.net/lab03data/ \
-output /user/pavel.murkin/lab-3s \
-file mapper.py \
-file reducer.py \
-mapper "python mapper.py" \
-reducer "python reducer.py" 
```

### Сохраним для дальнейшей обработки:
```
$ hadoop fs -cat /user/pavel.murkin/lab-3s/part-00000 > ./domains.txt
```

### Вычисляем необходимые константы:
```
$ cat domains.txt | awk '{x+=$2} END {print x}' # всего доменов
$ cat domains.txt | awk '{x+=$3} END {print x}' # доменов посещённых автомобилистами
```

### Вычисляем релевантность:
```
$ cat domains.txt | python relevant.py | sort -k2,2rn -k1,1 | head -n 200 > top200.txt
```