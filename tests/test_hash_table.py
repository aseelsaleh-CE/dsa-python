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

def test_delete_non_existing_key():
    ht = HashTable()

    ht.insert("name", "Ali")

    result = ht.delete("age")

    assert result is False
    assert len(ht) == 1

def test_update_method():
    ht = HashTable()

    ht.insert("name", "Ali")

    result = ht.update("name", "Mohammed")

    assert result is True
    assert ht.search("name") == "Mohammed"

def test_search_missing_key():
    ht = HashTable()

    assert ht.search("unknown") is None

def test_resize():
    ht = HashTable(capacity=2)

    ht.insert("a", 1)
    ht.insert("b", 2)
    ht.insert("c", 3)  # triggers resize

    assert len(ht) == 3
    assert ht.search("a") == 1
    assert ht.search("b") == 2
    assert ht.search("c") == 3
    assert ht.capacity >= 4