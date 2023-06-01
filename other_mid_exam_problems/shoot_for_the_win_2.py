# 70/100
targets_value = [int(nums) for nums in input().split()]

command = input()
count_targets = 0
shot_targets = []
while command != "End":

    command = int(command)

    if 0 <= command < len(targets_value):

        if targets_value[command] in targets_value and not targets_value[command] in shot_targets:
            count_targets += 1
            targets_value.insert(command,-1)
            command += 1

            new_value = targets_value[command]
            shot_targets.append(new_value)

            for num in targets_value:
                index = targets_value.index(num)
                if num > new_value and num != -1:
                    targets_value[index] = num - new_value
                elif num != -1 and num <= new_value:
                    targets_value[index] = num + new_value

            targets_value.pop(command)
            command = input()
        else:
            command = input()
    else:
        command = input()

targets_value = " ".join([str(x)for x in targets_value])

print(f"Shot targets: {count_targets} -> {targets_value}")
