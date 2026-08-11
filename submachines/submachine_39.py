import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 751) - 117
    _mask = _data(908, None)
    _enc = 237
    return _mask, _enc

def run():
    matrix = 'ssEn|A79KtNqSxP{%-~`Rgv/I1;uU%'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
