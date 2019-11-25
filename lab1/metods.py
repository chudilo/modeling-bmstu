def cal_comulsum(massive):
    count = len(massive)
    if count == 0:
        return 0
    maxmass = max(massive)
    for i in range(count):
        massive[i] = round(massive[i]/maxmass)
    massum = [massive[0]]

    for i in range(count - 1):
        massum.append(massive[++i] + massum[i])
    z = max(massum)

    start1 = round((-count/z + 1)*4)
    end = round((count/z - 1)*4)
    start2 = round((-count/z - 3)*4)
    ber1 = []
    ber2 = []
    for i in range(start1, end + 1):
        ber1.append(erf(((4*i+1)*z/sqrt(count))) - erf(((4*i-1)*z/sqrt(count))))
    for i in range(start2, end + 1):
        ber2.append(erf((4 * i + 3) * z / sqrt(count)) - erf((4 * i + 1) * z / sqrt(count)))
    sumber1 = sum(ber1)
    sumber2 = sum(ber2)
    P = 1 - sumber1 + sumber2

    return P

def corelation(nums):
    n = len(nums)
    sumUU = 0
    sumber = sum(nums)
    sumU2 = 0
    if n ==0:
        return 0
    for i in range(n):
        numj = int(nums[(i+1) % n])
        numi = int(nums[i])
        sumU2 += numi * numi
        sumUU += numi * numj
    top = n * sumUU - sumber ** 2
    bottom = n * sumU2 - sumber ** 2
    if bottom == 0:
        return 1
    return top / bottom

def alg_table_fill():
    random.seed()
    one_digit = [random.randint(0, 9) for i in range(10)]
    two_digits = [random.randint(10, 99) for i in range(10)]
    three_digits = [random.randint(100, 999) for i in range(10)]


    #table.resizeColumnsToContents()

    corel_1 = corelation(one_digit)
    corel_2 = corelation(two_digits)
    corel_3 = corelation(three_digits)
    return corel_1, corel_2, corel_3
    #win.Table_info1_1.setText('{:.4%}'.format(corel_1))
    #win.Table_info2_1.setText('{:.4%}'.format(corel_2))
    #win.Table_info3_1.setText('{:.4%}'.format(corel_3))


def table_table_fill(win):
    table = win.table_table
    numbers = set()
    with open('numbers.txt') as file:
        #lines = islice(file, win.line_num, None)
        for l in lines:
            numbers.update(set(l.split(" ")[:-1]))
            win.line_num += 1
            if len(numbers) >= 3001:
                break
        numbers.remove("")
        numbers = list(numbers)[:3000]
    one_digit = [int(i) % 9 + 1 for i in numbers[:1000]]
    two_digits = [int(i) % 90 + 10 for i in numbers[1000:2000]]
    three_digits = [int(i) % 900 + 100 for i in numbers[2000:3000]]

    for i in range(10):
        item1 = QTableWidgetItem(str(one_digit[i]))
        table.setItem(i, 0, item1)
        item2 = QTableWidgetItem(str(two_digits[i]))
        table.setItem(i, 1, item2)
        item3 = QTableWidgetItem(str(three_digits[i]))
        table.setItem(i, 2, item3)

    # table.resizeColumnsToContents()

    corel_1 = corelation(one_digit)
    corel_2 = corelation(two_digits)
    corel_3 = corelation(three_digits)
    #win.Alg_info1_1.setText('{:.4%}'.format(corel_1))
    #win.Alg_info2_1.setText('{:.4%}'.format(corel_2))
    #win.Alg_info3_1.setText('{:.4%}'.format(corel_3))

def comul_resolve(win):
    sequence = win.lineEdit.text().split()

    filtered_sequence = []
    for i in sequence:
        try:
            int(i)
        except ValueError:
            continue
        else:
            filtered_sequence.append(int(i))

    corel = cal_comulsum(filtered_sequence)
    #win.label_15.setText('{:.4%}'.format(corel))
