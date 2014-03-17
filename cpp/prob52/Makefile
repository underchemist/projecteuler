CC = g++
CFLAGS = -O3 -c -g -Wall -std=c++11

all: prob52

prob52: prob52.o
	$(CC) prob52.o -o prob52

prob52.o: prob52.cpp
	$(CC) $(CFLAGS) prob52.cpp

clean:
	rm -rf *.o prob52
