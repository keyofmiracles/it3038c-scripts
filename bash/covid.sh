#!/bin/bash
# This scripts downloads covid data and displays it

DATA=$(curl https://api.covidtracking.com/v1/us/current.json)
POSITIVE=$(echo $DATA | jq '.[0].positive')
NEGATIVE=$(echo $DATA | jq '.[0].negative')
DEATHS=$(echo $DATA | jq '.[0].death')
HOSPITALIZED=$(echo $DATA | jq '.[0].hospitalizedCumulative')

TODAY=$(date)

echo "On $TODAY, there were $POSITIVE positive COVID case, $NEGATIVE negative tests, $DEATHS deaths and $HOSPITALIZED hospitalized"

