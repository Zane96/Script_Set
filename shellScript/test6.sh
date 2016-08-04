#!/bin/sh
 a=10
 b=20
 val=`expr $a + $b`
 echo "a + b = $val"
 val=`expr $a - $b`
 echo "a - b = $val"
 vak=`expr $a \* $b`
 echo "a * b = $val"
 val=`expr $a / $b`
 echo "a / b = $val"
 val=`expr $a % $b`
 echo "a % b = $val"

if [ $a != $b ]
then
  echo "a is not equals b"
fi

if [ $a -gt $b ]
then
  echo "a < b"
fi

if [ $a -gt 8 -a $b -gt 10 ]
then
  echo "a > 8 and b > 10"
else
  echo "xxxx"
fi

a="abc"
b="efg"
if [ $a = $b ]
  then
  echo "a equals b"
else
  echo "a is not equals b"
fi

if [ $a ]
  then
  echo "a is not empty"
else
  echo "a is empty"
fi