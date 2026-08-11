import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 419) - 953
    _mask = _data(1464, None)
    _enc = 108
    return _mask, _enc

def run():
    matrix = ';<_|>-!5j:Dqvm k0TSB/zn>pZD.N>'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
