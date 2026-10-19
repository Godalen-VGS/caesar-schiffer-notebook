from notebook_loader import last_notebook

oppgave = last_notebook("oppgave")


def test_krypter_eksempel():
    assert oppgave.krypter("Hei", 5) == "Mjn"


def test_dekrypter_reverserer_kryptering():
    assert oppgave.dekrypter(oppgave.krypter("Hei", 5), 5) == "Hei"
