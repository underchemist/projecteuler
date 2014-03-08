CC = g++
CFLAGS = -Ofast -c -g -Wall -Werror -std=c++11

all: prob49

prob49: prob49.o
	$(CC) prob49.o -o prob49

prob49.o: prob49.cpp
	$(CC) $(CFLAGS) prob49.cpp

clean:
	rm -rf *.o prob49
