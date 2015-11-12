#!/bin/bash
#Miral Panchal - 100569725

lines=$(wc -l < $3)
declare -i k="$1"
declare -i m="$2"
declare -i first=$(($lines-$k))
declare -i second=$(($first-$m))
tail -n "$first" "$3" |head -n "$second"
