import csv
import time
from json import load

FILE_NAME = 'sl051bai.csv'
SCHOOL_NAME = 'SCHNAM05'
CITY, STATE, METRO_CENTRIC = 'LCITY05', 'LSTATE05', 'MLOCALE'
COL_INDEX = {}


def loaddata():
    out = []
    with open(FILE_NAME, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            out.append(row)
    headers = out[0]
    required_column = set((SCHOOL_NAME, CITY, STATE, METRO_CENTRIC))
    for i, col in enumerate(headers):
        if col in required_column:
            COL_INDEX[col] = i
    return headers, out[1:]


def print_counts():
    start = time.time()
    _, rows = loaddata()
    total_schools = []
    school_by_state = dict()
    school_by_metro_centric = dict()
    school_by_city = dict()

    for row in rows:
        school_name = row[COL_INDEX[SCHOOL_NAME]]
        if school_name == '':
            continue
        total_schools.append(school_name)
        state = row[COL_INDEX[STATE]]
        city = row[COL_INDEX[CITY]]
        metro_centric = row[COL_INDEX[METRO_CENTRIC]]
        school_by_state.setdefault(state, []).append(school_name)
        school_by_city.setdefault(city, []).append(school_name)
        school_by_metro_centric.setdefault(
            metro_centric, []
        ).append(school_name)

    print('Total school: ', len(total_schools))
    print('Schools by State:')
    for state in sorted(school_by_state):
        print(f'{state}: {len(school_by_state[state])}')

    print('Schools by Metro-centric locale:')
    for m in sorted(school_by_metro_centric):
        print(f'{m}: {len(school_by_metro_centric[m])}')

    max_schools_city = max(
        school_by_city,
        key=lambda k: len(school_by_city[k])
    )
    print(
        'City with most schools: '
        f'{max_schools_city} ({len(school_by_city[max_schools_city])} schools)'
    )
    print(
        'Unique cities with at least one school: '
        f'{len([k for k in school_by_city if len(school_by_city[k]) > 0])}'
    )
    print('-----------------')
    print(f'Execution time: {time.time() - start}')


if __name__ == '__main__':
    print_counts()
