# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
import torch
import crypten

crypten.init()

x = torch.tensor([1.0,2.0,3.0])
x_enc = crypten.cryptensor(x)

x_dec = x_enc.get_plain_text()

y_enc = crypten.cryptensor([2.0,3.0,4.0])
sum_xy = x_enc + y_enc
sum_xy_dec = sum_xy.get_plain_text()
print("sum_xy")
print(sum_xy)
print(sum_xy_dec)