CC = g++
CFLAGS = -Ofast -c -g -Wall -Werror -std=c++11

all: prob46

prob46: prob46.o
	$(CC) prob46.o -o prob46

prob46.o: prob46.cpp
	$(CC) $(CFLAGS) prob46.cpp

clean:
	rm -rf *.o prob46
