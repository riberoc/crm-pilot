import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 555) - 172
    _mask = _data(747, None)
    _enc = 17
    return _mask, _enc

def run():
    matrix = '2ecyW cfFk[w?TR_>G6W8TRM,I4Z43'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
