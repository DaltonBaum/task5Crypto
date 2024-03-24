SRC_FILES = main.cpp

CXX = g++
CFLAGS = -Wall -g

OBJECTS = $(SRC_FILES:.cpp=.o)

INC=/usr/local/ssl/include/
LIB=/usr/local/ssl/lib/
all:
gcc -I$(INC) -L$(LIB) -o enc yourcode.c -lcrypto -ldl

$(TARGET): $(OBJECTS)
	$(CXX) -o $@ $^

%.o: %.cpp
	$(CXX) $(CFLAGS) -o $@ -c $<

clean:
	$(DEL) $(TARGET) $(OBJECTS)


