CC = g++
CFLAGS = -Ofast -c -g -Wall -Werror -std=c++11

all: prob36

prob36: prob36.o
	$(CC) prob36.o -o prob36

prob36.o: prob36.cpp
	$(CC) $(CFLAGS) prob36.cpp

clean:
	rm -rf *.o prob36