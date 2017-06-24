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
