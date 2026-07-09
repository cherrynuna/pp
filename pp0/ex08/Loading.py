import os

def ft_tqdm(iterable):
    """
    Decorate an iterable object, returning an iterator which yields
    the original iterable values and displays a dynamically updating
    progressbar every time a value is requested.
    """
    total = len(iterable)
    for n, item in enumerate(iterable, 1):
        try:
            terminal_width = os.get_terminal_size().columns - 26
        except OSError:
            terminal_width = 178 - 26

        percent = int(n / total * 100)
        percent_str = f'{percent:3}%'
        curr_over_total = f' {n}/{total}'

        remain_length = terminal_width - \
            len(percent_str) - len(curr_over_total) - 2

        if remain_length < 10:
            remain_length = 10

        bar = "█" * int((n / total) * remain_length)
        space = " " * (remain_length - len(bar))
        process_bar = f'|{bar}{space}|'
        print(f"\r{percent_str}{process_bar}{curr_over_total}",
              end="", flush=True)
        yield item
