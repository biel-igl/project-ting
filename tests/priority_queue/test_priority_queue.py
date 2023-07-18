from ting_file_management.priority_queue import PriorityQueue
import pytest


def test_basic_priority_queueing():
    queue = PriorityQueue()

    ex1 = {"nome": "aqui.txt", "qtd_linhas": 5}
    ex2 = {"nome": "aqui.txt", "qtd_linhas": 1}

    queue.enqueue(ex1)
    assert len(queue) == 1

    queue.dequeue()
    assert len(queue) == 0

    queue.enqueue(ex1)
    queue.enqueue(ex2)
    assert queue.search(0) == ex2
    assert queue.search(1) == ex1

    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        queue.search(17)
