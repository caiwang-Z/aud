# -*- coding: utf-8 -*-
"""
@author: zcw
@software: PyCharm
@file: stack.py
@time: 07.10.2021 22:48
"""
class Stack:

    def __init__(self):
        self.stack = []

    def push(self, i):
        self.stack.append(i)

    def pop(self):
        self.stack.pop()

    def get_top(self):
        if len(self.stack):
            return self.stack[-1]
        else:
            return None
    def is_empty(self):
        return len(self.stack) == 0

def test(string):
    st = Stack()
    dic = {')': '(', ']': '[', '}': '{'}
    for ch in string:
        if ch in ['(', '[', '{']:
            st.push(ch)
        else:
            if st.is_empty():
                return False

            elif st.get_top() == dic[ch]:
                st.pop()
            else:
                return False
    if st.is_empty():
        return True
    else:
        return False

if __name__ == '__main__':
    print(test('()[]{()[(]}'))