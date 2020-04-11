UART="/dev/ttyUSB0"
BAUDRATE=115200

clean-board:
	rshell -p ${UART} -b ${BAUDRATE} --quiet rm /pyboard/*.*

load-program:
	rshell -p ${UART} -b ${BAUDRATE} --quiet cp src/*.* /pyboard

give-me-shell:
	rshell -p ${UART} -b ${BAUDRATE} --quiet

load-full-display:
	rshell -p ${UART} -b ${BAUDRATE} --quiet cp src/main.py /pyboard
	rshell -p ${UART} -b ${BAUDRATE} --quiet cp src/st7920.py /pyboard
	rshell -p ${UART} -b ${BAUDRATE} --quiet cp src/canvas.py /pyboard
load-main:
	rshell -p ${UART} -b ${BAUDRATE} --quiet cp src/main.py /pyboard

all: clean-board load-program
