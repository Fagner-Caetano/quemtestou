import main  # Importa o código principal
import datetime  # Importa para validar a hora
import pytest


def test_print_container_message_positive_integer(capsys):
    """Testa se a função imprime a mensagem corretamente com um inteiro positivo."""
    main.print_container_message(5)
    captured = capsys.readouterr()
    assert "O container rodou 5x..." in captured.out


def test_print_container_message_zero(capsys):
    """Testa se a função levanta ValueError para count igual a zero."""
    with pytest.raises(ValueError, match="Valor inválido: 0"):
        main.print_container_message(0)


def test_print_container_message_negative_integer(capsys):
    """Testa se a função levanta ValueError para count negativo."""
    with pytest.raises(ValueError, match="Valor inválido: -1"):
        main.print_container_message(-1)


def test_print_container_message_invalid_type(capsys):
    """Testa se a função levanta ValueError para tipo inválido de count (string)."""
    with pytest.raises(ValueError, match="Valor inválido: abc"):
        main.print_container_message("abc")


def test_get_current_time_format():
    """Testa se a hora retornada está no formato correto."""
    time_str = main.get_current_time()
    try:
        datetime.datetime.strptime(time_str, "%H:%M:%S")
    except ValueError:
        assert False, f"Formato de hora incorreto: {time_str}"