import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 236) - 460
    _mask = _data(739, None)
    _enc = 66
    return _mask, _enc

def run():
    matrix = 'n Z=@P/Ric:?It&l!42v6%8yYwip7('
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
