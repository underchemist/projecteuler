CC = g++
CFLAGS = -Ofast -c -g -Wall -Werror -std=c++11

all: prob47

prob47: prob47.o
	$(CC) prob47.o -o prob47

prob47.o: prob47.cpp
	$(CC) $(CFLAGS) prob47.cpp

clean:
	rm -rf *.o prob47
