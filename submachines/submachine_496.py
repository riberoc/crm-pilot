import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 350) - 258
    _mask = _data(25, None)
    _enc = 77
    return _mask, _enc

def run():
    matrix = '&LM6BE|R Y*.BpCVn4^wg*^vCp5gbh'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
