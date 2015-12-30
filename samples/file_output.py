#-*-confing:utf-8-*-
# output enternal file

contents = "test content"

file = open("output.txt","w",encoding="utf-8")
file.write(contents)
file.close
