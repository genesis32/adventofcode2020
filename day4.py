#!/usr/bin/env python

import re

def valid_record(record):
    required_fields = set(["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"])
    record_fields = set([x.split(":")[0] for x in record.split()])
    for r in record_fields:
        if r == "cid": continue
        if r in required_fields:
            required_fields.remove(r)

    return len(required_fields) == 0

def valid_record2(record):
    def validate_byr(v):
        vi = int(v)
        return vi >= 1920 and vi <= 2002
    
    def validate_iyr(v):
        vi = int(v)
        return vi >= 2010 and vi <= 2020
    
    def validate_eyr(v):
        vi = int(v)
        return vi >= 2020 and vi <= 2030

    def validate_hgt(v):
        if v.endswith("cm"):
            vi = int(v[:-2])
            return vi >= 150 and vi <= 193
        if v.endswith("in"):
            vi = int(v[:-2])
            return vi >= 59 and vi <= 76
        
        return False
    
    def validate_hcl(v):
        return re.search("^#([0-9a-f]{6})$", v) != None
    
    def validate_ecl(v):
        return v in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    
    def validate_pid(v):
        return re.search("^[0-9]{9}$", v) != None

    required_fields = {
        "byr": validate_byr,
        "iyr": validate_iyr, 
        "eyr": validate_eyr,
        "hgt": validate_hgt,
        "hcl": validate_hcl,
        "ecl": validate_ecl,
        "pid": validate_pid
    }
    record_fields = set([tuple(x.split(":")) for x in record.split()])
    validated_fields = set()
    for r, v in record_fields:
        if r == "cid": continue
        if r in required_fields:
            if required_fields[r](v):
                validated_fields.add(r)
        else:
            return False

    return validated_fields == set(required_fields.keys())
    
def split_records(lines):
    ret = []
    current_record = ""
    for line in lines:
        line = line.strip()
        if line == '':
            ret.append(current_record.strip())
            current_record = ""
            continue
        current_record += " " + line
    
    ret.append(current_record.strip())
    return ret

lines = open("day4.txt", "r").readlines()
records = split_records(lines)
num_valid_records = 0
for record in records:
    is_valid = valid_record2(record)
    if valid_record2(record):
        num_valid_records += 1

print(num_valid_records)
