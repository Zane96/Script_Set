package main

import "fmt"
import "reflect"

var(
	a = 2
	b = 3
)

type Rect struct {
	width int
	height int
}

func (r *Rect) areaSize() int  {
	return r.width * r.height
}


func main()  {
	fmt.Print("hello world!")
	a := 65;

	fmt.Println(a , " sss")

	b := make([]int, 5, 10);
	fmt.Println(len(b), cap(b))

	if num := 9; num < 0 {
		fmt.Println(" < 0")
	} else if num > 0 {
		fmt.Println("> 0")
	}

	m := make(map[string]int)
	m["k1"] = 1
	m["k2"] = 2

	delete(m, "k2")
	_, v2 := m["k2"]
	fmt.Println(v2)
	_, v1 := m["k1"]
	fmt.Println(v1)

	mapp := map[string]int{"k1":1, "k2":2}
	for k, v := range mapp {
		fmt.Println(k, " - ", v)
	}

	s2 := []int{1,2,3,4}
	for _, v := range s2 {
		fmt.Println(v)
	}

	test()

	rect := &Rect{width:10, height:10}
	fmt.Println(rect.areaSize())
}

type customError struct {
	arg int
}

func test(nums ...int) {
	fmt.Println(reflect.TypeOf(nums))
}
