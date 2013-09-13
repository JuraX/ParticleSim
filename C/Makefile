CC = gcc
CFLAGS = -Wall -g -DJDEBUG
LDFLAGS = -lm

.PHONY: all
all:
	make universe

.PHONY: clean
clean:
	rm -rf universe *.o

vmath.o: vmath.c vmath.h
	${CC} ${CFLAGS} -c vmath.c

particle.o: particle.c particle.h
	${CC} ${CFLAGS} -c particle.c

main.o: main.c
	${CC} ${CFLAGS} -c main.c

universe: vmath.o particle.o main.o
	${CC} ${CFLAGS} vmath.o particle.o main.o ${LDFLAGS} -o universe
