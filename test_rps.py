import rps
import pytest



def test_computer_action():
    assert rps.computer_action() in rps.possible_actions


@pytest.mark.parametrize("test_input, expected",
                            [
                            (['r'], 'r'),
                            (['p'], 'p'),
                            (['s'], 's'),
                            (['t', 'r'], 'r'),
                            (['q', 'z', 's'], 's')                            
                            ]
                        )
def test_user_input(monkeypatch, test_input, expected):

    def make_multiple_inputs(inputs):
        """ provides a function to call for every input requested. """
        def next_input(_):
            """ provides the first item in the list. """
            return inputs.pop()
        return next_input

    monkeypatch.setitem(__builtins__, 'input', make_multiple_inputs(test_input))    
    assert rps.user_input() == expected


@pytest.mark.parametrize("test_input, expected",
                            [
                            ("DRAW", "Game ended in a tie!\n"),
                            ("WIN", "You won the game!\n"),
                            ("LOSE", "You lost the game!\n"),
                            ]
                        )
def test_print_result(capfd, test_input, expected):
    rps.print_result(test_input)

    out, err = capfd.readouterr()
    assert out == expected

@pytest.mark.parametrize("user_action, computer_action, expected",
                            [
                            ('r', 'r', "DRAW"),
                            ('p', 'p', "DRAW"),
                            ('s', 's', "DRAW"),
                            ('r', 's', "WIN"),
                            ('p', 'r', "WIN"),
                            ('s', 'p', "WIN"),
                            ('r', 'p', "LOSE"),
                            ('p', 's', "LOSE"),
                            ('s', 'r', "LOSE"),
                            ]
                        )
def test_decide_result(user_action, computer_action, expected):
    assert rps.decide_result(user_action, computer_action) == expected


