#!/bin/sh

Hello () {
  Hello_2
  echo "Hello! $@"
  return 10
}

Hello_2 () {
  echo "Hello World!"
}

Hello Zane Xu

echo "return value is $?"