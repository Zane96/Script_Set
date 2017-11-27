package main

import (
	"fmt"
	"os/exec"
	"io/ioutil"
)

var p = fmt.Println

func main()  {
	var dateCommand *exec.Cmd
	dateCommand = exec.Command("date")
	dateOutput, err := dateCommand.Output()

	if err != nil {
		panic(err)
	}

	p(string(dateOutput))

	grepCommand := exec.Command("grep hello")

	//get pipeline
	stdIn, _ := grepCommand.StdinPipe()
	stdOut, _ := grepCommand.StdoutPipe()

	grepCommand.Start()
	stdIn.Write([]byte("hello grep \n byebye grep"))
	stdIn.Close()
	outData, _ := ioutil.ReadAll(stdOut)
	grepCommand.Wait()

	p(string(outData))
}
