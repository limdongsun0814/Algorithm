def solution(bridge_length, weight, truck_weights):
    arr=[0]*bridge_length
    answer = 0
    total = 0
    while len(truck_weights)>0 :

        if arr[0] != 0:
            total-=arr[0]
        arr.pop(0)
        arr.append(0)

        if total+truck_weights[0]<=weight:
            total+=truck_weights[0]
            arr[-1]=truck_weights.pop(0)
        answer+=1

    return answer+bridge_length