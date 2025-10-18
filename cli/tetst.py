import unittest
from unittest.mock import patch, MagicMock
from todo_sd.services import project_service
from todo_sd.main import show_tasks  # adjust import path to your structure


class TestShowTasks(unittest.TestCase):

    @patch("builtins.input", return_value="1")
    @patch("todo_sd.main.project_service")
    @patch("todo_sd.main.show_projects")
    def test_show_tasks_with_tasks(self, mock_show_projects, mock_project_service, mock_input):
        # Mock a project with tasks
        mock_project_service.get_project_by_id.return_value = MagicMock(
            id=1,
            tasks=[
                MagicMock(id=1, title="Task 1", status="Pending"),
                MagicMock(id=2, title="Task 2", status="Done")
            ]
        )

        with patch("builtins.print") as mock_print:
            show_tasks()

        mock_show_projects.assert_called_once()
        mock_print.assert_any_call("  1. Task 1 — status: Pending")
        mock_print.assert_any_call("  2. Task 2 — status: Done")

    @patch("builtins.input", return_value="1")
    @patch("todo_sd.main.project_service")
    @patch("todo_sd.main.show_projects")
    def test_show_tasks_no_tasks(self, mock_show_projects, mock_project_service, mock_input):
        # Mock project with no tasks
        mock_project_service.get_project_by_id.return_value = MagicMock(id=1, tasks=[])

        with patch("builtins.print") as mock_print:
            show_tasks()

        mock_print.assert_any_call(" No tasks for this project.")

    @patch("builtins.input", return_value="999")
    @patch("todo_sd.main.project_service")
    @patch("todo_sd.main.show_projects")
    def test_show_tasks_project_not_found(self, mock_show_projects, mock_project_service, mock_input):
        # Mock no project found
        mock_project_service.get_project_by_id.return_value = None

        with patch("builtins.print") as mock_print:
            show_tasks()

        mock_print.assert_any_call(" Project not found.")

    @patch("builtins.input", return_value="abc")
    @patch("todo_sd.main.project_service")
    @patch("todo_sd.main.show_projects")
    def test_show_tasks_invalid_input(self, mock_show_projects, mock_project_service, mock_input):
        # Mock invalid input (non-numeric)
        with patch("builtins.print") as mock_print:
            show_tasks()

        mock_print.assert_any_call("Error: invalid literal for int() with base 10: 'abc'")


if __name__ == "__main__":
    unittest.main()
