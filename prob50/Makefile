CC = g++
CFLAGS = -Ofast -c -pg -Wall -std=c++11

all: prob50

prob50: prob50.o
	$(CC) prob50.o -o prob50

prob50.o: prob50.cpp
	$(CC) $(CFLAGS) prob50.cpp

clean:
	rm -rf *.o prob50
