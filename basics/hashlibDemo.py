import hashlib

#print(sorted(hashlib.algorithms_guaranteed))   #sopported hash algorithms
#print(sorted(hashlib.algorithms_available))    #available hash algorithms 

superSecret= """Pass: Meatballs"""
print(superSecret)

#Before using hashlib the strings must be encoded
#For more understanging check basics/encodedVals.py file
originalHash= hashlib.sha256(superSecret.encode('utf8'))    #converts  
print(f"SHA256 {originalHash.hexdigest()}")
superSecret+=" and spaghetti"

changedHash = hashlib.sha256(superSecret.encode('utf8'))
print(changedHash.hexdigest())

if originalHash==changedHash:
    print("Code not changed")
else:
    print("Code modified")