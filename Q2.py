""" Data Science Project

users = [
    { "id": 0, "name": "Hero" },
    { "id": 1, "name": "Dunn" },
    { "id": 2, "name": "Sue" },
    { "id": 3, "name": "Chi" },
    { "id": 4, "name": "Thor" },
    { "id": 5, "name": "Clive" },
    { "id": 6, "name": "Hicks" },
    { "id": 7, "name": "Devin" },
    { "id": 8, "name": "Kate" },
    { "id": 9, "name": "Klein" },
   
]
friendship_pairs = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

1.	Creation of DataSciencester Network
2.	Find the total number of connections and average connections of the network
3.	Sort from “most friends” to “least friends”

4.	Find the friends of friends withput using any python library
 """
users = [
    { "id": 0, "name": "Hero" },
    { "id": 1, "name": "Dunn" },
    { "id": 2, "name": "Sue" },
    { "id": 3, "name": "Chi" },
    { "id": 4, "name": "Thor" },
    { "id": 5, "name": "Clive" },
    { "id": 6, "name": "Hicks" },
    { "id": 7, "name": "Devin" },
    { "id": 8, "name": "Kate" },
    { "id": 9, "name": "Klein" },
]
friendship_pairs = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4), (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]
friendships = {user["id"]: [] for user in users}

for i, j in friendship_pairs:
    friendships[i].append(j)
    friendships[j].append(i)


total_connections = sum(len(friendships[user["id"]]) for user in users)

num_users = len(users)
avg_connections = total_connections / num_users


fofs_by_id = {user["id"]: set() for user in users}
for user in users:
    for friend in friendships[user["id"]]:
        for fof in friendships[friend]:
            if fof != user["id"] and fof not in friendships[user["id"]]:
                fofs_by_id[user["id"]].add(fof)


print("Friends of friends for each user:")
for user_id in fofs_by_id:
    print(f"{users[user_id]['name']}: {', '.join(users[fof]['name'] for fof in fofs_by_id[user_id])}")
