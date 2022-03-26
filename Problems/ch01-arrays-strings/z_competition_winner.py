
def tournamentWinner(competitions, results):
  team_points = {}

  for i in range(len(competitions)):
    winner_idx = 0 if results[i] == 1 else 1
    competition = competitions[i]
    winner = competition[winner_idx]

    if winner in team_points:
      team_points[winner] += 3
    else:
      team_points[winner] = 3

  return max(team_points, key=team_points.get)

comp = [
  ["HTML", "C#"],
  ["C#", "Python"],
  ["Python", "HTML"]
]
res = [0, 0, 1]

comp1 = [
  ["HTML", "Java"],
  ["Java", "Python"],
  ["Python", "HTML"]
]
res1 = [0, 1, 1]

print(tournamentWinner(comp, res))
print(tournamentWinner(comp1, res1))
