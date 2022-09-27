# human parsing datasets analysis

In this repo I want to examin some of datasets that use in human parsing task.

- for more information about human parsinag task please see [Human Parsing](https://paperswithcode.com/task/human-parsing/latest)

# Lsit of datasets:
- CIHP

## CIHP:
**instance level human parsing** dataset or **CIHP** is one of datasets that use in human parsing task.

for download use this [google drive](https://drive.google.com/drive/folders/0BzvH3bSnp3E9ZW9paE9kdkJtM3M?resourcekey=0-vgKJX42GVFaAwjhEWAncjQ)
Or run :
```
gdown 1HdqA8yWVxZ8od0hngKzZTziHx_ONzCWj
tar -xvf  instance-level_human_parsing.tar.gz
mv instance-level_human_parsing datasets/CIHP

```
This dataset has 19 classes consists of:
1. Hat: Hat, helmet, cap, hood, veil, headscarf, part covering the skull and hair of a hood/balaclava, crown…
2. Hair
3. Glove
4. Sunglasses/Glasses: Sunglasses, eyewear, protective glasses…
5. UpperClothes: T-shirt, shirt, tank top, sweater under a coat, top of a dress…
6. Face Mask: Protective mask, surgical mask, carnival mask, facial part of a balaclava, visor of a helmet…
7. Coat: Coat, jacket worn without anything on it, vest with nothing on it, a sweater with nothing on it…
8. Socks
9. Pants: Pants, shorts, tights, leggings, swimsuit bottoms… (clothing with 2 legs)
10. Torso-skin
11. Scarf: Scarf, bow tie, tie…
12. Skirt: Skirt, kilt, bottom of a dress…
13. Face
14. Left-arm (naked part)
15. Right-arm (naked part)
16. Left-leg (naked part)
17. Right-leg (naked part)
18. Left-shoe
19. Right-shoe

## All objects instances are listed below

|  category  | #instances   |  category  | #instances   |   category   | #instances   |
|:----------:|:-------------|:----------:|:-------------|:------------:|:-------------|
|   Person   | 17520        |    Hat     | 2536         |     Hair     | 15797        |
|   Glove    | 530          | Sunglasses | 697          | UpperClothes | 13497        |
|   Dress    | 1509         |    Coat    | 6055         |    Socks     | 1109         |
|   Pants    | 9624         | Torso-skin | 14383        |    Scarf     | 575          |
|   Skirt    | 578          |    Face    | 16489        |   Left-arm   | 11249        |
| Right-arm  | 11825        |  Left-leg  | 2815         |  Right-leg   | 2809         |
| Left-shoe  | 4622         | Right-shoe | 4618         |              |              |
|   total    | 138837       |            |              |              |              |

