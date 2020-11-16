list_ = input("Enter sentence: ")
sep = [x for x in list_.split(" ")]
r_list_=list_.replace(",","").replace(".","").replace("?",".").replace("!",".").split(" ")
print (", ".join(sorted(list(set(r_list_)))))
input("Press any key to finish")
