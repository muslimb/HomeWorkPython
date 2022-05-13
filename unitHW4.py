from HW4 import Queue
from HW4 import Stack
from HW4 import Spiska
import unittest

###ocheridi
class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()
    def test_enqueue(self):
        self.queue.push(7)
        self.assertIn(7, self.queue.queue1)
    def test_pop(self):
        self.queue.queue1 = [5,6]
        self.assertEqual(self.queue.pop(), 5)

##Stack
class TestStack(unittest.TestCase):
    def setUp(self):
        self.stak = Stack()
    def test_push(self):
        self.stak.push(9)
        self.assertIn(9, self.stak.stack)
    def test_pop(self):
        self.stak.stack = [5, 6]
        self.assertEqual(self.stak.pop1(), 6)

#spiska
class TestSpiska(unittest.TestCase):
    def setUp(self):
        self.spiska = Spiska()
    def test_InsertAtEnd(self,):
        self.spiska.InsertAtEnd(88)
        self.assertIn(88, self.spiska.spiska1)
    def test_InsertAtHead(self):
        self.spiska.InsertAtHead(99)
        self.assertIn(99, self.spiska.spiska1)
    def test_Delete(self):
        self.spiska.spiska1 = [76, 81]
        self.spiska.Delete(81)
        self.assertIn(76, self.spiska.spiska1)
    def test_DeleteAtHead(self):
        self.spiska.spiska1 = [8, 7, 4]
        self.assertEqual(self.spiska.DeleteAtHead(),8)
    def test_DeleteAtEnd(self):
        self.spiska.spiska1 = [5, 4, 1]
        self.assertEqual(self.spiska.DeleteAtEnd(),1)
    def test_SearchIndexElement(self):
        self.spiska.spiska1 = [45, 12, 55]
        self.assertEqual(self.spiska.SearchIndexElement(55), 2)


