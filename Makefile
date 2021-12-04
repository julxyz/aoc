MAKEFLAGS += -s

# If the first argument is "run"...
ifneq ($(filter $(firstword $(MAKECMDGOALS)), run build new),)
  # use the rest as arguments for "run"
  ARGS := $(wordlist 2,$(words $(MAKECMDGOALS)),$(MAKECMDGOALS))
  # ...and turn them into do-nothing targets
  $(eval $(ARGS):;@:)
endif

.PHONY: build run new

build:
	g++ $(ARGS)/*.cpp -o $(ARGS)/solution.exe -std=c++17

run: build
	./$(ARGS)/solution.exe $(ARGS)

new:
	cp -r "_" $(ARGS)