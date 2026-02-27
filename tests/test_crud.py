import crud

def test_create_and_read():
    crud.data.clear()
    crud.create("item1")
    assert "item1" in crud.read()

def test_update():
    crud.data.clear()
    crud.create("item2")
    assert crud.update(0, "item2_updated")
    assert crud.read()[0] == "item2_updated"

def test_delete():
    crud.data.clear()
    crud.create("item3")
    assert crud.delete(0)
    assert "item3" not in crud.read()