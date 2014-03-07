CC = g++
CFLAGS = -Ofast -c -g -Wall -Werror -std=c++11

all: prob41

prob41: prob41.o
	$(CC) prob41.o -o prob41

prob41.o: prob41.cpp
	$(CC) $(CFLAGS) prob41.cpp

clean:
	rm -rf *.o prob41