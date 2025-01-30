package main

import (
	"fmt"
	"math/rand"
	"time"
)

func Random() {
	for {
		reasons := make([]string, 0)
		reasons = append(reasons,
			"Im working",
			"Im still working",
			"This program is working",
			"What do you think? It's still working",
		)

		if rand.Intn(5) == 4 { // 20% chance to panic
			panic("Программа завершилась с крашем")
		}

		fmt.Println(reasons[rand.Intn(len(reasons))])
		time.Sleep(2 * time.Second)
	}
}

func main() {
	Random()
}
