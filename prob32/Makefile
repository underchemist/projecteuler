CC = g++
CFLAGS = -c -g -Wall -Werror -std=c++11

all: prob32

prob32: prob32.o
	$(CC) prob32.o -o prob32

prob32.o: prob32.cpp
	$(CC) $(CFLAGS) prob32.cpp

clean:
	rm -rf *.o prob32