#!/usr/bin/env python
import yaml

from gendiff.generate_diff import generate_diff
import json


def test_generate_diff_with_identical_files_json():
    result = open('tests/fixtures/test1_result.txt', 'r').read()
    file_path_1 = json.load(open('tests/fixtures/test1_file1.json'))
    file_path_2 = json.load(open('tests/fixtures/test1_file2.json'))
    diff = generate_diff(file_path_1, file_path_2)
    assert diff == result


def test_diff_with_first_empty_file_json():
    result = open('tests/fixtures/test2_result.txt', 'r').read()
    file_path_1 = json.load(open('tests/fixtures/test2_file1.json'))
    file_path_2 = json.load(open('tests/fixtures/test2_file2.json'))
    diff = generate_diff(file_path_1, file_path_2)
    assert diff == result


def test_diff_with_second_empty_file_json():
    result = open('tests/fixtures/test3_result.txt', 'r').read()
    file_path_1 = json.load(open('tests/fixtures/test3_file1.json'))
    file_path_2 = json.load(open('tests/fixtures/test3_file2.json'))
    diff = generate_diff(file_path_1, file_path_2)
    assert diff == result


def test_diff_with_empty_files_json():
    result = open('tests/fixtures/test4_result.txt', 'r').read()
    file_path_1 = json.load(open('tests/fixtures/test4_file1.json'))
    file_path_2 = json.load(open('tests/fixtures/test4_file2.json'))
    diff = generate_diff(file_path_1, file_path_2)
    assert diff == result


def test_diff_files_json():
    result = open('tests/fixtures/test5_result.txt', 'r').read()
    file_path_1 = json.load(open('tests/fixtures/test5_file1.json'))
    file_path_2 = json.load(open('tests/fixtures/test5_file2.json'))
    diff = generate_diff(file_path_1, file_path_2)
    assert diff == result


def test_generate_diff_with_identical_files_yaml():
    result = open('tests/fixtures/test1_result.txt', 'r').read()
    file_path_1 = yaml.load(open('tests/fixtures/test1_file1.yaml'))
    file_path_2 = yaml.load(open('tests/fixtures/test1_file2.yaml'))
    diff = generate_diff(file_path_1, file_path_2)
    assert diff == result


def test_diff_with_first_empty_file_yaml():
    result = open('tests/fixtures/test2_result.txt', 'r').read()
    file_path_1 = yaml.load(open('tests/fixtures/test2_file1.yaml'))
    file_path_2 = yaml.load(open('tests/fixtures/test2_file2.yaml'))
    diff = generate_diff(file_path_1, file_path_2)
    assert diff == result


def test_diff_with_second_empty_file_yaml():
    result = open('tests/fixtures/test3_result.txt', 'r').read()
    file_path_1 = yaml.load(open('tests/fixtures/test3_file1.yaml'))
    file_path_2 = yaml.load(open('tests/fixtures/test3_file2.yaml'))
    diff = generate_diff(file_path_1, file_path_2)
    assert diff == result


def test_diff_with_empty_files_yaml():
    result = open('tests/fixtures/test4_result.txt', 'r').read()
    file_path_1 = yaml.load(open('tests/fixtures/test4_file1.yaml'))
    file_path_2 = yaml.load(open('tests/fixtures/test4_file2.yaml'))
    diff = generate_diff(file_path_1, file_path_2)

    assert diff == result


def test_diff_files_yaml():
    result = open('tests/fixtures/test5_result.txt', 'r').read()
    file_path_1 = yaml.load(open('tests/fixtures/test5_file1.yaml'))
    file_path_2 = yaml.load(open('tests/fixtures/test5_file2.yaml'))
    diff = generate_diff(file_path_1, file_path_2)
    assert diff == result
