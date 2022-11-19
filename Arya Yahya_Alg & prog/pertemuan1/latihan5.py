# belajar casting 
# merubah dari  satu tipe ke tipe lain 
# tipe data = int, float, string, boolean

# DATA INTEGER

print("=====INTEGER=====")

data_int = 9
print("data = ", data_int,",type=", type(data_int))

data_float = float(data_int)
data_str= str(data_int)
data_bool = bool(data_int) # akan false jika nilai nilai int = 0

print("data = ", data_float, ",type=", type(data_float))
print("data = ", data_str, ",type=", type(data_str))
print("data = ", data_bool, ",type=", type(data_bool))


# DATA FLOAT

print("=====FLOAT=====")

data_float = 9
print("data = ", data_float,",type=", type(data_float))

data_int = int(data_float)
data_str= str(data_float)
data_bool = bool(data_float) # akan false jika nilai nilai int = 0

print("data = ", data_int, ",type=", type(data_int))
print("data = ", data_str, ",type=", type(data_str))
print("data = ", data_bool, ",type=", type(data_bool))


# DATA  BOOLEAN

print("====BOOLEAN====")

data_Bool = False;
print("data = ", data_bool,",type=", type(data_bool))

data_int = float(data_bool)
data_str= str(data_bool)
data_float = bool(data_bool) # akan false jika nilai nilai int = 0

print("data = ", data_float, ",type=", type(data_float))
print("data = ", data_str, ",type=", type(data_str))
print("data = ", data_int, ",type=", type(data_int))


# DATA STRING

print("====STRING=====")

data_str = "10"
print("data = ", data_str,",type=", type(data_str))

data_int = int(data_str)
data_float = float(data_str)
data_bool = bool(data_str) # akan false jika nilai nilai int = 0

print("data = ", data_float, ",type=", type(data_float))
print("data = ", data_bool, ",type=", type(data_bool))
print("data = ", data_int, ",type=", type(data_int))




