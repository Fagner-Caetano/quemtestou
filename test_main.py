import main
import datetime

def test_get_current_time_format():
    time_str = main.get_current_time()
    try:
        datetime.datetime.strptime(time_str, "%H:%M:%S")
    except ValueError:
        assert False, f"Formato de hora inválido: {time_str}"

def test_print_container_message(capsys):
    main.print_container_message(1)
    captured = capsys.readouterr()
    assert "O container rodou 1x..." in captured.out
