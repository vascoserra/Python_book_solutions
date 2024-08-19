from Employee import Employe


def test_raise():
    nuno = Employe('Nuno', 'Silva')
    nuno.give_raise()
    assert nuno.salary == 15000


def test_raise_custom():
    nuno = Employe('Nuno', 'Silva')
    nuno.give_raise(10000)
    assert nuno.salary == 20000
