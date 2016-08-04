#!/bin/bash
for TOKEN in $@
do
  echo $TOKEN
done

a=0
while [ $a -lt 10 ]
do
  echo $a
  a=`expr $a + 1`
done

select Drink in tea cofee water juice appe all none
do
  case $Drink in
    tea|coffe|water|all )
    echo "Go to canteen"
    ;;
    juice|appe)
    echo "Avalicable at home"
    ;;
    none)
    echo "none"
    ;;
    *)
    echo " Error: Invalid selection"
    ;;
  esac
done