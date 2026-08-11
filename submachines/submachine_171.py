import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 803) - 764
    _mask = _data(195, None)
    _enc = 225
    return _mask, _enc

def run():
    matrix = '`fWXl zYqDts-TA[*Rv&$0&BS$DZLe'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
