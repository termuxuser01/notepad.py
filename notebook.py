from datetime import datetime
last_id = 0

class Note:
  def __init__(self, memo="Empty Note", tags=""):
    
    if input("write a memo? y/n".lower()) == "y":
      self.memo = input("what will your memeo be?")
    else:
      self.memo = memo
    if input("Add tags? y/n".lower()) == "y":
      self.tags = list(input("Enter tags, comma seperated/n").upper().split(","))
    else:
      self.tags = tags
    self.creation = datetime.now()
    global last_id
    last_id += 1
    self.id0 = last_id
  
  

note = Note()
note2 = Note()

# print(note.creation)
# print(note.memo)
# print(note.tags)
print(note.id0)
print(note2.id0)
