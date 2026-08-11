import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 506) - 514
    _mask = _data(913, None)
    _enc = 101
    return _mask, _enc

def run():
    matrix = 'fMhx#[fkV7^, r$[T(-k}#kcn-EB:k'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
