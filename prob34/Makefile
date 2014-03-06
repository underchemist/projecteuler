CC = g++
CFLAGS = -c -g -Wall -Werror -std=c++11

all: prob34

prob34: prob34.o
	$(CC) prob34.o -o prob34

prob34.o: prob34.cpp
	$(CC) $(CFLAGS) prob34.cpp

clean:
	rm -rf *.o prob34