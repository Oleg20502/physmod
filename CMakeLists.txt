cmake_minimum_required(VERSION 2.8)

project(class_examples C CXX)

#set(CMAKE_C_STANDARD 11)
#set(CMAKE_CXX_STANDARD 17)
set(CMAKE_C_FLAGS   "${CMAKE_CXX_FLAGS}  -std=c99 -g -Wall  -Wextra -pedantic")
set(CMAKE_CXX_FLAGS   "${CMAKE_CXX_FLAGS}  -std=c++17 -g -Wall  -Wextra -pedantic")


add_executable(ex_1.1 "wk_01/ex_1.c")
add_executable(ex_1.2 "wk_01/ex_2.cpp")
add_executable(ex_1.3 "wk_01/ex_3.cpp")
add_executable(ex_1.4 "wk_01/ex_4.cpp")
add_executable(ex_1.5 "wk_01/ex_5.cpp")
add_executable(ex_1.6 "wk_01/ex_6.cpp")
