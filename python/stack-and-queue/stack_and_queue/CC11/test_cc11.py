from CC11 import __version__

from CC11.stack_queue import PseudoQueue

def test_input_multi():
    Pseudoqueue = PseudoQueue()
    Pseudoqueue.enqueue(1)
    Pseudoqueue.enqueue(2)
    Pseudoqueue.enqueue(3)
    actual = Pseudoqueue.rear
    expected = 3
    assert expected == actual
