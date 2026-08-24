#utility function written by nadav for calculating percentages & gigabytes
#version 1.0 Aug 24,2026

def calculate_percentages(part,whole):
    part_percentage = round((part/whole)*100,2)
    return part_percentage

def bytes_into_gigabytes(bytes):
    gigabytes = round(bytes/(1024**3),3)
    return gigabytes
