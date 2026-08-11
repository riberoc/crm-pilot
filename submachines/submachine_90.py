import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 482) - 298
    _mask = _data(144, None)
    _enc = 80
    return _mask, _enc

def run():
    matrix = 'DI?cGM1u.Loa&KoZ}A!ZH6dZc8MsyU'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
