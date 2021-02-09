#!/bin/bash

now=$(date +"%d")
todate=$(date -d 2013-07-18 +%s)

if [ $now -ge 4 ];
then if [ $now -le 11 ]
        then

                ./ScriptLoad.sh >> "/home/dorectory/TSLOADDirectory/LogStore/TSLOADLOG `date +"%d-%m-%Y %T"`.log"
        fi
fi
~
~
~
~
~
