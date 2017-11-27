package main

import "fmt"
import "time"
//import "sync/atomic"
//import "runtime"

func fun1(from string) {
	for i := 0; i < 3; i++ {
		fmt.Println("from: ", from)
	}
}

func main() {
	//fun1("1")

	//go fun1("2")
	//
	//go func(from string) {
	//	for i := 0; i < 3; i++ {
	//		fmt.Println("from: ", from)
	//	}
	//}("4")
	//
	//fmt.Println("3")
	//
	//var input string
	//fmt.Scanln(&input)
	//fmt.Println("done")
	//
	//message := make(chan string, 2)
	//
	//go func() {
	//	message <- "ping"
	//	message <- "haha"
	//	fmt.Println("hahahaha")
	//}()
	//
	//msg := <- message
	//
	//fmt.Println(msg)
	//
	//var input string
	//fmt.Scanln(&input)
	

	//done := make(chan bool, 1)
	//work(done)
	//
	//<- done
	//fmt.Println("receive done...")

	//chan1 := make(chan string, 1)
	//chan2 := make(chan string, 1)
	//
	//go func(data chan<- string) {
	//	time.Sleep(time.Second * 2)
	//	data<- "sb1"
	//}(chan1)
	//
	//go func(data chan<- string) {
	//	time.Sleep(time.Second * 1)
	//	data<- "sb2"
	//}(chan2)
	//
	//for i := 0; i < 2; i++ {
	//	select {
	//		case msg1 := <-chan1:
	//			fmt.Println("receive: ", msg1)
	//		case msg2 := <-chan2:
	//			fmt.Println("receive: ", msg2)
	//	}
	//}

	//jobs := make(chan int, 5)
	//done := make(chan bool)
	//
	//go func() {
	//	for {
	//		if i, isDone := <-jobs; isDone {
	//			fmt.Println("receive job: ", i)
	//			time.Sleep(time.Second * 3)
	//		} else {
	//			fmt.Println("receive all jobs")
	//			done<- false
	//			break
	//		}
	//	}
	//}()
	//
	//for i := 0; i < 3; i++ {
	//	jobs<- i
	//	fmt.Println("send job, ", i)
	//}
	//
	//close(jobs)
	//<-done
	//
	//time1 := time.NewTicker(time.Second)
	////<-time1.C
	////fmt.Println("haha")
	//
	//for job := range time1.C  {
	//	fmt.Println("job:: ", job)
	//}
	//
	//time.Sleep(time.Second * 5)
	//time1.Stop()
	//fmt.Println("finish")

	//request := make(chan int, 100)
	//result := make(chan int, 100)
	//
	//for i := 0; i < 3; i++ {
	//	go work(i, request, result)
	//}
	//
	//for i := 0; i < 9; i++ {
	//	request<- i
	//}
	//
	//close(request)
	//fmt.Println("finish job dispatch")
	//
	//for i := 0; i < 9; i++ {
	//	<-result
	//}
	//
	//var ops uint64 = 0
	//for i := 0; i < 5; i++ {
	//	go func() {
	//		for j:=0; j < 10; j++{
	//
	//			ops++
	//			//atomic.AddUint64(&ops, 1)
	//			//runtime.Gosched()
	//		}
	//	}()
	//}
	//
	//time.Sleep(time.Second * 3)
	////opsFinal := atomic.LoadUint64(&ops)
	//fmt.Println("data : ", ops)
}
//
//func work(num int, request <-chan int, result chan<- int) {
//	for job := range request  {
//		fmt.Println("work ", num, " job ", job)
//		time.Sleep(time.Second)
//		result<- job
//	}
//}

//func work(done chan bool)  {
//	fmt.Println("working....")
//	time.Sleep(time.Second)
//	fmt.Println("done....")
//
//	done <- true
//}
