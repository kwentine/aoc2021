import pytest
from day16 import (parse, parse_number, parse_bits,
                   parse_header, parse_fixed_length,
                   parse_subpackets, part_one)


@pytest.mark.parametrize(
    'hex_s,bin_s',
    [
        ("D2FE28", "110100101111111000101000"),
        ("38006F45291200", "00111000000000000110111101000101001010010001001000000000"),
        ("EE00D40C823060", "11101110000000001101010000001100100000100011000001100000")
    ]
)
def test_parse(hex_s, bin_s):
    assert parse(hex_s) == bin_s


def test_parse_header():
    input_s = parse("D2FE28")
    assert parse_header(input_s, 0) == ((6, 4), 6)


def test_parse_number():
    input_s = parse("D2FE28")
    offset = 6
    assert parse_number(input_s, offset) == (2021, 21)


def test_parse_literal_value():
    input_s = parse("D2FE28")
    offset = 0
    assert parse_bits(input_s, offset) == ((6, 4, 2021), 21)


def test_parse_fixed_length():
    input_s = "00111000000000000110111101000101001010010001001000000000"
    offset = 22
    length = 27
    a = (6, 4, 10)
    b = (2, 4, 20)
    assert parse_fixed_length(input_s, offset, length) == ([a, b], 49)


def test_parse_sub_packets():
    input_s = "11101110000000001101010000001100100000100011000001100000"
    offset = 18
    length = 3
    a = (2, 4, 1)
    b = (4, 4, 2)
    c = (1, 4, 3)
    end_offset = len(input_s) - 5
    assert parse_subpackets(input_s, offset, length) == ([a, b, c], end_offset)


@pytest.mark.parametrize("input_s,result,offset",
                         [
                             ("38006F45291200",
                              (1, 6, [(6, 4, 10), (2, 4, 20)]), 49),
                             ("EE00D40C823060",
                              (7, 3, [(2, 4, 1), (4, 4, 2), (1, 4, 3)]), 51)
                         ]
                         )
def test_parse_list(input_s, result, offset):
    data = parse(input_s)
    r, o = parse_bits(data, 0)
    assert r == result
    assert o == offset


@pytest.mark.parametrize("input_s,version_sum", [
    ("8A004A801A8002F478", 16),
    ("620080001611562C8802118E34", 12),
    ("C0015000016115A2E0802F182340", 23),
    ("A0016C880162017C3686B18A3D4780", 31)
])
def test_part_one(input_s, version_sum):
    assert part_one(parse(input_s)) == version_sum
