#!/bin/bash
a=0
while [ $a -lt 10 ]
do
  b=$a
  while [ $b -ge 0 ]
  do
    echo -n "$b "
    b=`expr $b - 1`
  done
  echo
  a=`expr $a + 1`
done

nums="1 2 3 4 5 6 7"
for NUM in $nums
do
  Q = `expr $NUM % 2`
  if [ $Q -eq 0 ]
  then
    echo "even number"
    continue
  fi
  echo "odd number"
done