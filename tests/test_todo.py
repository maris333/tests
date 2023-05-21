import pytest

from src.todo import add_todo, todos, remove_todo, remove_all, edit_todo


class TestToDo:

    def test_remove_all_clears_the_list(self):
        remove_all()
        assert len(todos) == 0

    def test_add_todo_adds_to_list(self):
        remove_all()
        add_todo("Go to bed")
        assert len(todos) == 1

    def test_remove_todo_removes_from_list(self):
        remove_all()
        add_todo("Go to bed")
        remove_todo(0)
        assert len(todos) == 0

    def test_edit_todo_edits_todo(self):
        remove_all()
        add_todo("Go to bed")
        edit_todo(0, "Get up")
        assert todos[0] == "Get up"

    def test_check_pos_throws_exception(self):
        remove_all()
        with pytest.raises(Exception):
            remove_todo(0)
