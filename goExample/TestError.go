package main

import "errors"
import "fmt"

func fun1(arg int) (int ,error)  {
	if arg == 9 {
		return -1, errors.New("num == 9")
	}


	return arg, nil
}

func main()  {
	for _, i := range []int{2,3,4,5,6,9,10} {
		if num, err := fun1(i); err != nil {
			fmt.Println("filed: ", err)
		} else {
			fmt.Println("work: ", num)
		}
	}
}
