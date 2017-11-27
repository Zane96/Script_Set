package main

import (
	"fmt"
	"syscall"
	"os/signal"
	"os"
)

func main()  {
	sign := make(chan os.Signal, 1)
	done := make(chan bool, 1)

	signal.Notify(sign, syscall.SIGINT)

	go func () {
		sig := <-sign
		fmt.Println("receive: ", sig)
		done <- true
	}()

	fmt.Println("waiting")
	<-done
	fmt.Println("exit")

}
