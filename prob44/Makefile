CC = g++
CFLAGS = -Ofast -c -g -Wall -Werror -std=c++11

all: prob44

prob44: prob44.o
	$(CC) prob44.o -o prob44

prob44.o: prob44.cpp
	$(CC) $(CFLAGS) prob44.cpp

clean:
	rm -rf *.o prob44