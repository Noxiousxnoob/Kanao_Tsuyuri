from threading import RLock

from Chimku.database import MongoDB

INSERTION_LOCK = RLock()

class STUFF(MongoDB):
    db_name = "stuff"

    def __init__(self):
        super.__init__(self.db_name)

    def add_file(self, name: str, link: str, ncoin: int, dtype: str):
        with INSERTION_LOCK:
            curr = self.find_one({"link" : link})
            if not curr:
                self.insert_one(
                    {
                        "name": name,
                        "link": link,
                        "ncoin": ncoin,
                        "type": dtype
                    }
                )
                return
            else:
                return False
    
    def remove_file(self, link: str):
        with INSERTION_LOCK:
            curr = self.find_one({"link" : link})
            if curr:
                self.delete_one(curr)
                return True
            else:
                return False
    
    def get_files(self, type: str):
        curr = self.find_all({"type" : type})
        if curr:
            file_name = {i["name"] for i in curr}
            return list(file_name)
        else:
            return False