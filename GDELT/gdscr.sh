mkdir /home/ubuntu/GFX/GDELT/temp_l

DATE=`date +%Y-%m-%d`
echo $DATE
#mkdir /home/ubuntu/FOREX/GDELT/$DATE


python /home/ubuntu/GFX/GDELT/gdscrape.py

cd /home/ubuntu/GFX/GDELT/temp_l

mkdir /home/ubuntu/GFX/GDELT/temp_l/$DATE

pwd

for file in *.zip
do
    echo $file
    unzip $file -d /home/ubuntu/GFX/GDELT/temp_l/histgd
    unzip $file -d /home/ubuntu/GFX/GDELT/temp_l/$DATE
    hdfs dfs -put $DATE/ GDELT/
    hdfs dfs -put histgd/ GDELT/
    rm -r /home/ubuntu/GFX/GDELT/temp_l/histgd
    rm -r /home/ubuntu/GFX/GDELT/temp_l/$DATE
done



hive -e "CREATE EXTERNAL TABLE gdnew (
	GLOBALEVENTID	INT	,
	SQLDATE	INT	,
	MonthYear	INT	,
	Year	INT	,
	FractionDate	FLOAT	,
	Actor1Code	STRING	,
	Actor1Name	STRING	,
	Actor1CountryCode	STRING	,
	Actor1KnownGroupCode	STRING	,
	Actor1EthnicCode	STRING	,
	Actor1Religion1Code	STRING	,
	Actor1Religion2Code	STRING	,
	Actor1Type1Code	STRING	,
	Actor1Type2Code	STRING	,
	Actor1Type3Code	STRING	,
	Actor2Code	STRING	,
	Actor2Name	STRING	,
	Actor2CountryCode	STRING	,
	Actor2KnownGroupCode	STRING	,
	Actor2EthnicCode	STRING	,
	Actor2Religion1Code	STRING	,
	Actor2Religion2Code	STRING	,
	Actor2Type1Code	STRING	,
	Actor2Type2Code	STRING	,
	Actor2Type3Code	STRING	,
	IsRootEvent	INT	,
	EventCode	INT	,
	EventBaseCode	INT	,
	EventRootCode	INT	,
	QuadClass	INT	,
	GoldsteinScale	FLOAT	,
	NumMentions	INT	,
	NumSources	INT	,
	NumArticles	INT	,
	AvgTone	DOUBLE	,
	Actor1Geo_Type	INT	,
	Actor1Geo_FullName	STRING	,
	Actor1Geo_CountryCode	STRING	,
	Actor1Geo_ADM1Code	STRING	,
	Actor1Geo_Lat	DOUBLE	,
	Actor1Geo_Long	DOUBLE	,
	Actor1Geo_FeatureID	STRING	,
	Actor2Geo_Type	INT	,
	Actor2Geo_FullName	STRING	,
	Actor2Geo_CountryCode	STRING	,
	Actor2Geo_ADM1Code	STRING	,
        Actor2Geo_Lat   DOUBLE  ,
        Actor2Geo_Long  DOUBLE  ,
        Actor2Geo_FeatureID     STRING  ,
        ActionGeo_Type  INT     ,
        ActionGeo_FullName      STRING  ,
        ActionGeo_CountryCode   STRING  ,
        ActionGeo_ADM1Code      STRING  ,
        ActionGeo_Lat   DOUBLE  ,
        ActionGeo_Long  DOUBLE  ,
        ActionGeo_FeatureID     STRING  ,
        DATEADDED       INT     ,
        SOURCEURL       STRING)

ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\t'
stored as textfile
LOCATION '/user/ubuntu/GDELT/"$DATE"'"

hive -e "create table gdeconew (SQLDATE int, Actor1Code string, Actor2Code string, EventCode int, SumArticles int, SumSources int) ROW FORMAT DELIMITED FIELDS TERMINATED BY '\t';"


hive -e "INSERT INTO TABLE gdeconew SELECT SQLDATE, Actor1Code, Actor2Code, EventCode, SUM(NumArticles) as sum1, SUM(NumSources) AS sum2 from gdnew WHERE (EventCode = 0211 or EventCode = 0231 or EventCode = 0254 or EventCode = 0311 or EventCode = 0331 or EventCode = 0354 or EventCode = 061 or EventCode = 071 or EventCode = 085 or EventCode = 1011 or EventCode = 1031 or EventCode = 1054 or EventCode = 1211 or EventCode = 1221 or EventCode = 1244 or EventCode = 1312 or EventCode = 1621) and (NumSources > 1) and (SQLDATE > 20010101) group by SQLDATE, Actor1Code, Actor2Code, EventCode;"

hdfs dfs -get /user/hive/warehouse/gdeconew

cd /home/ubuntu/GFX/GDELT/temp_l/gdeconew

for f in *
do
    mysql -e "load data local infile '"$f"' into table gdecon2 fields TERMINATED BY '\t' LINES TERMINATED BY '\n'"  -u root -pcms001 test --local-infile
done

hive -e "drop table gdeconew; drop table gdnew;"


mysql -e "UPDATE gdecon2 SET norm = 73755 WHERE (day DIV 10000) = 2013; UPDATE gdecon2 SET norm = 90000 WHERE (day DIV 10000) = 2014; UPDATE gdecon2 SET ratio = SumArticles/norm;" -u root -pcms001 test

cd ..
pwd
cd ..
pwd

rm -r /home/ubuntu/GFX/GDELT/temp_l
