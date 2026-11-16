class Record:
    def __init__(self , title , category):
        self.title = title
        self.category = category
class StudyLog(Record):
       def __init__(self , title , category , minutes):
           super().__init__(title , category)
           self.minutes = minutes
       def to_line(self):
           return f"STUDY|{self.title}|{self.category}|{self.minutes}\n"
class ExpenseLog(Record):
       def __init__(self , title , category , amount):
           super().__init__(title , category)
           self.amount = amount
       def to_line(self):
           return f"EXPENSE|{self.title}|{self.category}|{self.amount}\n"  
FILE = "data.txt"
def save_record(rec):
      with open(FILE , "a") as f:
              f.write(rec.to_line())              
def load_records():
      records = [ ] 
      try:
              with open(FILE , "r") as f:
                  for line in f:
                      p = line.strip().split("|")
                      if len(p)  == 4:
                          records.append({
                                   "type" : p[0],
                                   "title" : p[1], 
                                   "category" : p[2],
                                   "value" : int(p[3])
                         })
      except FileNotFoundError:
           pass
      return records
def show_summary( ):
    data = load_records( )
    if not data:
        print("Abhi koi data nahi hai!")
        return
    study = [r for r in data if r["type"] == "STUDY"]
    expense = [r for r in data if r["type"] == "EXPENSE"]
    total_min = sum(map(lambda x: x["value"] , study))
    total_exp = sum(map(lambda x: x["value"] , expense))
    cats = set(map(lambda x: x["category"] , data))
    print("\n--- REPORT ---")
    print(f"Total Study: {total_min} mins ({total_min / 60:.1f})")
    print(f"Total Expense: Rs.{total_exp}")
    print(f"Categories: { cats}")
MENU = ("1.Add Study" , "2.Add Expense" , "3.Report" , "4.Exit")
while True:
    print("\n , MENU")
    ch = input("Choice(1 - 4):")
    try:
        if ch == "1":
            t = input("Topic:")
            c = input("Subject:")
            m = int(input("Minutes:  "))
            save_record(StudyLog(t , c , m))
            print("Saved!")
        elif ch == "2":
            t = input("Item:  ")
            c = input("Category:  ")
            a = int(input("Amount (Rs):  "))
            save_record(ExpenseLog(t , c , a))
            print("Saved")
        elif ch == "3":
            show_summary()
        elif ch == "4":
            print("Bye! Keep Coding!")
            break
        else:
            print("Sirf 1 se 4 chunein!")
    except ValueError:
        print("Error: Minutes/Amount mein sirf number dalein!")
        

     
 
                                                   
                                   
              
       
