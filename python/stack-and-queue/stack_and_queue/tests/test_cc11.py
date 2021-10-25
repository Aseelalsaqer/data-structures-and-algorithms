from stack_and_queue.CC11.stack_queue import PseudoQueue

def test_input_multi():
    # Arrange
    expected = 1
    Pseudoqueue = PseudoQueue()
    # Act
    Pseudoqueue.enqueue(1)
    Pseudoqueue.enqueue(2)
    Pseudoqueue.enqueue(3)
    actual = Pseudoqueue.rear
    # Assert
    assert expected == actual
def test_pseudo():
    # Arrange
    expected = 1
    Pseudoqueue = PseudoQueue()
    # Act
    Pseudoqueue.enqueue(0)
    Pseudoqueue.enqueue(1)
    Pseudoqueue.dequeue()
    actual = Pseudoqueue.dequeue()
    # Assert
    assert expected == actual
def test_empty():
    # Arrange
    expected = None
    Pseudoqueue = PseudoQueue()
    # Act
    actual = Pseudoqueue.dequeue()
    # Assert
    assert expected == actual
