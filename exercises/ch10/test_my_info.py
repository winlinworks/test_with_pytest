from unittest import mock
import my_info


def test_my_home_returns_correct_value():
    with mock.patch.object(my_info.Path, "home", return_value="/users/fake_user") as mock_home:
        value = my_info.home_dir()
        assert value == "/users/fake_user"


def test_my_home_is_called():
    with mock.patch.object(my_info.Path, "home", return_value="/users/fake_user") as mock_home:
        my_info.home_dir()
        # check to see if Path.home() was called
        mock_home.assert_called_once()
