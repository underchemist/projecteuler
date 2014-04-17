CC = g++
CFLAGS = -Ofast -c -g -Wall -Werror -std=c++11

all: prob45

prob45: prob45.o
	$(CC) prob45.o -o prob45

prob45.o: prob45.cpp
	$(CC) $(CFLAGS) prob45.cpp

clean:
	rm -rf *.o prob45