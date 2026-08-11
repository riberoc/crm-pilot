import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 640) - 856
    _mask = _data(284, None)
    _enc = 66
    return _mask, _enc

def run():
    matrix = '.FERlcssFS*)-{.#oG3~d(#Dpn}Dvg'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
