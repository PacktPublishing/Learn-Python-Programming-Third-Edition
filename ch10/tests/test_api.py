# tests/test_api.py
import re
from unittest.mock import patch, mock_open, call

import pytest

from ch10.api import is_valid, export, write_csv


@pytest.fixture
def min_user():
    """Represent a valid user with minimal data. """
    return {
        'email': 'minimal@example.com',
        'name': 'Primus Minimus',
        'age': 18,
    }


@pytest.fixture
def full_user():
    """Represent valid user with full data. """
    return {
        'email': 'full@example.com',
        'name': 'Maximus Plenus',
        'age': 65,
        'role': 'emperor',
    }


@pytest.fixture
def users(min_user, full_user):
    """List of users, two valid and one invalid. """
    bad_user = {
        'email': 'invalid@example.com',
        'name': 'Horribilis',
    }
    return [min_user, bad_user, full_user]


class TestIsValid:
    """Test how code verifies whether a user is valid or not. """

    def test_minimal(self, min_user):
        assert is_valid(min_user)

    def test_full(self, full_user):
        assert is_valid(full_user)

    @pytest.mark.parametrize('age', range(18))
    def test_invalid_age_too_young(self, age, min_user):
        min_user['age'] = age

        assert not is_valid(min_user)

    @pytest.mark.parametrize('age', range(66, 100))
    def test_invalid_age_too_old(self, age, min_user):
        min_user['age'] = age

        assert not is_valid(min_user)

    @pytest.mark.parametrize('age', ['NaN', 3.1415, None])
    def test_invalid_age_wrong_type(self, age, min_user):
        min_user['age'] = age

        assert not is_valid(min_user)

    @pytest.mark.parametrize('age', range(18, 66))
    def test_valid_age(self, age, min_user):
        min_user['age'] = age

        assert is_valid(min_user)

    @pytest.mark.parametrize('field', ['email', 'name', 'age'])
    def test_mandatory_fields(self, field, min_user):
        del min_user[field]

        assert not is_valid(min_user)

    @pytest.mark.parametrize('field', ['email', 'name', 'age'])
    def test_mandatory_fields_empty(self, field, min_user):
        min_user[field] = ''

        assert not is_valid(min_user)

    def test_name_whitespace_only(self, min_user):
        min_user['name'] = ' \n\t'

        assert not is_valid(min_user)

    @pytest.mark.parametrize(
        'email, outcome',
        [
            ('missing_at.com', False),
            ('@missing_start.com', False),
            ('missing_end@', False),
            ('missing_dot@example', False),

            ('good.one@example.com', True),
            ('δοκιμή@παράδειγμα.δοκιμή', True),
            ('аджай@экзампл.рус', True),
        ]
    )
    def test_email(self, email, outcome, min_user):
        min_user['email'] = email

        assert is_valid(min_user) == outcome

    @pytest.mark.parametrize(
        'field, value',
        [
            ('email', None),
            ('email', 3.1415),
            ('email', {}),

            ('name', None),
            ('name', 3.1415),
            ('name', {}),

            ('role', None),
            ('role', 3.1415),
            ('role', {}),
        ]
    )
    def test_invalid_types(self, field, value, min_user):
        min_user[field] = value

        assert not is_valid(min_user)


class TestExport:
    """Test behavior of `export` function. """

    @pytest.fixture
    def csv_file(self, tmp_path):
        """Yield a filename in a temporary folder.

        Due to how pytest `tmp_path` fixture works, the file does
        not exist yet.
        """
        yield tmp_path / "out.csv"

    @pytest.fixture
    def existing_file(self, tmp_path):
        """Create a temporary file and put some content in it. """
        existing = tmp_path / 'existing.csv'
        existing.write_text('Please leave me alone...')
        yield existing

    def test_export(self, users, csv_file):
        export(csv_file, users)

        text = csv_file.read_text()

        assert (
            'email,name,age,role\n'
            'minimal@example.com,Primus Minimus,18,\n'
            'full@example.com,Maximus Plenus,65,emperor\n'
         ) == text

    def test_export_quoting(self, min_user, csv_file):
        min_user['name'] = 'A name, with a comma'

        export(csv_file, [min_user])

        text = csv_file.read_text()

        assert (
            'email,name,age,role\n'
            'minimal@example.com,"A name, with a comma",18,\n'
         ) == text

    def test_does_not_overwrite(self, users, existing_file):
        with pytest.raises(IOError) as err:
            export(existing_file, users, overwrite=False)

        err.match(
            r"'{}' already exists\.".format(
                re.escape(str(existing_file))
            )
        )

        # let's also verify the file is still intact
        assert existing_file.read_text() == (
            'Please leave me alone...'
        )


class TextExportMock:
    """Example on how to test with mocks. """

    @pytest.fixture
    def write_csv_mock(self):
        with patch('ch10.api.write_csv') as m:
            yield m

    @pytest.fixture
    def get_valid_users_mock(self):
        with patch('ch10.api.get_valid_users') as m:
            yield m

    def test_export(
        self, write_csv_mock, get_valid_users_mock, users
    ):
        export('out.csv', users)

        # verify mocked funcs have been called properly
        assert [call(users)] == get_valid_users_mock.call_args_list

        valid_users = get_valid_users_mock.return_value
        assert [
            call('out.csv', valid_users)
        ] == write_csv_mock.call_args_list


class TestWriteCSV:
    """Example on how to test with mocks. """

    @pytest.fixture
    def open_mock(self):
        """Mocks the `open` function. """
        with patch('builtins.open', new_callable=mock_open()) as m:
            yield m

    @pytest.fixture
    def csv_mock(self):
        """Mocks the `csv` module as imported in `api.py`. """
        with patch('ch10.api.csv') as m:
            yield m

    def test_write_csv(self, open_mock, csv_mock, users):
        fieldnames = ['email', 'name', 'age', 'role']

        write_csv('out.csv', users)

        # verify both mocks are at work properly
        writer = csv_mock.DictWriter.return_value
        managed = open_mock().__enter__()

        assert [
            call(managed, fieldnames=fieldnames)
        ] == csv_mock.DictWriter.call_args_list

        assert [call()] == writer.writeheader.call_args_list

        assert [
            call(users[0]), call(users[1]), call(users[2])
        ] == writer.writerow.call_args_list
