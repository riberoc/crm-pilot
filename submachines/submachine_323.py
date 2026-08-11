import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 329) - 427
    _mask = _data(825, None)
    _enc = 210
    return _mask, _enc

def run():
    matrix = 'tk|Tu8iZ.#AlrI(k/#UaW8> +V*Y~1'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
