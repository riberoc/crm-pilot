import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 410) - 189
    _mask = _data(377, None)
    _enc = 38
    return _mask, _enc

def run():
    matrix = 'c,8W~{~06Y>p6_eA:Wym%$)El%wX>f'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
