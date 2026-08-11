import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 676) - 138
    _mask = _data(915, None)
    _enc = 186
    return _mask, _enc

def run():
    matrix = '$ZU1/76X7@1t{.&cP+efg<N ,&%%KV'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
