#!/usr/bin/env python

def coalesce_dates(dates):
    starts = [ date[0] for date in dates ]
    ends = [ date[1] for date in dates ]
    starts.sort()
    ends.sort()
    
    count = 0

    coalesced = []
    
    while starts:
        start = starts.pop(0)
        count += 1
        
        while count > 0:
            if starts[0] <= ends[0]:
                starts.pop(0)
                count += 1
            else:
                end = ends.pop(0)
                count -= 1
            
        coalesced.append((start,end))
