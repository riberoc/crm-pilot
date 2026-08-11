import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 341) - 344
    _mask = _data(199, None)
    _enc = 39
    return _mask, _enc

def run():
    matrix = 'FY*&tg(6,#c[mc^C*Hf#&~|$f>m6J '
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
