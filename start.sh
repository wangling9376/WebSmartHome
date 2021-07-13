#!/bin/bash

currentTime=`date "+%Y-%m-%d %H:%M:%S"`

python2.7 /opt/Web/main_up.py & >> /opt/Web/Logs/start_test.log
echo $currentTime >> /opt/Web/Logs/start_test.log
/bin/bash
