#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    # Fill missing elements with zeros if needed
    padded_tuple_a = tuple_a + (0, 0)
    padded_tuple_b = tuple_b + (0, 0)
    
    # Add corresponding elements and create the result tuple
    result_tuple = (padded_tuple_a[0] + padded_tuple_b[0],
                    padded_tuple_a[1] + padded_tuple_b[1])
    
    return result_tuple
