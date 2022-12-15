def payroll():
    while True:
        print("\t\t\t\tPhilippine College of Science and Technology")
        print("\t\t\t\t\t\t Nalsian Calasiao Pangasinan")
        print()
        print("\t\t\t\t\t\t\t\t\tPayroll")
        print()
        id = int(input("Enter Employee ID       :  "))
        name = str(input("Enter Employee Name     : "))
        pos= str(input("Enter Position          : "))
        rate = int(input("Rate                    :  "))
        hours = int(input("Hours                   :  "))

        if hours > 40:
            rt = hours - 40
            hrsrt = (rt * rate) * 1.5
            print("Over Time Pay           :", hrsrt)
            gp = hrsrt + (hours * rate)
            print("Gross Pay               :", gp)
            print("Deduction")
            SSS = .1 * gp
            print("SSS                     :", SSS)
            pgib= 250
            print("Pag-Ibig                :",pgib)
            ph = 100 + (.05 * gp)
            print("Phil Health             :", ph)
            if gp < 10000:
                a = 0.02 * gp
                print("Income Tax           :", a)
                td = a + SSS + ph + pgib
                np = gp - td
                print("Net Pay           :", np)

            elif gp <= 19999.99:
                b = 0.05 * gp
                print(" Income Tax             :", b)
                td = b + SSS + ph + pgib
                np = gp - td
                print("Net Pay                 :", np)
            elif gp <= 29999.99:
                c = 0.1 * gp
                print("Income Tax              :", c)
                td = c + SSS + ph + pgib
                np = gp - td
                print("Net Pay                 :", np)
            elif gp >= 50000:
                d = 0.15 * gp
                print("Income Tax              :", d)
                td = d + SSS + ph + pgib
                np = gp - td
                print("Net Pay                 :", np)
            elif gp <= 99999.99:
                e = 0.15 * gp
                print("Income Tax              :", e)
                td = e + SSS + ph + pgib
                print()
                np = gp - td
                print("Net Pay                 :", np)


        else:
            print("Over Time Pay           :")
            gp1 = hours * rate
            print("Gross Pay               :", gp1)
            SSS1 = .1 * gp1
            print("SSS                     :", SSS1)
            pgib1= 250
            print("Pag-Ibig                :",pgib1)
            ph1 = 100 + (.05 * gp1)
            print("Phil Health             :", ph1)

            if gp1 < 10000:
                a = 0.02 * gp1
                print("Income Tax              :", a)
                td1 = a + SSS1 + ph1 + pgib1
                np1 = gp1 - td1
                print("Net Pay                 :", np1)

            elif gp1 <= 19999.99:
                b = 0.05 * gp1
                print("Income Tax              :", b)
                td1 = b + SSS1 + ph1 + pgib1
                np1 = gp1 - td1
                print("Net Pay                 :", np1)
            elif gp1 <= 29999.99:
                c = 0.1 * gp1
                print("Income Tax              :", c)
                td1 = c + SSS1 + ph1 + pgib1
                np1 = gp1 - td1
                print("Net Pay                 :", np1)
            elif gp1 >= 50000.00:
                d = 0.15 * gp1
                print("Income Tax              :", d)
                td1 = d + SSS1 + ph1 + pgib1
                np1 = gp1 - td1
                print("Net Pay                 :", np1)
            elif gp1 <= 99999.99:
                e = 0.15 * gp1
                print("Income Tax              :", e)
                td1 = e + SSS1 + ph1 + pgib1
                print()
                np1 = gp1 - td1
                print("Net Pay                 :", np1)

        print()
        print("Period Start date   :     November 21, 2022 ")
        print("Period end Date     :     November 25, 2022")
        print("Payable date        :     November 26, 2022")
        z= str(input("Press 0 to Exit or Press any key to Repeat: "))
        if z == '0':
            break

payroll()
