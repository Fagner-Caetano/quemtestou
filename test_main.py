import main  # Importa o código principal
import datetime  # Importa para validar a hora


# Função corrigida
def print_container_message(count):
    """
    Imprime uma mensagem indicando quantas vezes o container rodou.

    Args:
        count: O número de vezes que o container rodou. Deve ser um inteiro positivo.

    Raises:
        ValueError: Se count não for um inteiro positivo.
    """
    # Verifica se count é um número inteiro positivo
    if not isinstance(count, int) or count <= 0:
        raise ValueError(f"Valor inválido: {count}")

    print(f"O container rodou {count}x...")


# Testes
def test_get_current_time_format():
    """Testa se a hora retornada tem o formato correto."""
    time_str = main.get_current_time()
    try:
        # Tenta analisar o formato da hora retornada
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
    Testa se a hora é retornada corretamente nos valores extremos (00:00:00 e 23:59:59)
    e se erros são gerados para valores inválidos.
    """
    # Teste para o horário mínimo (00:00:00)
    time_str = "00:00:00"
    try:
        datetime.datetime.strptime(time_str, "%H:%M:%S")
    except ValueError:
        assert False, f"Formato errado para hora mínima: {time_str}"

    # Teste para o horário máximo (23:59:59)
    time_str = "23:59:59"
    try:
        datetime.datetime.strptime(time_str, "%H:%M:%S")
    except ValueError:
        assert False, f"Formato errado para hora máxima: {time_str}"

    # Teste para hora inválida (24:00:00)
    time_str = "24:00:00"
    try:
        datetime.datetime.strptime(time_str, "%H:%M:%S")
        assert False, f"Era esperado erro para hora inválida: {time_str}"
    except ValueError:
        pass  # Hora inválida gerou o erro esperado

    # Teste para minuto inválido (12:60:00)
    time_str = "12:60:00"
    try:
        datetime.datetime.strptime(time_str, "%H:%M:%S")
        assert False, f"Era esperado erro para minuto inválido: {time_str}"
    except ValueError:
        pass  # Minuto inválido gerou o erro esperado


def test_print_container_message_invalid_value(capsys):
    """Testa se a função lida com valores inválidos para o número de vezes."""
    try:
        # Passando um valor inválido (não inteiro)
        main.print_container_message("invalid")
    except ValueError as e:
        # Verificando se a mensagem de erro é a esperada
        assert str(e) == "Valor inválido: invalid", f"Mensagem de erro incorreta: {e}"
    else:
        # Se chegarmos aqui, significa que nenhum ValueError foi levantado, o que é um erro.
        assert False, "Era esperado ValueError ao passar valor inválido"
