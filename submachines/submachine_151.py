import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 923) - 886
    _mask = _data(45, None)
    _enc = 87
    return _mask, _enc

def run():
    matrix = 'gH|dHF1zo<agAAGSw|&vI0} c|6E/;'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
