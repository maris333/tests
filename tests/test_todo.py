import pytest

from mock import patch

from src.todo import add_todo, remove_todo, remove_all, edit_todo, check_pos


class TestToDo:
    def test_remove_all_clears_the_list(self, mocker):
        todos = ["Go to bed"]
        mocker.patch("src.todo.todos", todos)
        remove_all()
        assert len(todos) == 0

    def test_add_todo(self, mocker):
        todos = []
        mocker.patch("src.todo.todos", todos)
        add_todo("Go to bed")
        assert len(todos) == 1
        assert todos[0] == "Go to bed"

    @patch("src.todo.todos", ["Go to bed"])
    def test_remove_todo_removes_from_list(self, mocker):
        todos = ["Go to bed"]
        mocker.patch("src.todo.todos", todos)
        remove_todo(0)
        assert len(todos) == 0

    def test_edit_todo_edits_todo(self, mocker):
        todos = ["Go to bed"]
        mocker.patch("src.todo.todos", todos)
        edit_todo(0, "Get up")
        assert todos[0] == "Get up"

    def test_check_pos_raises_exception_when_no_todos(self, mocker):
        todos = []
        mocker.patch("src.todo.todos", todos)
        with pytest.raises(Exception, match="No more todos!"):
            check_pos(0)

    def test_check_pos_raises_exception_when_invalid_position(self, mocker):
        todos = ["Go to bed", "Get up"]
        mocker.patch("src.todo.todos", todos)
        with pytest.raises(Exception, match="No such item number!"):
            check_pos(2)
