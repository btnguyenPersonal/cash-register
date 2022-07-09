#!/usr/bin/env python

import sys

def get_change(dollars, cents):
    hundred = 0
    fifty = 0
    twenty = 0
    ten = 0
    five = 0
    one = 0
    quarter = 0
    dime = 0
    nickel = 0
    penny = 0

    if dollars >= 100:
        hundred += int(dollars / 100)
        dollars %= 100
    if dollars >= 50:
        fifty += int(dollars / 50)
        dollars %= 50
    if dollars >= 20:
        twenty += int(dollars / 20)
        dollars %= 20
    if dollars >= 10:
        ten += int(dollars / 10)
        dollars %= 10
    if dollars >= 5:
        five += int(dollars / 5)
        dollars %= 5
    if dollars >= 1:
        one += int(dollars / 1)
        dollars %= 1
    if cents >= 25:
        quarter += int(cents / 25)
        cents %= 25
    if cents >= 10:
        dime += int(cents / 10)
        cents %= 10
    if cents >= 5:
        nickel += int(cents / 5)
        cents %= 5
    if cents >= 1:
        penny += int(cents / 1)
        cents %= 1

    return str(hundred) + " hundred dollar bill(s)\n" + str(fifty) + " fifty dollar bill(s)\n" + str(twenty) + " twenty dollar bill(s)\n" + str(ten) + " ten dollar bill(s)\n" + str(five) + " five dollar bill(s)\n" + str(one) + " one dollar bill(s)\n" + str(quarter) + " quarter(s)\n" + str(dime) + " dime(s)\n" + str(nickel) + " nickel(s)\n" + str(penny) + " penny(s)\n"

def main():
    if len(sys.argv) != 2:
        print('Error: input change not found')
        exit(1)
    temp = sys.argv[1].split(".")
    change = "Error"
    if len(temp) == 1:
        change = get_change(0, int(temp[0]))
    else:
        change = get_change(int(temp[0]), int(temp[1]))
    print(change)
    exit(0)

if __name__ == "__main__":
    main()
