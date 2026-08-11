import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 287) - 359
    _mask = _data(768, None)
    _enc = 164
    return _mask, _enc

def run():
    matrix = 'm9hNe#+NQH6]rzcBK|baM.{{Uk{Y :'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
