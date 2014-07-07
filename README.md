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


