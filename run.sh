#!/bin/bash
SCRIPTPATH="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"

WLSTRESULT="$(/opt/weblogic/oracle/oracle_common/common/bin/wlst.sh $SCRIPTPATH/wldepslist.py 2>/dev/null | egrep "DEPLOY")"


for app in $(echo $WLSTRESULT | sort | uniq)
do
    NAME=$(echo $app | cut -d ";" -f 2)
    STATE=$(echo $app | cut -d ";" -f 3)
    SERVER=$(echo $app | cut -d ";" -f 4)
    HOST=$(echo $app | cut -d ";" -f 5)
    WAR=$(echo $app | cut -d ";" -f 6)
    CONTEXT=$(unzip -p ${WAR} WEB-INF/weblogic.xml | grep context |  sed 's/\(.*<wls:context-root>\|<\/wls:context-root>\)//g' | sed 's/\(.*<context-root>\|<\/context-root>\)//g')
    if [ -z "$CONTEXT" ]
    then
        CONTEXT=$NAME
    fi 
    URL="$HOST/$CONTEXT"
    echo "$NAME;$STATE;$SERVER;$URL"
done

# name - state - server - url
