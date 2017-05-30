import os
import pytest
import datetime

from ran.screen import logo_lines, message, logo, stats, get_date, get_type
from ran.screen import get_duration, get_distance, get_sets, dict_to_str


class TestLogo():

    def test_logo_lines(self):
        lg = [
            ' _ __ __ _ _ __  ',
            "| '__/ _` | '_ \\ ",
            '| | | (_| | | | |',
            '|_|  \\__,_|_| |_|']

        assert logo_lines() == lg

    def test_logo(self, monkeypatch, capsys):
        def mockreturn(fd):
            return (15, 42)

        monkeypatch.setattr(os, 'get_terminal_size', mockreturn)
        logo()

        out, err = capsys.readouterr()

        text = (
            '\n\n\x1b[96m _ __ __ _ _ __  \x1b[0m\n' +
            "\x1b[96m| '__/ _` | '_ \\ \x1b[0m\n" +
            '\x1b[96m| | | (_| | | | |\x1b[0m\n' +
            '\x1b[96m|_|  \\__,_|_| |_|\x1b[0m\n')

        assert out == text


class TestMessage:

    def test_message_with_valid_command(self, capsys):
        message('')
        out, err = capsys.readouterr()

        assert out == 'Enter [h]elp\n'

    def test_message_with_invalid_command(self, capsys):
        message('none')
        out, err = capsys.readouterr()

        assert out == '\x1b[91mBad syntax, enter [h]elp\x1b[0m\n'


def test_stats(monkeypatch, capsys):
    def mockreturn(fd):
        return(42, 10)

    monkeypatch.setattr(os, 'get_terminal_size', mockreturn)
    stats('')

    out, err = capsys.readouterr()

    assert out == '\n\n'


@pytest.fixture()
def workout():
    data = {
        'date': {'year': 123, 'month': 1, 'day': 12},
        'run': {
            'type': 'test',
            'duration': {
                'hour': 0,
                'minute': 50,
                'second': 0,
                'micro': 0},
            'distance': 11300
        },
        'strength': {
            'pull-ups': [
                17,
                14,
                11
            ],
            'push-ups': [
                17,
                14,
                11
            ],
            'sit-ups': [
                17,
                14,
                11
            ]
        }
    }

    return data


@pytest.fixture()
def mockreturn():
    def mock(fd):
        return (42, 24)

    return mock


@pytest.mark.usefixtures('workout', 'mockreturn')
class TestGetDate:

    def test_get_date_with_true_cancel_arg(self, monkeypatch):

        monkeypatch.setitem(__builtins__, 'input', lambda x: '')
        monkeypatch.setattr(os, 'get_terminal_size', mockreturn())

        cancel = True
        (cancel, data) = get_date(cancel, workout())

        assert cancel
        assert list(data['date'].values()) == [123, 1, 12]

    def test_get_date_with_cancel_input(self, monkeypatch):

        monkeypatch.setitem(__builtins__, 'input', lambda x: 'c')
        monkeypatch.setattr(os, 'get_terminal_size', mockreturn())

        cancel = False
        (cancel, data) = get_date(cancel, workout())

        assert cancel
        assert list(data['date'].values()) == [123, 1, 12]

    def test_get_date_with_default_input(self, monkeypatch):

        monkeypatch.setitem(__builtins__, 'input', lambda x: '')
        monkeypatch.setattr(os, 'get_terminal_size', mockreturn())
        t = datetime.date.today()

        cancel = False
        (cancel, data) = get_date(cancel, workout())

        assert not cancel
        assert list(data['date'].values()) == [t.year, t.month, t.day]

    def test_get_date_with_valid_input(self, monkeypatch):

        monkeypatch.setitem(__builtins__, 'input', lambda x: '2017-5-29')
        monkeypatch.setattr(os, 'get_terminal_size', mockreturn())

        cancel = False
        (cancel, data) = get_date(cancel, workout())

        assert not cancel
        assert list(data['date'].values()) == [2017, 5, 29]


@pytest.mark.usefixtures('workout', 'mockreturn')
class TestGetType:

    def test_get_type_with_true_cancel_arg(self, monkeypatch):

        monkeypatch.setitem(__builtins__, 'input', lambda x: '')
        monkeypatch.setattr(os, 'get_terminal_size', mockreturn())

        cancel = True
        (cancel, data) = get_type(cancel, workout())

        assert cancel
        assert data['run']['type'] == 'test'

    def test_get_type_with_cancel_input(self, monkeypatch):

        monkeypatch.setitem(__builtins__, 'input', lambda x: 'c')
        monkeypatch.setattr(os, 'get_terminal_size', mockreturn())

        cancel = False
        (cancel, data) = get_type(cancel, workout())

        assert cancel
        assert data['run']['type'] == 'test'

    def test_get_type_with_default_input(self, monkeypatch):

        monkeypatch.setitem(__builtins__, 'input', lambda x: '')
        monkeypatch.setattr(os, 'get_terminal_size', mockreturn())

        cancel = False
        (cancel, data) = get_type(cancel, workout())

        assert not cancel
        assert data['run']['type'] == 'base'


@pytest.mark.usefixtures('workout', 'mockreturn')
class TestGetDuration:

    def test_get_duration_with_true_cancel_arg(self, monkeypatch):

        monkeypatch.setitem(__builtins__, 'input', lambda x: '')
        monkeypatch.setattr(os, 'get_terminal_size', mockreturn())

        cancel = True
        (cancel, data) = get_duration(cancel, workout())

        assert cancel
        assert list(data['run']['duration'].values()) == [0, 50, 0, 0]

    def test_get_duration_with_cancel_input(self, monkeypatch):

        monkeypatch.setitem(__builtins__, 'input', lambda x: 'c')
        monkeypatch.setattr(os, 'get_terminal_size', mockreturn())

        cancel = False
        (cancel, data) = get_duration(cancel, workout())

        assert cancel
        assert list(data['run']['duration'].values()) == [0, 50, 0, 0]

    def test_get_duration_with_valid_input(self, monkeypatch):

        monkeypatch.setitem(__builtins__, 'input', lambda x: '0:51:0.0')
        monkeypatch.setattr(os, 'get_terminal_size', mockreturn())

        cancel = False
        (cancel, data) = get_duration(cancel, workout())

        assert not cancel
        assert list(data['run']['duration'].values()) == [0, 51, 0, 0]


@pytest.mark.usefixtures('workout', 'mockreturn')
class TestGetDistance:

    def test_get_distance_with_true_cancel_arg(self, monkeypatch):

        monkeypatch.setitem(__builtins__, 'input', lambda x: '')
        monkeypatch.setattr(os, 'get_terminal_size', mockreturn())

        cancel = True
        (cancel, data) = get_distance(cancel, workout())

        assert cancel
        assert data['run']['distance'] == 11300

    def test_get_distance_with_cancel_input(self, monkeypatch):

        monkeypatch.setitem(__builtins__, 'input', lambda x: 'c')
        monkeypatch.setattr(os, 'get_terminal_size', mockreturn())

        cancel = False
        (cancel, data) = get_distance(cancel, workout())

        assert cancel
        assert data['run']['distance'] == 11300

    def test_get_distance_with_valid_input(self, monkeypatch):

        monkeypatch.setitem(__builtins__, 'input', lambda x: '11400')
        monkeypatch.setattr(os, 'get_terminal_size', mockreturn())

        cancel = False
        (cancel, data) = get_distance(cancel, workout())

        assert not cancel
        assert data['run']['distance'] == 11400


@pytest.mark.usefixtures('workout', 'mockreturn')
class TestGetSets:

    @pytest.fixture(
        scope='class',
        params=['pull-ups', 'push-ups', 'sit-ups'])
    def exercise(self, request):
        return request.param

    def test_get_sets_with_true_cancel_arg(self, monkeypatch, exercise):

        monkeypatch.setitem(__builtins__, 'input', lambda x: '')
        monkeypatch.setattr(os, 'get_terminal_size', mockreturn())

        cancel = True
        (cancel, data) = get_sets(cancel, workout(), exercise)

        assert cancel
        assert data['strength'][exercise] == [17, 14, 11]

    def test_get_sets_with_cancel_input(self, monkeypatch, exercise):

        monkeypatch.setitem(__builtins__, 'input', lambda x: 'c')
        monkeypatch.setattr(os, 'get_terminal_size', mockreturn())

        cancel = False
        (cancel, data) = get_sets(cancel, workout(), exercise)

        assert cancel
        assert data['strength'][exercise] == [17, 14, 11]

    def test_get_sets_with_valid_input(self, monkeypatch, exercise):

        monkeypatch.setitem(__builtins__, 'input', lambda x: '110, 220')
        monkeypatch.setattr(os, 'get_terminal_size', mockreturn())

        cancel = False
        (cancel, data) = get_sets(cancel, workout(), exercise)

        assert not cancel
        assert data['strength'][exercise] == [110, 220]


class TestDictToStr:

    @pytest.fixture(
        scope='class',
        params=[
            {
                'year': '',
                'month': '',
                'day': ''},
            {
                'hour': '',
                'minute': '',
                'second': '',
                'micro': ''}])
    def dicts(self, request):
        return request.param

    def test_dict_to_str_with_empty_arg(self, dicts):
        assert dict_to_str(dicts) == ''

    def test_dict_to_str_with_date(self):
        date = {'year': 2017, 'month': 2, 'day': 1}
        assert dict_to_str(date) == '2017-2-1'

    def test_dict_to_str_with_duration(self):
        duration = {'hour': 1, 'minute': 15, 'second': 0, 'micro': 0}
        assert dict_to_str(duration) == '1:15:0.0'
