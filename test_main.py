import main  # Importa o código principal
import datetime  # Importa para validar a hora
import pytest


# Função corrigida
def print_container_message(count):
    """
    Imprime uma mensagem indicando quantas vezes o container rodou.

    Args:
        count: O número de vezes que o container rodou. Deve ser um inteiro positivo.

    Raises:
        ValueError: Se count não for um inteiro positivo.
    """
    if not isinstance(count, int) or count <= 0:
        raise ValueError(f"Valor inválido: {count}")
    print(f"O container rodou {count}x...")


# Testes
def test_get_current_time_format():
    """Testa se a hora retornada tem o formato correto."""
    time_str = main.get_current_time()
    try:
        datetime.datetime.strptime(time_str, "%H:%M:%S")
    except ValueError:
        assert False, f"Formato errado: {time_str}"


def test_print_container_message(capsys):
    """Testa se a mensagem foi impressa corretamente."""
    main.print_container_message(1)
    captured = capsys.readouterr()
    assert "O container rodou 1x..." in captured.out, f"Mensagem não encontrada na saída: {captured.out}"


def test_get_current_time_not_empty():
    """Testa se a hora retornada não está vazia."""
    time_str = main.get_current_time()
    assert time_str != "", "A hora retornada está vazia!"


def test_get_current_time_extreme_values():
    """
    Testa os valores extremos de hora e minuto.
    """
    test_times = ["00:00:00", "23:59:59"]
    for time_str in test_times:
        try:
            datetime.datetime.strptime(time_str, "%H:%M:%S")
        except ValueError:
            assert False, f"Formato errado para hora: {time_str}"

    invalid_times = ["24:00:00", "12:60:00"]
    for time_str in invalid_times:
        with pytest.raises(ValueError):
            datetime.datetime.strptime(time_str, "%H:%M:%S")


def test_print_container_message_invalid_value():
    """Testa se a função lida com valores inválidos."""
    with pytest.raises(ValueError, match="Valor inválido: invalid"):
        main.print_container_message("invalid")
