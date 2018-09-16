#!/usr/bin/env python
# for i in range(3):
#     print('#'*10)
#     for j in range(2):
#         print('#'+3*'..#')
# print('#'*10)
a = ['#'+3*'..#' for i in range(3) for j in range(2)]
[a.insert(k,'#'*10) for k in range(0,10,3)]
print('\n'.join(a))
