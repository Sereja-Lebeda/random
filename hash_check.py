local_hash_1 = "5d652a03c3aa8d4d3bd1253abed1a6cb98b8292f"
local_hash_2 = "0fd1b406c3bce2e472516389cf7be0ea30bf0d0c"
local_hash_3 = "72cfd0972f89e7a3ab75a9dcc3338d5151006c31" 

git_hash_1 = "5d652a03c3aa8d4d3bd1253abed1a6cb98b8292f"
git_hash_2 = "0fd1b406c3bce2e472516389cf7be0ea30bf0d0c"
git_hash_3 = "72cfd0972f89e7a3ab75a9dcc3338d5151006c31"

print()
if local_hash_1 == git_hash_1:
    print("Local_1 hash and git_1 hash for text1.txt are the same")
if local_hash_1 != git_hash_1:
    print("Local_1 hash and git_1 hash for text1.txt are the different")
if local_hash_2 == git_hash_2:
    print("Local_2 hash and git_2 hash for text2.go are the same")
if local_hash_1 != git_hash_1:
    print("Local_2 hash and git_2 hash for text2.go are the different")
if local_hash_3 == git_hash_3:
    print("Local_2 hash and git_2 hash for check.txt are the same")
if local_hash_1 != git_hash_1:
    print("Local_3 hash and git_3 hash for check.txt are the different")