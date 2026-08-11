import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 999) - 363
    _mask = _data(609, None)
    _enc = 14
    return _mask, _enc

def run():
    matrix = '{n$[(^e/<~x!7gQ`e_h*: O9/Esacj'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
