package main

import (
	"encoding/json"
	"errors"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"os"
	"time"
)

type Config struct {
	Cookie string `json:"session-cookie"`
}

func checkErr(err error) {
	if err != nil {
		log.Fatal(err)
	}
}

func main() {
	// read session cookie
	file, err := os.Open("settings.json")
	checkErr(err)
	defer file.Close()
	bytes, _ := ioutil.ReadAll(file)
	var config Config
	json.Unmarshal(bytes, &config)
	client := &http.Client{}

	// date stuff
	year := 2023
	loc, _ := time.LoadLocation("America/New_York")
	today := time.Now().In(loc).Day()

	for day := 1; day <= today; day++ {
		// get input data
		req, err := http.NewRequest("GET", fmt.Sprintf("https://adventofcode.com/%d/day/%d/input", year, day), nil)
		checkErr(err)
		req.Header.Add("Cookie", "session="+config.Cookie)
		resp, err := client.Do(req)
		checkErr(err)
		body, err := ioutil.ReadAll(resp.Body)
		checkErr(err)
		path := fmt.Sprintf("../%02d", day)
		_ = os.Mkdir(path, os.ModePerm)
		err = os.WriteFile(path+"/input.txt", body, os.ModePerm)
		checkErr(err)

		//go template
		if _, err := os.Stat(fmt.Sprintf("../%02d/main.go", day)); errors.Is(err, os.ErrNotExist) {
			// path/to/whatever does not exist
			data, err := ioutil.ReadFile("template")
			checkErr(err)
			err = ioutil.WriteFile(fmt.Sprintf("../%02d/main.go", day), data, 0644)
			checkErr(err)
		}
	}
}
