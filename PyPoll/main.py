import csv

file = 'election_data.csv'

with open(file, 'r') as election_data:
    next(election_data)
    csv_reader = csv.reader(election_data, delimiter = ',')

    vote_count = 0
    candidates = []

    for row in csv_reader:
        vote_count = vote_count + 1
        if row[2] not in candidates:
            candidates.append(row[2])

votes = {candidate:0 for candidate in candidates}

with open(file, 'r') as election_data:
    next(election_data)
    csv_reader = csv.reader(election_data, delimiter=',')

    for row in csv_reader:
        votes[row[2]] = votes[row[2]] + 1

winner = list(votes.keys())[1]

for cand in votes.keys():
    if votes[cand] > votes[winner]:
        winner = cand

with open("output.txt", 'w') as txtfile:
    txtfile.writelines(
        f'Election Results \n'
        f'------------------------- \n'
        f'Total Votes: {vote_count}\n'
        f'-------------------------\n'
    )
    for cand,count in votes.items():
        txtfile.writelines(f"{cand}: {round(count/vote_count*100,3)}% ({count})\n")
    txtfile.writelines(
        f'------------------------- \n'
        f'Winner: {winner}\n'
        f'-------------------------'
    )

with open("output.txt", 'r') as readfile:
    print(readfile.read())