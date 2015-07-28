def find_common(list1,list2):

        result,inList1 = [],{}
        for i in list1:
                inList1[i] = True

        for i in list2:
                try:
                        if inList1[i]:
                                result.append(i)
                except KeyError:
                        pass

        return result

while True:
        list1 = map(int,raw_input().split())
        if list1 == [0]:
                break
        list2 = map(int,raw_input().split())
        list1.pop(0)
        list2.pop(0)

        common = find_common(list1,list2)
        marker1,marker2 = 0,0
        final_sum = 0

        for term in common:
                sum1,sum2 = 0,0
                while list1[marker1] != term:
                        sum1 += list1[marker1]
                        marker1 += 1
                while list2[marker2] != term:
                        sum2 += list2[marker2]
                        marker2 += 1
                #print sum1,sum2,term
                final_sum += max(sum1,sum2)

        final_sum += max(sum(list1[marker1:]),sum(list2[marker2:]))
        print final_sum
