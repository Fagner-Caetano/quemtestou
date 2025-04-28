import time
import datetime


def get_current_time():
    return datetime.datetime.now().strftime("%H:%M:%S")


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
        
    current_time = get_current_time()
    print(f"[{current_time}] O container rodou {count}x...")


def main_loop():
    count = 1
    try:
        print("Container iniciado. Pressione Ctrl+C para encerrar.")
        while True:
            print_container_message(count)
            count += 1
            time.sleep(5)
    except KeyboardInterrupt:
        print("\nContainer encerrado pelo usuário.")


if __name__ == "__main__":
    main_loop()