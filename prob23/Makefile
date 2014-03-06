CC = g++
CFLAGS = -Ofast -c -g -Wall -Werror -std=c++11

all: prob23

prob23: prob23.o
	$(CC) prob23.o -o prob23

prob23.o: prob23.cpp
	$(CC) $(CFLAGS) prob23.cpp

clean:
	rm -rf *.o prob23
