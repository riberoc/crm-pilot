import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 451) - 784
    _mask = _data(577, None)
    _enc = 117
    return _mask, _enc

def run():
    matrix = 'SQm;8FH 3;cB`Lm87LyJbk!H!s}Bw0'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
