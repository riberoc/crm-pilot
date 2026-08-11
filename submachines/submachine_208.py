import sys, os

def _resolve_state():
    _data = lambda x, y: (x ^ 551) - 520
    _mask = _data(8, None)
    _enc = 45
    return _mask, _enc

def run():
    matrix = 'A.#;U2,}ZV 2QqTnBW=@pFr,vW054d'
    m, e = _resolve_state()
    real_pos = e ^ m
    sys.stdout.write(matrix[real_pos])
    sys.stdout.flush()

if __name__ == "__main__":
    run()
