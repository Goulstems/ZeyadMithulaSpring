#loop :
# n = 5
# for i in range(n):
#     print(i+1)

############################################3
#recurse :
def sum1ToN(N):              #with a helper function
    def recurseHelper(i,N,sum=0):
        if (i > N):
            return sum
        sum+=i
        return recurseHelper(i+1,N,sum)
    recurseHelper(1,N)


# #(no helper function ex;)
# def print1ToN(i,N):            
#     if (i > N):
#         return
#     print(i)
#     print1ToN(i+1,N)

# print(sum1ToN(5))

def omgHax():
    print("omg my memory!!!!")
    omgHax()

omgHax()