#!/usr/bin/env python

import doctest


def coalesce_dates(dates):
    """
    Coalesces all date pairs into combined date pairs that makes it easy to find free time gaps.

    >>> from date_collapse import coalesce_dates
    >>> dates = [(1,4),(2,8),(12,16),(16,21)]
    >>> cdates = coalesce_dates(dates)
    >>> print(cdates)
    [(1, 8), (12, 21)]
    >>> dates = [(1,4),(2,8),(8,10),(12,16),(16,21),(21,31)]
    >>> cdates = coalesce_dates(dates)
    >>> print(cdates)
    [(1, 10), (12, 31)]

    """

    parsed_dates = []
    for date in dates:
        parsed_dates.extend([(date[0], 1),(date[1], -1)])
    parsed_dates.sort(key = lambda d: d[0])

    count = 0
    coalesced = []
    current_block = [None, None]
    for date in parsed_dates:
        if count == 0:
            if not coalesced or (coalesced[-1][1] != date[0]):
                current_block = [date[0], None]
            else:
                coalesced.pop()
        count += date[1]
        if count == 0:
            current_block[1] = date[0]
            coalesced.append((current_block[0], current_block[1]))

    return coalesced

def coalesce_dates2(dates):
    """
    Coalesces all date pairs into combined date pairs that makes it easy to find free time gaps.

    >>> from date_collapse import coalesce_dates2 as coalesce_dates
    >>> dates = [(1,4),(2,8),(12,16),(16,21)]
    >>> cdates = coalesce_dates(dates)
    >>> print(cdates)
    [(1, 8), (12, 21)]
    """

    starts = [ date[0] for date in dates ]
    ends = [ date[1] for date in dates ]
    starts.sort()
    ends.sort()
    
    count = 0

    coalesced = []
    
    while starts:
        start = starts.pop(0)
        count += 1
        
        while count > 0 and starts:
            if starts[0] <= ends[0]:
                starts.pop(0)
                count += 1
            else:
                end = ends.pop(0)
                count -= 1
        if not starts:
            end = ends.pop()
        coalesced.append((start,end))
    return coalesced

if __name__=="__main__":
    doctest.testmod()
