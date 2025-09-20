class Spreadsheet:
    def __init__(self,rows:int):
        self.sheet = {}

    def setCell(self,cell:str,value:int) -> None:
        self.sheet[cell] = value

    def resetCell(self,cell:str) -> None:
        self.sheet[cell] = 0

    def getValue(self,formula:str) -> int:
        formula = formula.removeprefix("=")
        x,y = formula.split("+")

        if x in self.sheet:
            x_val = self.sheet[x]
        else:
            if x.isdigit():
                x_val = int(x)
            else: x_val = 0

        if y in self.sheet:
            y_val = self.sheet[y]
        else:
            if y.isdigit():
                y_val = int(y)
            else: y_val = 0

        return x_val + y_val   

# class Spreadsheet:
#     def __init__(self, rows: int):
#         self.rows = rows
#         self.sheet = {ch: {} for ch in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}

#         for key in self.sheet:
#             self.sheet[key] = [0 for _ in range(self.rows)]

#         print(self.sheet)
#     @staticmethod
#     def extract_alpha_num(s: str):
#         alpha = ''.join([ch for ch in s if ch.isalpha()])
#         num = ''.join([ch for ch in s if ch.isdigit()])

#         return alpha,int(num)

#     def setCell(self, cell: str, value: int) -> None:
#         alpha,num = Spreadsheet.extract_alpha_num(cell)
#         self.sheet[alpha][num-1] = value 
#         print(self.sheet)

#     def resetCell(self, cell: str) -> None:
#         alpha,num = Spreadsheet.extract_alpha_num(cell)
#         self.sheet[alpha][num-1] = 0

#     def getValue(self, formula: str) -> int:
#         formula = formula.removeprefix("=")
#         formula = formula.split("+")
        
#         one,two = formula[0], formula[1]

#         if one.isdigit() and two.isdigit(): 
#             return int(one) + int(one)
        
#         if not one.isdigit() and two.isdigit():
#             alpha,num = Spreadsheet.extract_alpha_num(one)
#             return self.sheet[alpha][num-1] + int(two)
        
#         if one.isdigit() and not two.isdigit():
#             alpha,num = Spreadsheet.extract_alpha_num(two)
#             return int(one) + self.sheet[alpha][num-1]

#         if not one.isdigit() and not two.isdigit():
#             alpha1,num1 = Spreadsheet.extract_alpha_num(one)
#             alpha2,num2 = Spreadsheet.extract_alpha_num(two)
#             print(alpha1,alpha2,num1,num2,self.sheet[alpha1][num1-1],self.sheet[alpha2][num2-1])

#             return self.sheet[alpha1][num1-1] + self.sheet[alpha2][num2-1]
            

Obj = Spreadsheet(3)
Obj.setCell("A1", 10)
Obj.setCell("B2", 15)
print(Obj.getValue("=5+4"))
# print(Obj.getValue("=A1+B2"))
# # row = 4
# # sheet = {}
# # for ch in "ABCDEFGHIJKLMNOPQ":
# #     sheet[ch] = {}
# #     for i in range(1,row):
# #         sheet[ch][f"{ch}{i}"] = "" 

# # print(sheet)
# # sheet = {ch: {} for ch in "ABCDEFGHIJKLMNOPQ"}
# # row = 3

# # for key in sheet:
# #     sheet[key] = [[] for _ in range(row)]

# # print(sheet)

# # cell = "=5+7"

# # two_num = cell.split("=")
# # cell = cell.removeprefix("=")
# # print(cell.split("+"))