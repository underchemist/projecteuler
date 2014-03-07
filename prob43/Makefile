CC = g++
CFLAGS = -Ofast -c -g -Wall -std=c++11

all: prob43

prob43: prob43.o
	$(CC) prob43.o -o prob43

prob43.o: prob43.cpp
	$(CC) $(CFLAGS) prob43.cpp

clean:
	rm -rf *.o prob43