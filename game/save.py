import pickle
import time

with open(("f.pkl"), "wb") as f:
    import base
    x = base.Game()
    pickle.dump(x, f)
with open(("f.pkl"), "rb") as f:
    Stats = pickle.load(f)

for i in range(2):
    print("Hero did", Stats.Hattack, "to Enemys", Stats.Ehealth, "hp")
    Stats.Ehealth = Stats.Ehealth - Stats.Hattack
    print("Enemy did", Stats.Eattack, "to Heros", Stats.Hhealth, "hp")
    Stats.Hhealth = Stats.Hhealth - Stats.Eattack
    time.sleep(2)
