import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 906) - 376
    _mask = _data(408, None)
    _enc = 131
    return _mask, _enc

def run():
    matrix = 'K}1cD0ao_!=$H9$OF:m5{,o86 <gTs'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
