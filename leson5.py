# # class Window:

# #     def __init__(self, x, y, name='unk'): # окно в комнате
# #         self.square = x * y               # площадь


# # class Room:

# #     def __init__(self, x, y, z):
# #         self.work_square = (x + y) * 2 * z  # рабочая площадь комнаты
# #         self.windows = []      # тут передаем что нет окна в комнате
    
# #     def add_windown(self, x, y):
# #         self.windown.append(Window(x, y))  #добавить

# #     def get_square(self):
# #         new_square = self.work_square
# #         for windown in self.windows:
# #             new_square -= windown.square
# #         return new_square


# # r = Room(10, 20, 3)
# # r.add_windown(3, 2)
# # print(r.get_square())

# class Window:
 
#     def __init__(self, x, y, name='unk'):
#         self.square = x * y
 
 
# class Room:
 
#     def __init__(self, x, y, z):
#         self.work_square = (x + y) * 2 * z
#         self.windows = []
 
#     def add_window(self, x, y):
#         self.windows.append(Window(x, y))
 
#     def get_square(self):
#         new_square = self.work_square
#         for window in self.windows:
#             new_square -= window.square
#         return new_square
 
 
# r = Room(10, 20, 3)
# r.add_window(3, 2)
# print(r.get_square())
 
 