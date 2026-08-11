import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 747) - 932
    _mask = _data(340, None)
    _enc = 14
    return _mask, _enc

def run():
    matrix = 'eHp:LqS|}AXCpD3L6Abp{ KQB9s84r'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
