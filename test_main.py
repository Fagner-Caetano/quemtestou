import main  # Importa o código principal
import datetime  # Importa para validar a hora


# Testa se a hora retornada tem o formato correto
def test_get_current_time_format():
    time_str = main.get_current_time()
    try:
        datetime.datetime.strptime(time_str, "%H:%M:%S")
    except ValueError:
        assert False, f"Formato errado: {time_str}"


# Testa se a mensagem foi impressa corretamente
def test_print_container_message(capsys):
    main.print_container_message(1)
    captured = capsys.readouterr()
    assert "O container rodou 1x..." in captured.out

# O capsys captura tudo que é impresso na tela durante o teste
# Já capsys.readouterr() para pegar o que foi printado e testar o conteúdo
