from src.utils import load_operations, display_last_operations


def main():
    operations = load_operations('operations.json')
    display_last_operations(operations)


if __name__ == "__main__":
    main()
