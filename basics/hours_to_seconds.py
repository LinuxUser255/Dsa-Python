#!/usr/bin/env python3

def hours_to_seconds(hours):
    # convert hours to seconds and return the result
    # There are 3,600 seconds in an hour
    seconds_per_minute = 60
    minutes_per_hour   = 60
    converted = seconds_per_minute * minutes_per_hour * hours
    return converted
    # or, more concisely:
  #  return hours * 60 * 60


# Don't touch below this line


def test(hours):
    secs = hours_to_seconds(hours)
    print(hours, "hours is", secs, "seconds")


test(10)
test(1)
test(25)
test(100)
test(33)