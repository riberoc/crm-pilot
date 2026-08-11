import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 952) - 789
    _mask = _data(79, None)
    _enc = 234
    return _mask, _enc

def run():
    matrix = '-5lk|>wr L%XlO*jq:$[qBz7>R]K#l'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
