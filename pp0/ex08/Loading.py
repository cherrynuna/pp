from shutil import get_terminal_size
from time import time


def ft_tqdm(lst: range) -> None:
    """
    Custom implementation of tqdm progress bar using yield.

    Args:
        lst (range): Iterable range object.

    Yields:
        Elements from the iterable while displaying progress bar.
    """
    total = len(lst)
    start = time()

    for i, val in enumerate(lst, 1):
        percent = int(i / total * 100)

        width = get_terminal_size().columns - 30
        bar = int(i / total * width)

        elapsed = time() - start
        speed = i / elapsed if elapsed > 0 else 0

        print(
            f"\r{percent:3d}%|"
            f"[{'=' * bar}{'>' if i < total else '='}"
            f"{' ' * (width - bar)}]| "
            f"{i}/{total} [{elapsed:.2f}s, {speed:.2f}it/s]",
            end=""
        )

        yield val