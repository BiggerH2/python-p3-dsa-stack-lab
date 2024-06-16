import pytest
from Stack import Stack, StackFullException

class TestStack:
    def test_init(self):
        '''Initialize Stack with list'''
        stk = Stack([1,2,3,4,5])
        expected = [1,2,3,4,5]
        for index in range(len(expected)):
            assert expected[index] == stk.stack[index]

    def test_push(self):
        '''Push 0 to stack'''
        stk = Stack([1,2,3,4,5])
        stk.push(0)
        expected = [1,2,3,4,5,0]
        for index in range(len(expected)):
            assert expected[index] == stk.stack[index]

    def test_pop(self):
        '''Pop 1 off the stack'''
        stk = Stack([1,2,3,4,5])
        stk.pop()
        expected = [1,2,3,4]
        for index in range(len(expected)):
            assert expected[index] == stk.stack[index]

    def test_size(self):
        '''Test Stack size() method'''
        stk = Stack([1,2,3,4,5])
        expected_size = 5
        assert stk.size() == expected_size

    def test_empty(self):
        '''Test Stack empty() method'''
        stk = Stack()
        assert stk.empty()

    def test_full(self):
        '''Test Stack full() method'''
        stk = Stack([1], 1)
        assert stk.full()
        assert stk.size() == 1
        assert stk.pop() == 1
        stk.push(1)
        with pytest.raises(StackFullException):
            stk.push(2)

    def test_search(self):
        '''Test Stack search() method. How far is the element in the stack?'''
        stk = Stack([5,6,7,8,9,10])
        assert stk.search(5) == 5
        assert stk.search(8) == 2
        assert stk.search(10) == 0
        assert stk.search(1) == -1
