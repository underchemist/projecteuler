CC = g++
CFLAGS = -Ofast -c -g -Wall -Werror -std=c++11

all: prob42

prob42: prob42.o
	$(CC) prob42.o -o prob42

prob42.o: prob42.cpp
	$(CC) $(CFLAGS) prob42.cpp

clean:
	rm -rf *.o prob42