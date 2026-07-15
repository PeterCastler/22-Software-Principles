#!/bin/sh

# Before: a custom script reads a file, parses rows, filters status, sorts,
# formats a report, and owns flags for every variation.
# ./overdue-report --input invoices.csv --status overdue --sort total

# After: components communicate through a simple text stream.
# Each stage is independently useful and replaceable.
awk -F, '$4 == "overdue" { print $2 "," $3 }' invoices.csv |
  sort -t, -k2,2nr |
  head -n 10

# In production, choose a robust CSV parser when fields can contain commas or
# newlines. Unix composition does not justify using an inadequate text format.
