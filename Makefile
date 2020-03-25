UART="/dev/ttyUSB0"
BAUDRATE=115200

clean-board:
	rshell -p ${UART} -b ${BAUDRATE} --quiet rm /pyboard/*.*

load-program:
	rshell -p ${UART} -b ${BAUDRATE} --quiet cp src/*.* /pyboard

all: clean-board load-program
