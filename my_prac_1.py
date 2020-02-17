from matplotlib import pyplot as plt

# #scatter graph
# x=[5,2,9,4,7]
# y=[10,5,8,4,2]
# plt.scatter(x,y)
# plt.show()

# #line graph
# x= [5,2,9,8,4]
# y= [11,2,5,4,8]
# plt.plot(x,y)
# plt.show()

#histogram
# y= [11,2,5,4,8]
# plt.hist(y)
# plt.show()

#hiding ticks
x= [10,2,3,4,7]
y=[2,4,8,5,3]
plt.plot(x,y)
plt.xticks([],[])
plt.show()