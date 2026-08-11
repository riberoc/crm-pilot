import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 831) - 681
    _mask = _data(27, None)
    _enc = 121
    return _mask, _enc

def run():
    matrix = '_6yuNq=%-DD`X4nPN>59f$;@.#mut`'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
