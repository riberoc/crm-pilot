import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 233) - 661
    _mask = _data(969, None)
    _enc = 152
    return _mask, _enc

def run():
    matrix = 'ek~o1`sBlJ$~+Ko4a}UsKe_(B5^)kA'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
