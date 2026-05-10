t=(1,"arpan",45,"gudddu",88,55)
print(f"Before:",t)
store=list(t)
store.append("BABU")
store[2]=100
t=tuple(store)
print(f"After:",t)