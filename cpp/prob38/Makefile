CC = g++
CFLAGS = -Ofast -c -g -Wall -Werror -std=c++11

all: prob38

prob38: prob38.o
	$(CC) prob38.o -o prob38

prob38.o: prob38.cpp
	$(CC) $(CFLAGS) prob38.cpp

clean:
	rm -rf *.o prob38