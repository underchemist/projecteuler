CC = g++
CFLAGS = -c -g -Wall -Werror -std=c++11

all: prob33

prob33: prob33.o
	$(CC) prob33.o -o prob33

prob33.o: prob33.cpp
	$(CC) $(CFLAGS) prob33.cpp

clean:
	rm -rf *.o prob33