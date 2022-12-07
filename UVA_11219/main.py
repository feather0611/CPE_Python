caseCount = input()
case = []
for i in range(int(caseCount)):
    _, x, y = input(), input(), input()
    current = x.split("/")
    birth = y.split("/")
    case.append(
        {
            "currentDate": {
                "year": int(current[2]),
                "month": int(current[1]),
                "day": int(current[0]),
            },
            "birthDay": {
                "year": int(birth[2]),
                "month": int(birth[1]),
                "day": int(birth[0]),
            },
            "age": -1,
        }
    )
    

for idx, ele in enumerate(case):
    if ele["currentDate"]["year"] < ele["birthDay"]["year"]:
        ele["age"] = "Invalid birth date"
    elif ele["currentDate"]["year"] == ele["birthDay"]["year"]:
        if ele["currentDate"]["month"] < ele["birthDay"]["month"]:
            ele["age"] = "Invalid birth date"
        elif ele["currentDate"]["month"] == ele["birthDay"]["month"]:
            if ele["currentDate"]["day"] < ele["birthDay"]["day"]:
                ele["age"] = "Invalid birth date"
            else:
                ele["age"] = 0
        else:
            ele["age"] = 0
    else:
        if (ele["currentDate"]["month"] < ele["birthDay"]["month"]):
            if (ele["currentDate"]["year"] - ele["birthDay"]["year"] - 1 > 130):
                ele["age"] = "Check birth date"
            else:
                ele["age"] = ele["currentDate"]["year"] - ele["birthDay"]["year"] - 1
        elif (ele["currentDate"]["month"] == ele["birthDay"]["month"]):
            if (ele["currentDate"]["day"] < ele["birthDay"]["day"]):
                if (ele["currentDate"]["year"] - ele["birthDay"]["year"] - 1 > 130):
                    ele["age"] = "Check birth date"
                else:
                    ele["age"] = ele["currentDate"]["year"] - ele["birthDay"]["year"] - 1
            else:
                if (ele["currentDate"]["year"] - ele["birthDay"]["year"] > 130):
                    ele["age"] = "Check birth date"
                else:
                    ele["age"] = ele["currentDate"]["year"] - ele["birthDay"]["year"]
        else:
            if (ele["currentDate"]["year"] - ele["birthDay"]["year"] > 130):
                ele["age"] = "Check birth date"
            else:
                ele["age"] = ele["currentDate"]["year"] - ele["birthDay"]["year"]

    print("Case #{}: {}".format(idx+1, ele["age"]))
