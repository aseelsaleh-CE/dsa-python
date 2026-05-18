import pytest
from src.hash_table import HashTable

def test_insert():
    table = HashTable()

    table.insert("name", "Aseel")

    index = table._hash("name")
    node = table.buckets[index]

    assert node is not None
    assert node.key == "name"
    assert node.value == "Aseel"