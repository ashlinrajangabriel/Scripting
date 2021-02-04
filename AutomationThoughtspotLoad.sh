#!/bin/bash

 echo ""
                echo ""
                echo "-----------------------------------"
                echo "Running Data load for ProjectName
                echo "-----------------------------------"
                echo "|Project Owner :Project|"
                echo "|Project Location: Germany        |"
                echo "-----------------------------------"
                echo "@ $(date +"%d"-"%m"-"%y") Running Data loading script@/home/thoughtspot/TSLOAD/LoadScripts/ "


dom=$(date '+%d') # 02-31, day of month
year=$(date '+%Y') # four-digit year
month=$(date '+%m') # two-digit month
nworkdays=0





MY_FILENAME1_S3="File_$dom$month$year.zip"
MY_FILENAME1_LC="File_$dom$month$year.csv"

MY_FILENAME2_S3="File_$dom$month$year.zip"
MY_FILENAME2_LC="File_$dom$month$year.csv"

MY_FILENAME2_S4="File_$dom$month$year.zip"
MY_FILENAME2_L4="File_$dom$month$year.csv"





cd /home/thoughtspot/TSLOAD/LoadScripts  && wait

aws s3 cp --region eu-west-1  "s3://Location/$MY_FILENAME1_S3"  ./$MY_FILENAME1_S3 && wait

aws s3 cp --region eu-west-1  "s3://Location/$MY_FILENAME2_S3"  ./$MY_FILENAME2_S3 && wait

aws s3 cp --region eu-west-1  "s3://Location/$MY_FILENAME2_S4"  ./$MY_FILENAME2_S4 && wait

unzip $MY_FILENAME1_S3   && wait
unzip $MY_FILENAME2_S3   && wait


tsload --source_file /home/thoughtspot/TSLOAD/LoadScripts/$MY_FILENAME1_LC --target_database DBNAME --target_schema SchemaName --target_table tablename   --csv --field_separator "\t" --null_value "" --enclosing_character "\""  --empty_target  --date_format "%Y-%m-%d"  --date_time_format "%Y-%m-%d %H:%M:%S"  --skip_second_fraction   && wait ;

echo "TSLOAD FOR File IS DONE" && wait

tsload --source_file /home/thoughtspot/TSLOAD/LoadScripts/$MY_FILENAME2_LC --target_database DBNAME --target_schema SchemaName  --target_table tablename   --csv --field_separator "\t" --null_value "" --enclosing_character "\""   --date_format "%Y-%m-%d"  --date_time_format "%Y-%m-%d %H:%M:%S"  --skip_second_fraction  --empty_target && wait ;

echo "TSLOAD FOR File IS DONE" && wait
rm -f $MY_FILENAME1_LC && wait
rm -f $MY_FILENAME1_S3 && wait
rm -f $MY_FILENAME2_LC && wait
rm -f $MY_FILENAME2_S3  && wait

