import qrcode
data = input("Enter the FULL link: ")
img = qrcode.make(data)
save = input("Enter the file name for it: ")
finalsave = save + ".png"
img.save(finalsave)