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

skeleton = Undead("Bones", "Skeleton", 100, 20)

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