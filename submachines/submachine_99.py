import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 222) - 665
    _mask = _data(905, None)
    _enc = 169
    return _mask, _enc

def run():
    matrix = 'FJ!-eAT?~YEtEi}~&{[f&G~F7qQ]Pf'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
