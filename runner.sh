if [ ! -p fifo ]; then mkfifo fifo; fi
python3.5 $1 < fifo | python3.5 $2 > fifo
rm fifo
