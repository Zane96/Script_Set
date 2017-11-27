package main

import (
	"fmt"
	"io/ioutil"
	//"io"
	"os"
	"bufio"
	)

func check(e error)  {
	if e != nil {
		panic(e)
	}
}

func main()  {
	dat, err := ioutil.ReadFile("file.txt")
	check(err)

	fmt.Println(string(dat))

	f1, err2 := os.Open("file.txt")
	check(err2)
	b2 := make([]byte, 5)
	n1, err := f1.Read(b2)
	fmt.Println(string(b2), n1)

	f1.Seek(0, 0)

	r4 := bufio.NewReader(f1)
	b4, err := r4.Peek(5)
	check(err)
	fmt.Println(string(b4))
	f1.Close()
}
