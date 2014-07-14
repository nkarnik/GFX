#GFX

Global Events and FOREX Analysis Platform
GDELT + FOREX
===================

*Documentation is a work in progress*

Table of Contents

1. Introduction
2. Data Pipeline
3. Application Layer


## 1. Introduction

How do geopolitical events affect currency markets?

FOREX is driven by macroeconomics and geopolitics. Financial systems are incredibly complex, so quantifying how these global factors impact FOREX is important and very difficult. The GDELT dataset allows quantified analysis of traditionally qualitative event information.



## 2. Data Pipeline

<img src="https://raw.githubusercontent.com/nkarnik/GFX/master/images/data_pipeline.png"/>

The data pipeline is quite straightforward. Historical GDELT and FOREX data is pulled into the namenode for cleaning and import into HDFS. GDELT updates are logged once a day (with yesterday's events) so a cron job runs to download the data and push it to HDFS to update the master dataset (and then use Hive for running mapreduce jobs to generate aggregate queries/views for MySQL and Postgres. 

For realtime FOREX data, I am using Python and Fluentd to log the latest FOREX pairs' currency rates from Yahoo finance into a JSON format to store in HDFS.



Instructions:

- Edit gdscr.sh and gdscrape.py in GDELT (set paths that you want)
- Load data with gdscr.sh (schedule it in crontab every day).
- Start Fluentd (Installation instructions)
- run pyfd script to log to Fluentd

## 3. Application Layer

Instructions:

- Install algogd (sudo pip install algogd)
- Create mysql.conf file in GFX\_flask directory
- Deploy cmtest.py


