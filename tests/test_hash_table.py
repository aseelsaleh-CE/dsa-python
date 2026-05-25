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


def test_insert_and_search():
    ht = HashTable()

    ht.insert("name", "Ali")

    assert ht.search("name") == "Ali"
    assert len(ht) == 1