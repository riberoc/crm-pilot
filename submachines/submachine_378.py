import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 552) - 666
    _mask = _data(330, None)
    _enc = 221
    return _mask, _enc

def run():
    matrix = 'u~A$0KzifSDHjNqadRTv+ d!o*:a!U'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
