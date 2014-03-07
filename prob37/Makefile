CC = g++
CFLAGS = -Ofast -c -g -Wall -Werror -std=c++11

all: prob37

prob37: prob37.o
	$(CC) prob37.o -o prob37

prob37.o: prob37.cpp
	$(CC) $(CFLAGS) prob37.cpp

clean:
	rm -rf *.o prob37