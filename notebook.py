from datetime import datetime
last_id = 0

class Note:
  def __init__(self, memo="Empty Note", tags=""):
    """give option to add attributes to note upon creation"""
    if input("write a memo? y/n: ".lower()) == "y":
      self.memo = input("what will your memeo be?\n")
    else:
      self.memo = memo
    if input("Add tags? y/n: ".lower()) == "y":
      self.tags = list(input("Enter tags, comma seperated\n").upper().split(","))
    else:
      self.tags = tags
    self.creation = datetime.now()
    global last_id
    last_id += 1
    self.id0 = last_id
  
class NoteBook:
  def __init__(self):
    """create an Empty list to contain its notes"""
    self.notes = []
  
  def create_note(self):
    """call to create and append a note to the nb object"""
    self.notes.append(Note())
  
  def _find_n(self, ids):
    """find notes using an id to pass to other functions that may require it"""
    for n in self.notes:
      if n.id0 == ids:
        return n
    return None

  def search(self, memo="", tag=""):
    "get id of a note containing string in memo or tags"
    for n in self.notes: 
      if memo in n.memo:
        return n.id0
      elif tag in n.tags:
        return n.id0 
      else:
        print("note does not exist")
  
  def modify_memo(self, ids):
    """use thye finder function to return and change the memo of a given id"""
    self._find_n(ids).memo = input("type a new memo\n")

  def modify_tags(self, ids):
    self._find_n(ids).tags = input("enter new tags:\n")
