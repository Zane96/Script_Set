package main

import "encoding/json"
import "fmt"

var p = fmt.Println

type Response struct {
	Page int
	Datas []string
}

func main()  {
	rep := Response{
		Page: 1,
		Datas: []string{"1", "2"}}


	repStr, _ := json.Marshal(rep)
	p(string(repStr))

	s := `{"Page":1, "Datas":["1", "2"]}`
	repo := Response{}
	json.Unmarshal([]byte(s), &repo)
	p(repo)
}
