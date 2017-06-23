#!/usr/bin/env python

def coalesce_dates(dates):
    starts = [ date[0] for date in dates ]
    ends = [ date[1] for date in dates ]

    count = 0

    coalesced = []
    
    while starts:
        start = starts.pop
        count += 1
        
