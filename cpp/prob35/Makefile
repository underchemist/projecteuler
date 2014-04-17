CC = g++
CFLAGS = -Ofast -c -g -Wall -Werror -std=c++11

all: prob35

prob35: prob35.o
	$(CC) prob35.o -o prob35

prob35.o: prob35.cpp
	$(CC) $(CFLAGS) prob35.cpp

clean:
	rm -rf *.o prob35