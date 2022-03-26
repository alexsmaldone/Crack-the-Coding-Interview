
def tournamentWinner(competitions, results):
  team_points = {}

  for i in range(len(competitions)):
    winner_idx = results[i]
    competition = competitions[i]
    winner = competition[winner_idx]

    if winner in team_points:
      team_points[winner] += 3
    else:
      team_points[winner] = 3

  return max(team_points)

comp = [
  ["HTML", "C#"],
  ["C#", "Python"],
  ["Python", "HTML"]
]

res = [0, 0, 1]

print(tournamentWinner(comp, res))
