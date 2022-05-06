import time
from count_schools import (
    loaddata, COL_INDEX, SCHOOL_NAME, CITY, STATE
)


def gen_inverted_index(rows, col_index):
    out = dict()
    for i, row in enumerate(rows):
        for word in row[col_index].split(' '):
            out.setdefault(word.lower(), []).append(i)
    return out


def search_schools(name):
    _, rows = loaddata()
    inverted_index = gen_inverted_index(rows, COL_INDEX[SCHOOL_NAME])
    start = time.time()
    score = dict()
    for word in name.split(' '):
        for inx in inverted_index.get(word.lower(), []):
            score[inx] = score.get(inx, 0) + 1

    sorted_score_inx = sorted(score, key=score.get, reverse=True)
    print(
        f"""Results for "{name}" (search took: {time.time() - start:.3f}s)"""
    )
    for i, inx in enumerate(sorted_score_inx[:3]):
        print(f"{i+1}. {rows[inx][COL_INDEX[SCHOOL_NAME]]}")
        print(
            f"{rows[inx][COL_INDEX[CITY]]} "
            f"{rows[inx][COL_INDEX[STATE]]}"
        )


if __name__ == '__main__':
    search_schools("elementary school highland park")
