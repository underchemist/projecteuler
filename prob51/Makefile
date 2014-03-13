CC = g++
CFLAGS = -O3 -c -g -Wall -std=c++11

all: prob51

prob51: prob51.o
	$(CC) prob51.o -o prob51

prob51.o: prob51.cpp
	$(CC) $(CFLAGS) prob51.cpp

clean:
	rm -rf *.o prob51
