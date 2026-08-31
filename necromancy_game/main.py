from rune import Rune

bone_rune = Rune("Bone", 10)

print(bone_rune)

bone_rune.add(5)
print(bone_rune)

print(bone_rune.consume(8))
print(bone_rune)

from rune import Rune
from undead import Undead

bone_rune = Rune("Bone", 10)

skeleton = Undead("U001", "Bones", "Skeleton", 100, 20)

print(skeleton)

skeleton.take_damage(30)
print(skeleton)

skeleton.heal(10)
print(skeleton)

print(skeleton.attack())

from rune import Rune
from undead import Undead
from necromancer import Necromancer

bone_rune = Rune("Bone", 20)

necromancer = Necromancer("Mordred")

necromancer.add_rune(bone_rune)

print(necromancer)
print(bone_rune)

skeleton = necromancer.summon_undead(
    bone_rune,
    5,
    "U001",
    "Bones",
    "Skeleton",
    100,
    20
)
print(bone_rune)
print(skeleton)
print(necromancer)

for undead in necromancer.undead_army:
    print(undead)

print(len(necromancer.undead_army))

# necromancer.remove_undead(skeleton)



# print(len(necromancer.undead_army))


print(len(necromancer.undead_army))

print(necromancer.remove_undead_by_id("U001"))

print(len(necromancer.undead_army))



test_rune = Rune("Bone", 100)
test_necromancer = Necromancer("Test")

test_necromancer.add_rune(test_rune)

u1 = test_necromancer.summon_undead(
    test_rune, 5, "U001", "Skeleton 1", "Skeleton", 100, 20
)

u2 = test_necromancer.summon_undead(
    test_rune, 5, "U002", "Skeleton 2", "Skeleton", 100, 20
)

u3 = test_necromancer.summon_undead(
    test_rune, 5, "U003", "Skeleton 3", "Skeleton", 100, 20
)

u4 = test_necromancer.summon_undead(
    test_rune, 5, "U004", "Skeleton 4", "Skeleton", 100, 20
)

print(len(test_necromancer.undead_army))
print(u4)
print(test_rune.amount)


print(u1)

print(test_necromancer.level_undead_by_id("U001"))

print(u1)