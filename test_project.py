import pytest
from project import main_menu_choice

def test_enter_quits(monkeypatch):
    # setattr: temporarily sets the value of an attribute
    # builtins.input: input is from Python's builtins
    # lambda _: means random argument and returns an empty string ""
    monkeypatch.setattr("builtins.input", lambda _: "")
    with pytest.raises(SystemExit):
        main_menu_choice()

def test_invalid_input(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "xyz")
    result = main_menu_choice()
    assert result == "xyz"

def test_back(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "back")
    result = main_menu_choice()
    assert result == "back" 
