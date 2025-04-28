import main 
import datetime


# Testa se a hora retornada tem o formato correto
def test_get_current_time_format():
    time_str = main.get_current_time()
    try:
        # Tenta analisar o formato da hora retornada
        datetime.datetime.strptime(time_str, "%H:%M:%S")
    except ValueError:
        assert False, f"Formato errado: {time_str}"


# Testa se a mensagem foi impressa corretamente
def test_print_container_message(capsys):
    main.print_container_message(1)
    captured = capsys.readouterr()
    assert "O container rodou 1x..." in captured.out, f"Mensagem não encontrada na saída: {captured.out}"


# Testa se a hora retornada não está vazia
def test_get_current_time_not_empty():
    time_str = main.get_current_time()
    assert time_str != "", "A hora retornada está vazia!"


# Testa se a hora é retornada corretamente nos valores extremos (00:00:00 e 23:59:59)
def test_get_current_time_extreme_values():
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


# Testa se a função lida com valores inválidos para o número de vezes
def test_print_container_message_invalid_value(capsys):
    try:
        main.print_container_message("invalid")
        assert False, "Era esperado ValueError ao passar valor inválido"
    except ValueError as e:
        assert str(e) == "Valor inválido: 'invalid'", f"Mensagem de erro incorreta: {e}"
